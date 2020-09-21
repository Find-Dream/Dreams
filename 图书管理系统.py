class Book:
    def __init__(self):
        self.book_name = bookname
        # self.book_number = booknumber
        # self.book_author = bookauthor
        # self.book_index =bookindex
        # self.book_state=bookstate
        print(self.book_name)
    # def info(self):
    #     print('《{}》\n编号：{}\n作者：{}\n简介：{}\n状态：{}'.format(self.book_name,self.book_number,self.book_author,self.book_index,self.book_state))

def query():
    for q in booklist:
        print(q)

def add():
    name = input('请输入图书名称:')
    author = input('请输入作者:')
    index = input('请输入图书简介：')
    if name not in booklist:
        b_add = []
        b_add.append(new_number)
        b_add.append(author)
        b_add.append( index)
        b_add.append('未借出')
        booklist[name] = b_add
        print('图书添加成功:')
        print(booklist[name])
        main()
    else:
        print('添加失败:该图书已经存在')
        main()

def number():
    global new_number
    b_number = []
    for i in booklist:
        b_number.append(booklist[i][0])
    bl_number = b_number[-1]
    new_number = bl_number + 1




def main():
    print(
        '''
        欢迎来到图书管理系统,在这里您可以查询图书信息以及添加图书
        查询图书请按 1 ,查看图书详情请按 2 ,添加图书请按 3
        ''')
    main = input('请选择:')
    if main == '1':
        query()
    elif main == '3':
        number()
        add()
    elif main == '2':
        book_a = input('请输入您要查询的图书名称:')
        book_b = 'b'+ str(booklist[book_a][0])
        print(book_b)
        # book_b = Book(book_a)



booklist = {'洗脑术':[1001,'高德','如何快速说服别人','未借出']}
main()