
# 100 numpy exercises

This is a collection of exercises that have been collected in the numpy mailing list, on stack overflow and in the numpy documentation. The goal of this collection is to offer a quick reference for both old and new users but also to provide a set of exercises for those who teach.


If you find an error or think you've a better way to solve some of them, feel free to open an issue at <https://github.com/rougier/numpy-100>

#### 1. 引入NumPy包，并设置别名为`np` (★☆☆)


```python3
import numpy as np
```
一个py文件是一个模块（Module）
pip install 安装的整体是一个包（Package）
<br/>

#### 2. 打印NumPy的版本及配置 (★☆☆)


```python3
import numpy as np
print(np.__version__)

import pandas as pd
print(pd.__version__)

# import sys
# print(sys.__version__)  # AttributeError: module 'math' has no attribute '__version__'

np.show_config()
```
自定义安装的包有__version__属性,等价于pip list显示包的版本
安装python内置的包则无__version属性
show_config()是NumPy独有的方法
<br/>

#### 3. 创造大小为10，初始化为0的向量 (★☆☆)


```python3
import numpy as np
arr = np.zeros(10)
print(type(arr))
print(arr.size, arr.ndim, arr.shape, arr.dtype)  # 数组大小，数组维度，数组形状，数组元素类型
print(arr)
```
NumPy中的最基础的数据结构是ndarray，多维数组
1维数组是向量
2维数组是矩阵
3维及以上没有特定名称
<br/>

#### 4.  查询数组所占内存 (★☆☆)


```python3
import numpy as np
arr = np.zeros((10, 10))

import sys
print("%d bytes" % sys.getsizeof(arr))  # 对象所占总内存

print("%d bytes" %(arr.size * arr.itemsize))  # 数组本身所占内存

arr_int32 = arr.astype(np.int32)
print("%d bytes" % sys.getsizeof(arr_int32))  # 对象所占总内存

print("%d bytes" %(arr_int32.size * arr_int32.itemsize))  # 数组本身所占内存
```
对象所占总内存除了数组本身所占内存，还包括数组信息：数组大小，数组形状，数组元素类型等信息
观察上述程序可以发现数组信息所占内存为112bytes（912-800==512-400==112）
数组本身所占内存由数组大小和数组元素类型决定
<br/>

#### 5.  通过命令行获取NumPy add函数的文档说明 (★☆☆)



在终端(Terminal)中运行如下指令
```console
python3 -c "import numpy; numpy.info(numpy.add)"
```

Python等价代码
```python3
import numpy as np
print(np.info(np.add))  # 即打印np.add.__doc__
```
<br/>

#### 6.  创建大小为10，初始化为0的向量，但将第5个值赋值为1(★☆☆)


```python3
import numpy as np
arr = np.zeros(10)
arr[4] = 1
print(arr)
```
数组从0开始计数
如果是向量，第一个元素是arr[0]
如果是矩阵，第一个元素是arr\[0][0]
多维数组按行填充，一行填完，填充下一行
<br/>

#### 7.  创建一个向量，其值的范围从10到49(★☆☆)


```python3
import numpy as np
arr = np.arange(10, 50)
print(arr)
```
np.arange([start,] stop[, step,], dtype=None), 类似于range([start,] stop[, step,]), 
产生数的范围为左边包含，右边不包含[start, stop)
<br/>

####8.  反转一个向量 (第一个元素变为最后一个，第二个元素变为倒数第二个，以此类推) (★☆☆)



```python3
import numpy as np

arr = np.arange(0, 10)
print(arr)
# print(arr.reverse())  # AttributeError: 'numpy.ndarray' object has no attribute 'reverse'
# print(np.reverse(arr))  # AttributeError: module 'numpy' has no attribute 'reverse'
rev_arr = arr[::-1]
print(rev_arr)

rev_arr[-1] = -1
print(rev_arr)
print(arr)
```
np没有reverse()
使用切片，完成向量的反转
切片是对象视图，若改变切片，原对象也会发生改变
<br/>


#### 9.  创建一个 3x3 的矩阵，其值从0到8 (★☆☆)


```python3
import numpy as np
shape = (3, 3)
arr = np.arange(9)

res_arr = arr.reshape(shape)  # 等价于下面的代码：先赋值，再改变自身shape属性
# res_arr = arr
# res_arr.shape = shape
print(arr)
print(res_arr)

res_arr[-1, -1] = -1  # res_arr为矩阵，获取值需要(row, column)
print(res_arr)
print(arr)
```
np.reshape(arr, newshape, order='C')\ arr.reshape(newshape, order='C')
改变数组的形状, order可以改变数组的逻辑结构和存储结构
reshape也产生视图
<br/>

#### 10. 从\[1,2,0,0,4,0\]中发现非0元素的索引 (★☆☆)


```python3
import numpy as np
arr = np.array([1,2,0,0,4,0])

indices = arr.nonzero()  # 非0元素的索引
print(indices)
print(arr[indices])  # 非0元素的值
```
np.nonzero(arr)/arr.nonzero()
返回所有非0元素的索引 indices
根据索引，我们可以轻松找到相应的值
arr[indices]
<br/>

#### 11. 创建一个 3x3 单位矩阵 (★☆☆)


```python3
import numpy as np
n = 3
arr = np.identity(n)  # 产生一个单位矩阵
print(arr)

n = 3
m = 3
arr2 = np.eye(n, m)  # 产生一个对角矩阵, 对角线元素为1
print(arr2)

n = 3
m = 4

arr3 = np.eye(n, m)  # 产生一个对角矩阵, 对角线元素为1
print(arr3)
```
np.identity(n)产生一个单位矩阵
np.eye(n, m, k=0)产生一个对角矩阵, 对角线元素为1
当n=m，即产生单位矩阵，k为对角线的偏移量
<br/>

