#!/bin/bash
# Script that displays the size of the response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
