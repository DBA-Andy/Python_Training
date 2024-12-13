#!/bin/bash

for ((i=1; i<=100; i++)); do
  nohup time ./cpu_stress_test_multiprocessing.py --processes 100 &
done
