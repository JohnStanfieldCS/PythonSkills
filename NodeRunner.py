from LinkedList import LinkedList

# Function to return the nth to last node in a linked list using a runner technique
def nth_last_node(linked_list, n):
  current_pointer = None
  pointer_lead = linked_list.head_node
  counter = 1

  while pointer_lead:
    pointer_lead = pointer_lead.get_next_node()
    counter += 1

    if counter >= n + 1:
      if current_pointer == None:
        current_pointer = linked_list.head_node
      else:
        current_pointer = current_pointer.get_next_node()
  return current_pointer    

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)
