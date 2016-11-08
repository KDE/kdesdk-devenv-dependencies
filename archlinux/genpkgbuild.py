#!/usr/bin/env python3

import sys
import json
import subprocess

def main():
    jsoninfo = subprocess.check_output(["./packages", "packages-json"])
    deps = json.loads(jsoninfo.decode('utf-8'))

    with open('archlinux/PKGBUILD.in') as infile, open('archlinux-output/PKGBUILD', 'w') as outfile:
        replacements = { "@DEPENDS@": " ".join(deps["required"]), "@OPTDEPENDS@": " ".join(deps["suggested"]) }

        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)

if __name__ == "__main__":
    sys.exit(main())
