# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_puppet']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0', 'nonebot2>=2.0.0-beta.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-puppet',
    'version': '0.2.2',
    'description': 'Make NoneBot your puppet',
    'long_description': '# Nonebot Plugin Puppet\n\n基于 [nonebot2](https://github.com/nonebot/nonebot2) 和 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的会话转接插件\n\n[![License](https://img.shields.io/github/license/Jigsaw111/nonebot_plugin_puppet?style=flat-square)](LICENSE)\n![Python Version](https://img.shields.io/badge/python-3.7.3+-blue.svg?style=flat-square)\n![NoneBot Version](https://img.shields.io/badge/nonebot-2.0.0a11+-red.svg?style=flat-square&log")\n![Pypi Version](https://img.shields.io/pypi/v/nonebot-plugin-puppet.svg?style=flat-square)\n\n## 安装\n\n### 从 PyPI 安装（推荐）\n\n- 使用 nb-cli  \n\n```shell\nnb plugin install nonebot_plugin_puppet\n```\n\n- 使用 poetry\n\n```shell\npoetry add nonebot_plugin_puppet\n```\n\n- 使用 pip\n\n```shell\npip install nonebot_plugin_puppet\n```\n\n### 从 GitHub 安装（不推荐）\n\n```shell\ngit clone https://github.com/Jigsaw111/nonebot_plugin_puppet.git\n```\n\n## 使用\n\n**仅限超级用户使用**\n\n**不建议同时链接多个会话（尤其是大群），如被风控概不负责**\n\n- `puppet ln/link`链接会话\n  - `-u user_id..., -ua user_id..., --user-a user_id...`可选参数，指定源会话的 QQ 号\n  - `-g group_id..., -ga group_id..., --group-a group_id...`可选参数，指定源会话的群号\n    至少需要设置一个\n  - `-ub user_id..., --user-b user_id...`可选参数，指定链接会话的 QQ 号\n  - `-gb group_id..., --group-b group_id...`可选参数，指定链接会话的群号\n    不设置的话默认为当前会话的 QQ 号/群号\n  - `-q, --quiet`可选参数，静默链接（不发送链接成功消息）\n  - `-U, --unilateral`可选参数，单方面链接\n- `puppet rm/unlink`删除会话链接\n  - `-u user_id..., -ua user_id..., --user-a user_id...`可选参数，指定源会话的 QQ 号\n  - `-g group_id..., -ga group_id..., --group-a group_id...`可选参数，指定源会话的群号\n    不设置的话，默认为当前会话链接的所有会话\n  - `-ub user_id..., --user-b user_id...`可选参数，指定链接会话的 QQ 号\n  - `-gb group_id..., --group-b group_id...`可选参数，指定链接会话的群号\n    不设置的话默认为当前会话的 QQ 号/群号\n  - `-q, --quiet`可选参数，静默链接（不发送解除链接成功消息）\n  - `-U, --unilateral`可选参数，单方面解除链接\n- `puppet ls/list` 查看链接到当前会话的会话列表\n  - `-u user_id, --user user_id` 互斥参数，指定会话的 QQ 号\n  - `-g group_id, --group group_id` 互斥参数，指定会话的群号\n    不设置的话默认为当前会话的 QQ 号/群号\n- `puppet send message` 向指定会话发送消息，支持 CQ 码\n  - `message` 需要发送的消息，支持 CQ 码，如含空格请用 `""` 包裹\n  - `-u user_id..., --user user_id...`可选参数，指定接收会话的 QQ 号\n  - `-g group_id..., --group group_id...`可选参数，指定接收会话的群号\n    不设置的话默认为当前会话链接的所有会话\n  - `--a, --all`可选参数，指定所有群聊\n- `puppet aprv/approve` 同意请求/邀请\n  - `-f flag..., --flag flag...`可选参数，指定请求的 flag\n  - `--a, --all`可选参数，指定所有请求\n- `puppet rej/reject` 拒绝请求/邀请\n  - `-f flag..., --flag flag...`可选参数，指定请求的 flag\n  - `--a, --all`可选参数，指定所有请求\n- `puppet exit` 退出指定群聊\n  - `-g group_id..., --group group_id...`可选参数，指定要退出的群号\n\n## Bug\n\n- [x] 不允许多个超级用户链接到同一会话\n- [x] 如果指定的会话不在会话列表里会产生错误\n\n## To Do\n\n- [x] 允许单向转接\n- [x] 转接请求事件\n- [x] 提供退群功能\n- [ ] 提供默认设置\n\n## 原理\n\n```mermaid\ngraph LR\n用户 & 群 ---> Puppet ---> 用户 & 群\n```\n',
    'author': 'Jigsaw',
    'author_email': 'j1g5aw@foxmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Jigsaw111/nonebot_plugin_puppet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
