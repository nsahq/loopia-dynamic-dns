#!/bin/bash

isort *.py
black *.py --experimental-string-processing
flake8 *.py
