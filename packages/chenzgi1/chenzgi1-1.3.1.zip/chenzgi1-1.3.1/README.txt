1.创建一个发布文件
  d:\python34\python.exe setup.py sdist
2.将发布文件安装到本地副本
  d:\python34\python.exe setup.py install
  
  
  将python模块化一定要注意对齐格式
  
  import test1//是告诉python解释器允许访问test1命名空间
  执行test1中的某个函数时 必须使用 test1.parse(lists)  命名空间.函数名(参数)
  