def readFile(filename):
    boy = []
    gril = []
    count = 1
    f = open(filename)
    for each_line in f:
        if each_line[:6] != "======":
            (role, spoken_line) = each_line.split(":", 1)
            if role == "小甲鱼":
                boy.append(spoken_line)
            elif role == "小客服":
                gril.append(spoken_line)
        else:
            saveFile(count, boy, gril)

            boy = []
            gril = []
            count += 1
    saveFile(count, boy, gril)
    f.close()

# 用于创建文件进行保存
def saveFile(count, boy, gril):
    file_boy_name = 'boy' + str(count) + '.txt'
    file_gril_name = 'gril' + str(count) + '.txt'

    boy_file = open(file_boy_name, 'w')
    gril_file = open(file_gril_name, 'w')

    boy_file.writelines(boy)
    gril_file.writelines(gril)

    boy_file.close()
    gril_file.close()

readFile('report.txt')