#!/bin/bash
# This bash script gets he byte size of the HTTP protocol
# response header for the specified URL.
curl -s "$1" | wc -c
