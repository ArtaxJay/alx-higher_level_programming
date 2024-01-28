#!/bin/bash
# Send a GET request to a given URL with a header variable. Alt: curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
curl -s --header "X-HolbertonSchool-User-Id: 98" "${1}"
