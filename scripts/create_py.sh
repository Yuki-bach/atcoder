#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <problem_name>"
  exit 1
fi

PROBLEM=$1
DESTINATION="solutions_py/$PROBLEM"

# Check the directory exists
if [ -d "$DESTINATION" ]; then
  echo "Error: Directory $DESTINATION already exists."
  exit 1
else
  cp -r solutions_py/sample $DESTINATION
  echo "Created folder: $DESTINATION"
  code -r $DESTINATION/*
fi
