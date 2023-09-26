#类属性的使用方式

#定义Python中的类
class Student:  #Student为类的名称（类名）；由一个或者多个单词组成；每个单词首字母大写，其余小写
    native_place='河南'   #直接写在类之内的变量，称为类属性
    '''******************被该类的所有对象所共享**********************'''

    def __init__(self ,name,age):
        self.name=name
        self.age=age    #self.name称为实例属性，进行了赋值操作，将局部变量name的值赋值给实体属性
    #示例方法
    def eat(self):
        print("吃饭了")

    #静态方法
    @staticmethod
    def method():
        print("我使用了staticmethond，所以我是静态方法。")
    '''*****************使用类名直接访问********************'''
    #类方法
    @classmethod
    def cm(cls):
        print("我使用了classmethond，所以我是类方法。")

print(Student.native_place)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_place)
print(stu2.native_place)
'''
河南
河南
河南
'''
Student.native_place='光山'
print(stu1.native_place)
print(stu2.native_place)
'''
光山
光山
'''
print("-----------------------------------")
#调用类方法
Student.cm()
#调用静态方法
Student.method()



