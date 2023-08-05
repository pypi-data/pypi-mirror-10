#!/bin/sh
# Run the pyessv test suite.
#

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
export PYTHONPATH=PYTHONPATH:$DIR
nosetests -v -s tests
