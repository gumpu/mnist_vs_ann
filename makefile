# 


# score.csv : pred.txt
# 	python Tools/compare.py Processed/truth.txt pred.txt > score.csv

Processed/truth.txt : Tools/lab2ascii.py 
	python Tools/lab2ascii.py > Processed/truth.txt

#
clean :
	make -C SmokeTest clean

