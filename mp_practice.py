'''
create time 20210722
'''


import multiprocessing as mp
import time

class practice():

    def __init__(self,num):
        self.num = num
    
    def cal(self):
        for i in range(self.num+1):
            print(i)

class childprocess(mp.Process):

    def __init__(self, num):
        mp.Process.__init__(self)
        self.num = num

    def run(self):
        p = mp.current_process()
        print("New process -> [%s] %s" % (p.pid, p.name))
        obj = practice(self.num)
        obj.cal()
        time.sleep(1)
        print("[%s] %s terminated" % (p.pid, p.name))
    
if __name__ == "__main__":
    proc = []
    for i in range(5):
        proc.append(childprocess(i))
        proc[i].start()
    
    for i in range(5):
        proc[i].join()

    print('done')
        
