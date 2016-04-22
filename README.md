## sdustoj
---------
###1.建议环境部署：Django1.9+Mysql5.6+Python2.7＋nginx+uwsgi
###2.需要安装的插件DjangoCaptcha，lorun，pillow
###3.uwsgi 配置文件djang.xml
```
dajngo.xml
<uwsgi>
    <socket>0.0.0.0:9090</socket>
    <pythonpath>/home/sdustoj/sdustoj/sdustoj</pythonpath>
    <module>wsgi</module>
    <profiler>true</profiler>
    <plugin>python</plugin>
    <pythonpath>..</pythonpath>
    <memory-report>true</memory-report>
    <enable-threads>true</enable-threads>
    <logdate>true</logdate>
    <limit-as>6048</limit-as>
</uwsgi>
```
把此文件放到此项目sdustoj目录下 运行 uwsgi -x django.xml 或 用ini文件 运行 uwsgi －i django.ini
####4.安装cacptcha需要安装pillow（PIL），并且依赖 libjpeg,libpng,libfreetype
