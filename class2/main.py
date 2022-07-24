class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):  # 将self作为第一个变量 -dash __dunder
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '.' + '@email.com'

        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def __repr__(self):  # a more readable object 最终用户端显示
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):  # 对对象的明确表示应用与debug/log
        return '{} - {}'.format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


# 继承：子系有自己的特点也继承了父系特点


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # 或者 Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  # 或者 Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(('-->', emp.full_name()))

    # classmethod 代替构造函数（还不如直接构造呢，感觉用处不大） 将cls作为第一个参数

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


#     @staticmethod  # 不将self或cls作为变量
#     def is_workday(day):
#         if day.weekday == 5 or day.weekday == 6:
#             return False
#         return True
#
# import datetime
# my_date = datetime.date(2016, 7, 1)
# print(Employee.is_workday(my_date))


# dev_1 = Developer('corey', 'schafer', 50000, 'python')
# dev_2 = Developer('test', 'user', 60000, 'java')
# mar_1 = Manager('sue', 'smith', 90000, [dev_1])
# print(mar_1.email)
# mar_1.add_emp(dev_2)
# mar_1.print_emps()
emp_1 = Employee('corey', 'schafer', 50000)
emp_2 = Employee('test', 'user', 60000)


# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1)
# print(emp_1.__repr__())
# print(emp_1.__str__())
# emp_str_1 = 'john-doe-70000'
# emp_str_2 = 'steve-smith-30000'
# emp_str_3 = 'jane-doe-90000'
# new_emp_1 = Employee.from_string(emp_str_1)
# emp_1.first = 'corey'
# emp_1.last = 'schafer'
# emp_1.email = 'corey.schfaer@company.com'
# emp_1.pay = 50000
# emp_2.first = 'test'
# emp_2.last = 'user'
# emp_2.email = 'test.user@company.com'
# emp_2.pay = 60000
# print(emp_1.email)
# print(emp_2.email)
# print(Employee.full_name(emp_1))
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(Employee.num_of_emps)
# print(emp_1.__dict__)
# print(Employee.__dict__)
# Employee.raise_amount = 1.05
# emp_1.raise_amount = 1.05
# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(new_emp_1.email)
# print(new_emp_1.pay)
# print(dev_1.prog_lang)
# print(emp_1 + emp_2)
# print(len(emp_1))
# print(isinstance(mar_1, Developer))   # 检测是否为实例
# print(issubclass(Manager, Employee))  # 检查所属类

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # 属性装饰器 避免大规模修改
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp_1 = Employee('john', 'smith')
emp_1.fullname = 'corey schafer'
emp_1.first = 'jim'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

