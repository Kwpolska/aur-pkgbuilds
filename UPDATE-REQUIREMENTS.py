#!/usr/bin/python3
# Copyright © 2014–2015, Chris Warrick.
# All rights reserved.
# Licensed under the 3-clause BSD license.

"""requriements.txt generator"""

import pkgbuilder.utils

with open('PYTHON-PACKAGES.txt') as fh:
    aurpkgs = [i.strip() for i in fh.readlines() if i.strip()]

pkgs = {i.name: i.version for i in pkgbuilder.utils.msearch('Kwpolska') if i.name in aurpkgs}
newpkgs = {}

for _n, _v in pkgs.items():
    n = _n.split('-')[-1]
    v = _v.split('-')[0].split(':')[-1]
    if newpkgs.get(n, v) != v:
        print('==> WARNING: version conflict detected')
        print('==>          {0} found as {1} and {2}'.format(n, newpkgs[n], v))
        print()
    newpkgs[n] = v

with open('requirements.txt', 'w') as fh:
    for n, v in sorted(newpkgs.items()):
        o = '{0}=={1}\n'.format(n, v)
        print(o, end='')
        fh.write(o)

print('\n==> Written to requirements.txt.')