#### 12. 创建一个 3x3x3 单位矩阵，其值随机 (★☆☆)


```python3
import numpy as np
shape = (3, 3, 3)
np.random.seed(123456)
arr = np.random.random(shape)
print(arr)
```
np.random.random(shape) 产生值范围为[0, 1)的数组
(b - a) * np.random.random(shape) + a 即可产生值范围为[a, b)的数组 
<br/>

#### 13. 创建一个 10x10的数组，其值随机，并且找出它的最大值和最小值 (★☆☆)


```python3
import numpy as np
shape = (10, 10)
np.random.seed(220184597)
arr = np.random.random(shape)
max = arr.max()  # np.max(arr)
min = arr.min()  # np.min(arr)
print("最大值:" + str(max) + " 最小值:" + str(min))
```
arr.max(axis=None, out=None, keepdims=False) | np.max(arr, axis=None, out=None, keepdims=False)
求最大值
axis控制维度，out存储结果，keepdims保持结果维度
min()参数同上，但求的是最小值
<br/>


#### 14. 创建一个大小的30的随机向量，求其平均值(★☆☆)


```python3
import numpy as np
np.random.seed(220184597)
arr = np.random.random(30)
print(arr)
mean = arr.mean()  # np.mean(arr)
print(mean)
```
arr.mean(axis=None, dtype=None, out=None, keepdims=False) | np.mean(arr, axis=None, dtype=None, out=None, keepdims=False)
求平均值 
axis控制维度，dtype数组元素类型,out存储结果，keepdims保持结果维度
<br/>


#### 15. 创建一个二维数组，边界为1，内部为0(★☆☆)


```python3
import numpy as np
shape = (5, 5)
arr = np.zeros(shape)  # 初始化全为0
print(arr)
arr[0] = 1  # 第一行为1
arr[-1] = 1 # 最后一行为1
arr[:,0] = 1  # 第一列为1
arr[:,-1] = 1  # 最后一列为1
print(arr)

arr2 = np.ones(shape)  # 初始化全为1
print(arr2)
arr2[1:-1, 1:-1] = 0  # 内部为0
print(arr2)
```
arr[indices]:使用索引值获取数组中的值
[start:stop:step]类似于range([start,] stop[, step,])
[:, :],而其中的,则是隔开不同的维度
<br/>

#### 16. 给一个已经存在的数组用0扩充边界(★☆☆)


```python3
import numpy as np

arr = np.arange(25).reshape((5, 5))
print(arr)
pad_arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
print(pad_arr)
```
pad(array, pad_width, mode, **kwargs)
常用参数np.pad(arr, pad_width, mode)
arr为多维数组，pad_width为填充边界
若为1维数组，则pad_width需要2个值（左，右）；若为2维数组，则pad_width需要4个值（上，下，左，右）；
mode为填充方式：'constant', 'edge', 'maximum'...
<br/>

#### 17. 下列表达式的结果(★☆☆)


```python3
import numpy as np
# np.nan
print(type(np.nan), np.nan)  # nan: not a number
# print(repr(np.nan))

print(0 * np.nan)
print(np.nan == np.nan)  # False
print(np.nan != np.nan)  # True
print(np.nan is np.nan)  # True
print(np.nan in [np.nan])  # 逐个比较元素是否is
print(float(np.nan) == float(np.nan))  # False
print(float(np.nan) != float(np.nan))  # True
print(float(np.nan) is float(np.nan))  # True

print(np.nan - np.nan)
print(0.3 == 3 * 0.1)  # 小数在内存不是精确表示

# np.inf
print(type(np.inf), np.inf)
print(np.inf > np.nan)
print(np.inf < np.nan)

print(np.inf - np.inf)
print(np.inf > np.inf)
print(np.inf < np.inf)
print(np.inf == np.inf)  # True
print(np.inf != np.inf)  # False
print(np.inf is np.inf)  # True

print(np.isnan(np.nan))
print(np.isfinite(np.inf))  # nan or inf 返回False,其余返回true
```
np.nan, np.inf是NumPy中两个特殊的常量，不能进行通常数值意义上的比较
nan: not a number
inf:infinite
nan的内存编码是一段值，而不是一个值
IEEE754规定 > 0x7f800000的全都是nan
== 比较的是__eq__
is 比较的是id
np.innan()检测nan
np.isfinite()检测正常值
<br/>

#### 18. 创建一个5x5的矩阵，在主对角线下填充1,2,3,4 (★☆☆)


```python3
import numpy as np
v = [1, 2, 3, 4]

arr = np.diag(v, k=-1)
print(arr)

shape = (5, 5)
arr2 = np.eye(shape[0], shape[1], k=-1)
print(arr2)
```
np.diag(v, k)创建一个对角矩阵
v是对角的值，k是相对主对角线的偏移量，正右负左

np.eye(n, m, k=0)与之相比，也产生一个对角矩阵, 但对角线元素只能为1
<br/>

#### 19. 创建一个8x8的矩阵，其值0，1棋盘相间(★☆☆)


```python3
import numpy as np
shape = (8, 8)
arr = np.zeros(shape)
arr[::2,1::2] = 1
arr[1::2,::2] = 1
print(arr)
```

#### 20. 现在有一个形状为(6,7,8)的数组,求第100个元素的索引(★☆☆)


```python3
import numpy as np
shape = (6, 7, 8)
index = 99  #索引从0计数
indices = []
d = index
# 短除法求余数，即各个维度的索引
for value in shape[::-1]:
    b = d // value
    r = d % value
    d = b
    indices.append(r)
indices.reverse()
print(indices)

# np.unravel_index(index, shape)已经实现等价功能
print(np.unravel_index(index, shape))
```
arr[indices]:使用索引值获取数组中的值
[start:stop:step]类似于range([start,] stop[, step,])
[:, :],而其中的,则是隔开不同的维度
<br/>

