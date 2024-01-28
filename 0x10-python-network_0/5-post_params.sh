#!/bin/bash
# This script sends a POST HTTP rew to the specified url.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
