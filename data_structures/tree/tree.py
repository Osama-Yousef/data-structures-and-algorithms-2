class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    

    def in_order(self, node=None, results=None):
      node = node or self.root

      results = results or []
      if node:
        if node.left:
          self.in_order(node.left, results)
        
        results.append(node.value)

        if node.right:
          self.in_order(node.right, results)

      return results


    def pre_order(self, node=None, results=None):
      node = node or self.root

      results = results or []

      if node:
        results.append(node.value)

        if node.left:
          self.pre_order(node.left, results)

        if node.right:
          self.pre_order(node.right, results)

      return results

    def post_order(self, node=None, results=None):

      node = node or self.root

      results = results or []
      if node:
        if node.left:
          self.post_order(node.left, results)

        if node.right:
          self.post_order(node.right, results)
        
        results.append(node.value)

      return results


class BinarySearchTree(BinaryTree):

  def add(self, value, root=None):
    root = root or self.root

    node = Node(value)

    if not self.root:
      self.root = node
      return
    
    if value < root.value:
      if root.left:
        self.add(value, root.left)
      else:
        root.left = node
    else:
      if root.right:
        self.add(value, root.left)
      else:
       root.right = node
    

  def contains(self, value, current=None):
      current = current or self.root

      if not self.root or value == None:
        print('no')
        return False
    
      if current.value == value:
        print('yes')
        return True
      elif current.value < value:
        return self.contains(value, current.left)
      else:
        return self.contains(value, current.right)
      
      print('no')
      return False

def fizz_buzz_tree(node):
  if (node.value % 3 == 0 & node.value % 5 == 0):
    node.value = 'FizzBuzz'
  elif node.value % 3 == 0:
    node.value = 'Fizz'
  elif node.value % 5 == 0:
    node.value = 'Buzz'
  
  fizz_buzz_tree(node.left)
  fizz_buzz_tree(node.right)
  print(node)
  return node


if __name__ == "__main__":
  tree = BinarySearchTree()
  tree.add(20)
  tree.add(15)
  tree.add(10)


  # print(tree.post_order())
  # print(tree.in_order())
  # print(tree.pre_order())

  # tree.contains(11)
