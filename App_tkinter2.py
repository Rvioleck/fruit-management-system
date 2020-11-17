import pymssql
import sys,os
from abc import ABCMeta, abstractmethod
from tkinter import *
from tkinter.ttk import *

class SQL:
    """
    数据库类，连接数据库，增删改查
    """
    def __init__(self, host, user, pwd, db):
        # 构造函数参数数据库：(本地)服务器，用户名，密码，数据库
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def get_connect(self):
        # 进行数据库连接并且返回游标
        if not self.db:
            raise(NameError, "There is no datebase named" + db)

        # 打开数据库连接
        self.conn = pymssql.connect(host=self.host, user=self.user,
                                    password=self.pwd, database=self.db)
        # 创建cursor游标
        cur = self.conn.cursor()
        if not cur:
            raise(NameError, "Failed to connect!")
        else:
            # 返回操作游标
            return cur

    def execute_query(self, sql_query):
        # 查询
        try:
            cur = self.get_connect()
            # 执行sql查询语句
            cur.execute(sql_query)
            # 获取查询结果
            rows = cur.fetchall()
            # 关闭游标和数据库连接
            cur.close()
            self.conn.close()
            # 输出查询结果
            output_menu = Tk()
            output_menu.title("Output")
            l1 = Label(output_menu,
                       text = "Information",
                       font = ('Helvetica', 15, 'bold'))
            l1.pack(padx=10, pady=10)
            # treeview
            # Style().configure('Treeview', rowheight=40)
            tree = Treeview(output_menu, show='headings', height=18)
            # 多级列表显示
            if 'fruit' in sql_query:
                tree["column"] = ("0","1", "2", "3", "4", "5", "6", "7", "8")
                # 设置列宽度
                tree.column("0", width=80, anchor=CENTER)
                tree.column("1", width=100, anchor=CENTER)
                tree.column("2", width=100, anchor=CENTER)
                tree.column("3", width=400, anchor=CENTER)
                tree.column("4", width=100, anchor=CENTER)
                tree.column("5", width=100, anchor=CENTER)
                tree.column("6", width=100, anchor=CENTER)
                tree.column("7", width=100, anchor=CENTER)
                tree.column("8", width=100, anchor=CENTER)
                # 设置表头
                tree.heading("0", text = 'No.')
                tree.heading("1", text = 'FruitName')
                tree.heading("2", text = 'Manufacturer')
                tree.heading("3", text = 'Note')
                tree.heading("4", text = 'PurchasePrice')
                tree.heading("5", text = 'SellPrice')
                tree.heading("6", text = 'Storage')
                tree.heading("7", text = 'InputNumber')
                tree.heading("8", text = 'OutputNumber')
                # 设置值
            elif 'client' in  sql_query:
                tree["column"] = ("0", "1", "2")
                tree.column("0", width=80, anchor=CENTER)
                tree.column("1", width=100, anchor=CENTER)
                tree.column("2", width=100, anchor=CENTER)
                tree.heading("0", text = "No.")
                tree.heading("1", text = "Name")
                tree.heading("0", text = "Phone")
            for j, row in enumerate(rows):
                row = [str(i).strip() for i in row]
                tree.insert("", j, values=row)
            tree.pack()
        # frame框架显示
        # frame = {}
        # if 'fruit' in sql_query:
        #     l1.config(text = 'Fruit Information')
        #     t = "No.{}, Fruit name:{}, Manufacturer:{}, Note:{}, Purchase price:{}, Sell price:{}, Storage:{}, Total imports:{}, Total oxports:{} "
        # elif 'client' in sql_query:
        #     l1.config(text = 'Cleint Information')
        #     t = "No.{}, VIP name:{}, Phone:{} "
        # for j, row in enumerate(rows):
        #     frame[j] = Frame(output_menu)
        #     row = [str(i).strip() for i in row]
        #     m1 = Message(frame[j],
        #                  text = t.format(*row),
        #                  width = 800,
        #                  font = ('微软雅黑', 12)).pack(padx=5, pady=2)
        #     frame[j].pack(padx=5, pady=5, anchor=W)
            output_menu.mainloop()
        except:
            print("Unable to fetch data.")

    def execute_alter(self, sql_alter):
        # 更改
        try:
            cur = self.get_connect()
            # 执行数据库更改语句
            cur.execute(sql_alter)
            # 提交到数据库执行
            self.conn.commit()
            print("Successfully alter the information!")
            # 关闭游标和数据库连接
            cur.close()
            self.conn.close()
        except:
            # 发生错误时提示
            response = Tk()
            response.title("ERROR!")
            l1 = Label(response,
                       text='Unable to alter the data.\nplease check your input data.',
                       font=('Helvetica', 12, 'bold')).pack(padx=10, pady=10)
            b1 = Button(response,
                        text='OK',
                        command=response.destroy).pack(padx=10, pady=10)
            response.mainloop()
            if response:
                response.destroy()
            # print("Unable to alter data. Please check your input data.")
            # self.db.rollback()

    def execute_delete(self, sql_delete):
        # 删除
        try:
            cur = self.get_connect()
            # 执行数据库的删除语句
            cur.execute(sql_delete)
            # 提交到数据库执行
            self.conn.commit()
            print("Successfully delete the information!")
            # 关闭游标和数据库连接
            cur.close()
            self.conn.close()
        except:
            # 发生错误时提示
            response = Tk()
            response.title("ERROR!")
            l1 = Label(response,
                       text='Unable to delete the data.\nplease check your input data.\nYour fruit name must be in the database!',
                       font=('Helvetica', 12, 'bold')).pack(padx=10, pady=10)
            b1 = Button(response,
                        text='OK',
                        command=response.destroy).pack(padx=10, pady=10)
            response.mainloop()
            if response:
                response.destroy()
            # print("Unable to delete data. Please check your input.")
            # self.db.rollback()

    def execute_insert(self, sql_insert):
        # 增加
        try:
            cur = self.get_connect()
            # 执行数据库的插入语句
            cur.execute(sql_insert)
            # 提交到数据库执行
            self.conn.commit()
            # 关闭游标和数据库连接
            cur.close()
            self.conn.close()
        except:
            # 发生错误时回滚
            response = Tk()
            response.title("ERROR!")
            l1 = Label(response,
                       text='Unable to insert data.\nPlease check your input data.\nYour number (No.) must be in the format: 0001~9999',
                       font=('Helvetica', 12, 'bold')).pack(padx=10, pady=10)
            b1 = Button(response,
                        text='OK',
                        command=response.destroy).pack(padx=10, pady=10)
            response.mainloop()
            if response:
                response.destroy()
            # print("Unable to insert data. Please check your input data.")
            # self.db.rollback()

