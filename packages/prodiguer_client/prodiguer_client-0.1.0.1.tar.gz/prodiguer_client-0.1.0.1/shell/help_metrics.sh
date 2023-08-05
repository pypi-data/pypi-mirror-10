#!/bin/bash

# ###############################################################
# SECTION: HELP - METRICS COMMANDS
# ###############################################################

help_metrics_add()
{
	log "prodiguer-client-metrics-add PATH DUPLICATE_ACTION"
	log "Description: adds a group of metrics from a json file" 1
	log "PATH: path to a metrics file" 1
	log "DUPLICATE_ACTION: Action to take when adding a duplicate metric (skip | force)" 1
}

help_metrics_add_batch()
{
	log "prodiguer-client-metrics-add-batch PATH"
	log "Description: adds batches of metrics from json files" 1
	log "PATH: path to a directory containing formatted metrics files" 1
	log "DUPLICATE_ACTION: Action to take when adding a duplicate metric (skip | force)" 1
}

help_metrics_delete()
{
	log "prodiguer-client-metrics-delete GROUP-ID [FILTER]"
	log "Description: deletes a group of metrics" 1
	log "GROUP-ID: group identifier" 1
	log "FILTER: path to a metrics query filter file" 1
}

help_metrics_fetch()
{
	log "prodiguer-client-metrics-fetch GROUP-ID [FILTER]"
	log "Description: fetches a group of metrics" 1
	log "GROUP-ID: group identifier" 1
	log "FILTER: path to a metrics query filter file" 1
}

help_metrics_fetch_columns()
{
	log "prodiguer-client-metrics-fetch-columns GROUP-ID"
	log "Description: fetches list of metric group columns" 1
	log "GROUP-ID: group identifier" 1
}

help_metrics_fetch_count()
{
	log "prodiguer-client-metrics-fetch-count GROUP-ID [FILTER]"
	log "Description: fetches number of lines within a metric group" 1
	log "GROUP-ID: group identifier" 1
	log "FILTER: path to a metrics query filter file" 1
}

help_metrics_fetch_file()
{
	log "prodiguer-client-metrics-fetch-file GROUP-ID OUTPUT-DIR"
	log "Description: fetches a group of metrics & saves them to file system" 1
	log "GROUP-ID: group identifier" 1
	log "OUTPUT-DIR: path to a directory to which downloaded files will be written" 1
}

help_metrics_fetch_list()
{
	log "prodiguer-client-metrics-fetch-list"
	log "Description: lists all metric group names" 1
}

help_metrics_format()
{
	log "prodiguer-client-metrics-format GROUP-ID INPUT-DIR OUTPUT-DIR"
	log "Description: formats metrics file(s) in readiness for upload" 1
	log "GROUP-ID: group identifier" 1
	log "INPUT-DIR: path to a directory containing unformatted metrics files" 1
	log "OUTPUT-DIR: path to a directory to which formatted files will be written" 1
}

help_metrics_fetch_setup()
{
	log "prodiguer-client-metrics-fetch-setup GROUP-ID [FILTER]"
	log "Description: fetches a metric group's distinct column values" 1
	log "GROUP-ID: group identifier" 1
	log "FILTER: path to a metrics query filter file" 1
}

help_metrics_rename()
{
	log "prodiguer-client-metrics-rename GROUP-ID NEW-GROUP-ID"
	log "Description: renames a metric group" 1
	log "GROUP-ID: group identifier" 1
	log "NEW-GROUP-ID: new group identifier" 1
}

help_metrics_set_hashes()
{
	log "prodiguer-client-metrics-set-hashes GROUP-ID"
	log "Description: resets the hash identifiers for a metric group" 1
	log "GROUP-ID: group identifier" 1
}

help_metrics()
{
	commands=(
		add
		add_batch
		delete
		fetch
		fetch_columns
		fetch_count
		fetch_list
		format
		fetch_setup
		rename
		set_hashes
	)
	log_help_commands "metrics" ${commands[@]}
}
