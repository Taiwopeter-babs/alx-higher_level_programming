#!/bin/bash
# This script posts a json file format to a server
curl -s -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
