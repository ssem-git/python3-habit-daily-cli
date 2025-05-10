#!/bin/sh
echo 'Type "RESET" (all caps) to reset the program, or CTRL+D to QUIT.' 
read -p "> " input

if [ "$input" = "RESET" ]; then
    echo "PROGRAM RESET"
    echo "RUN PROGRAM.PY TO SETUP"
    rm -rf ./profile.json
else
  echo "OPERATION CANCELLED"
fi
