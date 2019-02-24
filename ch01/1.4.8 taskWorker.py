# coding: utf-8
import time
from multiprocessing.managers import BaseManager
# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass
# 第一步：使用QueueManager注册用于获取Queue的方法名称
# 任务进程只能通过来在网络上获取Queue
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# 第二步：连接到服务器,端口和验证口令保持与服务进程中完全一致
server_addr = '127.0.0.1'
print("Connet to server %s..." % server_addr)
# 端口和验证口令与服务进程保持一致
m = QueueManager(address=(server_addr, 8001), authkey='qiye')
# 从网络连接
m.connect()
# 第三步：从网络上获取Queue对象，并进行本地化
task = m.get_task_queue()
result = m.ger_result_queue()
# 第四步：从task队列获取任务，并把结果写入到resul队列
while(not task.empty()):
    image_url = task.get(True, timeout=5)
    print("run task download %s..." % image_url)
    time.sleep(1)
    result.put("%s--->sucess" % image_url)
# 处理结束
print("worker exit.")