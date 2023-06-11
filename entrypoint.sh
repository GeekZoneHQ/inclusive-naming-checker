#!/bin/bash

#find and checkout repo
readme="$(find -type f -maxdepth 2 -iname "readme.md")"
repoPath="${readme:0:-10}"
#previously hard coded main, should now get name of branch being pulled to
git checkout main

#find file paths of changed files for python script
#branch name hard coded again
git diff --name-only --stat=10000 --output=/home/root/working/changed-files-paths.txt main^ main

python3 /home/root/working/inclusive-naming-checker.py

cp /home/root/working/output.md /home/root/working/output

#move markdown file to output