#!/usr/bin/python
import os, sys, time
import optparse
from subprocess import Popen, call
from urlparse import urlparse
from ConfigParser import SafeConfigParser
import shlex

from bq.util.commands import find_site_cfg
from bq.util.dotnested import parse_nested

#from bq.commands.server_ops import root

PID_TEMPL = "bisque_%s.pid"
LOG_TEMPL = 'bisque_%s.log'
SITE_CFG = 'site.cfg'

if os.name == 'nt':
    #pylint:disable=F0401
    import win32api, win32con
    def kill_process(pid):
        try:
            handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, pid)
            win32api.TerminateProcess(handle, 0)
            win32api.CloseHandle(handle)
            return True
        except Exception:
            print 'Error terminating %s, the process might be dead' % pid
        return False
        #import subprocess
        #subprocess.call(['taskkill', '/PID', str(pid), '/F'])

else:
    import signal
    from bq.util.wait_pid import wait_pid
    def kill_process(pid):
        try:
            pid = os.getpgid(pid)
            os.killpg (pid, signal.SIGTERM)
            wait_pid(pid)
            return True
        except OSError, e:
            print "kill process %s failed with %s" % (pid, e)
        return False



#####################################################################
# utils


def readhostconfig (site_cfg):
    #vars = { 'here' : os.getcwd() }
    config = SafeConfigParser ()
    config.read (site_cfg)
    #root = config.get ('app:main', 'bisque.root')
    top_dir = config.get ('app:main', 'bisque.paths.root')
    service_items = config.items ('servers')
    hosts = [ x.strip() for x in config.get  ('servers', 'servers').split(',') ]
    hosts.append('celery')

    #print "SECTION", config.has_section('servers')

    # Service spec if server.key.url = url
    # Create a dictionary for each host listed
    # h1.key.key1 = aa
    # h1.key.key2 = bb
    # => { 'h1' : { 'key' : { 'key1' : 'val', 'key2' : 'bb' }}}
    # servers = {}
    # for host_spec, val in service_items:
    #     path = host_spec.split('.')
    #     if not path[0] in hosts:
    #         continue
    #     param = path[-1]
    #     d = servers
    #     for path_el in path[:-1]:
    #         d = d.setdefault(path_el, {})
    #     d[param] = val

    servers = parse_nested (service_items, hosts)
    celery = servers.pop ('celery', None)

    bisque = { 'top_dir': top_dir,  'servers': servers, 'log_dir': '.', 'pid_dir' : '.'}
    if celery:
        bisque['celery'] = celery
    if config.has_option('servers', 'log_dir'):
        bisque['log_dir'] = os.path.join (top_dir, config.get ('servers', 'log_dir'))
    if config.has_option('servers', 'pid_dir'):
        bisque['pid_dir'] = os.path.join (top_dir, config.get ('servers', 'pid_dir'))
    if config.has_option('servers','backend'):
        bisque['backend'] = config.get ('servers', 'backend')
    #if config.has_option('servers','mex_dispatcher'):
    #    bisque['mex_dispatcher'] = config.get ('servers', 'mex_dispatcher')
    if config.has_option('servers','logging_server'):
        bisque['logging_server'] = config.get ('servers', 'logging_server')

    return bisque


def prepare_log (logfile):
    if os.path.exists(logfile):
        oldlog = logfile + '.save'
        if os.path.exists(oldlog):
            os.remove (oldlog)
        os.rename (logfile, oldlog)
        #print ('%s -> %s' % (logfile, oldlog))
    #else:
    #    print ("No logfile %s" % logfile)

# def tail(file):
#     interval = 1.0
#     while True:
#         where = file.tell()
#         line = file.readline()
#         if not line:
#             time.sleep(interval)
#             file.seek(where)
#         else:
#             print line, # already has newline

def tail(f, window=20):
    lines = [''] * window
    count = 0
    for l in f:
        lines[count % window] = l
        count += 1
    print lines[count % window:], lines[:count % window]

def check_running (pid_file):
    if os.path.exists(pid_file):
        print "Warning you appear to be restarting another BISQUIK process"
        print "Please stop that process before starting another"
        print "Try to stop previous running instance (Y/n)"
        a = raw_input()
        if a == '' or a[0].upper() == "Y":
            return True
        else:
            return False

def kill_pidfile (pidfile):
    if  os.path.exists (pidfile):
        with open(pidfile, 'r') as pd:
            pid = int (pd.read())
            kill_process (pid)
        os.remove (pidfile)
        return True
    return False

