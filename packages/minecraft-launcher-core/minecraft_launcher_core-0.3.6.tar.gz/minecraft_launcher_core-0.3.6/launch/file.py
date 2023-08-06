import requests,os,sys

class File:
    def __init__(self,url,path):
        r1 = requests.get(url, stream=True, verify=False)
        total_size = int(r1.headers['Content-Length'])

        # 这重要了，先看看本地文件下载了多少
        if os.path.exists(path):
            temp_size = os.path.getsize(path)  # 本地已经下载的文件大小
        else:
            temp_size = 0
        # 显示一下下载了多少

        # 核心部分，这个是请求下载时，从本地文件已经下载过的后面下载
        headers = {'Range': 'bytes=%d-' % temp_size}
        # 重新请求网址，加入新的请求头的
        r = requests.get(url, stream=True, verify=False, headers=headers)

        # 下面写入文件也要注意，看到"ab"了吗？
        # "ab"表示追加形式写入文件
        with open(path, "ab") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    temp_size += len(chunk)
                    f.write(chunk)
                    f.flush()

                    ###这是下载实现进度显示####
                    done = int(50 * temp_size / total_size)
                    sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                    sys.stdout.flush()
        print()  # 避免上面\r 回车符
