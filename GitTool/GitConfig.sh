#!/bin/sh

 git config --global diff.tool vimdiff
 git config --global difftool.prompt false
 git config --global difftool.trustExitCode true
 git config --global alias.d difftool

 git config --global core.editor "vim"
