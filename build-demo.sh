#!/bin/bash

set -e

echo "Building default locale: english"
python3 publish_sb3.py -r demo -s https://coderdojotrento.github.io/publish-sb3/demo/ 

echo "Building italian locale"
python3 publish_sb3.py  -r demo-it -l it -s https://coderdojotrento.github.io/publish-sb3/demo-it/ 

