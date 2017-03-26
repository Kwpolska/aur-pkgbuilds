#!/usr/bin/python3
# Copyright © 2014–2017, Chris Warrick.
# All rights reserved.
# Licensed under the 3-clause BSD license.

"""requriements.txt generator"""

import pkgbuilder.utils
import sys

with open('PYTHON-PACKAGES.txt') as fh:
    aurpkgs = [i.strip() for i in fh.readlines() if i.strip()]

search = pkgbuilder.utils.msearch('Kwpolska')
search += pkgbuilder.utils.info('python-natsort')  # special casing
search_names = [i.name for i in search]

pkgs = {i.name: i.version for i in search if i.name in aurpkgs}
newpkgs = {}

unknown = [i for i in aurpkgs if i not in search_names]

for i in unknown:
    sys.stderr.write('==> WARNING: package {0} not found\n'.format(i))

for _n, _v in pkgs.items():
    n = _n.split('-')[-1]
    v = _v.split('-')[0].split(':')[-1]
    if newpkgs.get(n, v) != v:
        sys.stderr.write('==> WARNING: version conflict detected\n')
        sys.stderr.write('==>          {0} found as {1} and {2}\n\n'.format(n, newpkgs[n], v))
    newpkgs[n] = v

with open('requirements.txt', 'w') as fh:
    for n, v in sorted(newpkgs.items()):
        o = '{0}=={1}\n'.format(n, v)
        sys.stderr.write(o)
        fh.write(o)

sys.stderr.write('\n==> Written to requirements.txt.\n')
