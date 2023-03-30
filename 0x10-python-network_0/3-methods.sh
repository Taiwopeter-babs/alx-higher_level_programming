#!/bin/bash
# This script sends a request to a server to retrieve allowed methods
curl -sI "$1" | grep -i Allow | awk -F: '{for (i=2; i<=NF; i++) print $i}'
