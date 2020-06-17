#!/bin/bash

python3 -m pelican --ignore-cache && python3 -m pelican -l output -b 0.0.0.0 --ignore-cache
