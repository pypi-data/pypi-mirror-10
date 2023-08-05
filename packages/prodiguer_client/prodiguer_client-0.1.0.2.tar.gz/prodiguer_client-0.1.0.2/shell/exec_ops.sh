#!/bin/bash

# ###############################################################
# SECTION: EXEC - OPS COMMANDS
# ###############################################################

# Test to see if remote API is up.
exec_ops_heartbeat()
{
	python $DIR_JOBS/exec_ops_heartbeat.py
}

# List set of endpoints exposed by remote API.
exec_ops_list_endpoints()
{
	python $DIR_JOBS/exec_ops_list_endpoints.py
}
