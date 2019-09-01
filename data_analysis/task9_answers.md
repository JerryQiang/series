# 【Task9精选问题】

以前做数学建模的时候，会用**AR/MA/ARMA/ARIMA**模型分析时间序列数据。<br/>

滑动（移动）窗口(Moving Window Functions)，让我联想到了计算机网络的发送接收文件的滑动窗口以及计算机视觉里的卷积操作。<br/>

**滑动(移动)窗口**：为了提升数据的准确性，**用一段区间来表示某个点的取值**，其中这个区间称为窗口。直观解释：**平滑数据**，消除噪音
想要了解滑动窗口更多知识
**详见**：<a href="http://liao.cpython.org/pandas40/">Pandas的时间序列-滑动窗口</a>><br/>

## Q1：1.三种移动窗口函数的区别2.锚点偏移量（MonthEnd）的日期是如何确定？
1. `close_px.AAPL.rolling(250).mean().plot()` **平均加权**
2. `ma60 = aapl_px.rolling(30, min_periods=20).mean()`<br/>
`ewma60 = aapl_px.ewm(span=30).mean()` **指数加权**
3. `score_at_2percent = lambda x: percentileofscore(x, 0.02)`<br/>
`result = returns.AAPL.rolling(250).apply(score_at_2percent)`**自定义加权**

<br/>

移动窗口的区别在于**求权的方式**以及**窗口的大小**不同。

<br/>


```python3
from pandas.tseries.offsets import Day, MonthEnd
now = datetime(2019, 7, 27)
now + MonthEnd(2)
```
根据你的数据分析需求设定`MonthEnd`偏移量
<br/>

## Q2：三种移动窗口函数在实际应用场景有哪些？哪种应用频率最高？
- 指数移动窗口函数：整体平滑
- 二进制移动窗口函数：增量变化
- 自定义窗口函数：根据分析需求
看《统计数字会撒谎》、《精益数据分析》等书对统计有更多地了解。
<br/>


## Q3：1.企业级使用三种移动窗口函数哪一种比较频繁
一般使用**指数移动窗口函数**和**二进制移动窗口函数**。<br/>
遇到较为复杂的现实场景，肯定使用**自定义窗口函数**。
<br/>