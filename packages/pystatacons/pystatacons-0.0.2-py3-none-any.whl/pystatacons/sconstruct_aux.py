# Auxiliar functions to aid in writting SConstruct files for scons

import subprocess
import shlex
import re
import os
from pkg_resources import packaging
import sys
from pathlib import Path #scons' Glob is not recursive

import SCons
from SCons.Defaults import DefaultEnvironment
import SCons.Debug
import SCons.Script
from SCons.Script import AddOption, GetOption, SetOption
from SCons.Builder import Builder

pre_sys_stdout = sys.stdout #Need this sometimes to print while run from Stata (e.g., stata_run)

if packaging.version.parse(SCons.__version__) < packaging.version.parse("4.2.0"):
    SCons.Debug.Trace("WARNING: You are running SCons version" + SCons.__version__ + " and statacons has only been tested on 4.2.0+. \n", pre_sys_stdout)

def _find(pathname, paths=None):
    if paths is None:
        paths = os.environ['PATH'].split(os.pathsep)
    for dirname in paths:
        candidate = os.path.join(dirname, pathname)
        if os.path.isfile(candidate):
            return (pathname, candidate, dirname)
    return None

def configuration(config_user_ini = 'config_user.ini', config_project_ini='config_project.ini'):
    import shutil
    import configparser
    # Copies templates if no such file exists
    if not os.path.isfile(config_user_ini) and os.path.isfile('utils/config_user_template.ini'):
        shutil.copy('utils/config_user_template.ini', config_user_ini)

    CONFIG = configparser.ConfigParser()
    # Load the easy defaults initially
    CONFIG['SCons'] = {'success_batch_log_dir': '', 'use_custom_datasignature': 'Strict', 'stata_chdir': ''}
    
    # Loads config ini files (user ones can over-ride project ones)
    config_files = [f for f in [config_project_ini, config_user_ini] if os.path.isfile(f)]
    CONFIG.read(config_files)

    #Remove quotes form paths if people are confused
    def strip_quotes_config(k1, k2, conf):
        if k1 in conf and k2 in conf[k1]:
            conf[k1][k2] = conf[k1][k2].strip('"').strip("'")

    strip_quotes_config('Programs', 'stata_exe', CONFIG)
    strip_quotes_config('SCons', 'success_batch_log_dir', CONFIG)
    strip_quotes_config('Project', 'cache_dir', CONFIG)
    
    return CONFIG

AddOption(
    '--config-user',
    dest='config_user',
    action='store',
    type="string",
    help='config user',
)
if GetOption("config_user") is not None:
    config = configuration(config_user_ini=GetOption("config_user"))
else:
    config = configuration()

AddOption(
    '--show-config',
    dest='show_config',
    action='store_true',
    default=False,
    help='show config',
)




env = DefaultEnvironment(ENV=os.environ, tools=[])
env['CONFIG'] = config
def stata_tool(env):
    import platform
    plat = platform.system()
    if 'Programs' in env['CONFIG'] and 'stata_exe' in env['CONFIG']['Programs']:
        env['STATABATCHEXE'] = env['CONFIG']['Programs']['stata_exe']
    
    else:      
        #TODO: allow abs path for STATAEXE (use os.path.isabs(...))
        def_execs = {'Windows': ['StataMP-64.exe', 'StataSE-64.exe', 'StataBE-64.exe', 'Stata-64.exe'], 
                     'Linux':['stata-mp', 'stata-se', 'stata'],
                     'Darwin':['StataMP', 'StataSE', 'StataBE', 'Stata']}
        candidate_stata_exes = def_execs[plat]
        if 'STATAEXE' in os.environ:
            candidate_stata_exes = [os.environ['STATAEXE']] + candidate_stata_exes
        found_ret = None
        for candidate_stata_exe in candidate_stata_exes:
            found_ret = _find(candidate_stata_exe)
            if found_ret is not None:
                env['STATABATCHEXE'] = found_ret[0]
                break
        if found_ret is None and plat=='Windows':
            for candidate_stata_exe in candidate_stata_exes:
                found_ret = _find(candidate_stata_exe, [os.path.join(os.environ['ProgramFiles'], "Stata" + str(n)) for n in [17, 16]])
                if found_ret is not None:
                    env['STATABATCHEXE'] = found_ret[1]
                    break
        if found_ret is None and plat=='Darwin':
            for candidate_stata_exe in candidate_stata_exes:
                found_ret = _find(candidate_stata_exe, ["/Applications/Stata/" + st_type + ".app/Contents/MacOS/" for st_type in def_execs[plat]])
                if found_ret is not None:
                    env['STATABATCHEXE'] = found_ret[1]
                    break
            
        if found_ret is None:
            print("Can't find Stata from config or defaults")

    batch_flags = {'Windows': '/e', 
                   'Linux': '-b',
                   'Darwin': '-e'}
    
    env['STATABATCHFLAG'] = batch_flags[plat]
    env['STATABATCHCOM'] = '"' + env['STATABATCHEXE'] + '"' if " " in env['STATABATCHEXE'] else env['STATABATCHEXE']
    env['STATABATCHCOM'] = env['STATABATCHCOM']  + " " + batch_flags[plat]
   
