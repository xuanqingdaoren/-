import os

病毒库 = ['病毒.txt']

def getAllFile(path):
    # 获取目录中的所有文件并遍历
    files = os.listdir(path)
    for file in files:
        # 拼接路径，如果是目录则递归获取所有文件
        new_path = path + r'/' + file
        if os.path.isdir(new_path):
            getAllFile(new_path)
        else:
            # 如果是文件则查询病毒库，匹配成功则删除
            if file in 病毒库:
                os.remove(new_path)
                print('已经删除病毒文件', file)

path = input('请输入需要查杀的目录：')
getAllFile(path)
