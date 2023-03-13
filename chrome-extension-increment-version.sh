#!/bin/bash

git diff --cached --name-only | grep manifest.json || sed -ri 's/(\s*)"version": "([^\.]+?\.[^\.]+?\.[^\.]+?)(\.([^\.]+))?"/echo "\1\\"version\\": \\"\2\.$((\4 + 1))\\""/e' manifest.json
