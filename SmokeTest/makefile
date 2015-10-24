#
#
CXXNET=$(HOME)/bin/cxxnet

score.csv : pred.txt
	python ../Tools/compare.py ../Processed/truth.txt pred.txt > score.csv

pred.txt : models/0005.model
	$(CXXNET) test.conf

models/0005.model : train.conf
	$(CXXNET) train.conf

clean :
	-rm -f models/*.model
	-rm -f score.csv
	-rm -f pred.txt

