## 打包流程
### 1. 打包项目
```
python setup.py sdist  
python setup.py sdist bdist_wheel 
```
### 2. 检查
```
twine check dist/*
or
python3 -m twine check dist/*
```
### 3. 上传pypi
```
twine upload dist/* 
or
python3 -m twine upload dist/*
```
### 4. 安装最新版本
```
pip install iOS-tools
```

## 描述
本项目封装了获取iOS设备 安装卸载 app 等 的基本功能