#### 21. 使用tile创建一个8x8棋盘相间的矩阵(★☆☆)


```python3
import numpy as np
base = [[0, 1], [1, 0]]
print(np.array(base))
arr = np.tile(base, (4, 4))
print(arr)
```
np.tile(arr, reps)
以arr为整体，进行铺叠
<br/>

#### 22. 正则化一个5x5的随机矩阵 (★☆☆)


```python3
import numpy as np
np.random.seed(220184597)
shape = (5, 5)
arr = np.random.random(shape)
print(arr)
nor_arr = (arr-arr.mean())/arr.std()
print(nor_arr)
```
正则化：将原数组转换为均值为1，方差为0的新数组
（arr-mean）/std
arr.mean() 求均值
arr.std() 求标准差
<br/>

#### 23. 创建一个用4个无符号整型描述颜色的自定义类型 (RGBA) (★☆☆)


```python3
import numpy as np
RGBA = np.dtype([('r', np.uint8),
                 ('g', np.uint8),
                 ('b', np.uint8),
                 ('a', np.uint8)])
print(RGBA)
print("names:", RGBA.names, "itemsize:", RGBA.itemsize)
```

#### 24. 将一个5x3的矩阵与一个3x2的矩阵进行矩阵乘法运算 (real matrix product) (★☆☆)


```python3
import numpy as np
arr1 = np.arange(15).reshape((5, 3))
arr2 = np.arange(6).reshape((3, 2))
print(arr1.shape)
print(arr1)
print(arr2.shape)
print(arr2)

res = np.dot(arr1, arr2)
print(res.shape)
print(res)

res = arr1.dot(arr2)
print(res.shape)
print(res)
```
np.dot(a, b, out=None) | a.dot(b, out=None)
a,b为矩阵，进行矩阵乘法，要求第一个矩阵的列数等于第二个矩阵的行数
<br/>

#### 25. 给定一个一维数组，在原数组上将从3到8的所有值取反(★☆☆)


```python3
import numpy as np
np.random.seed(220184597)
arr = np.random.randint(0, 10, (100,))
arr[(arr <= 3) & (arr >= 8)] *= -1
print(arr)
```
ndarray也可以用布尔数组(bool)取值
由于逻辑运算符的优先级比比较运算符高，因此一定要加()，一般为了正确性和可读性，我们会给整体表达式加()
<br/>

#### 26. 求下列脚本的输出(★☆☆)


```python3
print(sum(range(5),-1))  # sum 0,1,2,3,4,-1 = 9
from numpy import *
print(sum(range(5),-1))  # # sum 0,1,2,3,4 = 10
```
第一个调用的sum是系统内置的sum函数，对所有的值求和
range(5) + -1, -1是加数

第二个调用的sum是np.sum函数，求和，指定axis=-1
即对列求和， range(5)， -1是指定的轴，不参与加法运算

所以我们在import包的时候，不建议引入所有的引用
为防止命名冲突(覆盖),需要什么就引用什么。例如 from numpy import sum
又或者 import numpy as np; np.sum(arr)
<br/>

#### 27. 考虑一个整数向量arr, 以下表达式是否合法(★☆☆)


```python3
import numpy as np
arr = np.arange(10)
print(arr**arr)
print(2 << arr >> 2)
print(arr <- arr)
print(1j*arr)
print(arr/1/1)
# print((2<arr)>5)
# print(arr<arr>arr)  # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
print((arr<arr)>arr)  # [False False False False False False False False False False]
print(arr<arr)
```
以上运算都是逐元素运算
**:逐元素幂次运算
<<, >>:左移，右移运算，相当于整体乘以2**n运算
复数分为实数部虚数部，1j是虚数，乘以实数，为虚数部
/:逐元素浮点数除法，因此结果为浮点数
<br/>

#### 28. 下列表达式的运行结果(★☆☆)


```python3
import numpy as np
print(np.array(0) / np.array(0))  # nan
print(np.array(0) // np.array(0))  # 0
print(np.array([np.nan]) == np.array([np.nan]))
print(np.array([np.nan]) is np.array([np.nan]))
print(np.array([np.nan]).astype(int))
print(np.array([np.nan]).astype(int).astype(float))
print(np.array([np.nan]).astype(int).astype(float) == np.array([np.nan]).astype(int).astype(float))  # True
print(np.array([np.nan]).astype(int).astype(float) is np.array([np.nan]).astype(int).astype(float))  # False
print(id(np.array([np.nan]).astype(int).astype(float)), id(np.array([np.nan]).astype(int).astype(float)))  # 4439748400 4439748400
print(id(np.array([np.nan]).astype(int).astype(float)) == id(np.array([np.nan]).astype(int).astype(float)))  # True
for i in range(10):
    print("id:", id(np.array([np.nan]).astype(int).astype(float)))
```

#### 29. 一个浮点型数组向0方向舍入 (★☆☆)


```python3
import numpy as np
np.random.seed(220184597)
arr = (np.random.random(10) - 0.5) * 100
print(arr)
print("向0舍入", np.trunc(arr))  # 向0舍入
print("向上取整", np.ceil(arr))  # 向上取整
print("向下取整", np.floor(arr)) # 向下取整
print("四舍五入取整", np.rint(arr))  # 四舍五入取整
print("四舍五入", np.round(arr, decimals=1)) # 四舍五入

print ("远离0舍入", np.copysign(np.ceil(np.abs(arr)), arr))  # 远离0舍入
```
类型(dtype)不变，数值取整
np.trunc:截取整数部分，向0舍入，即整除1
np.ceil:向上取整
np.floor:向下取整
np.rint:四舍五入取整
np.round(arr, decimals):四舍五入,decimals决定舍入的小数位数(0为整数，1为十分数，以此类推)
远离0舍入:取绝对值向上取整，再还原符号
<br/>