############################################
# -------- Commands ------------------------
def pserve_command(command, options, cfgopt, processes, cfg_file = None, *args):
    def verbose(msg):
        if options.verbose:
            print msg

    paster_verbose = '-v' if options.verbose else '-q'
    msg = { 'start': 'starting', 'stop':'stopping', 'restart':'restarting'}[command]
    verbose ("%s bisque on %s .. please wait" % (msg, cfgopt['port']))
    server_cmd = ['pserve',  paster_verbose]
    if not options.wait :
        server_cmd.extend (['--log-file', cfgopt['logfile'], '--pid-file', cfgopt['pidfile']])

    if command in ('start', 'restart'):
        prepare_log (cfgopt['logfile'])

    if options.reload:
        server_cmd.append ('--reload')
    server_cmd.extend ([
            #os.path.join(cfgopt['site_dir'], 'server.ini'),
            cfg_file or '',
            command,
            #'services_enabled=%s' % cfgopt['services_enabled'],
            #'services_disabled=%s' % cfgopt['services_disabled'],
            #'server=%s' % cfgopt['url'],
            #'http_port=%s' % cfgopt['port'],
            #'http_host=%s' % cfgopt['host'],
            #'rooturl=%s' % cfgopt['root'],
            #'sitecfg=%s' % cfgopt['site_cfg'],
            ])
    server_cmd.extend (args)
    verbose ('Executing: %s' % ' '.join(server_cmd))
    if not options.dryrun:
        processes.append(Popen(server_cmd))
    return processes

def uwsgi_command(command, options, cfgopt, processes,  cfg_file = None, *args):
    def verbose(msg):
        if options.verbose:
            print msg

    if command is 'stop':
        pidfile = cfgopt['pidfile']
        uwsgi_cmd = ['uwsgi', '--stop', pidfile]
        #processes.append(Popen(uwsgi_cmd,shell=True,stdout=sys.stdout))

        verbose('Executing: ' + ' '.join(uwsgi_cmd))
        if not options.dryrun:
            if  call(uwsgi_cmd) != 0:
                print "Stop failed .. process already dead?"
            if os.path.exists (pidfile):
                os.remove (pidfile)
    elif command is 'start':
        #uwsgi_opts = cfgopt['uwsgi']
        uwsgi_cmd = ['uwsgi', '--ini-paste', cfg_file,
#                     '--env', 'LC_ALL=en_US.UTF-8',
#                     '--env', 'LANG=en_US.UTF-8',
                     '--daemonize', cfgopt['logfile'],
                     '--pidfile', cfgopt['pidfile']]
        uwsgi_cmd.extend (args)
        verbose('Executing: ' + ' '.join(uwsgi_cmd))
        if not options.dryrun:
            if call(uwsgi_cmd) != 0:
                print "Start failed"
    return processes


def worker_command (command, options, cfgopt, processes):
    def verbose(msg):
        if options.verbose:
            print msg

    pidfile = os.path.join(cfgopt['pid_dir'], 'worker.pid')
    logfile = os.path.join(cfgopt['log_dir'], 'worker.log')

    if command in (  'stop', 'restart') :
        kill_pidfile (pidfile)

    if command in  ( 'start', 'restart') :
        worker_cmd = ['celery', 'worker',  '--app=bq.celery.app:app', '--loglevel=debug']    #TODO: change loglevel back to info/warn?
        worker_cmd.append('--pidfile=%s' % pidfile)
        worker_cmd.append('--logfile=%s' % logfile)
        if not options.wait:
            worker_cmd.append ('-D')

        verbose ('Executing: %s' % ' '.join(worker_cmd))
        if not options.dryrun:
            processes.append(Popen(worker_cmd))

    return processes



BACKENDS = {
    'pserve': pserve_command,
    'uwsgi': uwsgi_command,
}


def logger_command(command, cfgopt, processes):
    pidfile = os.path.join(cfgopt['pid_dir'], 'bisque_logger.pid')

    launcher  = shlex.split (cfgopt['logging_server'])

    print "%sing logging service" % command
    if command is 'start':
        with open(os.devnull, 'w') as fnull:
            #logger = Popen(cfgopt['logging_server'], stdout=fnull, stderr=fnull, shell=True)
            logger = Popen(launcher, shell= (os.name == 'nt') )
        if logger.returncode is None and logger.pid:
            with open(pidfile, 'w') as pd:
                pd.write("%s\n" % logger.pid)
        else:
            print "log_service pid %s with code %s" % (logger.pid, logger.returncode)
        processes.append(logger)
    elif command is 'stop':
        if  os.path.exists (pidfile):
            with open(pidfile, 'r') as pd:
                pid = int (pd.read())
            kill_process (pid)
            os.remove (pidfile)
        else:
            print "No pid file for logging server"


