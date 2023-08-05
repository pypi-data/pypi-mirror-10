#!/usr/bin/env sh
#

function pycd ()
{
  module_path=$(pycd.py find $1 --quiet)
  if [ "$module_path" != "" ]; then
    cd $module_path
  fi
}