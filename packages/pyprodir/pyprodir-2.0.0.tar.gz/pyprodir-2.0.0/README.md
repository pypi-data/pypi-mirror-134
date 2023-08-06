# pyprodir

## 需求

约定 pyproject.toml 位于项目根目录。
需要深层目录下的脚本被直接运行或者被 pytest 时，能够 import 项目级别下的模块。

## 安装

```sh
pip install -U pyprodir
pip install -i https://mirrors.aliyun.com/pypi/simple/ -U pyprodir
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U pyprodir
```

## 使用方法

```py
import pyprodir
```

## 内部细节

使用 python some/file.py 方式运行，some.file.py 无法使用 relative import，也无法使用 absolute import 引用项目目录下的 foo.bar 模块。

使用 python -m some.module 方式运行，虽然 some.module 既可以 relative import ..foo.bar 也可以 absolute import foo.bar，但没办法在 vscode 上配置 F5 启动任意文件。

不能依赖 sys.modules["__main__"] 因为它不一定是我们的脚本，可能是 pytest，也可能是交互式解释器。

这个模块是给应用程序使用的，不是给库使用的，禁止库代码 import 这个模块，必须是应用程序项目下的文件才能 import 这个模块。

导入该模块时，该模块会查谁 import 的它，然从那里向上搜索 pyproject.toml 文件，若找到，则把所在目录添加到 sys.path 前面。

[The pyproject.toml file](https://python-poetry.org/docs/pyproject/)


