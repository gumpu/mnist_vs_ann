# vi: spell spl=en
#
import sys

truth_file = sys.argv[1]
prediction_file = sys.argv[2]

n = 1
print("digit_id,truth,prediction")
with open(truth_file, "r") as tf:
    with open(prediction_file, "r") as pf:
        for tline in tf:
            pline = pf.readline()
            if tline == pline:
                pass
            else:
                tline = tline.strip()
                pline = pline.strip()
                print("{},{},{}".format(n, tline, pline))
            n += 1

