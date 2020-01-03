import psutil
import time
from datetime import date

def product_recycle_list_data() -> list:
    dataList = []
    for x in range(10):
        #print(x)
        dataList.append('a silple message')
    print(dataList)
    return dataList

def test():
    print([{'hello': ''.join('a simple message')}
           for x in range(10)])


#test()

#print(psutil.cpu_times())
#print(psutil.virtual_memory().percent)
#print(psutil.sensors_temperatures())
#a_list = ['a','b','c']
#print(str(a_list))
#print(psutil.net_io_counters().bytes_recv)
#time.sleep(3)
#print(psutil.net_io_counters().bytes_recv)

#print(type(str(date.today())))
#print(date.today().weekday())
print(time.localtime().tm_zone)
print(time.localtime().tm_min)
print (time.strftime("%H:%M", time.localtime()))
