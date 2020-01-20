#!/bin/bash

echo "Running tests with python2.7"
/usr/bin/env python2.7 contains_matcher_tests.py -v

echo "Running tests with python3"
/usr/bin/env python3 contains_matcher_tests.py -v