#### 30. 寻找两个数组的共同值(★☆☆)


```python3
import numpy as np
np.random.seed(220184597)
arr1 = np.random.randint(0, 10, 10)
arr2 = np.random.randint(0, 10, 10)
print(arr1)
print(arr2)
res = np.intersect1d(arr1, arr2)
print(res)

print(np.intersect1d(arr1.reshape((2, 5)), arr2.reshape((5, 2))))  # arr可为多维数组
```
np.intersect1d(arr1, arr2)
以升序，唯一的形式，返回两个数组中共同的值
arr可以为多维数组，但在运算中会转换为一维数组(arr.flatten())
<br/>

#### 31. 忽略所有的numpy警告 (不推荐) (★☆☆)


```python3
# Suicide mode on
defaults = np.seterr(all="ignore")
arr = np.ones(1) / 0

# Back to sanity
_ = np.seterr(**defaults)
```

An equivalent way, with a context manager:

```python3
with np.errstate(divide='ignore'):
    arr = np.ones(1) / 0
```

#### 32. 判断下列表达式的正确性 (★☆☆)


```python3
import numpy as np
print(np.sqrt(-1))  # nan
print(np.emath.sqrt(-1))  # 1j
print(np.sqrt(-1) == np.emath.sqrt(-1))  # False
```
np.sqrt(arr):实数开根号，\sqrt{-1}为nan
np.emath.sqrt(arr):复数开根号，\sqrt{-1}为1j
<br/>

#### 33. 获取昨天，今天，明天的日期(★☆☆)


```python3
import datetime
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
today = datetime.datetime.now()
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
print('yesterday:', yesterday.strftime("%Y-%m-%d"))
print('today:', today.strftime("%Y-%m-%d"))
print('tomorrow:', tomorrow.strftime("%Y-%m-%d"))

import numpy as np
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today     = np.datetime64('today', 'D')
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print('yesterday:', yesterday)
print('today:', today)
print('tomorrow:', tomorrow)
```
datetime由date和time组成
date为日期，包括year,month,day
time为时间，包括hour,minute.second等

timedelta为时间间隔

系统内置的datetime与str的转换
strftime(),其中f为formated(格式化)：datetime=>str
strptime(),其中p为parsed(解析)：str=>datetime
<br/>

#### 34. 获取2019年8月的所有日期 (★★☆)


```python3
import numpy as np
arr = np.arange("2019-08-01", "2019-09-01", dtype=np.datetime64)
print(arr.dtype)
print(arr)
```

#### 35. 原地计算(A+B)\*(-A/2))  (without copy)? (★★☆)


```python3
import numpy as np
arr_a = np.arange(5, dtype=np.float)
arr_b = np.arange(5, 10, dtype=np.float)
print(arr_a)
print(arr_b)

np.add(arr_a, arr_b, out=arr_b)
np.divide(arr_a, -2, out=arr_a)
np.multiply(arr_a, arr_b, arr_a)
print(arr_a)
```
numpy方法中的out参数存储运算的结果
初始化数组需要指定数据类型dtype=np.float，否则除法运算会报类型错误
TypeError: No loop matching the specified signature and casting was found for ufunc true_divide
<br/>

#### 36. 使用5种不同方法将一组随机数组截断整数部分 (★★☆)


```python3
import numpy as np
np.random.seed(220184597)
arr = np.random.random(10) * 100
print(arr)

print(arr//1)
print(np.trunc(arr))
print(np.ceil(arr) - 1)
print(np.floor(arr))
print(arr.astype(np.int))
```
np.ceil(scalar)>=scalar
np.floor(scalar)<=scalar
若为整数，取等号
np.ceil(3)==3
np.floor(3)==3
因此使用np.ceil(arr) - 1和np.floor(arr)有Bug，当且仅当产生的数恰好为整数时
但对于np.random.random(shape) * 100来说概率很小
<br/>

#### 37. 创建一个5x5的矩阵，每行的值从0到4(★★☆)


```python3
import numpy as np
arr = np.arange(0, 5)
arr = arr + np.zeros((5, 5))
print(arr)
```
当两个ndarray进行运算，维度不同时，numpy会扩充维度，这种机制称为广播（Broadcast）
一般遵守同一维度大的值是小的值得整数倍，不然可能会产生意想不到的错误
<br/>


#### 38. 创建一个生成器（generator）用于产生10个整数，并用它创建一个数组 (★☆☆)


```python3
import numpy as np

def generator():
    for i in range(10):
        yield i
        
arr = np.fromiter(generator(), dtype=np.int)
print(arr)
```
np.fromiter(iterable, dtype, count=-1)
接受一个可迭代对象，返回一个多维数组
<br/>

#### 39. 创建一个大小为10的向量，其值从0到1，不包括0，1 (★★☆)


```python3
import numpy as np
arr = np.linspace(0, 1, 12)
print(arr)
print(arr[1:-1])
```
np.linspace(start, stop, num=50, ....)
产生从start到stop等间隔的num个数组，包括start, stop
<br/>

#### 40. 创建一个大小为10的向量，升序排列(★★☆)


```python3
import numpy as np
np.random.seed(220184597)
arr = np.random.random(10)
print("排序前:", arr)
arr.sort()
print("排序后:", arr)
```
np.sort(arr, axis=-1, kind='quicksort', order=None) | arr.sort(axis=-1, kind='quicksort', order=None)
kind:排序算法 {'quicksort', 'mergesort', 'heapsort', 'stable'}
算法复杂度都为O(nlogn)

![array_sorting_methods](res/imgs/100_NumPy_exercises_solutions/array_sorting_methods.png)

<br/>

#### 41. 在小数组中比使用np.sum求和更快的方式(★★☆)


