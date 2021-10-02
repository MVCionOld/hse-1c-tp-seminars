from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    value: int
    left_child: Optional["TreeNode"]
    right_child: Optional["TreeNode"]


def traverse(node):
    result = ""
    result += traverse(node.left_child)
    result += str(node.value)
    result += traverse(node.right_child)
    return result


if __name__ == "__main__":
    tree = TreeNode(
        value=0,
        left_child=TreeNode(
            value=1,
            left_child=TreeNode(
                value=2,
                left_child=TreeNode(
                    value=3,
                    left_child=None,
                    right_child=None,
                ),
                right_child=None,
            ),
            right_child=TreeNode(
                value=4,
                left_child=None,
                right_child=None,
            ),
        ),
        right_child=TreeNode(
            value=5,
            left_child=None,
            right_child=TreeNode(
                value=6,
                left_child=TreeNode(
                    value=7,
                    left_child=None,
                    right_child=None,
                ),
                right_child=TreeNode(
                    value=8,
                    left_child=None,
                    right_child=TreeNode(
                        value=9,
                        left_child=None,
                        right_child=None,
                    ),
                ),
            ),
        ),
    )

    assert "0123456789" == traverse(tree)