import os
file_dir = 'D:\Work\项目\IPQ Translator\Code\Translator'  #你的文件路径
def getFlist(path):
    for root, dirs, files in os.walk(file_dir):
        print('root_dir:', root)  #当前路径
        print('sub_dirs:', dirs)   #子文件夹
        print('files:', files)     #文件名称，返回list类型
    return files
file_name = getFlist(file_dir)