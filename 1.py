def nzj(n,t):
    if t < 6:
        j = 500
    elif 6 <= t <= 12:
        j = t * 120
    else:
        j = t * 180
    print('{}来了{}个月,获得奖金{}元.'.format(n,t,j))

name = input('请输入员工姓名:')
time = int(input('请输入工作时间(月):')
nzj(name,time)
    
