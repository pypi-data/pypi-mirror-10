from __future__ import print_function

import os
import multiprocessing
from pulla.utils import is_this_a_git_dir

VERSION_WITH_C_FLAG_SUPPORT = "1.8.5"

class Pulla:
    ''' Pulla class
    '''
    def __init__(self, verbosity=None, recursive=None):
        self.verbosity = verbosity
        self.recursive = recursive
        self.tab_size = 20

    def pull_all(self, folder):
        for (_, dirnames, _) in os.walk(folder):
            threads = []
            for directory in dirnames:
                if len(directory) > self.tab_size:
                    self.tab_size = len(directory) + 5
                if is_this_a_git_dir(directory):
                    process = multiprocessing.Process(target=self.do_pull_in, args=[directory])
                    process.start()
                    threads.append(process)
            if not self.recursive:
                break
        return None

    def do_pull_in(self, directory):
        if self.verbosity:
            print('----------------------')
        status = self.perform_git_pull(directory)
        status_msg = 'Fail'
        if status == 0:
            status_msg = 'Success'
        print(self.get_formatted_status_message(directory, status_msg))
        if self.verbosity:
            print('----------------------')

    def perform_git_pull(self, directory):
        can_use_c_flag = self.get_git_version() >= VERSION_WITH_C_FLAG_SUPPORT
        if can_use_c_flag:
            cmd = 'git -C ' + directory + ' pull'
        else:
            os.chdir(directory)
            cmd = 'git pull'
        if self.verbosity:
            cmd += ' --verbose'
        else:
            cmd += ' &> /dev/null'
        status = os.system(cmd)
        if not can_use_c_flag:
            os.chdir('..')
        return status

    def get_formatted_status_message(self, directory, status_msg):
        return '{0:<30} {1:<10}'.format(os.path.join(directory), status_msg)
        # return '{0:<'+str(self.tab_size)+'} {1:<10}'.format(os.path.join(directory), status_msg)

    def get_git_version(self):
        han = os.popen('git --version')
        version_string = han.read()
        han.close()
        return version_string.split()[-1]
