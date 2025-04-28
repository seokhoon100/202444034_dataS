class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

    def pre_order(node):
        if node is None:
            return

        print(node.data, end="->")
        pre_order(node.left)
        pre_order(node.right)


    def in_order(node):
        if node is None:
            return

        in_order(node.left)
        print(node.data, end="->")
        in_order(node.right)


    def post_order(node):
        if node is None:
            return

        post_order(node.left)
        post_order(node.right)
        print(node.data, end="->")


    class TreeNode:



    if __names__ == "__main__":
        numbers = [10, 15, 8, 3, 9]
        root = Node

        node = TreeNode()
        node.data = numbers[0]
        root = node

        for number in numbers[1:]:
            node = TreeNode()
            node.data = number
            current = root
            while True:
                if number < current.data:
                    if current.left is None:
                        current.left = node
                        break

                    current = current.left  # 이동

                else:
                    if current.right is None:
                        current.right = node
                        break

                    current = current.right  # 이동


        print("BST 구성 완료")

        pre_order(root)