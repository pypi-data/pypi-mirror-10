#!/bin/bash

# ###############################################################
# SECTION: INITIALIZATION
# ###############################################################

declare -a initializers=(
	'init_action'
	'init_helpers'
	'init_paths'
	'exec_metrics'
	'exec_ops'
	'help'
	'help_metrics'
	'help_ops'
)
for initializer in "${initializers[@]}"
do
	source $DIR/$initializer.sh
done
