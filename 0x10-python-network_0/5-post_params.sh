#!/bin/bash
# This script sends a POST request
curl -sX POST -H "Content-Type: application/x-www-form-urlencoded" -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
