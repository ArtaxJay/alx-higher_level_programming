#!/bin/bash
# This script shows the res status code after making a GET req.
curl -s --output /dev/null -w "%{http_code}" "$1"
