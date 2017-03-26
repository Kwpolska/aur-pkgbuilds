#!/usr/bin/env python
# Usage: base64-encoded JSON on stdin
import base64
import io
import json
import os
import subprocess
import sys

BASEDIR = os.path.expanduser('~/git/aur-pkgbuilds')


def commitaur(msg):
    with open('.SRCINFO', 'wb') as fh:
        fh.write(subprocess.check_output(['makepkg', '--printsrcinfo']))
    subprocess.check_call(['git', 'add', '.'])
    subprocess.check_call(['git', 'commit', '-asm', msg])
    subprocess.check_call(['git', 'push', '-u', 'origin', 'master'])

data = base64.b64decode(sys.stdin.read().encode('utf-8'))
data = json.loads(data.decode('utf-8'))
msg = data['project'] + ' v' + data['version']
sys.stderr.write("[host] Updating AUR packages...\n")
sys.stderr.flush()

os.chdir(BASEDIR)
os.chdir(data['projectlc'])
with io.open('PKGBUILD', 'w', encoding='utf-8') as fh:
    fh.write(data['pkgbuild'])
commitaur(msg)
os.chdir(BASEDIR)

if data['use_git']:
    os.chdir(data['projectlc'] + '-git')
    subprocess.check_call(["sed", "s/pkgver=.*/pkgver="+data['gitver']+"/", "PKGBUILD", "-i"])
    commitaur(msg)
    os.chdir(BASEDIR)

subprocess.check_call(['./UPDATE-REQUIREMENTS.py'])
subprocess.check_call(['git', 'commit', '-asm', msg])
subprocess.check_call(['git', 'push'])
sys.stderr.write("[host] Done!\n")
sys.stderr.flush()
