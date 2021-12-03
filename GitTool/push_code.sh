#!/bin/bash

if [ ! $1 ]; then
	remote_branch="master"
else
	remote_branch=$1
fi

git push origin HEAD:refs/for/$remote_branch