```python3
import numpy as np
np.random.seed(220184597)
arr = np.random.random(10)
```
```jupyter-notebook
%timeit np.sum(arr)
```
2.68 µs ± 35.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

```jupyter-notebook
%timeit np.add.reduce(arr)
```
1.03 µs ± 2.91 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
<br/>

#### 42. 比较两个随机数组a和b是否相等 (★★☆)


```python3
import numpy as np
np.random.seed(220184597)
a = np.random.random(10)
b = np.random.random(10)
print(a)
print(b)
print(np.allclose(a, b, atol=1,rtol=0.5))  # 一定范围容忍的相等
print(np.array_equal(a, b))  # 完全相等
res = (a==b)
print(res.all())  # all True:True else:False
```
np.allclose(a, b, rtol=1.e-5, atol=1.e-8, equal_nan=False)
一定范围容忍的相等
absolute(`a` - `b`) <= (`atol` + `rtol` * absolute(`b`)) return True

np.array_equal(a, b) 
完全相等

arr_bool.all()  # all True:True else:False
arr_bool.any()  # exist True:True else:False
<br/>

#### 43. 使一个数组不可更改 (read-only) (★★☆)


```python3
import numpy as np
arr = np.zeros(10)
arr.flags.writeable = False
arr[0] = 1  # ValueError: assignment destination is read-only
print(arr)
```

#### 44. 将一个随机的10x2矩阵由笛卡尔坐标系(cartesian coordinates)转换为极坐标系(polar coordinates) (★★☆)


```python3
import numpy as np
np.random.seed(220184597)
arr = np.random.random((10, 2))
print(arr)
x, y = arr[:, 0], arr[:, 1]
r = np.sqrt(x**2+y**2)
tanh = np.arctan(y/x)  # np.arctan2(y,x)
print(r)
print(tanh)
```

#### 45. 创建一个大小为10的随机向量，用0替换其最大值 (★★☆)


```python3
import numpy as np
np.random.seed(220184597)
arr = np.random.random(10)
print(arr)
print(arr.argmax(), arr.max())
arr[arr.argmax()] = 0
print(arr)
```

#### 46. 在覆盖\[0,1\]x\[0,1\]区域的`x` 和 `y` 坐标系创建一个结构化数组 (★★☆)


```python3
import numpy as np
arr = np.zeros((6, 6), dtype=[('x', float), ('y', float)])
x = np.linspace(0, 1, 6)
y = np.linspace(0, 1, 6)
arr['x'], arr['y'] = np.meshgrid(x, y)
print(arr)
```

####  47. 计算两个数组x和y的柯西矩阵(Cauchy matrix) C (Cij =1/(xi - yj))


```python3
import numpy as np
x = [4,5,6]
y = [1,2,3]
c = 1.0 / np.subtract.outer(x,y)
# print(np.subtract.outer(x,y))
print(c)
print(np.linalg.det(c))  # 计算行列式(determinant)
```

#### 48. 打印每个numpy标量类型的最大和最小可表示值 (★★☆)


```python3
import numpy as np
for dtype in [np.uint8, np.int8, np.int32, np.int64]:
   print(np.iinfo(dtype).min)
   print(np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
   print(np.finfo(dtype).min)
   print(np.finfo(dtype).max)
   print(np.finfo(dtype).eps)
```

#### 49. 无限制打印数组的值 (★★☆)


```python3
import numpy as np
arr = np.zeros((50, 50))
print(arr)
np.set_printoptions(threshold=np.inf)  # 打印内容全部显示
print(arr)
```

#### 50. 给一个标量，在一个向量中寻找与之最接近的值(★★☆)


```python3
import numpy as np
np.random.seed(220184597)
arr = np.random.random(10) * 100
scalar = np.random.randint(100)
print(arr)
print(scalar)
index = np.abs(arr-scalar).argmin()
print(arr[index])
```

#### 51. 创建一个结构化数组，表示a position (x,y) 和 a color (r,g,b) (★★☆)


```python3
Z = np.zeros(10, [ ('position', [ ('x', float, 1),
                                  ('y', float, 1)]),
                   ('color',    [ ('r', float, 1),
                                  ('g', float, 1),
                                  ('b', float, 1)])])
print(Z)
```

#### 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)


```python3
Z = np.random.random((10,2))
X,Y = np.atleast_2d(Z[:,0], Z[:,1])
D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
print(D)

# Much faster with scipy
import scipy
# Thanks Gavin Heverly-Coulson (#issue 1)
import scipy.spatial

Z = np.random.random((10,2))
D = scipy.spatial.distance.cdist(Z,Z)
print(D)
```

#### 53. 将float (32 bits)数组原地转换为integer (32 bits)(★★☆)


```python3
Z = np.arange(10, dtype=np.float32)
Z = Z.astype(np.int32, copy=False)
print(Z)
```

#### 54. 读取文件 (★★☆)


```python3
from io import StringIO

# Fake file
s = StringIO("""1, 2, 3, 4, 5\n
                6,  ,  , 7, 8\n
                 ,  , 9,10,11\n""")
Z = np.genfromtxt(s, delimiter=",", dtype=np.int)
print(Z)
```

#### 55. 枚举遍历数组 (★★☆)


```python3
Z = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(Z):
    print(index, value)
for index in np.ndindex(Z.shape):
    print(index, Z[index])
```

#### 56. 创建一个通用性的二维高斯数组(★★☆)


```python3
X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
D = np.sqrt(X*X+Y*Y)
sigma, mu = 1.0, 0.0
G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )
print(G)
```

#### 57. 在2维数组中随机替换p个元素 (★★☆)


```python3
# Author: Divakar

n = 10
p = 3
Z = np.zeros((n,n))
np.put(Z, np.random.choice(range(n*n), p, replace=False),1)
print(Z)
```

