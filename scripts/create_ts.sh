#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <problem_name>"
    exit 1
fi

PROBLEM=$1
DESTINATION="solutions_ts/$PROBLEM"

# Check the directory exists
if [ -d "$DESTINATION" ]; then
  echo "Error: Directory $DESTINATION already exists."
  exit 1
else
  cp -r solutions_ts/sample $DESTINATION
  echo "Created folder: $DESTINATION"
fi
