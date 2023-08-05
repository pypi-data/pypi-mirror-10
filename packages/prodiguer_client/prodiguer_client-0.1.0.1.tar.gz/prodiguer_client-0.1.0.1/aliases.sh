# Supported command types.
declare -a command_types=(
	metrics
	ops
)

# Supported commands.
declare -a commands=(
	metrics-add
	metrics-add-batch
	metrics-delete
	metrics-fetch
	metrics-fetch-columns
	metrics-fetch-count
	metrics-fetch-file
	metrics-fetch-setup
	metrics-fetch-list
	metrics-format
	metrics-rename
	metrics-set-hashes
	ops-heartbeat
	ops-list-endpoints
)

# Set path to exec.sh.
PRODIGUER_SHELL_EXEC="$( dirname "${BASH_SOURCE[0]}" )"/shell/exec.sh

# Create command aliases.
for command in "${commands[@]}"
do
	alias prodiguer-client-$command=$PRODIGUER_SHELL_EXEC" "$command
done

# Create command type help aliases.
for command_type in "${command_types[@]}"
do
	alias help-prodiguer-client-$command_type=$PRODIGUER_SHELL_EXEC" help-"$command_type
done

# Create command help aliases.
for command in "${commands[@]}"
do
	alias help-prodiguer-client-$command=$PRODIGUER_SHELL_EXEC" help-"$command
done

# Unset work vars.
unset PRODIGUER_SHELL_EXEC
unset command_type
unset command_types
unset command
unset commands
