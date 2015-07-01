#!/usr/bin/python

import subprocess

CMD = "git config --global push.default simple"
gPull = subprocess.check_output(CMD, stderr=subprocess.STDOUT, shell=True)
print gPull

CMD = "git push"
gPull = subprocess.check_output(CMD, stderr=subprocess.STDOUT, shell=True)
print gPull