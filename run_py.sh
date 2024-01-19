#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <task_name>"
  exit 1
fi

TASK=$1

python3 ./solutions_py/$TASK/answer.py < ./solutions_py/$TASK/input.txt
