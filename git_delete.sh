#!/bin/bash
# delete deleted files from git repository
for i in `git status | grep deleted | awk '{print $3}'`; do git rm $i; done

