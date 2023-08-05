#!/bin/bash

# ###############################################################
# SECTION: HELP
# ###############################################################

# Displays help text to user.
log_help_commands()
{
	local typeof=$1
	shift
	local cmds=$@
	for cmd in $cmds
	do
		"help_"$typeof"_"$cmd
		log
	done
}

# Displays help text to user.
exec_help()
{
	helpers=(
		help_metrics
		help_ops
	)

	log "------------------------------------------------------------------"
	for helper in "${helpers[@]}"
	do
		$helper
		log "------------------------------------------------------------------"
	done
}


