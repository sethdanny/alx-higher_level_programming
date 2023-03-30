#!/bin/bash
# sends a request to the url and displays the size of the body of a response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