env.Tool(stata_tool)

# add the Builder stata_bld to env, give it the name StataBuild
# tell scons how to tell stata to run a do-file in batch mode

AddOption(
    '--assume-built',
    dest='assume_built',
    action='store',
    type="string",
    help='assume built',
)
AddOption(
    '--assume-done',
    dest='assume_done',
    action='store',
    type="string",
    help='assume done',
)


# Deciders
# Note that timestamp-newer/make compares target vs source, whereas timestamp-changed doesn't look at target (just prev vs current of source)
# 'content-timestamp' = 'timestamp-changed' and 'content'

# 'make' and 'content'
def dependency_newer_then_content_changed(dependency, target, prev_ni, repo_node=None):
    return dependency.changed_timestamp_newer(target, prev_ni, repo_node) and dependency.changed_content(target, prev_ni, repo_node)

# 'make' and 'content-timestamp'
def changed_timestamp_then_dependency_newer_then_content_content(dependency, target, prev_ni, repo_node=None):
    return dependency.changed_timestamp_newer(target, prev_ni, repo_node) and dependency.changed_timestamp_then_content(target, prev_ni, repo_node)

decider_str_lookup = {'content-timestamp-newer': dependency_newer_then_content_changed,
                      'content-timestamp-newer-timestamp-changed': changed_timestamp_then_dependency_newer_then_content_content}
decider_str_lookup.update({k:k for k in ['MD5', 'content', 'MD5-timestamp', 'content-timestamp', 'timestamp-newer', 'make', 'timestamp-match']})


#We impliment these skip-logic routines in stata_run() and not a dedicated Decider so that
# someone can change them on the command-line without changing any files and is orthogonal
# to what decider they choose (MD5, MD5-timestamp)
assume_built = GetOption('assume_built') #If there are outer quotes on the cli, these are stripped.
assume_built_list = []
if not assume_built is None:
    assume_built_list = [str(path) for file_pattern in assume_built.split(':') for path in Path().rglob(file_pattern) if not path.is_dir()] #could've used os.pathsep, but want consistent across sytems

assume_done = GetOption('assume_done') #If there are outer quotes on the cli, these are stripped.
assume_done_list = []
if not assume_done is None:
    assume_done_list = [str(path) for file_pattern in assume_done.split(':') for path in Path().rglob(file_pattern) if not path.is_dir()] #could've used os.pathsep, but want consistent across sytems

#AddOption(
#    '--skip-newer',
#    dest='skip_newer',
#    action='store_true',
#    default=False,
#    help='skip newer',
#)

# Can't use the Builder chdir option, since that moves the target dir (and we want source)
stata_chdir = config['SCons']['stata_chdir']
if stata_chdir=='': stata_chdir = 0
if stata_chdir=='1' or stata_chdir=='0': stata_chdir = int(stata_chdir)


