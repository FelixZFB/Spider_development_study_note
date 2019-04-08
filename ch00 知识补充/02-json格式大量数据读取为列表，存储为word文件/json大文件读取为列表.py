import json
import docx

# 将json文件读取出来，然后提取部分内容，最后写入到word文件中

# 由于文件中有多行，直接读取会出现错误，因此一行一行读取
def read_json():
    # 读取json文件，加入到列表中,注意文件名称前面加一个r,去掉\作为转义符的含义，有时候需要路径打开要使用\
    file = open(r'papers.json', 'r', encoding='utf-8')
    papers = []
    for line in file.readlines():
        dic = json.loads(line)
        papers.append(dic)
    print(len(papers))

    # 提取列表中的部分内容，写入到docx文件中
    file = docx.Document()
    for paper in papers:
        mag = str(paper['title']) + ":\n" + str(paper['content'])
        file.add_paragraph(mag)
    file.save('D:\Hello World\python_work\Spider_development_study_note\ch12\中文高清字幕+有码名站.docx')

if __name__ == '__main__':
    read_json()



