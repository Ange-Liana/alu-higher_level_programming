#!/bin/bash
# Sends a GET request to the URL with a custom header
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
