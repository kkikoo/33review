# 定义一个员工类
class Employee:

    raise_count = 1.04  # 工资上升
    num_of_emps = 0  # 创建的员工类的个数

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + "." + last +"@company.com"
        self.pay = pay
        Employee.num_of_emps += 1  # 计算创建的员工类的个数

    # 对象方法，输出员工全名
    def fullname(self):
        return '{}{}'.format(self.first,self.last)

    # 对象方法，计算上涨后的工资
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_count)


# 定义一个开发者类，继承自员工类
class Developer(Employee):
    raise_count = 1.5       # 重写了工资上涨幅度

    def __init__(self, first, last, pay, pro_lang):  # 重写__init__方法, pr_lang意为擅长的语言
        super().__init__(first,last,pay)             # 继承Employee的__init__方法，并赋初值
        self.pro_lang = pro_lang                     # 初始化pro_lang


# 定义一个管理者类，继承自员工类
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None): # 重写__init__方法, employees意为手下员工
        super().__init__(first, last, pay)                # 继承Employee的__init__方法，并赋初值
        if employees is None:
            employees = []
        else:
            self.employees = employees

    # 定义一个对象方法，功能为添加员工
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print("已存在")

    # 定义一个对象方法，功能为删除员工
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # 定义一个对象方法，功能为展示所有
    def show_all_emp(self):
        for emp in self.employees:
            print(emp.fullname())

if __name__ == '__main__':
    # 实例化两个开发者类并显示信息
    dev1 = Developer('Mike', 'Black', 5000, 'Python')
    dev2 = Developer('Bod', 'Sqod', 6000, 'Java')
    print(dev1.email, '\t',  dev1.first, '\t', dev1.last, '\t', dev1.pay, '\t', dev1.pro_lang)
    print(dev1.email, '\t',  dev2.first, '\t', dev2.last, '\t', dev2.pay, '\t', dev2.pro_lang)
    print("\n")
    # 实例化管理者类
    mgr1 = Manager('Zhang', 'San', 9000, [dev1]) # 注意，初始化时，员工一定要是一个列表
    print(mgr1.first, mgr1.last, mgr1.email)
    print("\n")
    # 展示员工
    print(mgr1.fullname(), "手下的员工有：")
    mgr1.show_all_emp()
    print("\n")
    # 增加员工
    mgr1.add_emp(dev2)
    print(mgr1.fullname(), "手下的员工有：")
    mgr1.show_all_emp()
    print("\n")
    # 删除员工
    mgr1.remove_emp(dev1)
    print(mgr1.fullname(), "手下的员工有：")