class User():
    # 抽象父类
    __metaclass__ = ABCMeta

    def __init__(self, sql):
        self.sql = sql

    @abstractmethod # 插入操作
    def _insert_database(self): pass

    @abstractmethod # 删除操作
    def _delete_database(self): pass

    @abstractmethod # 修改操作
    def _alter_database(self): pass

    @abstractmethod # 查询操作
    def _select_database(self): pass

    @abstractmethod # 图形页面主框架
    def main_frame(self): pass

class Employee(User):
    # 员工类
    def __init__(self, sql):
        super().__init__(sql)

    def _insert_database(self):
        # 添加信息
        def to_database(sql):
            # b_ok的响应函数
            fruit = e_fruit.get()
            no = e_no.get()
            manufacturer = e_manu.get()
            note = e_note.get()
            pur_price = e_pprice.get()
            sell_price = e_sprice.get()
            storage = e_storage.get()
            # 为空则为0，非空转为数字类型
            if pur_price == '':
                pur_price = 0
            else:
                pur_price = int(pur_price)
            if note == '':
                note = '(备选字段)'
            if sell_price == '':
                sell_price = 0
            else:
                sell_price = int(sell_price)
            if storage == '':
                storage = 0
            else:
                storage = int(storage)
            innumber = storage
            outnumber = 0
            if no == '' or fruit == '':
                response = Tk()
                response.title("ERROR!")
                l1 = Label(response,
                           text="The fruit name or fruit number cannot be empty!",
                           font=('Helvetica', 12, 'bold'))
                l1.pack(padx=10, pady=10)
                b1 = Button(response,
                            text='OK',
                            width=10,
                            command=response.destroy)
                b1.pack(padx=10, pady=10)
                response.mainloop()
                if response:
                    response.destroy()
            else:
                # 执行插入语句
                insert_fruit = "insert into fruit values" \
                               "(\'{}\', \'{}\', \'{}\', \'{}\'," \
                               " {}, {}, {}, {}, {})".format(no, fruit, manufacturer, note,
                                                             pur_price, sell_price, storage,
                                                             innumber, outnumber)
                sql.execute_insert(insert_fruit)
                # 图形提示
                response = Tk()
                response.title("Tips interface")
                l1 = Label(response,
                           text="Successfully inserted the information into the database",
                           font=('Helvetica', 12))
                l1.pack(padx=10, pady=10)
                b1 = Button(response,
                            text='OK',
                            command=response.destroy)
                b1.pack(padx=10, pady=10)
                response.mainloop()
                if response:
                    response.destroy()
                # if ins_menu:
                #     ins_menu.destroy()
        ins_menu = Tk()
        ins_menu.geometry('600x300')
        ins_menu.title("Insert interface")
        # 图片frame
        img_frame = Frame(ins_menu)
        img_text_label = Label(img_frame,
                               text="Fruit Management System",
                               font=('微软雅黑', 20, 'bold')).pack(side=RIGHT)
        img = PhotoImage(file=r"D:\Python\python实验设计\软件工程\调试文件\fruit1.png")
        img_label = Label(img_frame,
                          image=img,
                          width=5)
        img_label.pack(side=LEFT)
        img_frame.pack(padx=5, pady=5)
        # 显示输入信息
        l1 = Label(ins_menu,
                   text="Please enter the information of fruit",
                   font=('Helvetica', 15, 'bold'))
        l1.pack(padx=20, pady=10)
        # frame1输入框提示和标签
        frame1 = Frame(ins_menu)
        # fruit标签与输入框
        l_fruit = Label(frame1,
                        text='Fruit:',
                        font=('微软雅黑', 12),
                        width=5).pack(side=LEFT, padx=2, pady=5)
        e_fruit = Entry(frame1,
                        width=5)
        e_fruit.pack(side=LEFT)
        # no标签与输入框
        l_no = Label(frame1,
                        text='No:',
                        font=('微软雅黑', 12),
                        width=4).pack(side=LEFT, padx=2, pady=5)
        e_no = Entry(frame1,
                     width=5)
        e_no.pack(side=LEFT)
        # manufactor标签与输入框
        l_manu = Label(frame1,
                       text='Manufacturer:',
                       font=('微软雅黑', 12),
                       width=12).pack(side=LEFT, padx=2, pady=5)
        e_manu = Entry(frame1,
                       width=8)
        e_manu.pack(side=LEFT)
        # note备注 标签与输入框
        l_note = Label(frame1,
                       text='Note:',
                       font=('微软雅黑', 12),
                       width=5).pack(side=LEFT, padx=2, pady=5)
        e_note = Entry(frame1,
                       width=8)
        e_note.pack(side=LEFT)
        # frame2
        frame2 = Frame(ins_menu)
        # pur_price进价 标签与输入框
        l_pprice = Label(frame2,
                       text='Purchase price:',
                       font=('微软雅黑', 12),
                       width=12).pack(side=LEFT, padx=2, pady=5)
        e_pprice = Entry(frame2,
                         width=5)
        e_pprice.pack(side=LEFT)
        # sell_price售价 标签与输入框
        l_sprice = Label(frame2,
                       text='Sell price:',
                       font=('微软雅黑', 12),
                       width=10).pack(side=LEFT, padx=2, pady=5)
        e_sprice = Entry(frame2,
                         width=5)
        e_sprice.pack(side=LEFT)
        # storage库存 标签与输入框
        l_store = Label(frame2,
                        text='Storage:',
                        font=('微软雅黑', 12),
                        width=8).pack(side=LEFT, padx=2, pady=5)
        e_storage = Entry(frame2,
                          width=5)
        e_storage.pack(side=LEFT)
        # frame1和frame2 pack()
        frame1.pack(padx=20, pady=10)
        frame2.pack(padx=20, pady=10)
        # b_ok和b_return 提交和返回
        b_ok = Button(ins_menu,
                      text='OK',
                      # command=lambda: [ins_menu.destroy(), to_database(self.sql)],
                      command= lambda: to_database(self.sql),
                      width=8).pack()
        b_return = Button(ins_menu,
                          text='Main menu',
                          command=lambda: [ins_menu.destroy(), self.main_frame()]).pack(side=RIGHT)
        ins_menu.mainloop()
        if ins_menu:
            ins_menu.destroy()

    def _delete_database(self):
        # 删除信息
        def to_database(sql):
            fruit = e_fruit.get()
            if fruit == '':
                response = Tk()
                response.title("ERROR!")
                l1 = Label(response,
                           text="The fruit name can't be empty",
                           font=('Helvetica', 15, 'bold')).pack(padx=10,pady=10)
                b1 = Button(response,
                            text="OK",
                            command=response.destroy).pack(padx=10, pady=10)
                response.mainloop()
                if response:
                    response.destroy()
            else:
                response = Tk()
                delete_fruits = "delete from fruit where Fname = \'{}\'".format(fruit)
                sql.execute_delete(delete_fruits)
                response.title("Tips interface")
                l1 = Label(response,
                           text="Successfully deleted the information of {}".format(fruit),
                           font=('Helvetica', 12)).pack(padx=10, pady=10)
                b1 = Button(response,
                            text='OK',
                            command=response.destroy)
                b1.pack(padx=10, pady=10)
                response.mainloop()
                if response:
                    response.destroy()

        del_menu = Tk()
        del_menu.geometry('600x260')
        del_menu.title("Delete interface")
        # 图片frame
        img_frame = Frame(del_menu)
        img_text_label = Label(img_frame,
                               text="Fruit Management System",
                               font=('微软雅黑', 20, 'bold')).pack(side=RIGHT)
        img = PhotoImage(file=r"D:\Python\python实验设计\软件工程\调试文件\fruit1.png")
        img_label = Label(img_frame,
                          image=img,
                          width=5)
        img_label.pack(side=LEFT)
        img_frame.pack(padx=5, pady=5)
        # 显示输入信息
        l1 = Label(del_menu,
                   text="Please enter the fruit name which you want to delete",
                   font=('Helvetica', 15, 'bold'))
        l1.pack(padx=20, pady=10)
        frame1 = Frame(del_menu)
        l_fruit = Label(frame1,
                        text='Fruit name:',
                        font=('微软雅黑', 12),
                        width=14).pack(side=LEFT, padx=2, pady=5)
        e_fruit = Entry(frame1,
                        width=10)
        e_fruit.pack(side=LEFT)
        frame1.pack(padx=5, pady=5)
        b_ok = Button(del_menu,
                      text='OK',
                      command=lambda: to_database(self.sql))
        b_ok.pack(padx=5, pady=5)
        b_return = Button(del_menu,
                          text='Main menu',
                          command=lambda: [del_menu.destroy(), self.main_frame()]).pack(side=RIGHT)
        del_menu.mainloop()
        if del_menu:
            del_menu.destroy()

    def _alter_database(self):
        # 修改信息
        def exhaustive_alter(sql):
            # alter的二层窗口
            def direct_alter(sql):
                # alter的三层窗口，进行写入数据库操作
                def to_database(sql, value2):
                    # 进行数据库写入操作
                    fruit_name, inventory = e_fruit.get(), e_storage.get()
                    if fruit_name == '' or inventory == '':
                        # 图形提示
                        response = Tk()
                        response.title("Tips interface")
                        l1 = Label(response,
                                   text="The fruit name and inventory can't be empty.",
                                   font=('Helvetica', 12))
                        l1.pack(padx=10, pady=10)
                        b1 = Button(response,
                                    text='OK',
                                    command=response.destroy)
                        b1.pack(padx=10, pady=10)
                        response.mainloop()
                        if response:
                            response.destroy()
                    if value2 == 1:
                        alter_fruits_inventory = 'update fruit set Storage = Storage + {} ' \
                                                 'where Fname = \'{}\''
                        alter_fruits_innumber = 'update fruit set Innumber = Innumber + {} ' \
                                                'where Fname = \'{}\''
                    else:
                        alter_fruits_inventory = 'update fruit set Storage = Storage - {} ' \
                                                 'where Fname = \'{}\''
                        alter_fruits_innumber = 'update fruit set Innumber = Innumber - {} ' \
                                                'where Fname = \'{}\''
                    alter_fruits_inventory = alter_fruits_inventory.format(inventory, fruit_name)
                    alter_fruits_innumber = alter_fruits_innumber.format(inventory, fruit_name)
                    sql.execute_alter(alter_fruits_inventory)
                    sql.execute_alter(alter_fruits_innumber)
                    # 图形提示
                    response = Tk()
                    response.title("Tips interface")
                    l1 = Label(response,
                               text="Successfully altered the information into the database",
                               font=('Helvetica', 12))
                    l1.pack(padx=10, pady=10)
                    b1 = Button(response,
                                text='OK',
                                command=response.destroy)
                    b1.pack(padx=10, pady=10)
                    response.mainloop()
                    if response:
                        response.destroy()

                value2 = var2.get()
                alt_menu3 = Tk()
                alt_menu3.title("Alter interface")
                # 图片frame
                img_frame = Frame(alt_menu3)
                img_text_label = Label(img_frame,
                                       text="Fruit Management System",
                                       font=('微软雅黑', 20, 'bold')).pack(side=RIGHT)
                img = PhotoImage(file=r"D:\Python\python实验设计\软件工程\调试文件\fruit1.png")
                img_label = Label(img_frame,
                                  image=img,
                                  width=5)
                img_label.pack(side=LEFT)
                img_frame.pack(padx=5, pady=5)
                # 提示输入标签
                if value2 == 1:
                    l1_text = "please enter the name and input of the fruit"
                else:
                    l1_text = "please enter the name and output of the fruit"
                l1 = Label(alt_menu3,
                           text=l1_text,
                           font=('Helvetica', 15, 'bold')).pack(padx=20, pady=10)
                # 输入框和输入标签
                frame1 = Frame(alt_menu3)
                l_fruit = Label(frame1,
                                text='Fruit:',
                                font=('微软雅黑', 12),
                                width=8).pack(side=LEFT, padx=2, pady=5)
                e_fruit = Entry(frame1,
                                width=10)
                e_fruit.pack(side=LEFT)
                frame2 = Frame(alt_menu3)
                l_storage = Label(frame2,
                                  text='Storage:',
                                  font=('微软雅黑', 12),
                                  width=8).pack(side=LEFT, padx=2, pady=5)
                e_storage = Entry(frame2,
                                  width=10)
                e_storage.pack(side=LEFT)
                frame1.pack(padx=5, pady=5)
                frame2.pack(padx=5, pady=5)
                b3_ok = Button(alt_menu3,
                               text='OK',
                               # command=lambda: [alt_menu3.destroy(), to_database(self.sql, value2)],
                               command=lambda: to_database(self.sql, value2),
                               width=8).pack()
                b3_return = Button(alt_menu3,
                                   text='Main menu',
                                   command=lambda: [alt_menu3.destroy(), self.main_frame()]).pack(side=RIGHT)
                alt_menu3.mainloop()
                if alt_menu3:
                    alt_menu3.destroy()

            def direct_alter2(sql):
                # alter的三层窗口，进行写入数据库操作
                def to_database(sql, value2):
                    # 进行数据库写入操作
                    fruit_name, price = e_fruit.get(), e_price.get()
                    if value2 == 1:
                        alter_fruits_price = 'update fruit set Purchase_price = {} ' \
                                             'where Fname = \'{}\''
                    else:
                        alter_fruits_price = 'update fruit set Sell_price = {} ' \
                                             'where Fname = \'{}\''
                    alter_fruits_price = alter_fruits_price.format(price, fruit_name)
                    sql.execute_alter(alter_fruits_price)
                    # 图形提示
                    response = Tk()
                    response.title("Tips interface")
                    l1 = Label(response,
                               text="Successfully altered the information into the database",
                               font=('Helvetica', 12))
                    l1.pack(padx=10, pady=10)
                    b1 = Button(response,
                                text='OK',
                                command=response.destroy)
                    b1.pack(padx=10, pady=10)
                    response.mainloop()
                    if response:
                        response.destroy()

                value2 = var2.get()
                alt_menu3 = Tk()
                alt_menu3.title("Alter interface")
                # 图片frame
                img_frame = Frame(alt_menu3)
                img_text_label = Label(img_frame,
                                       text="Fruit Management System",
                                       font=('微软雅黑', 20, 'bold')).pack(side=RIGHT)
                img = PhotoImage(file=r"D:\Python\python实验设计\软件工程\调试文件\fruit1.png")
                img_label = Label(img_frame,
                                  image=img,
                                  width=5)
                img_label.pack(side=LEFT)
                img_frame.pack(padx=5, pady=5)
                # 提示输入标签
                if value2 == 1:
                    l1_text = "please enter the name and purchase price of the fruit"
                else:
                    l1_text = "please enter the name and sell price of the fruit"
                l1 = Label(alt_menu3,
                           text=l1_text,
                           font=('Helvetica', 15, 'bold')).pack(padx=20, pady=10)
                # 输入框和输入标签
                frame1 = Frame(alt_menu3)
                l_fruit = Label(frame1,
                                text='Fruit:',
                                font=('微软雅黑', 12),
                                width=8).pack(side=LEFT, padx=2, pady=5)
                e_fruit = Entry(frame1,
                                width=5)
                e_fruit.pack(side=LEFT)
                frame2 = Frame(alt_menu3)
                l_price = Label(frame2,
                                  text='Price:',
                                  font=('微软雅黑', 12),
                                  width=8).pack(side=LEFT, padx=2, pady=5)
                e_price = Entry(frame2,
                                  width=5)
                e_price.pack(side=LEFT)
                frame1.pack(padx=5, pady=5)
                frame2.pack(padx=5, pady=5)
                b3_ok = Button(alt_menu3,
                               text='OK',
                               # command=lambda: [alt_menu3.destroy(), to_database(self.sql, value2)],
                               command=lambda: to_database(self.sql, value2),
                               width=8).pack()
                b3_return = Button(alt_menu3,
                                   text='Main menu',
                                   command=lambda: [alt_menu3.destroy(), self.main_frame()]).pack(side=RIGHT)
                alt_menu3.mainloop()
                if alt_menu3:
                    alt_menu3.destroy()

            def to_database_note(sql):
                fruit_name, note = e_fruit.get(), e_note.get()
                alter_fruits_notes = 'update fruit set Fnote = \'{}\' ' \
                                     'where Fname = \'{}\''
                alter_fruits_notes = alter_fruits_notes.format(note, fruit_name)
                sql.execute_alter(alter_fruits_notes)
                # 图形提醒
                response = Tk()
                response.title("Tips interface")
                l1 = Label(response,
                           text="Successfully altered the information into the database",
                           font=('Helvetica', 12))
                l1.pack(padx=10, pady=10)
                b1 = Button(response,
                            text='OK',
                            command=response.destroy)
                b1.pack(padx=10, pady=10)
                response.mainloop()
                if response:
                    response.destroy()

            value = var.get()
            alt_menu2 = Tk()
            alt_menu2.title("Alter interface")
            # 图片frame
            img_frame = Frame(alt_menu2)
            img_text_label = Label(img_frame,
                                   text="Fruit Management System",
                                   font=('微软雅黑', 20, 'bold')).pack(side=RIGHT)
            img = PhotoImage(file=r"D:\Python\python实验设计\软件工程\调试文件\fruit1.png")
            img_label = Label(img_frame,
                              image=img,
                              width=5)
            img_label.pack(side=LEFT)
            img_frame.pack(padx=5, pady=5)
            l1 = Label(alt_menu2,
                       text="Please choose an operation",
                       font=('Helvetica', 15, 'bold'))
            l1.pack(padx=20, pady=10)
            if value == 1:
                # 修改库存
                var2 = IntVar()
                var2.set(1)
                r11 = Radiobutton(alt_menu2,
                                  text="Update the fruits input information.",
                                  variable=var2,
                                  # font=('Helvetica', 12),
                                  value=1)
                r11.pack(anchor=W, padx=150, pady=10)
                r12 = Radiobutton(alt_menu2,
                                  text="Update the fruits output infroamtion,",
                                  variable=var2,
                                  # font=('Helvetica', 12),
                                  value=2)
                r12.pack(anchor=W, padx=150, pady=10)
                b2_ok = Button(alt_menu2,
                              text='OK',
                              command=lambda: [alt_menu2.destroy(), direct_alter(self.sql)],
                              width=8).pack()
                b2_return = Button(alt_menu2,
                                  text='Main menu',
                                  command=lambda: [alt_menu2.destroy(), self.main_frame()]).pack(side=RIGHT)
                alt_menu2.mainloop()
                if alt_menu2:
                    alt_menu2.destroy()
            elif value == 2:
                # 修改价格
                var2 = IntVar()
                var2.set(1)
                r21 = Radiobutton(alt_menu2,
                                  text="Update the fruits purchase price.",
                                  variable=var2,
                                  # font=('Helvetica', 12),
                                  value=1)
                r21.pack(anchor=W, padx=150, pady=10)
                r22 = Radiobutton(alt_menu2,
                                  text="Update the fruits sell price.",
                                  variable=var2,
                                  # font=('Helvetica', 12),
                                  value=2)
                r22.pack(anchor=W, padx=150, pady=10)
                b2_ok = Button(alt_menu2,
                              text='OK',
                              command=lambda: [alt_menu2.destroy(), direct_alter2(self.sql)],
                              width=8).pack()
                b2_return = Button(alt_menu2,
                                  text='Main menu',
                                  command=lambda: [alt_menu2.destroy(), self.main_frame()]).pack(side=RIGHT)
                alt_menu2.mainloop()
                if alt_menu2:
                    alt_menu2.destroy()
            else:
                l1.config(text="Please input the fruit and the note")
                frame1 = Frame(alt_menu2)
                l_fruit = Label(frame1,
                                text='Fruit:',
                                font=('微软雅黑', 12),
                                width=8).pack(side=LEFT, padx=2, pady=5)
                e_fruit = Entry(frame1,
                                width=5)
                e_fruit.pack(side=LEFT)
                frame1.pack(padx=5, pady=5)

                frame2 = Frame(alt_menu2)
                l_note = Label(frame2,
                                text='Note:',
                                font=('微软雅黑', 12),
                                width=8).pack(side=LEFT, padx=2, pady=5)
                e_note = Entry(frame2,
                                width=10)
                e_note.pack(side=LEFT)
                frame2.pack(padx=5, pady=5)

                b2_ok = Button(alt_menu2,
                               text='OK',
                               # command=lambda: [alt_menu2.destroy(), to_database_note(self.sql)],
                               command=lambda: to_database_note(self.sql),
                               width=8).pack()
                b2_return = Button(alt_menu2,
                                   text='Main menu',
                                   command=lambda: [alt_menu2.destroy(), self.main_frame()]).pack(side=RIGHT)
                alt_menu2.mainloop()
                if alt_menu2:
                    alt_menu2.destroy()

        alt_menu = Tk()
        # alt_menu.geometry('600x240')
        alt_menu.title("Alter interface")
        # 图片frame
        img_frame = Frame(alt_menu)
        img_text_label = Label(img_frame,
                               text="Fruit Management System",
                               font=('微软雅黑', 20, 'bold')).pack(side=RIGHT)
        img = PhotoImage(file=r"D:\Python\python实验设计\软件工程\调试文件\fruit1.png")
        img_label = Label(img_frame,
                          image=img,
                          width=5)
        img_label.pack(side=LEFT)
        img_frame.pack(padx=5, pady=5)
        # label提示
        l1 = Label(alt_menu,
                   text="Please choose an operation",
                   font=('Helvetica', 15, 'bold'))
        l1.pack(padx=20, pady=10)
        # Radio_button单选
        var = IntVar()
        var.set(1)
        r1 = Radiobutton(alt_menu,
                         text="Update the fruits storage information.",
                         variable=var,
                         # font=('Helvetica', 12),
                         value=1,)
                         # command=exhaustive_alter)
        r1.pack(anchor=W, padx=150, pady=10)
        r2 = Radiobutton(alt_menu,
                         text="Update the prices of fruits.",
                         variable=var,
                         # font=('Helvetica', 12),
                         value=2,)
                         # command=exhaustive_alter)
        r2.pack(anchor=W, padx=150, pady=10)
        r3 = Radiobutton(alt_menu,
                         text="Update the note of fruits.",
                         variable=var,
                         # font=('Helvetica', 12),
                         value=3,)
                         # command=exhaustive_alter)
        r3.pack(anchor=W, padx=150, pady=10)
        # b_ok和b_return 提交和返回
        b_ok = Button(alt_menu,
                       text='OK',
                       command=lambda: [alt_menu.destroy(), exhaustive_alter(self.sql)],
                       width=8).pack()
        b_return = Button(alt_menu,
                           text='Main menu',
                           command=lambda: [alt_menu.destroy(), self.main_frame()]).pack(side=RIGHT)
        alt_menu.mainloop()
        if alt_menu:
            alt_menu.destroy()

    def _select_database(self):
        # 查找信息
        select_phrase = ['select * from fruit', 'select * from client']
        sel_menu = Tk()
        sel_menu.title("Select interface")
        # 图片frame
        img_frame = Frame(sel_menu)
        img_text_label = Label(img_frame,
                               text="Fruit Management System",
                               font=('微软雅黑', 20, 'bold')).pack(side=RIGHT)
        img = PhotoImage(file=r"D:\Python\python实验设计\软件工程\调试文件\fruit1.png")
        img_label = Label(img_frame,
                          image=img,
                          width=5)
        img_label.pack(side=LEFT)
        img_frame.pack(padx=5, pady=5)
        l1 = Label(sel_menu,
                   text = 'Please choose an operation',
                   font = ('Helvetica', 15, 'bold')).pack(padx=10, pady=10)
        b1 = Button(sel_menu,
                    text = 'Fruits information',
                    command = lambda: self.sql.execute_query(select_phrase[0]))
        b1.pack(padx=10, pady=10)
        b2 = Button(sel_menu,
                    text = 'VIP clients information',
                    command = lambda: self.sql.execute_query(select_phrase[1]))
        b2.pack(padx=10, pady=10)
        b_return = Button(sel_menu,
                          text = 'main menu',
                          command = lambda: [sel_menu.destroy() ,self.main_frame()])
        b_return.pack(side=RIGHT)
        sel_menu.mainloop()
        if sel_menu:
            sel_menu.destroy()

    def main_frame(self):
        # emp_main_menu = Toplevel()
        emp_main_menu = Tk()
        emp_main_menu.title("Employee inteface")
        # 图片frame
        img_frame = Frame(emp_main_menu)
        img_text_label = Label(img_frame,
                               text="Fruit Management System",
                               font=('微软雅黑', 20, 'bold')).pack(side=RIGHT)
        img = PhotoImage(file=r"D:\Python\python实验设计\软件工程\调试文件\fruit1.png")
        img_label = Label(img_frame,
                          image=img,
                          width=5)
        img_label.pack(side=LEFT)
        img_frame.pack(padx=5, pady=5)

        # 标签l1提示操作
        l1 = Label(emp_main_menu,
                   text='Choose an operation which you want',
                   font=('Helvetica', 15, 'bold'))
        l1.pack(padx=10, pady=10)
        # frame1存放前两个操作
        frame1 = Frame(emp_main_menu)
        Style().configure("TButton", padding=2, relief="flat", background='grey', font=('Comic Sans MS', 12))
        b1 = Button(frame1,
                    text = "query information",
                    # font = ("微软雅黑", 5, 'bold'),
                    width=20,
                    # style = "my.Tbutton",
                    # height=2,
                    command=lambda: [emp_main_menu.destroy(), self._select_database()])  # command传参数lambda:函数(参数)
        b1.pack(side=LEFT, padx=10, pady=10)
        b2 = Button(frame1,
                    text="update information",
                    width=20,
                    # height=2,
                    command=lambda: [emp_main_menu.destroy(), self._alter_database()])
        b2.pack(side=LEFT, padx=10, pady=10)
        frame1.pack()
        # frame2存放后两个操作
        frame2 = Frame(emp_main_menu)
        b3 = Button(frame2,
                    text="delete information",
                    width=20,
                    # height=2,
                    command=lambda: [emp_main_menu.destroy(), self._delete_database()])
        b3.pack(side=LEFT, padx=10, pady=10)
        b4 = Button(frame2,
                    text="insert information",
                    width=20,
                    # height=2,
                    command=lambda: [emp_main_menu.destroy(), self._insert_database()])
        b4.pack(side=LEFT, padx=10, pady=10)
        frame2.pack()
        # 返回按钮
        Style().configure("TButton", relief="flat", background='grey')
        b5 = Button(emp_main_menu,
                    text="logout",
                    # command调用两个函数，返回主菜单和关闭该组件
                    command=lambda: [emp_main_menu.destroy(), login_database()]).pack(side=RIGHT, pady=10)
        def ending():
            sys.exit(0)
            # man_main_menu.destroy()
        emp_main_menu.protocol("WM_DELETE_WINDOW", ending)
        emp_main_menu.mainloop()
        if emp_main_menu:
            emp_main_menu.destroy()

