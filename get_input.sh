#!/bin/bash
year=$(echo $(date -I) | grep -Eoa '[0-9]+')
echo $year[0]