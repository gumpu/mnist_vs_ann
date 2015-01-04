n = 1
print("digit_it,truth,prediction")
with open("truth.txt", "r") as tf:
    with open("pred.txt", "r") as pf:
        for tline in tf:
            pline = pf.readline()
            if tline == pline:
                pass
            else:
                tline = tline.strip()
                pline = pline.strip()
                print("{},{},{}".format(n, tline, pline))
            n += 1

