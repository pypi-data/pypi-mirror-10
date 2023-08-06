#!/usr/bin/env python
import appdirs
import os
import os.path
import sys
import signal
import json
import subprocess
import shutil
import socket

def pexec(cmd):
    """ executes shell command cmd with the output 
        printed in the parent shell. Returns when the
        command has finished.
    """
    os.system(cmd)

def rexec(cmd):
    """ executes shell command cmd with the output 
        returned as a string when the command has 
        finished.
    """
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    return process.communicate()[0][:-1]

def opexec(cmd):
    """ same as pexec() but with current working 
        directory set to the odoo server path
    """
    path = odoo_path_or_crash()
    process = subprocess.Popen(cmd.split(), cwd=path)
    return process.wait() == 0

def otexec(cmd):
    """ executes the command cmd with the odoo 
        server path as current working dir. 
        All output is hidden. Returns True if the
        call exited successfully, False otherwise.
    """
    path = odoo_path_or_crash()
    process = subprocess.Popen(cmd.split(), cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.wait() == 0

def orexec(cmd):
    """ same as rexec() but with current working 
        directory set to the odoo server path
    """
    path = odoo_path_or_crash()
    process = subprocess.Popen(cmd.split(), cwd=path, stdout=subprocess.PIPE)
    return process.communicate()[0][:-1]

def is_port_taken(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    return result == 0

def find_port(start=8069):
    for port in range(start, 8079):
        if not is_port_taken(port):
            return port
    return None

#   +============================+ 
#   |        HELP STRINGS        |
#   +============================+


PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
COLOR_END = '\033[0m'

def clr(c, txt):
    return c + txt + COLOR_END

CMD_HELP = {
    "help": """
   help [CMD]
       prints this help, or the help of the
       provided command.
    """,
    "start": """
   start [args]
       [Re]start the Odoo server on port 8069
       with a db named with the current git
       branch. It will create a database 
       with demo data if it doesn't exist.

       [args] will be passed to the odoo 
       server command line.
    """,
    "reset": """
   reset [args]
       Restart the server with a new database
       
       [args] will be passed to the odoo
       server command line at restart.
    """,
    "stop": """
   stop
       Stops the current server.
    """,
    "log": """
   log 
       Prints the last 20 commits.
    """,
    "find": """
   find STR 
       Finds files in the repository that
       contains STR in their filename
    """,
    "try": """
   try BRANCH [args]
       Launches a Odoo server with the code found
       in the branch BRANCH, without changing the
       current branch of the repository.

       Odoo servers launched with 'try' are not
       affected by the start / stop / reset commands

       The databases created by try are recycled after
       a while

       [args] will be passed to the odoo
       server command line at restart.
    """,
    "path": """
   path 
       Prints the path to the odoo server directory
    """,
    "fetch": """
   fetch BRANCH
       If there is no local branch named BRANCH, try
       to find a branch named BRANCH on one of the
       official repositories and create a new git
       branch with the same name with remote tracking
       activated 
    """,
    "branch": """
   branch 
       Prints the current branch of the odoo repository
    """,
    "git": """
   git [git command]
       Executes the git command in the odoo repository. 
    """,
    "config": """
   config [key] [value]
       Prints the content of the Ook config file.

       [key] Prints the value associated with key
       in the Ook config file.

       [key] [value]
       Sets the Ook config option 'key' to 'value'
    """,
}

HELP = "\n".join([
    "Usage: ook [COMMAND]",
    "".join(CMD_HELP.values()),
])


#   +============================+ 
#   |        CONFIG FILE         |
#   +============================+

def config_file():
    path = os.path.join(appdirs.user_config_dir(),'ook.json')
    if os.path.exists(path):
        return open(path,'r+')
    else:
        return open(path,'w+')

def set_config(key, value):
    with config_file() as config:
        contents = config.read()
        parsed   = json.loads(contents if contents else "{}")
        parsed[key] = value
        config.seek(0)
        config.truncate(0)
        config.write(json.dumps(parsed, indent=4))

def get_config(key, default=None):
    with config_file() as config:
        contents = config.read()
        parsed   = json.loads(contents if contents else "{}")
        return parsed.get(key, default)

#   +============================+ 
#   |      REPOSITORY INFO       |
#   +============================+

def odoo_branch():
    return orexec("git rev-parse --abbrev-ref HEAD")

def odoo_path():
    def is_path_repo(path):
        return ".git" in os.listdir(path)

    def is_path_odoo(path):
        return "openerp-server" in os.listdir(path)

    def get_odoo(path):
        if is_path_repo(path) and is_path_odoo(path):
            return path
        elif os.path.samefile(path, os.path.join(path,'..')):
            return None
        else:
            return get_odoo(os.path.abspath(os.path.join(path,"..")))

    path = get_odoo(os.getcwd())

    if path:
        set_config('path', path)
        return path
    
    path = get_config('path')
    if path and os.path.exists(path) and is_path_odoo(path):
        return path

    for path in ['~/odoo','~/odoo/odoo','~/code/odoo','~/projects/odoo','~/Projects/odoo','~/Code/odoo/',"/opt/odoo"]:
        path = os.path.expanduser(path)
        if os.path.exists(path) and is_path_odoo(path) and is_path_repo(path):
            set_config('path',path)
            return path

    return None

def odoo_path_or_crash():
    path = odoo_path()
    if path:
        return path
    else:
        sys.exit("Could not find the odoo server directory.")

#   +============================+ 
#   |         COMMANDS           |
#   +============================+

def cmd_help(args):
    if len(args) < 2:
        print HELP
    else:
        print CMD_HELP[args[1]]

def cmd_log():
    opexec("git log --oneline -n 20")

def cmd_port():
    print find_port()

def cmd_branch():
    print '"' + odoo_branch() + '"'

def cmd_git(args):
    opexec(" ".join(args))

def cmd_ook():
    print ""
    print PURPLE + "      The Odoo Code Monkey Helper" + COLOR_END
    print "  Type '" + UNDERLINE + "ook help" + COLOR_END +"' to display the help"
    print
    print "\n".join([
        """                         .="=.          """,
        """                Ook!   _/.-.-.\\_     _  """,
        """                   \\  ( ( o o ) )    )) """,
        """                       |/  "  \\|    //  """,
        """       .-------.        \\'---'/    //   """,
        """      _|~~ ~~  |_       /`"'"`\\\\  ((    """,
        """    =(_|_______|_)=    / /_,_\\ \\\\  \\\\   """,
        """      |:::::::::|      \_\\_'__/ \\  ))  """,
        """      |:::::::[]|       /`  /`~\\  |//   """,
        """      |o=======.|      /   /    \\  /    """,
        """      `"'"'"'"'"`  ,--`,--'\\/\\    /     """,
        """                    '-- "--'  '--'      """,
        "",
    ])

def cmd_stop():
    pid = get_config("server_pid")
    if pid and pid > 0:
        pexec("pkill -TERM -P " + str(pid))
        set_config("server_pid",-1)

def cmd_dropdb():
    branch = odoo_branch()
    cmd_stop()
    pexec('dropdb ' + branch)

def cmd_start(args):
    path = odoo_path_or_crash()
    opath = path + "/odoo.py"
    branch = odoo_branch()

    if len(args) < 2:
        args = []
    else:
        args = args[1:]

    cmd_stop()

    print "Starting Odoo:"
    print "     Server: " + opath
    print "   Database: " + branch
    if len(args):
        print "       args: " + " ".join(args)
    print ""

    set_config("server_pid", os.getpid())

    cmd = opath + " start -d " + branch + " " + " ".join(args)
    
    return subprocess.Popen(cmd.split(), cwd=path).wait()

def cmd_tmp_export(args):
    path = odoo_path_or_crash()
    if len(args) < 2:
        sys.exit("Please provide the name of the branch to export.")

    branch = args[1]
    try_path = '/tmp/' + branch
    try_db   = "tmp-"  + branch

    trials = get_config('tmps',[])
    
    exists = False
    for trial in trials:
        if trial['path'] == try_path:
            exists = True
            break
    if not exists:
        trials.append({'path': try_path, 'db': try_db})

    if len(trials) > 3:
        print "Cleaning up old exports... "
        for trial in trials[:-3]:
            if os.path.exists(trial['path']):
                shutil.rmtree(trial['path'])
            pexec('dropdb ' + trial['db'])
        trials = trials[-3:]

    set_config('tmps',trials)

    if os.path.exists(try_path):
        shutil.rmtree(try_path)
    os.makedirs(try_path)

    print "Exporting branch", branch, "to /tmp ..."
    os.system("cd " + path + "; git archive " + branch + " | tar -x -C " + try_path)

def cmd_try(args):
    path = odoo_path_or_crash()
    if len(args) < 2:
        sys.exit("Please provide the name of the branch to try.")

    branch = args[1]
    try_path = '/tmp/' + branch
    try_db   = "try-"  + branch

    cmd_fetch(args)
    cmd_tmp_export(args)

    if len(args) < 3:
        oargs = []
    else:
        oargs = args[2:]

    opath = try_path + '/odoo.py'

    port = find_port(8070)
    if not port:
        sys.exit('Could not find an available server port')
    else:
        port = str(port)

    print "Starting Odoo:"
    print "     Server: " + opath
    print "   Database: " + try_db
    print "       Port: " + port
    if len(oargs):
        print "       args: " + " ".join(oargs)
    print ""

    cmd = opath + " start -d " + try_db + " --xmlrpc-port=" + port + " " + " ".join(oargs)
    
    return subprocess.Popen(cmd.split(), cwd=path).wait()

def cmd_test(args):
    path = odoo_path_or_crash()
    if len(args) < 2:
        sys.exit("Please provide the name of the branch to test.")

    branch = args[1]
    try_path = '/tmp/' + branch
    try_db   = "try-"  + branch

    cmd_fetch(args)
    cmd_tmp_export(args)

    #TODO

def cmd_reset(args):
    cmd_dropdb()
    cmd_start(args)

def cmd_path():
    print odoo_path_or_crash()

def cmd_find(args):
    if len(args) < 2:
        print "Please provide a pattern to find"
        print CMD_HELP["find"];
    else:
        path = odoo_path_or_crash()
        pexec('find ' + path + ' -name "*' + args[1] + '*"') 

def cmd_fetch(args):
    if len(args) < 2:
        print "Please provide the branch to fetch"
        print CMD_HELP["fetch"]
    else:
        branch = args[1]
        if otexec('git rev-parse --verify ' + branch):
            print 'Found local branch', branch
            return

        fetched = False
        for repo in ['enterprise-dev', 'odoo-dev', 'enterpise', 'odoo']:
            if otexec('git ls-remote --heads --exit-code ' + repo + ' ' + branch):
                print "Fetching", branch, "from", repo, "..."
                otexec('git fetch ' + repo + ' ' + branch + ':' + branch)
                fetched = True

        if not fetched:
            sys.exit("Branch " + branch + "could not be found on odoo repositories")

def cmd_config(args):
    if len(args) == 1:
        with config_file() as config:
            contents = config.read()
            if contents:
                print contents
            else:
                print "Empty Configuration"
    elif len(args) == 2:
        print get_config(args[1],"None")
    elif len(args) >  2:
        print "Setting", args[1], "to", args[2]
        set_config(args[1], args[2])

def cmd_todo(args):
    todos = get_config("todo",[])
    if len(args) == 1:
        if not len(todos):
            print "Nothing to do !"
        else:
            for i, todo in enumerate(todos):
                if todo["status"] == "done":
                    s = GREEN + "DONE" + COLOR_END
                else:
                    s = RED + "TODO" + COLOR_END
                print s +  " " + str(i) + ": " + todo["task"] 
    elif len(args) > 1:
        task = " ".join(args[1:])
        todos.append({ "status":"todo", "task":task })
        set_config("todo",todos)

def cmd_done(args):
    todos = get_config("todo",[])
    if len(args) == 1:
        if len(todos):
            todos[0]["status"] = "done"
    elif len(args) == 2:
        todos[int(args[1])]["status"] = "done"
    set_config("todo",todos)


#   +============================+ 
#   |           MAIN             |
#   +============================+

def main():
    args = sys.argv[1:]
    if len(args) == 0 :
        cmd_ook()
    elif args[0] == "help":
        cmd_help(args)
    elif args[0] == "log":
        cmd_log()
    elif args[0] == "git":
        cmd_git(args)
    elif args[0] == "path":
        cmd_path()
    elif args[0] == "test":
        print rexec("git rev-parse --abbrev-ref HEAD")
    elif args[0] == "find":
        cmd_find(args)
    elif args[0] == "config":
        cmd_config(args)
    elif args[0] == "branch":
        cmd_branch()
    elif args[0] == "try":
        cmd_try(args)
    elif args[0] == "start":
        cmd_start(args)
    elif args[0] == "dropdb":
        cmd_reset(args)
    elif args[0] == "reset":
        cmd_reset(args)
    elif args[0] == "stop":
        cmd_stop()
    elif args[0] == "fetch":
        cmd_fetch(args)
    elif args[0] == "port":
        cmd_port()
    elif args[0] == "todo":
        cmd_todo(args)
    elif args[0] == "done":
        cmd_done(args)
    else:
        print "Unknown command", args[0]
        print HELP

if __name__ == "__main__":
    main()

