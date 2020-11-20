#!/bin/bash

# install package in develop mode without the script
python setup.py develop --user -x
python setup.py install_scripts -d /opt/jarvis