def server_operation(command, options, *args):
    """Run a multi-server command to start several bisque jobs
    """
    def verbose(msg):
        if options.verbose:
            print msg

    cfg_file=SITE_CFG
    site_cfg = options.site or find_site_cfg(cfg_file)
    if site_cfg is None:
        print "Cannot find site.cfg.. please make sure you are in the bisque dir"
        return
    site_dir = os.path.dirname(os.path.abspath(site_cfg))

    verbose('using config : %s' % site_cfg)
    try:
        config = readhostconfig(site_cfg)
        verbose("SERVERS %s" % (config['servers'].keys()))
        processes = []
        cfgopt = {} # {'root': config['root']}
        cfgopt['site_dir'] = site_dir
        cfgopt['site_cfg'] = site_cfg
        cfgopt['virtualenv'] = os.getenv('VIRTUAL_ENV')
        for f in ('log_dir', 'pid_dir', 'logging_server', 'celery'):
            if f in config:
                cfgopt[f] = config[f]

        if not os.path.exists (config['top_dir']):
            print "Please check your site.cfg.  bisque.paths.root is not set correctly"
            return
        os.chdir (config['top_dir'])
        # Get the backend
        backend = config.get('backend', None)
        verbose("using backend: " + str(backend))
        if backend == None:
            verbose("Backend not configured. defaulting to paster")
            backend = 'pserve'
        backend_command = BACKENDS[backend]

        # Process non-server commands
        if command == 'list':
            print "ARGS: %s" % (args,)
            for server, params in  config['servers'].items():
                print "server %s  : %s " % (server, params)
            return

        if not args and 'logging_server' in cfgopt:
            if command in ('restart'):
                logger_command ('stop', cfgopt, processes)
            if command in ('start', 'restart'):
                logger_command ('start', cfgopt, processes)


        if 'celery' in cfgopt:
            worker_command (command, options, cfgopt, processes)

        for key, serverspec in sorted(config['servers'].items()):

            if args and key not in args:
                continue

            print "%sing %s" % (command, key)

            cfgopt['server_name'] = key
            cfgopt['services_enabled'] = ','.join([
                l.strip() for l in serverspec.pop('services_enabled', '').split(',')])
            cfgopt['services_disabled'] = ','.join([
                l.strip() for l in serverspec.pop('services_disabled', '').split(',')])
            cfgopt['url'] = serverspec.pop('url')
            fullurl = urlparse (cfgopt['url'])
            cfgopt['host'] = fullurl[1].split(':')[0]
            cfgopt['port'] = str(fullurl.port)
            cfgopt['logfile'] = os.path.join(config['log_dir'], LOG_TEMPL % cfgopt['port'])
            cfgopt['pidfile'] = os.path.join(config['pid_dir'], PID_TEMPL % cfgopt['port'])
            cfgopt['uwsgi']  = serverspec.pop('uwsgi', None)

            cfg_file_name =  "%s_%s.cfg" % (key, backend)
            cfg_file  = find_site_cfg(cfg_file_name)
            if not cfg_file:
                print ("Cannot find config file %s" % cfg_file_name)
                print ("Please run bq-admin setup configuration")
                return

            if command in ('stop', 'restart'):
                backend_command ('stop', options, cfgopt, processes, cfg_file)
                error = None
                for proc in processes:
                    try:
                        proc.wait()
                    except KeyboardInterrupt:
                        error = True

                if error is not None and backend != 'uwsgi':
                    print 'Paste windows error while stopping process, re-running'
                    processes = paster_command('stop', options, cfgopt, processes, args)
                    for proc in processes:
                        proc.wait()
                    print 'Recovered after error and successfully stopped daemon'

                processes = []

            if command in ('start', 'restart'):
                if os.path.exists(cfgopt['pidfile']):
                    if options.force:
                        print 'old pid file: %s exists! restarting...' % cfgopt['pidfile']
                        backend_command("stop", options, cfg_file, processes, args)
                        time.sleep(5)
                    else:
                        print "Can't start because of existing PID file"
                        sys.exit(2)
                processes = backend_command('start', options, cfgopt, processes, cfg_file)

        if not args and 'logging_server' in cfgopt:
            if command in ('stop'):
                logger_command ('stop', cfgopt, processes)

        if options.wait:
            for proc in processes:
                proc.wait()

    except KeyboardInterrupt:
        pass



class server(object):
    desc = "Start or stop a bisque server"

    def __init__(self, version):
        parser = optparse.OptionParser(
                    usage="%prog servers [options] start|stop|restart",
                    version="%prog " + version)
        parser.add_option("--reload", action="store_true", help="autoreload for development" )
        parser.add_option("-n", "--dryrun", action="store_true", help="Dry run and show commands")
        parser.add_option("-v", "--verbose", action="store_true", help="show commands as run" )
        parser.add_option("-w", "--wait", action="store_true", help="wait for children" )
        parser.add_option("-s", "--site", help="specify location of site.cfg" )
        parser.add_option("-f", "--force", action="store_true", default=False, help="try force start or stop: ignore old pid files etc." )

        options, args = parser.parse_args()
        self.command = self.options = None
        if len(args) < 1 or args[0] not in ['start', 'stop', 'restart', 'echo', 'list' ]:
            parser.print_help()
            return

        if options.dryrun:
            options.verbose = True

        self.options = options
        self.command = args[0]
        self.args = args[1:]

    def run(self):
        #Check for self.command in init..
        if self.command:
            server_operation(self.command, self.options, *self.args)
