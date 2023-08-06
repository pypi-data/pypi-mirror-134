import functools
import itertools


def normalize_leaf(leaf):
    iterable = iter(leaf)
    name = next(iterable)
    children = next(iterable, None)

    return [name, children]


def flatten_deep(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten_deep(item)
        else:
            yield item


def make_joints(tree, parent=None):
    normalized_tree = normalize_leaf(tree)
    leaf, children = normalized_tree

    if children is None:
        return {leaf: [parent]}

    flat_children = list(itertools.chain(*children))
    neighbors = list(filter(
        lambda neighbor: neighbor is not None and
        not isinstance(neighbor, list),
        [*flat_children, parent],
    ))
    joints = functools.reduce(
        lambda acc, child: {**acc, **make_joints(child, leaf)},
        children,
        {},
    )

    return {leaf: neighbors, **joints}


def build_tree_from_leaf(joints, leaf):
    def iter(current, acc):
        checked = [*acc, current]
        neighbors = joints[current]

        filtered_neighbors = filter(
            lambda neighbor: neighbor not in checked,
            neighbors,
        )
        mapped_neighbors = list(map(
            lambda neighbor: iter(neighbor, checked),
            filtered_neighbors,
        ))

        return [current, mapped_neighbors] if mapped_neighbors else [current]

    return iter(leaf, [])


def map_tree(callback_fn, tree):
    normalized_tree = normalize_leaf(tree)
    name, children = normalized_tree

    updated_name = callback_fn(name)

    if children is None:
        return [updated_name]

    updated_children = list(map(
        lambda child: map_tree(callback_fn, child),
        children,
    ))

    return [updated_name, updated_children]


def sort_joints(joints):
    return functools.reduce(
        lambda acc, name: {**acc, name: sorted(joints[name])},
        joints,
        {},
    )


def make_associations(unique_tree, tree):
    unique_leafs = flatten_deep(unique_tree)
    leafs = flatten_deep(tree)
    return dict(zip(unique_leafs, leafs))


def sort_tree(tree):
    count = itertools.count()

    unique_tree = map_tree(
        lambda name: name + str(next(count)),
        tree
    )
    associations = make_associations(unique_tree, tree)
    root, *_ = unique_tree
    joints = make_joints(unique_tree)
    sorted_joints = sort_joints(joints)

    return map_tree(
        lambda leaf: associations[leaf],
        build_tree_from_leaf(sorted_joints, root),
    )
