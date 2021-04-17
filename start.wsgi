#!/usr/bin/python
import os
import sys

# virtualenv
this_dir = os.path.dirname(os.path.abspath(__file__))
activate_this = this_dir + '/obsidian/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# anhadir dir de este fichero a path
sys.path.insert(0, this_dir)

from routes import app as application