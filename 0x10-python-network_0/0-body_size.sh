#!/bin/bash
# This script sends a request to a server and prints size - content-length
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' 
