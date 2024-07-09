#!/bin/bash
# Script that sends a JSON POST request
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
