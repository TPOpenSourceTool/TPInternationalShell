## ChangeLog

#### V0.1.0 

加入工程

## 使用方法

### 0.安装Python, 2.7以上

### 1.安装pyexcelerator组件

切换到pyexcelerator-0.6.4.1目录,执行sudo python setup.py install 安装


### 2.安装xld组件

切换到xlrd-1.0.0目录,执行sudo python setup.py install 安装

### 3.使用脚本
#### 将iOS的Localizable.strings 文件转成excel语言包文件
./ios2xls.sh

#### 将Android多个目录的strings.xml文件转成excel语言包文件
./android2xls.sh

#### 将excel语言包文件转成iOS的Localizable.strings文件
./xls2ios.sh

#### 将excel语言包文件转成Android多个目录下的strings.xml文件
./xls2android.sh

#### 项目工程必须和整个脚本工程在一个目录内,同时需要修改ios2xls.sh,xls2ios.sh内的国际化文件目录.
