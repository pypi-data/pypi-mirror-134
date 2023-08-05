# treenodedefinition

**treenodedefinition** is a helper module providing an interface for 
definition of which parts of a nested list or dictionary are handled as a 
node (containing further tree items) or a leaf (being a top item of the tree).

## Installation

Installing the latest release using pip is recommended.

```` shell script
    $ pip install treenodedefinition
````

The latest development state can be obtained from gitlab using pip.

```` shell script
    $ pip install git+https://gitlab.com/david.scheliga/treenodedefinition.git@dev
````


## Basic Usage

Use `treenodedefinition.this_item_is_a_leaf` for this module's default definition of 
tree leafs. For more details read function definition of `treenodedefinition
.this_item_is_a_leaf`.

    >>> from treenodedefinition import this_item_is_a_leaf
    >>> this_item_is_a_leaf([[1, 2], [3, 4]])
    True
    >>> this_item_is_a_leaf([[1, 2], [3]])
    False
    >>> this_item_is_a_leaf("any single data type")
    True
    >>> this_item_is_a_leaf({"any": "dict or mapping"})
    False

Or use `treenodedefinition.DetectsATreeLeaf = Callable[[Any], bool]` to declare the 
type of a custom detection within function arguments or a classes attributes.


## Module *treenodedefinition*

### treenodedefinition.predict_tensor_item_count(potential_tensor: Sequence) -> int

Predicts the assumed tensor size on basis of the first element within the potentially 
nested sequence `potential_tensor`. It is assumed that the given potential tensor has a
shape of (i, j, ...). The shape's product reflects the tensor's item count. It also 
implies that all sub tensors within each level of the tensor have the same item count, 
therefore the first item within each level defines the shape of this particular level.


For 'clean' tensors the prediction is equal to the actual item count.

    >>> from treenodedefinition import predict_tensor_item_count
    >>> predict_tensor_item_count([])
    0
    >>> predict_tensor_item_count([[], []])
    0
    >>> predict_tensor_item_count([1, 2])
    2
    >>> predict_tensor_item_count([[1, 1], [2, 2]])
    4
    >>> predict_tensor_item_count(
    ...     [
    ...         [[1, 1], [2, 2]],
    ...         [[3, 3], [4, 4]]
    ...     ]
    ... )
    8

In this case the tensor should had an item count of 6, while two
items are lacking in their tensor size.

    >>> predict_tensor_item_count([[1, 2], 3, 4])
    6
    
### treenodedefinition.count_tensor_items(potential_tensor: Sequence) -> int
Counts the actual items within the potentially nested sequence `potential_tensor`.

    >>> from treenodedefinition import count_tensor_items
    >>> count_tensor_items([1, 2])
    2
    >>> count_tensor_items([[1, 1], [2, 2]])
    4
    >>> count_tensor_items(
    ...     [
    ...         [[1, 1], [2, 2]],
    ...         [[3, 3], [4, 4]]
    ...     ]
    ... )
    8
    >>> count_tensor_items([[1, 2], 3, 4])
    4

### treenodedefinition.is_proper_sized_tensor(potential_tensor: Sequence) -> bool

Estimates whether the given potential tensor has a proper shape of all
items, or is inadequately filled.

Raises TypeError, if given `potential_tensor` doesn't implement len, which means
that `potential_tensor` is not a sequence.

    >>> from treenodedefinition import is_proper_sized_tensor
    >>> is_proper_sized_tensor([])
    False
    >>> is_proper_sized_tensor([1, 2])
    True
    >>> is_proper_sized_tensor([[1, 1], [2, 2]])
    True
    >>> is_proper_sized_tensor(
    ...     [
    ...         [[1, 1], [2, 2]],
    ...         [[3, 3], [4, 4]]
    ...     ]
    ... )
    True
    >>> is_proper_sized_tensor([[1, 1], 2, 3])
    False
    >>> is_proper_sized_tensor("A string is a sequence, but not a tensor,")
    False
    >>> is_proper_sized_tensor(["while", "a", "sequence", "of", "strings", "is."])
    True

### treenodedefinition.this_sequence_is_a_leaf(potential_tensor: Sequence) -> bool

States if the given sequence `potential_tensor` is a leaf or node.

All sequences, which are *proper sized tensor*
(`is_proper_sized_tensor(..)`) are considered as values.

Sequences which contain mixed containers (Sequences and Mappings) are
considered as nodes. Also if the sequence contains different sized
sequences.

    >>> from treenodedefinition import this_sequence_is_a_leaf
    >>> this_sequence_is_a_leaf([])
    False
    >>> this_sequence_is_a_leaf([1, 2])
    True
    >>> this_sequence_is_a_leaf([[1, 1], [2, 2]])
    True
    >>> this_sequence_is_a_leaf([[1, 1], 2, 3])
    False
    >>> this_sequence_is_a_leaf("A single string is a leaf, ")
    True
    >>> this_sequence_is_a_leaf(["while", "a", "sequence", "of", "strings", "is."])
    True
    >>> this_sequence_is_a_leaf([["a", "good", "start"], {"ended": "wrong"}])
    False


### treenodedefinition.DetectsATreeLeaf = Callable[[Any], bool]

Declares a function, which task is to detect, whether the given single argument is a
tree leaf.

### treenodedefinition.this_item_is_a_leaf(tree_node_item: Any) -> bool

Differentiates a `tree_node_item` being a tree leaf or not. 

**Examples**

An empty sequence is treatend as a node, as a potential placeholder for
a future nested sequence.

    >>> from treenodedefinition import this_item_is_a_leaf
    >>> this_item_is_a_leaf([])
    False

(Nested) sequences are treatend as leafs, as long the resemble a proper
filled tensor. The item type doesn't matter.

    >>> this_item_is_a_leaf([1, 2])
    True
    >>> this_item_is_a_leaf([[1, 1], [2, 2]])
    True
    >>> this_item_is_a_leaf([[1, 1], 2, 3])
    False
    >>> this_item_is_a_leaf("A string is.")
    True
    >>> this_item_is_a_leaf(["As", "is", "also", "a", "sequence", "of", "strings"])
    True
    >>> this_item_is_a_leaf(1)
    True
    >>> this_item_is_a_leaf(object())
    True

A nested sequence with different containers is a node, with leafs.

    >>> this_item_is_a_leaf([["a", "good", "start"], {"ended": "wrong"}])
    False

A dictionary is always a node, not a leaf.

    >>> this_item_is_a_leaf({"ended": "wrong"})
    False

## Contribution

Any contribution by reporting a bug or desired changes are welcomed. The preferred 
way is to create an issue on the gitlab's project page, to keep track of everything 
regarding this project.

### Contribution of Source Code
#### Code style
This project follows the recommendations of [PEP8](https://www.python.org/dev/peps/pep-0008/).
The project is using [black](https://github.com/psf/black) as the code formatter.

#### Workflow

1. Fork the project on Gitlab.
2. Commit changes to your own branch.
3. Submit a **pull request** from your fork's branch to our branch *'dev'*.

## Authors

* **David Scheliga** 
    [@gitlab](https://gitlab.com/david.scheliga)
    [@Linkedin](https://www.linkedin.com/in/david-scheliga-576984171/)
    - Initial work
    - Maintainer

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the
[LICENSE](LICENSE) file for details

## Acknowledge

[Code style: black](https://github.com/psf/black)
