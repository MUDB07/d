import os

class Handler:
    def __init__(self):
        pass

    def show_file(self):
        path = r'/home/tarena/aid1807/pythonNet/day08/ftp文件服务器0.1/files'
        files = os.listdir(path)
        return files