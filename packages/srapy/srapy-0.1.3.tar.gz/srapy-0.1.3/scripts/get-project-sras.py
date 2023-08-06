#!/usr/bin/env python
from __future__ import print_function
from Bio import Entrez
from docopt import docopt
from os import path
import sys

import srapy
from srapy import (
    get_sample_runs,
    download_run,
)


CLI_USAGE = """
USAGE:
    get-project.py [-e EMAIL -d OUTDIR] -p PROJECT_ID

OPTIONS:
    -e EMAIL        Your email, to provide to Bio.Entrez
                    [default: '']
    -d OUTDIR       Output directory, must exist. [default: .]
    -p PROJECT_ID   BioProject ID
"""


def main(argv=sys.argv[1:]):
    opts = docopt(CLI_USAGE, argv=argv)
    proj_id = int(opts['-p'])
    Entrez.email = opts['-e']
    outdir = opts['-d']

    if not path.isdir(outdir):
        print("ERROR: output directory '{}' doesn't exitst".format(outdir),
              file=sys.stderr)
        exit(1)

    for sra_id in get_sample_runs(proj_id):
        download_run(sra_id)


if __name__ == "__main__":
    print("SRApy version", srapy.__version__, file=sys.stderr)
    main()
