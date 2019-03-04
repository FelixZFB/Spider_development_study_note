# coding: utf-8
'''
第一步： 创建一个分布式管理器
第二步： 创建URL管理进程、 数据提取进程、数据存储进程
URL管理进程里面有两个队列：url_q和result_q，和爬虫节点中的两个节点（self.task和self.result）是联络在一起的
数据提取进程里面有两个队列：conn_q和store_q，分别用于放置待提交给URL管理进程的数据和数据存储进程的数据
第三步： 启动三个进程和管理器

爬取流程逻辑：
整个控制节点和爬取节点靠的是4个队列进行联络：
    url_q：在爬虫节点SpiderWork中被重命名为self.task，其实本质都是get_task_queue队列
           控制节点中向url_q放入数据，爬虫节点从self.task取出数据，然后用于下载HTML页面和解析页面
           解析出来的数据放进self.result队列，返回给控制节点
    result_q：在爬虫节点SpiderWork中被重命名为self.result，其实本质都是get_result_queue队列
           爬虫节点中向self.result放入数据，控制节点从result_q取出数据，
           取出的数据中的URL交给了conn_q队列，然后又循环给url_q队列,提交给爬虫节点，进行下一轮爬取
           其它数据交给了store_q，然后存储到文件中，一直循环下去，到达限定条件结束爬取。
    store_q：该队列只在控制节点中使用，数据提取进程用于放置待提交给数据存储进程的数据，
            数据来源于result_q，实际是SpiderWork中的self.result队列
    conn_q：该队列只在控制节点中使用，数据提取进程用于放置待提交给URL管理进程的URL，
            数据来源于result_q，实际是SpiderWork中的self.result队列

运行步骤：先启动控制节点NodeManager.py,再启动爬虫节点SpiderWorker.py

'''


from multiprocessing.managers import BaseManager
import time
from multiprocessing import Process, Queue
from ControlNode.DataOutput import DataOutput
from ControlNode.URLManager import UrlManager

class NodeManager(object):

    # 第一步：创建分布式管理器
    def start_Manager(self, url_q, result_q):
        '''
        创建一个分布式管理器
        :param url_q: url地址队列，URL管理进程将URL传递给爬虫节点的通道（爬虫节点：SpiderWork.py）
        :param result_q: 结果队列, 爬虫节点将数据返回给数据提取进程的通道
        :return:
        '''
        # 把创建的两个队列注册在网络上，利用register方法, call参数关联了Queue对象
        # 将Queue对象在网络中暴露，网络中一个任务队列一个结果队列
        # 队列经过BaseManager封装后进行重命名，其实get_task_queue队列就是url_q队列
        BaseManager.register('get_task_queue', callable=lambda: url_q)
        BaseManager.register('get_result_queue', callable=lambda: result_q)
        # 绑定端口8001，设置验证口令‘baike'，这个相当于对象的初始化
        manager = BaseManager(address=('127.0.0.1', 8001), authkey='baike'.encode('utf-8'))
        # 返回manager对象
        return manager

    # 第二步：创建URL管理进程、 数据提取进程、数据存储进程
    # URL管理进程（利用URLManager.py）
    def url_manager_proc(self, url_q, conn_q, root_url):
        '''
        URL管理进程
        :param url_q: 任务进程队列，放置即将爬取URL，URL管理进程将URL传递给爬虫节点的通道（爬虫节点：SpiderWork.py）
        :param conn_q: 数据提取进程将新的URL提交给URL管理进程的通道
        :param root_url: 最原始的url,第一个用于爬取的网址
        :return:
        '''
        # Url管理器实例化
        url_manager = UrlManager()
        # 将第一个网址加入到未爬取的URL集合中
        url_manager.add_new_url(root_url)
        while True:
            # 判断是否有新的未爬取的URL
            while(url_manager.has_new_url()):
                # 从未爬取的URL集合中取出新的URL
                new_url = url_manager.get_new_url()
                # 将新的URL放入任务进程队列，放置即将爬取的URL
                url_q.put(new_url)
                # 打印已爬取过URL集合的大小
                print('old_url=', url_manager.old_url_size())
                # 加一个判断条件，当爬取2000个链接后就关闭爬行节点，并保存进度
                if(url_manager.old_url_size() > 30):
                    # 通知爬行节点工作结束，即使未爬取的URL集合中还有URL或者任务队列中还有未爬取的URL
                    url_q.put('end')
                    print("控制节点发起结束通知!")
                    # 关闭管理节点，同时存储set状态
                    url_manager.save_progerss('new_urls.txt', url_manager.new_urls)
                    url_manager.save_progerss('old_urls.txt', url_manager.old_urls)
                    return
            # 将从result_solve_proc获取到的urls添加到URL管理器之间
            try:
                urls =conn_q.get()
                url_manager.add_new_urls(urls)
            except BaseException as e:
                # 延时休息一会儿
                time.sleep(0.1)

    # 数据提取进程
    def result_solve_proc(self, result_q, conn_q, store_q):
        '''
        数据提取进程
        :param result_q: 结果队列, 爬虫节点将数据返回给数据提取进程的通道
        :param conn_q: 数据提取进程将新的URL提交给URL管理进程的通道
        :param store_q: 数据提取进程将获取的数据提交给数据存储进程的通道
        :return:
        '''
        while(True):
            try:
                if not result_q.empty():
                    content = result_q.get(True) # 从result_q就是SpiderWork中的self.result队列，里面放置了网页分析后的数据
                    if content['new_urls']=='end':
                        #结果分析进程接受通知然后结束
                        print('结果分析进程接受通知然后结束!')
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])#url为set类型
                    store_q.put(content['data'])#解析出来的数据为dict类型，然后放入通道中待存储
                else:
                    time.sleep(0.1)#延时休息
            except BaseException as e:
                time.sleep(0.1)#延时休息

    # 数据存储进程
    def store_proc(self, store_q):
        '''
        数据存储进程
        :param store_q: 数据提取进程将获取的数据提交给数据存储进程的通道，里面放的是HTML解析出来待存储的数据
        :return:
        '''
        # 数据存储实例化
        output = DataOutput()
        while True:
            # 判读队列中是否为空，前面加了not，不是空就返回True
            if not store_q.empty():
                # 取出数据
                data = store_q.get()
                # 如果里面的数据是字符串end，就代表结束存储进程
                if data=='end':
                    print('存储进程收到结束通知，立刻结束!')
                    # 写入HTML的结束标签内容
                    output.output_end(output.filepath)
                    return
                output.store_data(data) # 不是end，就一直向datas列表里面一直添加数据
            else:
                time.sleep(0.1)
        pass


# 进程运行逻辑顺序
if __name__=='__main__':

    #初始化4个队列
    url_q = Queue()
    result_q = Queue()
    store_q = Queue()
    conn_q = Queue()

    #创建分布式管理器
    node = NodeManager()
    manager = node.start_Manager(url_q, result_q)
    #创建URL管理进程、 数据提取进程和数据存储进程
    url_manager_proc = Process(target=node.url_manager_proc, args=(url_q, conn_q, 'http://baike.baidu.com/view/284853.htm',))
    result_solve_proc = Process(target=node.result_solve_proc, args=(result_q, conn_q, store_q,))
    store_proc = Process(target=node.store_proc, args=(store_q,))
    #启动3个进程和分布式管理器
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    manager.get_server().serve_forever()






