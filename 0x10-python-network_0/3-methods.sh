#!/bin/bash
# This script sends a request to a server to retrieve allowed methods
curl -sI "$1" | grep -i Allow | cut -c 8-
