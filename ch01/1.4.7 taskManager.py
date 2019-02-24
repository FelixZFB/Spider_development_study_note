# 服务进程在windows系统和Linux系统上有所不同
# 创建一个分布式进程：包括服务进程和任务进程
# 多个进程之间的通信使用Queue
# 该代码为服务进程

# -*- coding:utf-8 -*-
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 第一步：定义任务个数，定义收发队列，
# 既建立任务队列和结果队列,用来存放任务和结果
task_number = 10
task_queue = queue.Queue(task_number)
result_queue = queue.Queue(task_number)
def get_task():
    global task_queue
    return task_queue
def get_result():
    global result_queue
    return result_queue

# 第二步：把上面创建的两个队列注册在网络上，利用register方法
# callable参数关联了Queue对象，将Queue对象在网络中暴露
# 先定义一个类继承BaseManager类
class QueueManager(BaseManager):
    pass
def win_run():
    # windows下绑定调用接口不能使用lambda,所有需要先定义函数再绑定
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)

    # 第三步：绑定端口8001，设置验证口令’qiye',这个相当于对象的初始化
    # 绑定端口并填写验证口令，windows下需要填写IP地址，Linux下默认为本地，地址为空
    manager = QueueManager(address=('127.0.0.1', 8001), authkey='yiye')

    # 第四步：启动管理，监听信息通道
    manager.start()

    # 第五步：通过管理实例的方法获得通过网络访问的Queue对象
    # 即通过网络访问获取任务队列和结果队列
    try:
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        # 第六步：添加任务，获取返回的结果
        for url in ["ImageUrl_" + str(i) for i in range(10)]:
            print("Put task %s ..." % url)
            task.put(url)
        print("try get result...")
        for i in range(10):
            print("result is %s" % result.get(timeout=10))
    except:
        print("Manager error")
    finally:
        # 最后一定要关闭服务，不然会报管道未关闭的错误
        manager.shutdown()

if __name__ == '__main__':
    # Windows下多进程可能出现问题，添加以下代码可以缓解
    freeze_support()
    # 运行服务
    win_run()




