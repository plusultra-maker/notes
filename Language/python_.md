# 这是一个从0开始记录python这门语言的功能和特性的笔记
- source:
  - cb老师mooc：python语言基础及应用
## 数据类型
1. 不可变类型：
   - 不灵活，难以操作
   - 整数，浮点数，复数，字符串，逻辑值（bool）,元组：用()框住的有序组
2. 可变：
   - 可以用成员函数进行操作
   - 列表：list()或[]框住的有序组（下标为序号）
   - 字典：{}或set()，元素类型为key:value,key为索引
   - 集合：无序集合，集合的元素不能是可变类型
   - 注意可变变量的=操作为引用，则说明被引用的对象在后面改变了，所有引用都会变
   - 通过列表和字典嵌套其他可变or不可变数据类型实现复杂的数据结构
3. 输入输出：
   - x=input('x:'),返回值是字符串，用int(x)强制转换为整数
   - print可选参数包括：变量簇，sep：间隔字符串，end：句尾，file：out文件
   - 也可以用类似c的做法 '%d %s' % (21,'asd')
## 面向对象：
 - 对象+属性and操作，实现了属性和方法的封装
 - python 可以随时动态的添加or删除属性
 - 类的定义：
  ```python
  class <name>:
      def __init__(self,<parameter>)：
      def <function>(self,<parameter>):
  ```
   - 这里定义函数时通过self.fx来引用属性（类似this指针）
 - 调用：obj=name(parameter)
 - 类定义中的特殊方法（以两个下划线__开始和结束）
  ``` python
   - 构造:__init__
   - 析构:__del__
   - 算术操作符：__add__ etc.
   - 反运算:__radd__ etc.
   - 比较:__eq__ etc.
   - 输出易读字符串:__str__
   - 还有很多可以查
  ```
 - 排序
   - 列表中用sort(),降序可以sort(reverse=True)
     - 用sorted()返回一个排好序的副本
   - 类中可以定```__lt__(self,y)```定义self比y应靠前排，则返回True
 - 继承
   - 从已有的类中衍生出新的类，添加或修改功能
   ```python
  class <son>(<father>):
      def <redefinefunction>(self,<parameter>):
   ```
   - 可以完全添加新的，也可以覆盖
    - 当覆盖时，可以用```super().<function>```调用父类中的原方法，从而方便迭代的定义
## 其他高级特性
   - 有时间看：[高级特性（二）](https://www.icourse163.org/spoc/learn/PKU-1206269805?tid=1206594202#/learn/content?type=detail&id=1211325297&sm=1)