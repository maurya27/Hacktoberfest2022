class Node(object):
  def __init__(self,data,next):
    self.data = data
    self.next = next

class SLL:
  def __init__(self):
    self.head = None
    self.tail = None
  def append(self,data):
    node = Node(data,Node)
    if self.head is None:
      self.head = self.tail = node
    else:
      self.tail.next = node
    self.tail = node

  def remove(self,node_value):
    current_node = self.head
    previous_node = None
    while current_node is not Node:
      if current_node.data == node_value:
        if previous_node is not None:
          previous_node.next = current_node.next
        else:
          self.head = current_node.next
      previous_node = current_node
      current_node = current_node.next
    
  def display(self):
    current_node = self.head
    print("Linked List: ", end = " ")
    while current_node is not Node:
      print(current_node.data, end = " ")
      current_node = current_node.next
    print()

r = SLL()
print("Singly Linked List:\n 1.Add Node\n 2.Delete Node\n 3.Display Linked List\n 4.Exit\n")
while(True):
  chce = int(input("Enter Choice: "))
  if chce is 1:
    n = int(input("how many nodes want to add? "))
    ele = list(map(int, input("Add nodes in list: ").split()))
    for i in range(n):
      r.append(ele[i])
  elif chce is 2:
    ele = int(input("Node want to delete: "))
    r.remove(ele)
  elif chce is 3:
    r.display()
  else:
    print("LOL")
    break
    exit()

