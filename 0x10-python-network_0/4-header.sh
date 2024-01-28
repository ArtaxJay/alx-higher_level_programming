#!/bin/bash
# Send a GET request to a given URL with a header variable.
curl -s --header "X-HolbertonSchool-User-Id: 98" "${1}"
