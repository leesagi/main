#!/usr/bin/python

import subprocess

CMD = "git config --global push.default simple"
gPull = subprocess.check_output(CMD, stderr=subprocess.STDOUT, shell=True)
print gPull

CMD = "git config --global user.name 'GiddyUp'"
gPull = subprocess.check_output(CMD, stderr=subprocess.STDOUT, shell=True)
print gPull

CMD = "git config --global user.email giddyup@roku.com"
gPull = subprocess.check_output(CMD, stderr=subprocess.STDOUT, shell=True)
print gPull

CMD = "git pull"
gPull = subprocess.check_output(CMD, stderr=subprocess.STDOUT, shell=True)
print gPull

CMD = "s3cmd sync . s3://ods-working/git/"
gPull = subprocess.check_output(CMD, stderr=subprocess.STDOUT, shell=True)
print gPull