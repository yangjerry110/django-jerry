# django-jerry
jerry的django框架

1.首先需要，用python加载html，解析html。
2.假如需要登录，可以使用命令行式的chrome，进行动态点击，可以模拟一些点击和验证码拖拽等等。
3.采集，整理出来的数据，可以整理成一个json，进行存储。
4.设计表的时候，要考虑数据表的增加和修改，等等。
5.设计表的时候，不要实现一些耦合的数据关系。
6.选择存储的数据库时，可以考虑一些sqlite和一些比较好的第三方。

#配置conf，进行抓取
example : 图片
1.配置url，要抓取的url
2.data，获取urls列表的js代码
3.params 获取单个参数的js配置

实现逻辑：
1.通过chrome加载data里面的js，拿到详情的urls列表
2.再单个加载详情url，执行params里面的js，获取对应的参数的值。
