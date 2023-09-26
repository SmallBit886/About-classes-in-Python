#定义Python中的类
class Student:  #Student为类的名称（类名）；由一个或者多个单词组成；每个单词首字母大写，其余小写
    native_place='河南'   #直接写在类之内的变量，称为类属性

    def __init__(self ,name,age):
        self.name=name
        self.age=age    #self.name称为实例属性，进行了赋值操作，将局部变量name的值赋值给实体属性
    #实例方法
    def eat(self):
        print("吃饭了")

    #静态方法
    @staticmethod
    def method():
        print("我使用了staticmethond，所以我是静态方法。")

    #类方法
    @classmethod
    def cm(cls):
        print("我使用了classmethond，所以我是类方法。")

 #在类之外的称为函数，在类之内的称为方法
def drink():
    print("喝水了")

#创建student的对象
stu1=Student('张三',20)
print(id(stu1)) #2233712699088
print(type(stu1))   #<class '__main__.Student'>
print(stu1) #<__main__.Student object at 0x0000020813A6E6D0>
print("-------------------------------------")
print(id(Student))  #1639086214768
print(type(Student))    #<class 'type'>
print(Student)  #<class '__main__.Student'>
