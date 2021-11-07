from mss.darwin import MSS as mss

with mss() as sct:
    for filename in sct.save():
        print(filename)
