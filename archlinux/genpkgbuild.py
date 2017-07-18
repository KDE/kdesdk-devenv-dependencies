#!/usr/bin/env python3

import sys
import json
import hashlib
import subprocess
import datetime

def sha256(fname):
    hash_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def main():
    jsoninfo = subprocess.check_output(["./packages", "packages-json", "archlinux"])
    deps = json.loads(jsoninfo.decode('utf-8'))

    with open('archlinux/PKGBUILD.in') as infile, open('archlinux-output/PKGBUILD', 'w') as outfile:
        replacements = {
            "@DEPENDS@": "\n         ".join(deps["required"]),
            "@OPTDEPENDS@": "\n            ".join(deps["suggested"]),
            "@SHA256@": "\n            ".join([sha256("org.kde.development.appdata.xml"),sha256("kdesdk-devenv-dependencies.svg")]),
            "@PKGVER@": datetime.datetime.now().strftime('%Y%m%d')
        }

        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)

if __name__ == "__main__":
    sys.exit(main())
