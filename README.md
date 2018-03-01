# generate_configuration_in_batch


## 介绍
网工经常要生成很多交换机配置，那么就需要根据模版和参数表来批量生成大量的配置文件<br>

原理很简单，比如模版文件内容如下：
``` python
sysnmae @SYSNAME

int  @INTNAME
    ip address @IP
    description @DES
```
<br>
我需要生成三个交换机配置文件，参数放在了excel里面<br>
![](https://github.com/luffycjf/generate_configuration_in_batch/blob/master/QQ%E6%88%AA%E5%9B%BE20180301173438.png)<br>
filename一栏是强制关联的参数名称，如果修改名称需要在程序里面修改对应参数，这一栏主要用于生成的配置文件名称。<br>

执行 python templatecreater.py<br>

会生成配置文件<br>
1.txt<br>
2.txt<br>
3.txt<br>

cat 1.txt<br>
``` python
sysnmae cjf

int  LO0
    ip address 1.1.1.1
    description L0123
```   
 
