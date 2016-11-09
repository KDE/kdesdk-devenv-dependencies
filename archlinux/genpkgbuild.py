#!/usr/bin/env python3

import sys
import json
import hashlib
import subprocess

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    jsoninfo = subprocess.check_output(["./packages", "packages-json"])
    deps = json.loads(jsoninfo.decode('utf-8'))

    with open('archlinux/PKGBUILD.in') as infile, open('archlinux-output/PKGBUILD', 'w') as outfile:
        replacements = {
            "@DEPENDS@": " ".join(deps["required"]),
            "@OPTDEPENDS@": " ".join(deps["suggested"]),
            "@MD5@": md5("org.kde.development.appdata.xml")
        }

        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)

if __name__ == "__main__":
    sys.exit(main())
