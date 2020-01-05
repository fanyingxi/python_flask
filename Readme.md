

## 代码Github URL：https://github.com/fanyingxi/python_flask
## pythonanywhere URL：http://dataweb.pythonanywhere.com/

### 将17级同学给的全球富豪榜排名数据进行清洗
* 运用了字典循环，分割、切片操作等将全球富豪行业与国籍前二十和前一百占比做成图表展示
* 运用了条件判断、推导式进行数据清理和排序
* 将17级同学给的地图.html文件和柱形图.html文件进行链接

### html文件
* 用base.html文件模板做了首页.html文件
* 用result2.html首页为模板，做了总表数据预览（/all）
* 将切片操作做的前二十和前一百的详情表与17级同学所给的柱形图.html联系在一起（/forbes）
* 将全球富豪榜排名前二十、前一百、全部的地图分布链接到首页.html（/allmap）、（/map20）、（/map100）

### python文档
* 导入数据、数据清洗分析
* 用@app.route进行表和html链接
* 通过网址后缀链接进行数据交互

### 首页（/）按下拉菜单
- 总信息表单 http://dataweb.pythonanywhere.com/all
- 全球富豪排名前二十信息详细 http://dataweb.pythonanywhere.com/forbes?limit=20
- 全球富豪排名前一百信息详细 http://dataweb.pythonanywhere.com/forbes?limit=100
- 全球富豪排名前二十所在地分布 http://dataweb.pythonanywhere.com/map20
- 全球富豪排名前一百所在地分布 http://dataweb.pythonanywhere.com/map100
- 全球所有富豪所在地分布 http://dataweb.pythonanywhere.com/allmap
