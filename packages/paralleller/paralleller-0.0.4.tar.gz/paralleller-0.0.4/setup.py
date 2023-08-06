# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['paralleller']

package_data = \
{'': ['*']}

install_requires = \
['importlib_metadata>=3.4.0,<4.0.0']

entry_points = \
{'console_scripts': ['paralleller = paralleller.cli:main']}

setup_kwargs = {
    'name': 'paralleller',
    'version': '0.0.4',
    'description': '用于进行并行处理的接口库。',
    'long_description': '# paralleller 介绍\n\n\n[![PyPI version](https://badge.fury.io/py/paralleller.svg)](https://badge.fury.io/py/paralleller)\n![versions](https://img.shields.io/pypi/pyversions/paralleller.svg)\n[![GitHub license](https://img.shields.io/github/license/mgancita/paralleller.svg)](https://github.com/mgancita/paralleller/blob/main/LICENSE)\n\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n\n用于进行并行处理的接口库。\n\n\n- 开源许可: MIT\n- 文档: https://llango.github.io/paralleller.\n\n\n## 特征\n\n* TODO\n\n\n## 项目布局\n\n    main.py    # 项目主文件，服务使用它启动。 uvicorn main:app --reload\n    .env       # 环境变量文件\n    requirements.txt    # 依赖文件\n    readme.md       # 简单说明文件\n    test.db         # 生成的数据库文件\n    mkdocs.yml      # mkdocs文档构建配置文件\n    LICENSE         # 开源许可文件\n    Procfile        # 容器用来执行用户设定的命令\n    Makefile        # 用来启动docker-compose 文件\n    .dockerignore   # docker打包上传到容器里过滤文件\n    .gitignore      # 版本控制过滤上传文件\n    docker-compose.yaml # docker-compose配置启动文件\n    Dockerfile      # Docker文件\n    core/\n        blog.py     # 与数据库进行博客交互文件\n        user.py     # 与数据库进行用户交互文件\n        __init__.py # 声明为包所需文件\n    database/\n        config.py   # 数据库连接配置文件\n        __init__.py # 声明为包所需文件\n    docs/\n        index.md    # 文档首页\n        database_config.md      # 对应database/config.py 文件的讲解\n    models/\n        models.py   # 用来建立数据库表映射的类文件\n        __init__.py # 声明为包所需文件\n    route/\n        auth.py     # 登录认证接口文件\n        blog.py     # 博客接口文件\n        user.py     # 用户接口文件\n        __init__.py # 声明为包所需文件\n    schema/\n        schemas.py  # 声明类型文件\n        __init__.py # 声明为包所需文件\n    static/\n        css/\n            index.css   # 样式文件\n        js/\n            main.js     # 脚步\n        images/         # 图片文件夹\n    templates/\n        index.html      # 模板文件\n    test/               # 测试目录\n    utils/\n        hash.py         # 密码处理文件\n        oa2.py          # 认证处理文件\n        token.py        # 指令处理文件\n        __init__.py     # 声明为包所需文件  \n\n\n## 项目启动\n    1. 进行该项目中，建立虚拟环境\n    ```\n    virtualenv venv\n    source  venv/bin/activate\n    ```\n    2. 安装依赖\n    ```\n    pip install -r requirements.txt\n    ```\n    3. 直接使用如下命令启动:\n        ``` \n        uvicorn main:app --realod \n        ```\n    \n## 文档启动\n\n```\nmkdocs serve --livereload -t shadocs -a localhost:8080\n```\n\n\n## 制作\n\n\n该包使用 [Cookiecutter](https://github.com/audreyr/cookiecutter) 和 [`llango/cookiecutter-mkdoc-shapackage`](https://github.com/llango/cookiecutter-mkdoc-shapackage/) 项目模版创建。\n',
    'author': 'Rontomai',
    'author_email': 'rontomai@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/llango/paralleller',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
