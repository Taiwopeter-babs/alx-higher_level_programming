#!/bin/bash
# This script writes out only the status code
curl -s -o /dev/null -w "%{http_code}" "1"