#### 58. 矩阵每行减去其平均值(★★☆)


```python3
# Author: Warren Weckesser

X = np.random.rand(5, 10)

# Recent versions of numpy
Y = X - X.mean(axis=1, keepdims=True)

# Older versions of numpy
Y = X - X.mean(axis=1).reshape(-1, 1)

print(Y)
```

#### 59. 按第n列排序数组(★★☆)


```python3
# Author: Steve Tjoa

Z = np.random.randint(0,10,(3,3))
print(Z)
print(Z[Z[:,1].argsort()])
```

#### 60. 判断一个2维数组是否含有空列(★★☆)


```python3
# Author: Warren Weckesser

Z = np.random.randint(0,3,(3,10))
print((~Z.any(axis=0)).any())
```

#### 61. 给定一个值，在一个数组中找到最接近的值(★★☆)


```python3
Z = np.random.uniform(0,1,10)
z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]
print(m)
```

#### 62. 使用迭代器将形状不同的两个数组求外积和(★★☆)


```python3
A = np.arange(3).reshape(3,1)
B = np.arange(3).reshape(1,3)
it = np.nditer([A,B,None])
for x,y,z in it: z[...] = x + y
print(it.operands[2])
```

#### 63. Create an array class that has a name attribute (★★☆)


```python3
class NamedArray(np.ndarray):
    def __new__(cls, array, name="no name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        self.info = getattr(obj, 'name', "no name")

Z = NamedArray(np.arange(10), "range_10")
print (Z.name)
```

#### 64. 以一个数组的元素值为索引，对给定的另一个数组元素值加1(注意重复的索引)(★★★)


```python3
# Author: Brett Olsen

Z = np.ones(10)
I = np.random.randint(0,len(Z),20)
Z += np.bincount(I, minlength=len(Z))
print(Z)

# Another solution
# Author: Bartosz Telenczuk
np.add.at(Z, I, 1)
print(Z)
```

#### 65. 基于索引列表（I）将向量（X）的元素累积到数组（F）(★★★)


```python3
# Author: Alan G Isaac

X = [1,2,3,4,5,6]
I = [1,3,9,3,4,1]
F = np.bincount(I,X)
print(F)
```

#### 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★★)


```python3
# Author: Nadav Horesh

w,h = 16,16
I = np.random.randint(0,2,(h,w,3)).astype(np.ubyte)
F = I[...,0]*256*256 + I[...,1]*256 +I[...,2]
n = len(np.unique(F))
print(np.unique(I))
```

#### 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)


```python3
A = np.random.randint(0,10,(3,4,3,4))
# solution by passing a tuple of axes (introduced in numpy 1.7.0)
sum = A.sum(axis=(-2,-1))
print(sum)
# solution by flattening the last two dimensions into one
# (useful for functions that don't accept tuples for axis argument)
sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
print(sum)
```

#### 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset  indices? (★★★)


```python3
# Author: Jaime Fernández del Río

D = np.random.uniform(0,1,100)
S = np.random.randint(0,10,100)
D_sums = np.bincount(S, weights=D)
D_counts = np.bincount(S)
D_means = D_sums / D_counts
print(D_means)

# Pandas solution as a reference due to more intuitive code
import pandas as pd
print(pd.Series(D).groupby(S).mean())
```

#### 69. How to get the diagonal of a dot product? (★★★)


```python3
# Author: Mathieu Blondel

A = np.random.uniform(0,1,(5,5))
B = np.random.uniform(0,1,(5,5))

# Slow version  
np.diag(np.dot(A, B))

# Fast version
np.sum(A * B.T, axis=1)

# Faster version
np.einsum("ij,ji->i", A, B)
```

#### 70. Consider the vector \[1, 2, 3, 4, 5\], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)


```python3
# Author: Warren Weckesser

Z = np.array([1,2,3,4,5])
nz = 3
Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))
Z0[::nz+1] = Z
print(Z0)
```

#### 71. Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)? (★★★)


```python3
A = np.ones((5,5,3))
B = 2*np.ones((5,5))
print(A * B[:,:,None])
```

#### 72. How to swap two rows of an array? (★★★)


```python3
# Author: Eelco Hoogendoorn

A = np.arange(25).reshape(5,5)
A[[0,1]] = A[[1,0]]
print(A)
```

#### 73. Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the  triangles (★★★)


```python3
# Author: Nicolas P. Rougier

faces = np.random.randint(0,100,(10,3))
F = np.roll(faces.repeat(2,axis=1),-1,axis=1)
F = F.reshape(len(F)*3,2)
F = np.sort(F,axis=1)
G = F.view( dtype=[('p0',F.dtype),('p1',F.dtype)] )
G = np.unique(G)
print(G)
```

#### 74. Given an array C that is a bincount, how to produce an array A such that np.bincount(A) == C? (★★★)


```python3
# Author: Jaime Fernández del Río

C = np.bincount([1,1,2,3,4,4,6])
A = np.repeat(np.arange(len(C)), C)
print(A)
```

#### 75. How to compute averages using a sliding window over an array? (★★★)


```python3
# Author: Jaime Fernández del Río

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
Z = np.arange(20)
print(moving_average(Z, n=3))
```

#### 76. Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z\[0\],Z\[1\],Z\[2\]) and each subsequent row is  shifted by 1 (last row should be (Z\[-3\],Z\[-2\],Z\[-1\]) (★★★)


```python3
# Author: Joe Kington / Erik Rigtorp
from numpy.lib import stride_tricks

def rolling(a, window):
    shape = (a.size - window + 1, window)
    strides = (a.itemsize, a.itemsize)
    return stride_tricks.as_strided(a, shape=shape, strides=strides)
Z = rolling(np.arange(10), 3)
print(Z)
```

