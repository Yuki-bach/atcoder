#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <task_name>"
    exit 1
fi

TASK=$1

## Oxlint
npx oxlint solutions_ts/$TASK/answer.ts
if [ $? -ne 0 ]; then
    echo "Oxlint found issues."
    exit 1
fi

## Run
npx tsx solutions_ts/$TASK/answer.ts < solutions_ts/$TASK/input.txt
