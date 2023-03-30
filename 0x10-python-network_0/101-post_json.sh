#!/bin/bash
# This script posts a json file format to a server
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