def stata_run(target, source, env, params="", file_cmd="do", full_cmd=None):
    if full_cmd is None: 
        fname = str(source[0]) #Assumes the first element of source is the do file
        
    assume_built = GetOption('assume_built')
    if not assume_built is None and all([str(t) in assume_built_list for t in target]):
        if full_cmd is None: full_cmd = file_cmd + ' "' + fname + '" ' + params
        for t in target: Path(str(t)).touch() #In case someone is using a time-stamp option for content being up-to-date. Touch() doesn't seem to work
        if not GetOption('silent'):
            SCons.Debug.Trace("Assuming built: " + full_cmd + "\n", pre_sys_stdout)
        return 0
    assume_done = GetOption('assume_done')
    if not assume_done is None and 'fname' in locals() and fname in assume_done_list:
        for t in target: Path(str(t)).touch() #In case someone is using a time-stamp option for content being up-to-date. Touch() doesn't seem to work
        if not GetOption('silent'):
            SCons.Debug.Trace("Assuming done: " + fname + "\n", pre_sys_stdout)
        return 0

    #if GetOption('skip_newer') and min([os.path.getmtime(str(t)) for t in target]) > max([os.path.getmtime(str(s)) for s in source]):
    #    if not GetOption('silent'):
    #        if full_cmd is None: full_cmd = file_cmd + ' "' + fname + '" ' + params
    #        SCons.Debug.Trace("Skipping newer: " + full_cmd + "\n", pre_sys_stdout)
    #    return 0

    cwd = None
    if stata_chdir == 1 and full_cmd is None:
        cwd = os.path.dirname(fname)
        fname = os.path.basename(fname)
    elif stata_chdir != 0:
        cwd = stata_chdir
        fname = os.path.relpath(fname, stata_chdir)

    if full_cmd is None: 
        full_cmd = file_cmd + ' "' + fname + '" ' + params
    
    #Get hash of command to avoid collisions
    import hashlib
    max_digest_len = 8
    cmd_digest = hashlib.md5(full_cmd.encode('utf-8')).hexdigest()[:max_digest_len]

    if 'fname' in locals():
        recipe_basename = os.path.splitext(os.path.basename(fname))[0]
        #TODO (potential): could track all basefnames (in StataBuild) and if there's duplicates then attach digests to those
        if file_cmd!="do" or params!="": 
            recipe_basename = recipe_basename + "-" + cmd_digest
    else:
        recipe_basename = "stata-"+cmd_digest
        
    log_basename = recipe_basename + ".log"
    if cwd is not None:
        log_name = os.path.join(cwd, log_basename)
    else:
        log_name = log_basename


    import tempfile
    with tempfile.TemporaryDirectory() as tmpdirname:
        #if GetOption("debug")!=[] and not GetOption('silent'):
        #    SCons.Debug.Trace("Executing in temporary directory: " + tmpdirname+"\n", pre_sys_stdout)
        recipe_fname = os.path.join(tmpdirname, recipe_basename+".do")
        with open(recipe_fname, "w") as recipe:
            recipe.write(full_cmd + '\n')
        
        args_split = [env['STATABATCHEXE'], env['STATABATCHFLAG'], "do", recipe_fname]
        digest_str = "" if 'fname' in locals() and file_cmd=="do" and params=="" else ". log="+log_basename
        if not GetOption('silent'):
            SCons.Debug.Trace("Running: "+env['STATABATCHCOM'] + " " +full_cmd+digest_str+"\n", pre_sys_stdout)
        cproc = subprocess.run(args_split, cwd=cwd)
        
    if cproc.returncode!=0: #In case the Stata executable has a real issue
        return cproc.returncode

    #check if script had an error
    retcode = 0
    with open(log_name, 'r') as f:
        lines = f.readlines() #if logs are really big, iterate until end to not store whole thing
        # Thanks to Kyle https://gist.github.com/pschumm/b967dfc7f723507ac4be#gistcomment-2657900
        match = re.search('^r\(([0-9]+)\);$', lines[-1]) #pytask looks in any of last 10 lines
        if match is not None:
            retcode = int(match[1])
    if retcode!=0: 
        os.replace(log_name, os.path.join(".", recipe_basename + ".log"))
        return retcode
    
    success_batch_log_dir = env['CONFIG']['SCons']['success_batch_log_dir']
    if success_batch_log_dir=="":
        os.remove(log_name)
    elif success_batch_log_dir!="." and success_batch_log_dir!="":
        os.replace(log_name, os.path.join(success_batch_log_dir, recipe_basename + ".log"))

    return 0
stata_do_bld = Builder(action=stata_run)
env.Append(BUILDERS={'StataDo': stata_do_bld})

