#动态绑定属性和放法
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print(self.name+'在吃饭')

'''一个Student对象可以创建N多个实例对象，每个实例对象的属性值不同'''
stu1=Student('张三',20)
stu2=Student('李四',30)
print(id(stu1))
print(id(stu2))
'''
3080636524720
3080636523712
'''
print('---------------为stu2动态绑定性别属性------------------------')
stu2.gender='女'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)
'''
张三 20
李四 30 女
'''
print('------------------动态绑定show方法-----------------------')
stu1.eat()
stu2.eat()
print('----------------------')
def show():
    print('定义在类之外的称为，函数')

stu1.show=show

stu1.show()
#stu2.show()