a1 = []
a2 = []
a3 = []

print('''1、请在每行输入任意数字；\n2、请确保每行输入的数字位数相等；\n''')
q1 = input('请输入：')
q2 = input('请输入：')
q3 = input('请输入：')

if len(q1) == len(q2) == len(q3):   # 检查三次输入位数是否相等
    for i in range(len(q1)):        # 根据输入的位数,设置循环次数
        a1.append(int(q1[i]))       # 遍历输入的内容,并将输入内容内的每一个元素单独增加到列表内,并将将类型转换为整型
        a2.append(int(q2[i]))
        a3.append(int(q3[i]))
        
    b=a1+a2+a3                      # 将以上三个列表合并成一个列表

    c = int(len(a1))                # 计算单个列表内元素个数，以便后面循环使用

    print('\n原题：\n{}\n{}\n{}\n'.format(a1,a2,a3))         # 打印原题

    print('答案：')
    for x in range(c):              # 循环c次，将整个列表遍历一遍
        print(b[x::c])              # 打印列表内的元素，x为起始位置，c为步长，这样确保能够打印每个列表内相同位置的元素。



else:
    print('错误：三次输入数字位数不同！')
