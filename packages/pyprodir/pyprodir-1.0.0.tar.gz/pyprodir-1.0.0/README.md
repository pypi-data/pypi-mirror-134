# pyprodir

## 安装

```sh
pip install -U pyprodir
pip install -i https://mirrors.aliyun.com/pypi/simple/ -U pyprodir
```

## 使用方法

### 导入该模块时会根据 pyproject.toml 定位项目目录并将项目目录加到 sys.path 前面

```py
import pyprodir
```

目的：深层目录下的脚本被直接运行时，能够 import 项目级别下的模块

[The pyproject.toml file](https://python-poetry.org/docs/pyproject/)

### 获取项目目录位置
```py
import pyprodir
print("prodir:", pyprodir.prodir)
```

### 从某一路径开始向上查找某一个文件，得到 None 或者 pathlib.Path 对象

```py
import pyprodir
profile = find_up(sys.modules["__main__"].__file__, "pyproject.toml")
print(profile.read_text("utf_8"))
```

## 原因
使用 python some/file.py 方式运行，some.file.py 无法使用 relative import，同时也无法使用 absolute import 引用项目目录下的 foo.bar 模块。

使用 python -m some.module 方式运行，虽然使 some.module 可以用 relative import，但在 vscode 上没办法配置按 F5 用这种方式运行任意文件。


