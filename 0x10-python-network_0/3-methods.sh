#!/bin/bash
# This script lists all HTTP methods.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
