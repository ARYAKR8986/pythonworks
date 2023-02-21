import threading
def coder(numberr):
    print("coders:",numberr)
    return
threads = []
for i in range(5):
    t = threading.Thread(target=coder,args=(i,))
    threads.append(t)
    t.start()