#### 77. How to negate a boolean, or to change the sign of a float inplace? (★★★)


```python3
# Author: Nathaniel J. Smith

Z = np.random.randint(0,2,100)
np.logical_not(Z, out=Z)

Z = np.random.uniform(-1.0,1.0,100)
np.negative(Z, out=Z)
```

#### 78. Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i  (P0\[i\],P1\[i\])? (★★★)


```python3
def distance(P0, P1, p):
    T = P1 - P0
    L = (T**2).sum(axis=1)
    U = -((P0[:,0]-p[...,0])*T[:,0] + (P0[:,1]-p[...,1])*T[:,1]) / L
    U = U.reshape(len(U),1)
    D = P0 + U*T - p
    return np.sqrt((D**2).sum(axis=1))

P0 = np.random.uniform(-10,10,(10,2))
P1 = np.random.uniform(-10,10,(10,2))
p  = np.random.uniform(-10,10,( 1,2))
print(distance(P0, P1, p))
```

#### 79. Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j (P\[j\]) to each line i (P0\[i\],P1\[i\])? (★★★)


```python3
# Author: Italmassov Kuanysh

# based on distance function from previous question
P0 = np.random.uniform(-10, 10, (10,2))
P1 = np.random.uniform(-10,10,(10,2))
p = np.random.uniform(-10, 10, (10,2))
print(np.array([distance(P0,P1,p_i) for p_i in p]))
```

#### 80. Consider an arbitrary array, write a function that extract a subpart with a fixed shape and centered on a given element (pad with a `fill` value when necessary) (★★★)


```python3
# Author: Nicolas Rougier

Z = np.random.randint(0,10,(10,10))
shape = (5,5)
fill  = 0
position = (1,1)

R = np.ones(shape, dtype=Z.dtype)*fill
P  = np.array(list(position)).astype(int)
Rs = np.array(list(R.shape)).astype(int)
Zs = np.array(list(Z.shape)).astype(int)

R_start = np.zeros((len(shape),)).astype(int)
R_stop  = np.array(list(shape)).astype(int)
Z_start = (P-Rs//2)
Z_stop  = (P+Rs//2)+Rs%2

R_start = (R_start - np.minimum(Z_start,0)).tolist()
Z_start = (np.maximum(Z_start,0)).tolist()
R_stop = np.maximum(R_start, (R_stop - np.maximum(Z_stop-Zs,0))).tolist()
Z_stop = (np.minimum(Z_stop,Zs)).tolist()

r = [slice(start,stop) for start,stop in zip(R_start,R_stop)]
z = [slice(start,stop) for start,stop in zip(Z_start,Z_stop)]
R[r] = Z[z]
print(Z)
print(R)
```

#### 81. Consider an array Z = \[1,2,3,4,5,6,7,8,9,10,11,12,13,14\], how to generate an array R = \[\[1,2,3,4\], \[2,3,4,5\], \[3,4,5,6\], ..., \[11,12,13,14\]\]? (★★★)


```python3
# Author: Stefan van der Walt

Z = np.arange(1,15,dtype=np.uint32)
R = stride_tricks.as_strided(Z,(11,4),(4,4))
print(R)
```

#### 82. Compute a matrix rank (★★★)


```python3
# Author: Stefan van der Walt

Z = np.random.uniform(0,1,(10,10))
U, S, V = np.linalg.svd(Z) # Singular Value Decomposition
rank = np.sum(S > 1e-10)
print(rank)
```

#### 83. How to find the most frequent value in an array?


```python3
Z = np.random.randint(0,10,50)
print(np.bincount(Z).argmax())
```

#### 84. Extract all the contiguous 3x3 blocks from a random 10x10 matrix (★★★)


```python3
# Author: Chris Barker

Z = np.random.randint(0,5,(10,10))
n = 3
i = 1 + (Z.shape[0]-3)
j = 1 + (Z.shape[1]-3)
C = stride_tricks.as_strided(Z, shape=(i, j, n, n), strides=Z.strides + Z.strides)
print(C)
```

#### 85. Create a 2D array subclass such that Z\[i,j\] == Z\[j,i\] (★★★)


```python3
# Author: Eric O. Lebigot
# Note: only works for 2d array and value setting using indices

class Symetric(np.ndarray):
    def __setitem__(self, index, value):
        i,j = index
        super(Symetric, self).__setitem__((i,j), value)
        super(Symetric, self).__setitem__((j,i), value)

def symetric(Z):
    return np.asarray(Z + Z.T - np.diag(Z.diagonal())).view(Symetric)

S = symetric(np.random.randint(0,10,(5,5)))
S[2,3] = 42
print(S)
```

#### 86. Consider a set of p matrices wich shape (n,n) and a set of p vectors with shape (n,1). How to compute the sum of of the p matrix products at once? (result has shape (n,1)) (★★★)


```python3
# Author: Stefan van der Walt

p, n = 10, 20
M = np.ones((p,n,n))
V = np.ones((p,n,1))
S = np.tensordot(M, V, axes=[[0, 2], [0, 1]])
print(S)

# It works, because:
# M is (p,n,n)
# V is (p,n,1)
# Thus, summing over the paired axes 0 and 0 (of M and V independently),
# and 2 and 1, to remain with a (n,1) vector.
```

#### 87. Consider a 16x16 array, how to get the block-sum (block size is 4x4)? (★★★)


```python3
# Author: Robert Kern

Z = np.ones((16,16))
k = 4
S = np.add.reduceat(np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                                       np.arange(0, Z.shape[1], k), axis=1)
print(S)
```

#### 88. How to implement the Game of Life using numpy arrays? (★★★)


