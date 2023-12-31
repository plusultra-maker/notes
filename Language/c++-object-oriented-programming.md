# C++ object-oriented programming
旨在记录一些C++面向对象技巧

## 类的定义
- 提醒：
  - 23.4.10：当类的成员函数包含指针时，要么就是浅复制（只传地址），要么就是深复制：既要在构造时new出自己的空间，也在析构时delete [] p;new和delete总是成对出现

## 运算符重载
- 重载算术运算符+，-，etc.
  - 实质上是重载函数
  - 可以重载为
    - 普通函数：就需要n个形参
    - 成员函数：n-1个形参，另一个就是对象本身
- 赋值运算符重载
  - 只能定义为成员函数，通常用于把一个其他类型的值赋到对象上
  - 返回值为引用：```String & operator = (const char* s);```
    - 注意这里返回引用的原因是尽量保留运算符的原本特性，要求如果这个赋值语句再参与其他运算，应当指的是该对象eg.(a=b)=c    
  - 只能用于赋值，不能在定义构造时使用（否则会调用复制构造）
  - String类的深拷贝浅拷贝
    - string类的成员变量为一个字符串指针，如果不定义逐渐的赋值运算，则会导致两个String指向同一处
  - PS.赋值运算符重载的时候要注意，如果涉及到指针的操作，一定要记得给指针赋值之前要确保__指针是NULL__，否则会造成内存泄漏
- 当运算符写为成员函数的形式不能满足要求eg.5+complex
  - 但又需要访问私有变量
  - 则重载为友元函数
- 一个例子：可变长数组：
  - P215 
  - 注意：
    - 对于以指针为成员变量的类，其赋值运算和复制构造要小心需不需要重新建立指针、开空间
    - 重载[]时，返回值为引用（本质上是要返回那个变量，而非值）
    - 如果只是复制指针而不是新开空间的话，会在析构时把同一个地址析构两次，导致 __Seg fault__
- 流插入与流提取
  - 流插入```cout<<```,cout是ostream类的对象，"<<"提取运算符在这个类上重载
  - 为了使其可以连续运行```cout<<5<<"this"```,则应该使其返回类型为ostream &，返回值即本身*this，类似之前赋值中的的a=b=c
  - 如果要为新的类的对象写输出，则在ostream上重载<<为普通函数
   ```cpp
    ostream & operator(ostream & os,const T t)//注意不需要变的引用都加上const
    {
      os<<t.fx;
      return os;//记得返回os!!!!!
    }
   ```
   
  - 输入流是一样的，istream类，但函数体可能更复杂，需要拆解输入的字符串并拆解读值
- 类型转换与自增自减
  - 类型转换：指将该类转换为别的类，不需要写返回值类型
  ```cpp
    //complex to double保留实部
    Complex::operater double (){return real;}
    cout<<(double)c;
    double a=c;
  ```
  - 自增自减：前置与后置
    - 前置作为一元运算符
      - 成员函数定义直接空参数，返回为引用
    - 后置作为二元运算符，多写一个没用的参数(int)
      - 但注意按照定义 后置要返回原值 而不是加过的值
     

## 继承

## 多态
- 多态是派生带来的应用方式，cpp中用虚函数实现
- cpp中最好用指针和引用来操作虚函数
  - >在 C++ 中，虚函数的调用一般都需要使用指针或者引用的形式，而不能直接使用对象的形式。这是因为 C++ 中的虚函数是通过虚表来实现的，每个对象都有一个指向虚表的指针。
- 优点在于当一个函数的参数或一个需要操作的对象可能是很多种派生类时，可以直接将其写为大类的形式，并以大类的形式调用虚函数。此时当执行时，该值被确定为哪个派生类，就调用哪个派生类的函数。
  - 实际上即以大类的形式同一的构建关系，但执行时按派生类分方式执行。
- 实例：用一个基类指针（！）数组储存所有派生类的变量指针，但每个变量指针都是以派生类创造的，这样对数组内值的同一操作（写法上）可以产生对应的不同的效果
  - >用基类指针数组存放指向各种派生类对象的指针，然后遍历该数组，就能对各个派生类对象做各种操作，是很常用的做法
- 究竟调用哪个派生类的虚函数，看的是调用指针所指对象的类型，而非调用指针的类型
  - >在 C++ 中，虚函数的动态绑定是基于对象的实际类型来进行的，而不是基于指针或引用的类型。当通过基类指针或引用调用虚函数时，编译器会根据指针或引用所指向的对象的实际类型来确定调用哪个版本的虚函数，而不是根据指针或引用本身的类型来确定。
- 虚函数表
- 虚析构函数：当构造函数和析构函数被声明为虚时，则会先按虚函数规则执行对应函数，再执行该析构函数

## 输入输出
- 相关类
  - iostream:标准输入输出流
  - fstream：文件
