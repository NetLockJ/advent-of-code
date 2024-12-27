#!/bin/bash

echo "Year:"
read year
cd $year

for i in {1..25}
do
	cd "Day-$i"
    rm *.txt
	cd ..
done

echo "Removed inputs"