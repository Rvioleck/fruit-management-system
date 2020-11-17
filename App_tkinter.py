import pymssql
import sys,os
from tkinter import *

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
            raie(NameError, "There is no datebase named" + db)

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
            for row in rows:
                for data in row:
                    print('{}\t'.format(str(data).strip()), end=' ')
                print()
            os.system('pause')
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
            print("Unable to alter data. Please check your input data.")
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
            print("Unable to delete data. Please check your input.")
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
            print("Unable to insert data. Please check your input data.")
            # self.db.rollback()

def interface_login_database():
    """
    登录数据库, 登录菜单设计
    :return:
    """
    def main_frame():
        """
        在登录菜单中选择login时触发
        主程序判断账号密码，并且选择进入管理员和普通员工的功能模块
        :return:
        """
        user = e1.get()
        pwd = e2.get()
        response_menu = Tk()
        # # 设置窗口出现位置
        # width, height = 300, 100
        # screen_width, screen_height = response_menu.winfo_screenmmwidth(), response_menu.winfo_screenheight()
        # alignstr = '%dx%d+%d+%d' % (width, height, (screen_width-width)/2, (screen_height-height)/2)
        # response_menu.geometry(alignstr)
        if user == 'sa' and pwd == '123456':
            # 普通水果管理员入口
            sql = SQL(host='(local)', user='sa', pwd='123456', db='fmdb')
            # response_menu.geometry('200x100')
            response_menu.title("Tips interface")
            # 标签提示
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
            response_menu.destroy()
            login_menu.destroy()
            # employee主功能
            employee_main_frame(sql)
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
            response_menu.destroy()
            login_menu.destroy()
            manager_main_frame(sql)
        else:
            # 非法的账号密码，提示窗口
            response_menu.geometry('380x100')
            response_menu.title("Tips interface")
            l1 = Label(response_menu,
                       text="Please check your password or username!\n Failed to connect the database.",
                       font=('Helvetica', 12, 'bold')).pack(padx=10,pady=10)

            b1 = Button(response_menu,
                        text="OK",
                        command=response_menu.quit)
            b1.pack(padx=10, pady=10)
            response_menu.mainloop()
            response_menu.destroy()
            # login_menu.destroy()
    # inteface_login_datebase主体
    login_menu = Tk()
    login_menu.geometry('500x200')
    login_menu.title("Login interface")
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
    e1.pack(side=RIGHT)
    frame1.pack(padx=20, pady=10)
    # frame2输入框的提示标签和输入框
    frame2 = Frame(login_menu)
    l2 = Label(frame2,
               text='Passport:',
               font=('Helvetica', 12),
               width=10).pack(side=LEFT)
    e2 = Entry(frame2)
    e2.pack(side=RIGHT)
    frame2.pack(padx=20, pady=10)
    # 创建按钮
    b1 = Button(login_menu, text='Login', command=main_frame).pack()
    b2 = Button(login_menu, text='Exit', command=login_menu.quit).pack(side=RIGHT)
    login_menu.mainloop()
    login_menu.destroy()

def employee_select_database(sql):
    select_phrase = ['select * from fruit', 'select * from client']
    tag = input("Please choose an operation：1. Check the fruits details\n"
                "                        \t2. Check the VIP clients details\n"
                "                        \t3. return to main menu.")
    if tag == '1':
        # 搜索水果的详情
        sql.execute_query(select_phrase[0])
    elif tag == '2':
        # 搜索顾客的详情
        sql.execute_query(select_phrase[1])
    elif tag == '3':
        return
    else:
        print("Please enter the correct choice！")

