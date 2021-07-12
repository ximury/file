import datetime
import os
import time

dir = '/home/wyj/VscodeProjects/testnginx/dist/video/'
file = 'out202104211438.flv'

state = os.stat(dir + file)

print(state)
print(state.st_size)
print(state.st_ctime)  # 获取文件创建时间
print(state.st_mtime)  # 获取文件最后修改时间
print(state.st_atime)  # 获取文件最后访问时间

time1 = state.st_mtime.__str__().split('.')[0]
# time1 = int(state.st_mtime).__str__()  # 与上同效
print(time1)
time2 = time.strftime("%Y.%m.%d-%H:%M:%S", time.localtime(int(time1)))
print(time2)

time3 = time.time()
print(time3)

print(state.st_mtime < time.time())


def get_file_size(file):
    fsize = os.path.getsize(file)
    print(fsize)
    fsize = fsize / float(1024 * 1024)
    return '%.2f MB' % (round(fsize, 2))


print(get_file_size(dir + file))
