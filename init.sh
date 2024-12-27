#!/bin/bash

echo "Year:"
read year
mkdir $year
cd $year

for i in {1..25}
do 
	mkdir "Day-$i"
	cd "Day-$i"
	touch "input.txt"
	cd ..
done

echo "Finished making $year directory"
