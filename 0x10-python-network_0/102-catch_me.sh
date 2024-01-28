#!/bin/bash
# This scripts prints d msg "You got me!" by making a req to 0.0.0.0:5000/catch_me.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
