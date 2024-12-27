#!/bin/bash

year=$(cd ..; basename $(pwd))
day=$(basename $(pwd))
day=$(echo $day | cut -c 5-)
echo $(echo $(date -I) | grep -Eoa '[0-9]+')
cookie=$(cd ..; cd ..; cat 'cookie.txt')
touch input.txt
curl 'https://adventofcode.com/'$year'/day/'$day'/input' -H 'Cookie: session='$cookie'' > 'input.txt'