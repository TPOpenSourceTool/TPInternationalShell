#!/bin/sh  

sed -i '' "s/string-array/array/g" `grep string-array -rl ../../icarbonx-android-project/`

python android2xls.py -f ../../icarbonx-android-project/ -t ../xls/
