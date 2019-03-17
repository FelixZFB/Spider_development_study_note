# 以时间戳作为名称命名图片
# 图片是按顺序下载的，按顺序保存
# 可以选择时间戳的秒数作为图片的命名

import time
t = time.time()
t1 = list(str(t))
filename = ''.join(t1[0:10]) + '.jpg'
print(filename)