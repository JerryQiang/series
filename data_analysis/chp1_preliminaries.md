# 使用Python进行数据分析
Python for Data Analysis
Data Wrangling with Pandas, NumPy, and IPython 2nd Edition

# 第一章 总览

## 1.1 这本书的主要内容
这本书主要讲述数据的预处理过程(manipulating, processing, cleaning, and crunching data)。
面向**Python3**编程实现，讲述**pandas**的使用。
ps：作者Wes McKinney，是该库的主要实现者。

### 数据的种类
主要处理**结构化数据**。
- 电子表格（excel等），其中每列可以是不同的类型（字符串，数字，日期等）；
- 制表符或逗号分隔的文本文件；
- **多维数组**（矩阵，Matrices）；
- 关系数据库的数据表（SQL用户的主键或外键）；
- 均匀或不均匀的**时间序列**（Time Series）。


## 1.2 使用Python做数据分析的原因

数据处理的目的在于将杂乱，无序的数据变得结构化，为机器学习模型提供输入。

python作为一门“胶水”语言，能够很快的实现数据分析和逻辑处理，必要时还可以使用C/C++拓展。

但python**不适合**高频率，低延时的场景
  毕竟Python是解释性语言，优势在于开发便捷，性能方面的确比不上编译语言C/C++和java。

python**不适合**多线程并发处理
  由于python的**GIL**机制(Global Interpreter Lock，全局解释器锁 )，本质上是一个全局排他锁，导致各线程空占CPU，而无法执行相关运算。因此python不适合多线程并发处理。
  详见<a href="https://www.cnblogs.com/SuKiWX/p/8804974.html">python中的GIL详解</a>
  多进程和多线程详见<a href="https://www.liaoxuefeng.com/wiki/1016959663602400/1017627212385376">廖雪峰 进程和线程</a>




## 1.3 基本Python库
以下是几个重要的用于数据分析的Python库，我会给予简单的介绍，后面的章节会有详细的阐述。
### NumPy
NumPy（Numerical Python），Python中数值计算的基石，提供了数值计算的数据结构和算法，涉及数值数据的大多数科学应用库都基于它实现。 
NumPy包含以下内容：
- 快速高效的多维数组对象ndarray
- 阵列计算和逐元素计算函数
- 从磁盘读取和写入多维数组的工具
- 线性代数运算，傅里叶变换和随机数生成
- 成熟的C API，支持Python扩展和本地C/C++代码，以访问NumPy的数据结构和计算设施
除了NumPy为Python添加的快速数组处理功能之外，它在数据分析中的主要用途之一是作为数据在数据库和库之间传递的容器。对于数值数据，NumPy数组比其他内置Python数据结构更有效地存储和操作数据。此外，用较低级语言（如C或Fortran）编写的库可以对存储在NumPy数组中的数据进行操作，而无需将数据复制到其他内存表示中。因此，许多用于Python的数值计算工具要么将NumPy数组假设为主要数据结构，要么将目标与NumPy无缝互操作。

### pandas


### matplotlib


### IPython and Jupyter


### SciPy

### scikit-learn



### statsmodels


## 1.4 Installation and Setup



### 1.5 Community and Conferences


