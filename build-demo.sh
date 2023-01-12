#!/bin/bash

set -e

echo "Building default locale: english"
python3 sb3_to_turbowarp.py  -s https://coderdojotrento.github.io/sb3-to-turbowarp/demo -r demo

echo "Building italian locale"
python3 sb3_to_turbowarp.py  -s https://coderdojotrento.github.io/sb3-to-turbowarp/demo-it -r demo-it -l it