```python3
# Author: Nicolas Rougier

def iterate(Z):
    # Count neighbours
    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
         Z[1:-1,0:-2]                + Z[1:-1,2:] +
         Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])

    # Apply rules
    birth = (N==3) & (Z[1:-1,1:-1]==0)
    survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)
    Z[...] = 0
    Z[1:-1,1:-1][birth | survive] = 1
    return Z

Z = np.random.randint(0,2,(50,50))
for i in range(100): Z = iterate(Z)
print(Z)
```

#### 89. How to get the n largest values of an array (★★★)


```python3
Z = np.arange(10000)
np.random.shuffle(Z)
n = 5

# Slow
print (Z[np.argsort(Z)[-n:]])

# Fast
print (Z[np.argpartition(-Z,n)[:n]])
```

#### 90. Given an arbitrary number of vectors, build the cartesian product (every combinations of every item) (★★★)


```python3
# Author: Stefan Van der Walt

def cartesian(arrays):
    arrays = [np.asarray(a) for a in arrays]
    shape = (len(x) for x in arrays)

    ix = np.indices(shape, dtype=int)
    ix = ix.reshape(len(arrays), -1).T

    for n, arr in enumerate(arrays):
        ix[:, n] = arrays[n][ix[:, n]]

    return ix

print (cartesian(([1, 2, 3], [4, 5], [6, 7])))
```

#### 91. How to create a record array from a regular array? (★★★)


```python3
Z = np.array([("Hello", 2.5, 3),
              ("World", 3.6, 2)])
R = np.core.records.fromarrays(Z.T,
                               names='col1, col2, col3',
                               formats = 'S8, f8, i8')
print(R)
```

#### 92. Consider a large vector Z, compute Z to the power of 3 using 3 different methods (★★★)


```python3
# Author: Ryan G.

x = np.random.rand(int(5e7))

%timeit np.power(x,3)
%timeit x*x*x
%timeit np.einsum('i,i,i->i',x,x,x)
```

#### 93. Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain elements of each row of B regardless of the order of the elements in B? (★★★)


```python3
# Author: Gabe Schwartz

A = np.random.randint(0,5,(8,3))
B = np.random.randint(0,5,(2,2))

C = (A[..., np.newaxis, np.newaxis] == B)
rows = np.where(C.any((3,1)).all(1))[0]
print(rows)
```

#### 94. Considering a 10x3 matrix, extract rows with unequal values (e.g. \[2,2,3\]) (★★★)


```python3
# Author: Robert Kern

Z = np.random.randint(0,5,(10,3))
print(Z)
# solution for arrays of all dtypes (including string arrays and record arrays)
E = np.all(Z[:,1:] == Z[:,:-1], axis=1)
U = Z[~E]
print(U)
# soluiton for numerical arrays only, will work for any number of columns in Z
U = Z[Z.max(axis=1) != Z.min(axis=1),:]
print(U)
```

#### 95. Convert a vector of ints into a matrix binary representation (★★★)


```python3
# Author: Warren Weckesser

I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128])
B = ((I.reshape(-1,1) & (2**np.arange(8))) != 0).astype(int)
print(B[:,::-1])

# Author: Daniel T. McDonald

I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128], dtype=np.uint8)
print(np.unpackbits(I[:, np.newaxis], axis=1))
```

#### 96. Given a two dimensional array, how to extract unique rows? (★★★)


```python3
# Author: Jaime Fernández del Río

Z = np.random.randint(0,2,(6,3))
T = np.ascontiguousarray(Z).view(np.dtype((np.void, Z.dtype.itemsize * Z.shape[1])))
_, idx = np.unique(T, return_index=True)
uZ = Z[idx]
print(uZ)

# Author: Andreas Kouzelis
# NumPy >= 1.13
uZ = np.unique(Z, axis=0)
print(uZ)
```

#### 97. Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function (★★★)


```python3
# Author: Alex Riley
# Make sure to read: http://ajcr.net/Basic-guide-to-einsum/

A = np.random.uniform(0,1,10)
B = np.random.uniform(0,1,10)

np.einsum('i->', A)       # np.sum(A)
np.einsum('i,i->i', A, B) # A * B
np.einsum('i,i', A, B)    # np.inner(A, B)
np.einsum('i,j->ij', A, B)    # np.outer(A, B)
```

#### 98. Considering a path described by two vectors (X,Y), how to sample it using equidistant samples (★★★)?


```python3
# Author: Bas Swinckels

phi = np.arange(0, 10*np.pi, 0.1)
a = 1
x = a*phi*np.cos(phi)
y = a*phi*np.sin(phi)

dr = (np.diff(x)**2 + np.diff(y)**2)**.5 # segment lengths
r = np.zeros_like(x)
r[1:] = np.cumsum(dr)                # integrate path
r_int = np.linspace(0, r.max(), 200) # regular spaced path
x_int = np.interp(r_int, r, x)       # integrate path
y_int = np.interp(r_int, r, y)
```

#### 99. Given an integer n and a 2D array X, select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees, i.e., the rows which only contain integers and which sum to n. (★★★)


```python3
# Author: Evgeni Burovski

X = np.asarray([[1.0, 0.0, 3.0, 8.0],
                [2.0, 0.0, 1.0, 1.0],
                [1.5, 2.5, 1.0, 0.0]])
n = 4
M = np.logical_and.reduce(np.mod(X, 1) == 0, axis=-1)
M &= (X.sum(axis=-1) == n)
print(X[M])
```

#### 100. Compute bootstrapped 95% confidence intervals for the mean of a 1D array X (i.e., resample the elements of an array with replacement N times, compute the mean of each sample, and then compute percentiles over the means). (★★★)


```python3
# Author: Jessica B. Hamrick

X = np.random.randn(100) # random 1D array
N = 1000 # number of bootstrap samples
idx = np.random.randint(0, X.size, (N, X.size))
means = X[idx].mean(axis=1)
confint = np.percentile(means, [2.5, 97.5])
print(confint)
```