class Manager(User):
    # 经理类
    def __init__(self, sql):
        super().__init__(sql)

    def _insert_database(self):
        # 添加新员工信息
        employee = input("Please enter the employee's name which you want to insert into this system: ")
        no = input("Please enter the number of the employee which is not in system (0001-9999): ")
        manager_no = input("Please enter the number of the manager which is in system (0001-9999): ")
        sex = input("Please enter the sex of the employee: ")
        age = int(input("Please enter the age of the employee: "))
        salary = int(input("Please enter the salary of the employee: "))
        position = input("Please enter the position of the employee: ")
        # 生成insert的sql语句
        insert_employee = "insert into employee values" \
                          "(\'{}\', \'{}\', \'{}\', \'{}\'," \
                          " {}, {}, \'{}\')".format(no, manager_no, employee, sex, age, salary, position)
        self.sql.execute_insert(insert_employee)

    def _delete_database(self):
        tag = input("Please choose an operation: 1. Delete information from fruits.\n"
                    "                        \t2. Delete information from employees.\n"
                    "                        \t3. Delete information from VIP customers.\n"
                    "                        \t4. Return to main menue.")
        if tag == '1':
            fruit = input("Please enter the fruit's name which you want to delete from this system.\n"
                          "(enter 'exit' to return to main menu.)")
            if fruit == 'exit':
                return
            else:
                delete_fruits = "delete from fruit where Fname = \'{}\'".format(fruit)
                self.sql.execute_delete(delete_fruits)
        elif tag == '2':
            employee = input("Please enter the employee's name which you want to delete from this system.\n"
                             "(enter 'exit' to return to main menu.)")
            if employee == 'exit':
                return
            else:
                delete_employee = "delete from employee where Ename = \'{}\'".format(employee)
                self.sql.execute_delete(delete_employee)
        elif tag == '3':
            customer = input("Please enter the VIP's name which you want to delete from this system.\n"
                             "(enter 'exit' to return to main menu.)")
            if customer == 'exit':
                return
            else:
                delete_customer = "delete from client where Cname = \'{}\'".format(customer)
                self.sql.execute_delete(delete_customer)
        elif tag == '4':
            return
        else:
            print("Please enter the correct choice！")

    def _alter_database(self):
        tag = input("Please choose an operation：1. Update the salary of employee.\n"
                    "                        \t2. Update the prices of fruits.\n"
                    "                        \t3. return to main menu.")
        if tag == '1':
            # 更新员工薪资
            alter_employee_salary = 'update employee set Esalary = {}' \
                                    'where Ename = \'{}\''
            name, salary = input("Please enter the name and salary of the the employee:").split()
            alter_employee_salary = alter_employee_salary.format(salary, name)
            self.sql.execute_alter(alter_employee_salary)
        elif tag == '2':
            # 更新价格
            tag2 = input("Please choose an operation：1. Update the purchase prices of fruits\n"
                         "                          \t2. Update the sell prices of fruits\n"
                         "                          \t3. \n")
            if tag2 == '1':
                # 更新进货价格
                alter_fruits_price = 'update fruit set Purchase_price = {} ' \
                                     'where Fname = \'{}\''
                fruit_name, pur_price = input("Please enter the name and purchase price of the fruit:").split()
                alter_fruits_price = alter_fruits_price.format(pur_price, fruit_name)
                self.sql.execute_alter(alter_fruits_price)
            elif tag2 == '2':
                # 更新出售价格
                alter_fruits_price = 'update fruit set Sell_price = {} ' \
                                     'where Fname = \'{}\''
                fruit_name, sell_price = input("Please enter the name and sell price of the fruit:").split()
                alter_fruits_price = alter_fruits_price.format(sell_price, fruit_name)
                self.sql.execute_alter(alter_fruits_price)
        elif tag == '3':
            return
        else:
            print("Please enter the correct choice！")

    def _select_database(self):
        select_phrase = ['select * from fruit', 'select * from employee', 'select * from client']
        tag = input("Please choose an operation：1. Check the fruits details\n"
                    "                          \t2. Check the employees details\n"
                    "                          \t3. Check the VIP clients details\n"
                    "                          \t4. return to main menu.")
        if tag == '1':
            # 搜索水果的详情
            self.sql.execute_query(select_phrase[0])
        elif tag == '2':
            # 搜索员工的详情
            self.sql.execute_query(select_phrase[1])
        elif tag == '3':
            # 搜索顾客的详情
            self.sql.execute_query(select_phrase[2])
        elif tag == '4':
            return
        else:
            print("Please enter the correct choice！")

    def main_frame(self):
        man_main_menu = Tk()
        man_main_menu.title("Manager inteface")
        # 标签l1提示操作
        l1 = Label(man_main_menu,
                   text='Choose an operation which you want.',
                   font=('Helvetica', 12))
        l1.pack(padx=10, pady=10)
        # frame1存放前两个操作
        frame1 = Frame(man_main_menu)
        b1 = Button(frame1,
                    text="query information",
                    width=20,
                    height=2,
                    command=lambda: [man_main_menu.quit(), self._select_database()])  # command传参数lambda:函数(参数)
        b1.pack(side=LEFT, padx=10, pady=10)
        b2 = Button(frame1,
                    text="update information",
                    width=20,
                    height=2,
                    command=lambda: [man_main_menu.quit(), self._alter_database()])
        b2.pack(side=LEFT, padx=10, pady=10)
        frame1.pack()
        # frame2存放后两个操作
        frame2 = Frame(man_main_menu)
        b3 = Button(frame2,
                    text="delete information",
                    width=20,
                    height=2,
                    command=lambda: [man_main_menu.quit(), self._delete_database()])
        b3.pack(side=LEFT, padx=10, pady=10)
        b4 = Button(frame2,
                    text="insert information",
                    width=20,
                    height=2,
                    command=lambda: [man_main_menu.quit(), self._insert_database()])
        b4.pack(side=LEFT, padx=10, pady=10)
        frame2.pack()
        # 返回按钮
        b5 = Button(man_main_menu,
                    text="logout",
                    # command调用两个函数，返回主菜单和关闭该组件
                    command=lambda: [man_main_menu.quit(), login_database()]).pack(side=RIGHT)

        def ending():
            sys.exit(0)
            # man_main_menu.destroy()
        man_main_menu.protocol("WM_DELETE_WINDOW", ending)
        man_main_menu.mainloop()
        man_main_menu.destroy();


