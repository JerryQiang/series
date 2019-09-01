#【Task8精选问题】

## Q1：画图注释的annotate函数参数不是很理解；seaborn做barplot的例子出图有问题？

'''
    xy=(横坐标，纵坐标)  箭头尖端
    xytext=(横坐标，纵坐标) 文字的坐标，指的是最左边的坐标
    arrowprops= {
        facecolor= '颜色',
        shrink = '数字' <1  收缩箭头
    }  箭头格式
'''

**详见**：<a href="https://blog.csdn.net/wizardforcel/article/details/54782628">Matplotlib 中文用户指南 4.5 标注</a>>

<br/>

## Q2："1. 在章节9.1.5中，用含title和xlabel作为键的字典向ax.set()传入参数，可以批量设置绘图选项，那么，如何批量设置如何批量设置xticks, xticklabels, xlabels等等参数呢？

```python3
props = {
    'title': 'My first matplotlib plot2',
    'xlabel': 'Stages2'
}
ax.set(**props)

```
以关键字参数**kwargs的形式批量设置


<br/>
### 2. 在章节9.1.7中，crisis_data是列表类型的数据，for循环中，为什么能辨别date和label呢？如果把其中一个去掉就不行了，这又是为什么呢？"

```python3
crisis_data = [
    (datetime(2007, 10, 11), 'Peak of bull market'),
    (datetime(2008, 3, 12), 'Bear Stearns Fails'),
    (datetime(2008, 9, 15), 'Lehman Bankruptcy')
]

for date, label in crisis_data:
    pass
```

因为列表中的元素为元组，`for date, label in crisis_data`，通过**拆包**一一对应。