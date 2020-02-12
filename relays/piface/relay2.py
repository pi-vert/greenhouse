import pifaceio, time
pf = pifaceio.PiFace()

while True:
    pf.write(pf.read())
    time.sleep(.01)
