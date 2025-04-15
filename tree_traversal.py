from collections import deque
from dataclasses import dataclass
from typing import TypeVar, Optional

T = TypeVar("T")


@dataclass(frozen=True)
class TreeNode[T]:
    val: T
    left: "Optional[TreeNode[T]]" = None
    right: "Optional[TreeNode[T]]" = None

    # Recursively traverse a queue depth-first
    def recursiveDfs(
        self, node: "Optional[TreeNode[T]]"
    ) -> "Optional[TreeNode[T]]":
        if node is None:
            return
        print(node.val)

        for child in [node.left, node.right]:
            self.recursiveDfs(child)

    # Iteratively traverse a queue depth-first
    def iterativeDfs(self) -> None:
        stack: "list[TreeNode[T]]" = [self]

        while stack:
            node = stack.pop()
            print(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # Iteratively traverse a queue breadth-first
    def iterativeBfs(self) -> None:
        # Initialise the queue with the root node
        queue: "deque[TreeNode[T]]" = deque([self])

        while queue:
            # For each element in the queue, pop it from the left and
            # add its children to the right. When the queue is empty,
            # we've traversed the tree
            for _ in range(len(queue)):
                node = queue.popleft()
                print(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


if __name__ == "__main__":
    root = TreeNode[int](
        val=3,
        left=TreeNode[int](val=9, left=TreeNode(val=4)),
        right=TreeNode[int](
            val=20, left=TreeNode(val=15), right=TreeNode(val=7)
        ),
    )

    root.recursiveDfs(root)
    print("---")
    root.iterativeDfs()
    print("---")
    root.iterativeBfs()
