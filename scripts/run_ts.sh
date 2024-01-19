#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <task_name>"
    exit 1
fi

TASK=$1

npx ts-node solutions_ts/$TASK/answer.ts < solutions_ts/$TASK/input.txt