#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <task_name>"
  exit 1
fi

TASK=$1

ruby ./solutions_rb/$TASK/answer.rb < ./solutions_rb/$TASK/input.txt