def employee_alter_database(sql):
    tag = input("Please choose an operation：1. Update the fruits inventory information.\n"
                "                        \t2. Update the prices of fruits.\n"
                "                        \t3. Update the notes of fruits.\n"
                "                        \t4. Return to main menu.")
    if tag == '1':
        # 更新库存
        tag2 = input("Please choose an operation：1. Update the fruits income information\n"
                    "                          \t2. Update the fruits outcome information\n"
                    "                          \t3. \n")
        if tag2 == '1':
            # 增加水果库存的同时更改累计入库的数量
            alter_fruits_inventory = 'update fruit set Storage = Storage + {} ' \
                                     'where Fname = \'{}\''
            alter_fruits_innumber = 'update fruit set Innumber = Innumber + {} ' \
                                     'where Fname = \'{}\''
            fruit_name, inventory = input("Please enter the name and inventory of the fruit:").split()
            alter_fruits_inventory = alter_fruits_inventory.format(inventory, fruit_name)
            alter_fruits_innumber = alter_fruits_innumber.format(inventory, fruit_name)
            sql.execute_alter(alter_fruits_inventory)
            sql.execute_alter(alter_fruits_innumber)
        elif tag2 == '2':
            # 减少水果库存的同时更改累计出库的数量
            alter_fruits_inventory = 'update fruit set Storage = Storage + {} ' \
                                     'where Fname = \'{}\''
            alter_fruits_outnumber = 'update fruit set Outnumber = Outnumber + {} ' \
                                     'where Fname = \'{}\''
            fruit_name, inventory = input("Please enter the name and inventory of the fruit:").split()
            alter_fruits_inventory = alter_fruits_inventory.format(inventory, fruit_name)
            alter_fruits_outnumber = alter_fruits_outnumber.format(inventory, fruit_name)
            sql.execute_alter(alter_fruits_inventory)
            sql.execute_alter(alter_fruits_outnumber)
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
            sql.execute_alter(alter_fruits_price)
        elif tag2 == '2':
            # 更新出售价格
            alter_fruits_price = 'update fruit set Sell_price = {} ' \
                                 'where Fname = \'{}\''
            fruit_name, sell_price = input("Please enter the name and sell price of the fruit:").split()
            alter_fruits_price = alter_fruits_price.format(sell_price, fruit_name)
            sql.execute_alter(alter_fruits_price)
    elif tag == '3':
        # 修改水果的备注
        alter_fruits_notes = 'update fruit set note = \'{}\' ' \
                                 'where Fname = \'{}\''
        fruit_name, notes = input("Please enter the name and notes of the fruit which you want to modify:").split()
        alter_fruits_notes = alter_fruits_innumber.format(notes, fruit_name)
        sql.execute_alter(alter_fruits_notes)
    elif tag == '4':
        return
    else:
        print("Please enter the correct choice！")

def employee_delete_datebase(sql):
    fruit = input("Please enter the fruit name which you want to delete from this system.\n"
                  "(enter 'exit' to return to main menu.)")
    if fruit == 'exit':
        return
    else:
        delete_fruits = "delete from fruit where Fname = \'{}\'".format(fruit)
        sql.execute_delete(delete_fruits)

def employee_insert_database(sql):
    # 添加新水果信息
    fruit = input("Please enter the fruit name which you want to insert into this system: ")
    no = input("Please enter the number of the fruit which is not in system (0001-9999): ")
    manufactor = input("Please enter the manufactor of the fruit: ")
    note = input("Please enter the note of the fruit (less than 40 words): ")
    pur_price = int(input("Please enter the purchase price of the fruit (Yuan/kg): "))
    sell_price = int(input("Please set the sell price of the fruit (Yuan/kg): "))
    storage = int(input("Please enter the storage number of the fruit: "))
    innumber = storage
    outnumber = 0
    # 生成insert的sql语句
    insert_fruit = "insert into fruit values" \
                   "(\'{}\', \'{}\', \'{}\', \'{}\'," \
                   " {}, {}, {}, {}, {})".format(no, fruit, manufactor, note, pur_price, sell_price, storage, innumber, outnumber)
    sql.execute_insert(insert_fruit)

def employee_main_frame(sql):
    emp_main_menu = Tk()
    emp_main_menu.title("Employee inteface")
    # 标签l1提示操作
    l1 = Label(emp_main_menu,
               text='Choose an operation which you want.',
               font=('Helvetica', 12))
    l1.pack(padx=10, pady=10)
    # frame1存放前两个操作
    frame1 = Frame(emp_main_menu)
    b1 = Button(frame1,
                text="query information",
                width=20,
                height=2,
                command=lambda: [emp_main_menu.destroy(), employee_select_database(sql)]) # command传参数lambda:函数(参数)
    b1.pack(side=LEFT, padx=10, pady=10)
    b2 = Button(frame1,
                text="update information",
                width=20,
                height=2,
                command=lambda: [emp_main_menu.destroy(), employee_alter_database(sql)])
    b2.pack(side=LEFT, padx=10, pady=10)
    frame1.pack()
    # frame2存放后两个操作
    frame2 = Frame(emp_main_menu)
    b3 = Button(frame2,
                text="delete information",
                width=20,
                height=2,
                command=lambda: [emp_main_menu.destroy(), employee_delete_datebase(sql)])
    b3.pack(side=LEFT, padx=10, pady=10)
    b4 = Button(frame2,
                text="insert information",
                width=20,
                height=2,
                command=lambda: [emp_main_menu.destroy(), employee_insert_database(sql)])
    b4.pack(side=LEFT, padx=10, pady=10)
    frame2.pack()
    # 返回按钮
    b5 = Button(emp_main_menu,
                text="logout",
                # command调用两个函数，返回主菜单和关闭该组件
                command=lambda: [emp_main_menu.destroy(), interface_login_database()]).pack(side=RIGHT)
    emp_main_menu.mainloop()
    # emp_main_menu.destroy()

