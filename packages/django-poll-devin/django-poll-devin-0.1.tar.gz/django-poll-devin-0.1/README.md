

poll是用django开发的应用

快速上手
-----------

1. 将该应用添加到django项目设置文件中的已安装app列表，如下::

    INSTALLED_APPS = [
        ...
        'app1.apps.App1Config',
    ]

2. 在主urls文件添加路径如下::

    path('app1/', include('app1.urls')),

3. 运行 ``python manage.py migrate`` 指令  创建模型和迁移到数据库

4. 启动服务器，访问 http://127.0.0.1:8000/admin/ 进入管理页面 添加和修改问题


5. 访问 http://127.0.0.1:8000/app1/ 查看问题