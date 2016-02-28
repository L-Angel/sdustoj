#!/bin/bash
sudo kill `ps aux | egrep "^nobody .*? judger.py" | cut -d " "  -f4`
