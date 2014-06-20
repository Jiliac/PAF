#!/bin/bash

for frequency in 250000 300000 350000 400000 500000 600000 800000 900000 1000000 1100000 1200000 1300000 1400000 1500000 1600000; do

	python frequency.py $frequency

	python runBenchmark.py 2dfir-O3 800000000 25

	python runBenchmark.py crc32-O3 3000000000 25

	python runBenchmark.py dijkstra-O3 700 25

	python runBenchmark.py float_matmult-O3 180000000 25

	python runBenchmark.py rijndael-O3 1500000000 25

	python runBenchmark.py blowfish-O3 950000000 25

	python runBenchmark.py cubic-O3 500000000 25

	python runBenchmark.py fdct-O3 700000000 25

	python runBenchmark.py int_matmult-O3 65000000 25

	python runBenchmark.py sha-O3 32000000 25

done

exit 0

