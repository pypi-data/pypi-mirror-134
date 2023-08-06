# python-graphs

[![github action status](https://github.com/hexlet-components/python-graphs/workflows/Python%20CI/badge.svg)](../../actions)

## Install

```bash
pip install hexlet-graphs
```

## Usage example

```python
from hexlet.fs import (
  build_tree_from_leaf
  make_joints,
  sortTree
)

tree = ['B', [
    ['D'],
    ['A', [
        ['C', [
            ['F'],
            ['E'],
        ]],
    ]],
]]

joints = make_joints(tree)
transformed = build_tree_from_leaf(joints)
// ['C', [
//     ['F'],
//     ['E'],
//     ['A', [
//         ['B', [
//             ['D'],
//         ]],
//     ]],
// ]]

sort_tree(transformed)
// ['C', [
//     ['A', [
//         ['B', [
//             ['D'],
//         ]],
//     ]],
//     ['E'],
//     ['F'],
// ]]
```

For more information, see the [Full Documentation](docs)

[![Hexlet Ltd. logo](https://raw.githubusercontent.com/Hexlet/assets/master/images/hexlet_logo128.png)](https://ru.hexlet.io/pages/about?utm_source=github&utm_medium=link&utm_campaign=python-graphs)

This repository is created and maintained by the team and the community of Hexlet, an educational project. [Read more about Hexlet (in Russian)](https://ru.hexlet.io/pages/about?utm_source=github&utm_medium=link&utm_campaign=python-graphs).

See most active contributers on [hexlet-friends](https://friends.hexlet.io/).
