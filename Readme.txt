
一、测试对象：图书管理测试项目nbop-plat-test-app。实现http接口自动化化测试

二、测试设计: 采用Python+Unittest+request实现http接口自动化测试
    1、主体结构介绍
       1）casesrc：测试运行入口，测试案例源码
          run.py:主体入口，实现运行测试案例、记录日志、出测试报告等功能。
          testlist.txt:放置要运行的测试案例文件名，文件名以test开头
          addBook.py: 新增接口公共模块
          deleteBook.py: 删除接口公共模块
          getBookList.py：查询接口公共模块
          updateBook.py: 更新接口公共模块
          test开头文本：实现增、删、改、查测试脚本

       2）common:公共模块源码
	  config.ini：放置URL、timeout、database参数
          ReadConfig.py：读取公共参数config.ini模块
          ConnetExcel.py:读写excel模块
          Log.py：日志模块
          CallHttp: http基本操作模块
       4）log/report：运行日志、测试报告
       5) testData:存放测试数据，已设计多个测试案例
          数据输入datain页：为每个案例设计编号、描述
          数据输出dataout页：记录每个案例运行结果信息，并与期望值比较，得出测试结果。

    2、测试案例设计：
       1）调度方式：使用unittest调度不同场景测试用例。
       2）案例标注：为每个测试用例标准唯一的case id
       3）一个脚本执行多个案例:  在同个场景下，设计可执行连续的测试案例
       4）可重复性：测试用例可重复执行                       

三、框架待持续补充：
    1、补充测试案例、断言
    2、补充database操作


          

                 








