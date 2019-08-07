我的提问

git pull request 为开源代码做贡献



【Task0精选问题】

Q1：打开jupyter notebook后偶尔会出现无工具栏

刷新界面




Q2：jupyter notebook 在使用中有什么好用的小技巧吗？

Magic指令，参照书《Python for Data Analysis》2nd中2.2 IPython BasicsAPPENDIX BMore on the IPython System



Q3：markdown编辑使用html+css样式本地上可以显示效果，但是上传到github上样式都没有了，这是什么回事呢？？？

github不提供html,css渲染和latex解析，请自行在浏览器安装插件



Q4：发现commit message写错了的时候该怎么修改？

git commit -m "new_message"覆盖你提交的message

 

Q5： jupyter notebook写python程序的时候，要打开一个文件或者说一张图片，相对路径是怎样的？（貌似不是当前的Python3）我这里直接用了绝对路径

相对地址：相对你notebook所在的地址，请先明确notebook在你系统的位置。



相对路径是相对于当前文件位置

而绝对路径是相对于系统根目录的位置

一般编程都用相对位置，但实际上最终都转换为绝对路径，例如web网站内部网页的跳转

