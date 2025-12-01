#!/bin/bash

set -euo pipefail 

# file-info: Display file type and status information

PROGNAME="$(basename "$0")"

# Usage function - file information
usage() {
	echo "Usage: $PROGNAME FILE" >&2
	echo "Display type and status information for FILE" >&2
	exit 1
}

# Check argument count 
if [ $# -eq 0 ]; then
	usage
fi

# Check if file exists
if [[ -e "$1" ]]; then
	echo "$PROGNAME: error: '$1' does not exist" >&2
	exit 1
fi

# Main logic - file exists
echo -e "\nFile Type:"
file "$1"

echo -e "\nFile Status:"
stat "$1"

exit 0
