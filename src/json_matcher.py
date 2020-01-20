#!/usr/bin/env python3

import json
import sys
from contains_matcher.matcher import contains

if len(sys.argv) <= 2 or len(sys.argv) > 3:
    print("Usage:", sys.argv[0], "<file_path> <pattern_as_json>")
else:
    doc = json.load(open(sys.argv[1]))
    pattern = json.loads(sys.argv[2])
    print("Pattern", "is" if contains(doc, pattern) else "is not", "contained.")