def copy_func(f):
    import types
    import functools
    """Based on http://stackoverflow.com/a/6528148/190597 (Glenn Maynard)"""
    g = types.FunctionType(f.__code__, f.__globals__, name=f.__name__,
                           argdefs=f.__defaults__,
                           closure=f.__closure__)
    g = functools.update_wrapper(g, f)
    g.__kwdefaults__ = f.__kwdefaults__
    return g

builder_counter = 1
task_dependencies = []
def stata_run_params_factory(self, target, source=None, do_file=None, params="", file_cmd="do", full_cmd=None, depends=None):
    #partial approach doesn't work because the signature includes the address of original function
    env = self #print(type(self)) #self is env
    
    #scons typically deletes targets when they will be re-made, but we want to allow assume_built
    env.Precious(target)

    if do_file is not None: source = [do_file]

    if (params=="") and (file_cmd=="do") and (full_cmd is None): #don't need a custom builder
        build_obj = env.StataDo(target, source)
    else:
        custom_stata_run = copy_func(stata_run)
        custom_stata_run.__defaults__ = (params,file_cmd,full_cmd)
        global builder_counter
        cust_name = 'StataBuild' + str(builder_counter)
        builder_counter = builder_counter+1
        cust_builder = Builder(action=custom_stata_run)
        env.Append(BUILDERS={cust_name: cust_builder}) #TODO: Do I need this?
        
        build_obj = env.__dict__[cust_name](target, source) #don't think i need the env.XXX form
    
    if depends is not None:
        env.Depends(build_obj, depends)

    if type(source) is not list: source = [source]
    global task_dependencies
    deps = source
    if depends is not None: deps = deps + depends
    task_dependencies.append((target, deps))

    return build_obj
    
env.AddMethod(stata_run_params_factory, 'StataBuild')


if GetOption("show_config"):	
    SetOption("no_exec", True)
    SetOption("silent", True)
    SCons.Debug.Trace("Current config:\n", pre_sys_stdout)
    if 'Programs' not in env['CONFIG'] or 'stata_exe' not in env['CONFIG']['Programs']:
        SCons.Debug.Trace("Stata batch found automatically: "+env['STATABATCHCOM']+"\n", pre_sys_stdout)
    for section in config.sections():
        SCons.Debug.Trace("["+section+"]\n", pre_sys_stdout)
        for key in config[section]:
            SCons.Debug.Trace(key + ": " + config[section][key] + "\n", pre_sys_stdout)
    SCons.Debug.Trace("\n", pre_sys_stdout)

    

# how to get a Stata-style datasignature
def get_datasign(fname):
    m_str = env['CONFIG']['SCons']['use_custom_datasignature']
    meta = m_str!="DataOnly" and m_str!="Datasignature"
    meta_arg_split = [] if meta else ["nometa"]
    vv_only = m_str=="VVLabelsOnly"
    vv_only_arg_split = ["vv_labels_only"] if vv_only else []
    slow = ('Project' in env['CONFIG'] and 'cache_dir' in env['CONFIG']['Project']) or ('Project' in env['CONFIG'] and 'dta_sig_mode' in env['CONFIG']['Project'] and env['CONFIG']['Project']['dta_sig_mode']=='slow')
    fast_arg_split = [] if slow else ["fast"]
    fname_abs = os.path.abspath(fname)
    
    #Run in temp-dir as in parallel mode we don't want to processes to try writing to the same stata.log
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdirname:
        sig_fname="sig.txt"
        args_split = [env['STATABATCHEXE'], env['STATABATCHFLAG'], 'complete_datasignature,', 'dta_file("' + fname_abs + '")', 'fname("' + sig_fname + '")'] + meta_arg_split + fast_arg_split + vv_only_arg_split
        #SCons.Debug.Trace(str(args_split) + "\n", pre_sys_stdout) 
        cproc = subprocess.run(args_split, cwd=tmpdirname)
        if cproc.returncode!=0: #In case the Stata executable has a real issue
            raise Exception("Couldn't get the file data-signature. Stata error")
        #Don't need to check log error, because lack of sig_fname will just raise exception
        with open(os.path.join(tmpdirname,sig_fname), "r") as f:
            sig = f.readline()
    return sig

