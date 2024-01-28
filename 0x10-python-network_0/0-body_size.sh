#!/bin/bash
# This bash script gets the byte size of the HTTP res header
curl -s "$1" | wc -c
