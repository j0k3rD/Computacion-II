import os
ret = os.fork()
if not ret:
    print("soy el hijo")
    print("chau, me muero..")
    sys.exit()
time.sleep(100)
