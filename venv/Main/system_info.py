import psutil

# print(psutil.cpu_times())

# for x in range(3):
#     print(psutil.cpu_percent(interval=0.5, percpu=True))

# print(psutil.cpu_count(logical=False))
#print(psutil.disk_partitions())

print(psutil.net_if_addrs())