
# 
CXXNET=$(HOME)/bin/cxxnet

score.csv : pred.txt
	python Tools/compare.py Processed/truth.txt pred.txt > score.csv

pred.txt : models/0015.model
	$(CXXNET) PRED.conf

Processed/truth.txt : Tools/lab2ascii.py 
	python Tools/lab2ascii.py > Processed/truth.txt

#

