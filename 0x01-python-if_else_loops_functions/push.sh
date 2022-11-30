#!/bin/bash

echo "Enter file name: "
read file_name
git add $file_name

echo "Enter commit message: "
read commit_message
git commit -m "$commit_message"

git push

