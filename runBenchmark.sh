#!/bin/bash
#1600000 1500000 1400000 1300000 1200000 1100000 1000000 500000 400000 350000 300000

python frequency.py 1200000 600000 

for frequency in 250000; do

	python frequency.py $frequency

	python runBenchmark.py 2dfir-O3 80000000 25

	python runBenchmark.py blowfish-O3 950000000 25

	python runBenchmark.py crc32-O3 300000000 25

	python runBenchmark.py cubic-O3 50000000 25

	python runBenchmark.py dijkstra-O3 700000 25

	python runBenchmark.py fdct-O3 70000000 25

	python runBenchmark.py float_matmult-O3 18000000 25

	python runBenchmark.py int_matmult-O3 6500000 25

	python runBenchmark.py rijndael-O3 150000000 25

	python runBenchmark.py sha-O3 32000000 25

done

exit 0

