#!/usr/bin/bash
# takes in a URL, sends a request to that URL
curl -s -w "%{size_download}" -o /dev/null "$1"
