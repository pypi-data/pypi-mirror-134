# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['graphs']
setup_kwargs = {
    'name': 'hexlet-graphs',
    'version': '0.1.0',
    'description': '',
    'long_description': "# python-graphs\n\n[![github action status](https://github.com/hexlet-components/python-graphs/workflows/Python%20CI/badge.svg)](../../actions)\n\n## Install\n\n```bash\npip install hexlet-graphs\n```\n\n## Usage example\n\n```python\nfrom hexlet.fs import (\n  build_tree_from_leaf\n  make_joints,\n  sortTree\n)\n\ntree = ['B', [\n    ['D'],\n    ['A', [\n        ['C', [\n            ['F'],\n            ['E'],\n        ]],\n    ]],\n]]\n\njoints = make_joints(tree)\ntransformed = build_tree_from_leaf(joints)\n// ['C', [\n//     ['F'],\n//     ['E'],\n//     ['A', [\n//         ['B', [\n//             ['D'],\n//         ]],\n//     ]],\n// ]]\n\nsort_tree(transformed)\n// ['C', [\n//     ['A', [\n//         ['B', [\n//             ['D'],\n//         ]],\n//     ]],\n//     ['E'],\n//     ['F'],\n// ]]\n```\n\nFor more information, see the [Full Documentation](docs)\n\n[![Hexlet Ltd. logo](https://raw.githubusercontent.com/Hexlet/assets/master/images/hexlet_logo128.png)](https://ru.hexlet.io/pages/about?utm_source=github&utm_medium=link&utm_campaign=python-graphs)\n\nThis repository is created and maintained by the team and the community of Hexlet, an educational project. [Read more about Hexlet (in Russian)](https://ru.hexlet.io/pages/about?utm_source=github&utm_medium=link&utm_campaign=python-graphs).\n\nSee most active contributers on [hexlet-friends](https://friends.hexlet.io/).\n",
    'author': 'Hexlet Team',
    'author_email': 'info@hexlet.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hexlet-components/python-graphs',
    'package_dir': package_dir,
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
