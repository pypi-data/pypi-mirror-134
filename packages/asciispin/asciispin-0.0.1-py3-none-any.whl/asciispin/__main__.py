import time, sys
def ch(c):
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write("\r")
    sys.stdout.flush()
while True:
    ch("|")
    ch("/")
    ch("-")
    ch("\\")