# replacement of hash_file_signature. Checks if .dta and then special call, otherwise hands off to reguarl hash_file_signature()
def hash_file_signature_new(fname, chunksize=65536, hash_format=None):
    """
    Generate the md5 signature of a file

    Args:
        fname: file to hash
        chunksize: chunk size to read
        hash_format: Specify to override default hash format

    Returns:
        String of Hex digits representing the signature
    """
    import SCons.Util

    #SCons.Debug.Trace('new hash: ' + fname + "\n", pre_sys_stdout) 
    if os.path.splitext(fname)[1]==".dta":
        try:
            sig = get_datasign(fname)
            if not GetOption('silent'):
                SCons.Debug.Trace('Computed dta-signature: ' + fname + "\n", pre_sys_stdout)
            return sig
        except Exception as e:
            pass

    return SCons.Util.hash_file_signature(fname, chunksize, hash_format)

# replacement of get_content_hash, just called hash_file_signature_new() instead of default
def get_content_hash_new(self) -> str:
    """
    Compute and return the hash for this file.
    """
    import SCons.Util
    import SCons.Node.FS
    if not self.rexists():
        return SCons.Util.hash_signature(SCons.Util.NOFILE)
    fname = self.rfile().get_abspath()
    try:
        cs = hash_file_signature_new(fname, chunksize=SCons.Node.FS.File.hash_chunksize)
    except EnvironmentError as e:
        if not e.filename:
            e.filename = fname
        raise
    return cs

# Remove condition where if file size < hash_chunksize it calls hash_signature(contents) instead of going down to hash_file_signature
def get_csig_new(self) -> str:
	"""Generate a node's content signature."""
	import SCons.Util
	ninfo = self.get_ninfo()
	try:
		return ninfo.csig
	except AttributeError:
		pass

	csig = self.get_max_drift_csig()
	if csig is None:
		try:
			size = self.get_size()
			if size == -1:
				contents = SCons.Util.NOFILE
			#elif size < File.hash_chunksize:
			#    contents = self.get_contents()
			else:
				csig = get_content_hash_new(self)
		except IOError:
			# This can happen if there's actually a directory on-disk,
			# which can be the case if they've disabled disk checks,
			# or if an action with a File target actually happens to
			# create a same-named directory by mistake.
			csig = ''
		else:
			if not csig:
				csig = SCons.Util.hash_signature(contents)
	
	ninfo.csig = csig

	return csig

def monkey_patch_scons():
    m_str = env['CONFIG']['SCons']['use_custom_datasignature']
    if not GetOption('silent'):
        if m_str!="DataOnly" and m_str!="Datasignature" and m_str!="VVLabelsOnly":
            print("Using 'Strict' custom_datasignature.")
            print("Calculates timestamp-independent checksum of dataset, including all metadata.")
            print("Edit use_custom_datasignature in config_project.ini to change.")
            print("  (other options are DataOnly, VVLabelsOnly, False)")
        elif m_str=="VVLabelsOnly":
            print("Using 'VVLabelsOnly' custom_datasignature.")
            print("Calculates timestamp-independent checksum of dataset, including variable and value labels.")
            print("Edit use_custom_datasignature in config_project.ini to change.")
            print("  (other options are Strict, DataOnly, False)")
        else:       
            print("Using 'DataOnly' datasignature.")
            print("Calculates timestamp-independent checksum of dataset, not including metadata")
            print("Edit use_custom_datasignature in config_project.ini to change.")
            print("  (other options are Strict, VVLabelsOnly, False)")
    ### Allow using Stata-style data-signatures instead of MD5 file hashes
    # Can't do this in SConstruct
    # Can't use Decider because I need my hash of the previous file and don't want to store it
    import SCons.Node.FS
    # Can't easily replace SCons.Util.hash_file_signature because it's imported druing SCons/Script/__init__.py
    # (https://medium.com/@chipiga86/python-monkey-patching-like-a-boss-87d7ddb8098e)
    # So have to override the calling class method instead
    SCons.Node.FS.File.get_content_hash = get_content_hash_new
    #Overwrite this one too that used a different hash method with small files
    SCons.Node.FS.File.get_csig = get_csig_new

if env['CONFIG']['SCons']['use_custom_datasignature']!="False": monkey_patch_scons()
elif not GetOption('silent'):
    print("Using default timestamp-dependent checksums of dataset,")
    print("Edit use_custom_datasignature in config_project.ini to change (Strict, DataOnly, VVLabelsOnly)")
