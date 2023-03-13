#!/usr/bin/env bash
# Automates basic git actions

arg1="$1"
arg2="$2"

git add $arg1

git commit -m "$arg2"

git push