def manager_select_database(sql):
    select_phrase = ['select * from fruit', 'select * from employee', 'select * from client']
    tag = input("Please choose an operation：1. Check the fruits details\n"
                "                          \t2. Check the employees details\n"
                "                          \t3. Check the VIP clients details\n"
                "                          \t4. return to main menu.")
    if tag == '1':
        # 搜索水果的详情
        sql.execute_query(select_phrase[0])
    elif tag == '2':
        # 搜索员工的详情
        sql.execute_query(select_phrase[1])
    elif tag == '3':
        # 搜索顾客的详情
        sql.execute_query(select_phrase[2])
    elif tag == '4':
        return
    else:
        print("Please enter the correct choice！")

def manager_alter_database(sql):
    tag = input("Please choose an operation：1. Update the salary of employee.\n"
                "                        \t2. Update the prices of fruits.\n"
                "                        \t3. return to main menu.")
    if tag == '1':
        # 更新员工薪资
        alter_employee_salary = 'update employee set Esalary = {}' \
                                'where Ename = \'{}\''
        name, salary = input("Please enter the name and salary of the the employee:").split()
        alter_employee_salary = alter_employee_salary.format(salary, name)
        sql.execute_alter(alter_employee_salary)
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
            sql.execute_alter(alter_fruits_price)
        elif tag2 == '2':
            # 更新出售价格
            alter_fruits_price = 'update fruit set Sell_price = {} ' \
                                 'where Fname = \'{}\''
            fruit_name, sell_price = input("Please enter the name and sell price of the fruit:").split()
            alter_fruits_price = alter_fruits_price.format(sell_price, fruit_name)
            sql.execute_alter(alter_fruits_price)
    elif tag == '3':
        return
    else:
        print("Please enter the correct choice！")

def manager_delete_datebase(sql):
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
            sql.execute_delete(delete_fruits)
    elif tag == '2':
        employee = input("Please enter the employee's name which you want to delete from this system.\n"
                      "(enter 'exit' to return to main menu.)")
        if employee == 'exit':
            return
        else:
            delete_employee = "delete from employee where Ename = \'{}\'".format(employee)
            sql.execute_delete(delete_employee)
    elif tag == '3':
        customer = input("Please enter the VIP's name which you want to delete from this system.\n"
                      "(enter 'exit' to return to main menu.)")
        if customer == 'exit':
            return
        else:
            delete_customer = "delete from client where Cname = \'{}\'".format(customer)
            sql.execute_delete(delete_customer)
    elif tag == '4':
        return
    else:
        print("Please enter the correct choice！")

def manager_insert_database(sql):
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
    sql.execute_insert(insert_employee)

def manager_main_frame(sql):
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
                command=lambda: [man_main_menu.destroy(), manager_select_database(sql)])  # command传参数lambda:函数(参数)
    b1.pack(side=LEFT, padx=10, pady=10)
    b2 = Button(frame1,
                text="update information",
                width=20,
                height=2,
                command=lambda: [man_main_menu.destroy(), manager_alter_database(sql)])
    b2.pack(side=LEFT, padx=10, pady=10)
    frame1.pack()
    # frame2存放后两个操作
    frame2 = Frame(man_main_menu)
    b3 = Button(frame2,
                text="delete information",
                width=20,
                height=2,
                command=lambda: [man_main_menu.destroy(), manager_delete_datebase(sql)])
    b3.pack(side=LEFT, padx=10, pady=10)
    b4 = Button(frame2,
                text="insert information",
                width=20,
                height=2,
                command=lambda: [man_main_menu.destroy(), manager_insert_database(sql)])
    b4.pack(side=LEFT, padx=10, pady=10)
    frame2.pack()
    # 返回按钮
    b5 = Button(man_main_menu,
                text="logout",
                # command调用两个函数，返回主菜单和关闭该组件
                command=lambda: [man_main_menu.destroy(), interface_login_database()]).pack(side=RIGHT)
    man_main_menu.mainloop()
    # emp_main_menu.destroy()

if __name__ == '__main__':
    interface_login_database()
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