- iostream
  - istream
    - cin:用while(cin>>x)，此时cin作为是一个流对象，支持 bool 类型转换运算符，可以将其转换为 bool 值。从而没有数据可读的时候，就返回false，结束循环
      - 更严格的说：
        >当输入流遇到文件末尾或错误时，会将流状态置为 eofbit 或 failbit。在布尔上下文中，istream 对象被隐式转换为 true，除非它的状态包含 eofbit 或 failbit，此时它会被转换为 false。因此，在输入操作返回 istream 对象时，检查输入流的状态即可判断输入操作是否成功。
        因此我们可以用
  - istream类的成员函数
    - istream & getline(char * buf, int bufSize,char delim);
      - 从输入流读写到缓冲区buf，到delim结束（缺省则为'\n'），delim会被读，但不会被写入buf，数据结尾添\0。
      - 但最多读bufsize-1个，达到或超过都会导致之后的读入错误
      - 可以用 if(!cin.getline(…)) 判断输入是否结束,与上文类似
    - bool eof()判断输入流是否结束
      ```cpp
      while (true) {
        int x;
        cin >> x;
        if (cin.eof()) {
            break; // 输入流已经结束，退出循环
        }
        // 处理读入的数据
      }
    - int peek(); 返回下一个字符,但不从流中去掉.如果输入流已经结束，则返回 EOF（即 -1）。
      - 如果想要其从流中去掉，用cin.get()
      - 这两者方式让我们更好的控制如何读输入
    - istream & putback(char c); 将字符ch放回输入流
    - istream & ignore( int nCount = 1, int delim = EOF );从流中删掉最多nCount个字符，遇到EOF时结束。
  - 重定向
    - ```cpp
      freopen(“t.txt”,“r”,stdin); //cin被改为从 t.txt中读取数据
      freopen("test.txt","w",stdout); //将标准输出重定向到 test.txt文件
    - 其他正常写即可
- 流操纵算子
  - #include <iomanip>
  - 整数流的基数（进制）：流操纵算子dec,oct,hex
  - 浮点数精度：
    - precision是成员函数，其调用方式为：cout.precision(5);
    - setprecision 是流操作算子，其调用方式为：cout << setprecision(5); // 可以连续输出
    - 默认是n位有效数字（非定点）
      - 加入setiosflags(ios::fixed)，小数点固定，变为小数点后n位
      - 再加入resetiosflags(ios::fixed)，则取消固定
    - 只对浮点数，对整型不影响
  - 设置域宽
    - ```cin >> setw(n) or  cin.width(n)；```cout类似
    - 默认靠右，左侧填充，可以在```setw<<left``` 等控制
    - 可以选择setfill('*')填充物
- 自定义流操作算子 
  - ```cpp
    ostream &tab(ostream &output){
      return output << '\t';
    }
    cout << “aa” << tab << “bb” << endl;
  - 原因是<<重载了这样的参数
    ```cpp 
    ostream & operator<<( ostream & ( * p ) ( ostream & ) ) ;
- 文件
  - #include <fstream>
  - ofstream
    ```cpp 
    ofstream fout;
    fout.open("test.out",ios::out|ios::binary);
    ```
  - ios::out是删除重写，ios::app是续写
  - 读写操作是基于读写指针的，用过tellp()获取，通过seekp()移动
  - 文件流是和标准流一样的，可以用<<,>>,也可以加成员函数和操作算子
    - 文件专有的，read 和 write
## 模板
### 函数模板
- 函数模板的定义格式如下：
  ```cpp
  template <typename T>
  T func_name(T arg1, T arg2, ...)
  {
      // 函数体
  }
- 当然也可以有多于一个类型参数
  ```cpp
  template <class T1, class T2>
  T2 print(T1 arg1, T2 arg2)
  {
    cout<< arg1 << " "<< arg2<<endl;
    return arg2;
  }
- 也可以主动实例化模板，主动决定类型
  ```cpp
  template<typename T>
  T Inc(T n)
  {
      return 1 + n;
  }

  int main()
  {
      cout << Inc<double>(4)/2.0; // 输出 2.5
      return 0;
  }
- 函数模板可以重载，只要它们的形参表或类型参数表不同即可
- 选择函数调用的顺序
  1) 先找参数完全匹配的普通函数(非由模板实例化而得的函数)。
  2) 再找参数完全匹配的模板函数。
  3) 再找实参数经过自动类型转换后能够匹配的普通函数。
  4) 上面的都找不到，则报错。
  - 匹配模板函数时，不进行类型自动转换

### 类模板

- 与函数模板类似，类模板的定义格式也是类型参数表+类定义
  - 成员函数的定义，无论是在内部还是外部，都再写一遍类型参数表
  - 实例化对象的时候：类模板名 <真实类型参数表> 对象名(构造函数实参表);
- 类模板的类型参数表里可以出现非类型参数，比如一个需要给出的数组长度int size
- 类模板与派生
  - 从类模板派生类模板
  ```cpp
  template <typename T>
  class DerivedClass : public BaseClass<T> {
    // 派生类的成员和特性
  };
  ```
  - 实例化时，逻辑上可以理解为，我把派生类实例化了，从而确定了T，从而再实例化基类
- 类模板与友元
  - 在模板中定义的友元函数，那所有实例化的对象都有这些友元函数
  - 友元函数也可以以函数模板形式存在
  - 友元类也可以以类模板的形式存在
- 类模板也可以包含static变量，每一个被实例化的类都有自己的那个static变量
 
 
  