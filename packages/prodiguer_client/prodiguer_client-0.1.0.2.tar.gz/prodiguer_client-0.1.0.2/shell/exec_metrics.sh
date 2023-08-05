#!/bin/bash

# ###############################################################
# SECTION: EXEC - METRICS COMMANDS
# ###############################################################

# Add metrics.
exec_metrics_add()
{
	if [ "$2" ]; then
		python $DIR_JOBS/exec_metrics_add.py --file=$1 --duplicate_action=$2
	else
		python $DIR_JOBS/exec_metrics_add.py --file=$1 --duplicate_action=skip
	fi
}

# Adds a batch of metrics.
exec_metrics_add_batch()
{
	if [ "$2" ]; then
		python $DIR_JOBS/exec_metrics_add_batch.py --directory=$1 --duplicate_action=$2
	else
		python $DIR_JOBS/exec_metrics_add_batch.py --directory=$1 --duplicate_action=skip
	fi
}

# Delete metric.
exec_metrics_delete()
{
	python $DIR_JOBS/exec_metrics_delete.py --group=$1 --filter=$2
}

# Fetch metric group.
exec_metrics_fetch()
{
	python $DIR_JOBS/exec_metrics_fetch.py --group=$1 --filter=$2 --encoding=json
}

# Fetch metric group columns.
exec_metrics_fetch_columns()
{
	python $DIR_JOBS/exec_metrics_fetch_columns.py --group=$1
}

# Fetch metrics group count.
exec_metrics_fetch_count()
{
	python $DIR_JOBS/exec_metrics_fetch_count.py --group=$1 --filter=$2
}

# Fetch metric group to file system.
exec_metrics_fetch_file()
{
	python $DIR_JOBS/exec_metrics_fetch_file.py --group=$1 --output_dir=$2
}

# List groups.
exec_metrics_fetch_list()
{
	python $DIR_JOBS/exec_metrics_fetch_list.py
}

# Format a set of metrics files.
exec_metrics_format()
{
	python $DIR_JOBS/exec_metrics_format.py --group=$1 --input_dir=$2 --output_dir=$3
}

# Fetch metric group line count.
exec_metrics_fetch_setup()
{
	python $DIR_JOBS/exec_metrics_fetch_setup.py --group=$1 --filter=$2
}

# Format a set of metrics files.
exec_metrics_rename()
{
	python $DIR_JOBS/exec_metrics_rename.py --group=$1 --new_name=$2
}

# Sets the hash identifiers over a set of metrics.
exec_metrics_set_hashes()
{
	python $DIR_JOBS/exec_metrics_set_hashes.py --group=$1
}
