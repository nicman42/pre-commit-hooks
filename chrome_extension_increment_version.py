#!/bin/env python3

import re
import subprocess

MANIFEST='manifest.json'

def main():
    if MANIFEST in subprocess.run(['git', 'diff', '--cached', '--name-only'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n'):
        exit(0)

    manifest = ''
    with open(MANIFEST, 'r') as file:
        for line in file:
            m = re.match(r'^(.*"version": ")([^.]+?\.[^.]+?\.[^.]+?)(\.([^.]+))?(".*)$', line, re.DOTALL)
            if m:
                v1 = m.group(2)
                v2 = m.group(4)
                if v2:
                    v2 = int(v2) + 1
                else:
                    v2 = '1'
                version = f'{v1}.{v2}'
                line = f'{m.group(1)}{version}{m.group(5)}'

            manifest += line

    with open(MANIFEST, 'w') as file:
        file.write(manifest)

if __name__ == "__main__":
    main()