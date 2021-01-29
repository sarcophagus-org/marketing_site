#!/usr/bin/env python3
import os
import sys
import glob
import shutil
import subprocess
from re import search


def remove_dir(dir_path):
    try:
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
    except OSError as e:
        print("Failed removing {}: {}".format(dir_path, e))
    else:
        print("Remove dir: {}".format(dir_path))


def create_dir(dir_path):
    try:
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
    except OSError as e:
        print("Failed creating {}: {}".format(dir_path, e))
    else:
        print("Create dir: {}".format(dir_path))


def read_file(file):
    try:
        if os.path.isfile(file):
            with open(file, 'r') as f:
                lines = f.readlines()
            return lines
    except (OSError, IOError) as e:
        print("Failed reading {}: {}".format(file, e))


def write_file(file, lines):
    try:
        if os.path.isfile(file):
            with open(file, 'r+') as f:
                f.write(lines)
    except (OSError, IOError) as e:
        print("Failed writing {}: {}".format(file, e))


def compare_lines(lines, needle):
    # This only finds the first occurrence.
    for line in lines:
        if search(needle, line):
            return lines.index(line)


def python_os():
    if sys.platform == 'win32':
        python = 'python'
    elif sys.platform == 'linux':
        python = 'python3'
    elif sys.platform == 'darwin':
        python = 'python3'
    else:
        python = 'python'

    return python


class ArweaveBuild:
    """
    This script builds the marketing site of Sarcophagus for the Arweave permaweb.
    Afterwards it outputs a command for deploying the site on Arweave.
    """

    def __init__(self):
        self.baseurl = 'baseurl: "."'
        self.config_file = os.getcwd() + '/' + '_config.yml'
        self.arweave_dir = os.getcwd() + '/' + '_site_arweave/'
        self.config_lines, self.html_files = [], []
        self.config_state = ''  # commented/uncommented
        self.index = False
        self.html_lines = ''
        self.GREEN, self.ENDC = '\033[92m', '\033[0m'

    def create_folder(self):
        # A separate build folder for Jekyll files for an Arweave deploy.
        remove_dir(self.arweave_dir)
        create_dir(self.arweave_dir)

    def get_config_lines(self):
        self.config_lines = read_file(self.config_file)

    def get_config_state(self):
        if compare_lines(self.config_lines, '#' + self.baseurl):
            self.config_state = 'commented'
        elif compare_lines(self.config_lines, self.baseurl):
            self.config_state = 'uncommented'
        else:
            print(
                'Could not find {} or {} in your Jekyll config file. Check your \'baseurl\' setting in _config.yml.'.format(
                    '#' + self.baseurl, self.baseurl))

    def commented_state(self):
        if self.config_state == 'commented':
            return True

    def uncommented_state(self):
        if self.config_state == 'uncommented':
            return True

    def get_index(self):
        # Get the line number of the baseurl: setting.
        if self.commented_state():
            self.index = compare_lines(self.config_lines, '#' + self.baseurl)
        elif self.uncommented_state():
            self.index = compare_lines(self.config_lines, self.baseurl)
        else:
            print('Could not get the line number of the \'baseurl\' setting in your config file.')

    def toggle_config(self):
        # We need a dot in front of some links
        if self.commented_state():
            self.config_lines[self.index] = self.config_lines[self.index][1:]
            write_file(self.config_file, "".join(self.config_lines))
            print('\nUncommented the baseurl setting in your Jekyll config.\n')
        if self.uncommented_state():
            self.config_lines[self.index] = '#' + self.config_lines[self.index]
            write_file(self.config_file, "".join(self.config_lines))
            print('\nCommented the baseurl setting in your Jekyll config.')

    def create_build(self):
        # Create a fresh build
        self.get_config_state()
        if self.uncommented_state():
            cmd = ['bundle', 'exec', 'jekyll', 'build', '--destination', self.arweave_dir]
            if sys.platform == 'win32':
                subprocess.run(cmd, shell=True, check=True)  # No user input here.
            else:
                subprocess.Popen(cmd, stdout=subprocess.PIPE)  # No user input here.
        elif self.commented_state():
            print('NOT READY for a build, config state was {}. Running a new instance of this script.'.format(
                self.config_state))
            cmd = [python_os(), os.getcwd() + '/arweave_build.py']
            if sys.platform == 'win32':
                subprocess.run(cmd, shell=True, check=True)  # No user input here.
            else:
                subprocess.Popen(cmd, stdout=subprocess.PIPE)
            exit()  # Exit the current instance, we are running a new one now.

    def read_files(self):
        # Search all 1st lvl html files for unconverted links (e.g. main menu).
        os.chdir(self.arweave_dir)
        self.html_files = glob.glob('*.html')

    def change_lines(self):
        # Change lines with ="/ to ="./
        for file in self.html_files:
            index_list, new_html = [], []
            the_file = self.arweave_dir + '/' + file
            with open(the_file, 'r+') as f:
                self.html_lines = f.readlines()
                new_html = self.replace_string(new_html)
            write_file(the_file, "".join(new_html))

    def replace_string(self, new_html):
        for line in self.html_lines:
            if search('="/', line):
                new_line = line.replace('="/', '="./')
                new_html.append(new_line)
            else:
                new_html.append(line)
        return new_html

    def deploy_build(self):
        # Print help for deploying the build to the Arweave permaweb
        print('\n' + self.GREEN + 'DONE. You can now deploy the build to Arweave with the following command:'
              + self.ENDC)
        print('\n' + self.GREEN + '$ arweave deploy-dir ' + self.arweave_dir +
              ' --key-file /<path to your keyfile>/<name of your keyfile>.json \n' + self.ENDC)

    def run(self):
        self.create_folder()
        self.get_config_lines()
        self.get_config_state()
        self.get_index()
        self.toggle_config()
        self.create_build()
        self.read_files()
        self.change_lines()
        self.get_config_state()
        self.toggle_config()
        self.deploy_build()


if __name__ == '__main__':
    AD = ArweaveBuild()
    AD.run()
