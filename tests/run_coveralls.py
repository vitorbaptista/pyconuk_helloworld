#!/bin/env/python

import os
import subprocess


if (__name__ == '__main__') and ('TRAVIS' in os.environ):
    rc = subprocess.call('coveralls')
    raise SystemExit(rc)
