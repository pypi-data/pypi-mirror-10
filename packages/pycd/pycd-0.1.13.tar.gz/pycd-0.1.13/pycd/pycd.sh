#!/usr/bin/env sh
#

function pycd ()
{
  module_path=$(pycd_py find $1 --quiet)
  if [ "$module_path" != "" ]; then
    cd $module_path
  fi
}