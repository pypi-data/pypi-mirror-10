#!/bin/bash

# ###############################################################
# SECTION: INITIALIZE PATHS
# ###############################################################

# Path to CLI shell.
declare DIR_SHELL=$DIR

# Path to repo root.
declare DIR_ROOT="$(dirname "$DIR")"

# Path to CLI jobs.
declare DIR_JOBS=$DIR_SHELL/jobs

# Extend python path.
export PYTHONPATH=$PYTHONPATH:$DIR_ROOT
