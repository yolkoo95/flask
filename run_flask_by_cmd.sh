#!/bin/bash
# Program: this program will help you run flask in terminal. Since default FLASK_APP=app.py, 
# it will throw a error if your filename != app.py. this program can be called by following, 
# sh run_flask_by_cmd.py <filename>

if [ ! $# -lt 2 ]; then
	echo "input error: fun_flask_by_cmd.py <filename>"
	exit 1
fi

filename=$1

export FLASK_APP=$filename