def login_database():
    """
    登录数据库, 登录菜单设计，访问数据库
    :return:
    """
    def to_main_frame():
        """
        在登录菜单中选择login时触发
        主程序判断账号密码，并且选择进入管理员和普通员工的功能模块
        """
        # Entry e1和e2分别输入账户和密码
        user = e1.get()
        pwd = e2.get()
        # 登录login后的响应窗口 response_menu
        response_menu = Tk()
        # # 设置窗口出现位置
        # width, height = 300, 100
        # screen_width, screen_height = response_menu.winfo_screenmmwidth(), response_menu.winfo_screenheight()
        # alignstr = '%dx%d+%d+%d' % (width, height, (screen_width-width)/2, (screen_height-height)/2)
        # response_menu.geometry(alignstr)
        if user == 'sa' and pwd == '123456':
            # 普通水果管理员入口
            # 实例数据库对象，本地服务器，sa用户，123456密码，fmdb数据库
            sql = SQL(host='(local)', user='sa', pwd='123456', db='fmdb')
            # response_menu.geometry('200x100')
            response_menu.title("Tips interface")
            # 标签提示
            l1 = Label(response_menu,
                       text="Successfully connecting to the database: {}！".format(sql.db),
                       font=('Helvetica', 15)).pack(padx=10, pady=10)
            l2 = Label(response_menu,
                       text="User: {}".format(sql.user.upper()),
                       font=('Helvetica', 15, 'bold')).pack(padx=10, pady=10)
            # 按钮确认，跳转主程序功能界面
            b1 = Button(response_menu,
                        text="Enter",
                        command=response_menu.quit)
            b1.pack(padx=10, pady=20)
            response_menu.mainloop()
            # 关闭窗口
            if response_menu:
                response_menu.destroy()
            if login_menu:
                login_menu.destroy()
            # employee主功能
            emp = Employee(sql)
            emp.main_frame()
            # employee_main_frame(sql)
        elif user == 'admin' and pwd == '123456':
            # 员工管理员入口
            sql = SQL(host='(local)', user='admin', pwd='123456', db='fmdb')
            # response_menu.geometry('500x200')
            response_menu.title("Tips interface")
            l1 = Label(response_menu,
                       text="Successfully connecting to the database: {}！".format(sql.db),
                       font=('Helvetica', 12)).pack(padx=10, pady=10)
            l2 = Label(response_menu,
                       text="User: {}".format(sql.user.upper()),
                       font=('Helvetica', 12, 'bold')).pack(padx=10, pady=10)
            # 按钮确认，跳转主程序功能界面
            b1 = Button(response_menu,
                        text="Enter",
                        command=response_menu.quit)
            b1.pack(padx=10, pady=10)
            response_menu.mainloop()
            # 关闭窗口
            if response_menu:
                response_menu.destroy()
            if login_menu:
                login_menu.destroy()
            # manager主功能
            manager = Manager(sql)
            manager.main_frame()

        else:
            # 非法的账号密码，提示窗口
            response_menu.geometry('380x120')
            response_menu.title("Tips interface")
            l1 = Label(response_menu,
                       text="Please check your password or username!\n Failed to connect the database.",
                       font=('Helvetica', 12, 'bold')).pack(padx=10,pady=10)

            b1 = Button(response_menu,
                        text="OK",
                        command=response_menu.quit)
            b1.pack(padx=10, pady=10)
            response_menu.mainloop()
            if response_menu:
                response_menu.destroy()
            # login_menu.destroy()
    # inteface_login_datebase主体
    login_menu = Tk()
    login_menu.geometry('700x300')
    login_menu.title("Login interface")

    # 图片提示标签
    img_frame = Frame(login_menu)
    img_text_label = Label(img_frame,
                           text = "Welcome to the Fruit Management System",
                           font=('微软雅黑', 20, 'bold')).pack(side=RIGHT)
    img = PhotoImage(file=r"D:\Python\python实验设计\软件工程\调试文件\fruit1.png")
    img_label = Label(img_frame,
                      image = img,
                      width = 5)
    img_label.pack(side=LEFT)
    img_frame.pack(padx=5, pady=5)

    # 文字提示标签Label
    login_label = Label(login_menu,
                        text="Please enter your user name and passport",
                        font=('Helvetica', 15, 'bold'))
    login_label.pack(padx=20, pady=10)

    # frame1输入框的提示标签和输入框
    frame1 = Frame(login_menu)
    l1 = Label(frame1,
               text='UserName:',
               font=('Helvetica', 12),
               width=10).pack(side=LEFT)
    e1 = Entry(frame1)
    e1.pack(side=RIGHT, pady=4)
    frame1.pack(padx=20, pady=10)
    # frame2输入框的提示标签和输入框
    frame2 = Frame(login_menu)
    l2 = Label(frame2,
               text='Passport:',
               font=('Helvetica', 12),
               width=10).pack(side=LEFT)
    e2 = Entry(frame2)
    e2.pack(side=RIGHT, pady=4)
    frame2.pack(padx=20, pady=10)
    # 创建按钮 b1转向主功能页面，b2退出程序
    Style().configure("TButton", padding=2, relief="flat", background='#cccccc')
    b1 = Button(login_menu, text='Login', command=to_main_frame).pack(pady=10)
    b2 = Button(login_menu, text='Exit', command=login_menu.quit).pack(side=RIGHT)
    def ending():
        sys.exit(0)
        login_menu.destroy()
    login_menu.protocol("WM_DELETE_WINDOW", ending)
    login_menu.mainloop()
    # if login_menu:
    #     login_menu.destroy()

if __name__ == '__main__':
    # 主程序登录
    login_database()


    # 调试
    # sql = login_database()
    #
    #
    # while True:
    #     if sql.user == 'sa':
    #         print("Welcome to the Fruit Management System.\nUser: " + sql.user + "\nCompetence:" + " Fruit manager")
    #         employee_main_frame(sql)
    #     elif sql.user == 'admin':
    #         print("Welcome to the Fruit Management System.\nUser: " + sql.user + "\nCompetence:" + " Employee manager")
    #         manager_main_frame(sql)


    # sql.execute_insert("insert into fruit values"
    #                    "('0001', '苹果', 'MK', '健脾益气，和胃止痛', 3, 6, 20, 20, 0)")
    # sql.execute_delete("delete from fruit where Fname = '苹果'")
    # sql.execute_alter("update fruit set Sell_price = Sell_price + 1"
    #                   "where Fname = '苹果'")
    # select_database(sql)