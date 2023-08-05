#!/bin/bash

# ###############################################################
# SECTION: HELP - METRICS COMMANDS
# ###############################################################

help_ops_heartbeat()
{
	log "prodiguer-client-ops-heartbeat"
	log "Description: tests to see if remote API is up." 1
}

help_ops_list_endpoints()
{
	log "prodiguer-client-ops-list-endpoints"
	log "Description: Lists set of endpoints exposed by remote API" 1
}

help_ops()
{
	commands=(
		heartbeat
		list_endpoints
	)
	log_help_commands "ops" ${commands[@]}
}
