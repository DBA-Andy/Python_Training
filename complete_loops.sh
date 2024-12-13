#!/bin/bash

SCROLLING_DOT="."

for ((i=0; i<=100000000; i++)); do
    if (($i % 1000000 == 0))
    then 
       SCROLLING_DOT="$SCROLLING_DOT."
       echo $i
    fi
done
