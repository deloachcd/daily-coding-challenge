#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


typedef struct node {
  int position;
  int value;
  void * both;
} node;


node * create_node(int value) {
  node * n = malloc(sizeof(node));
  n->value = value;
  n->both = NULL;
  return n;
}


void add(node * element, node * list_root) {
  if (list_root->both == NULL) {
    list_root->both = element; // first node gets direct pointer to next
    element->both = list_root;
  } else {
    node * prev_node = list_root;
    node * current_node = list_root->both;
    node * tmp_node;
    while (current_node->both != prev_node) {
      tmp_node = current_node;
      current_node = (node *) ((uintptr_t)prev_node ^ (uintptr_t)current_node->both);
      prev_node = tmp_node;
    }
    // current_node should be tail at this point
    current_node->both = (node *) ((uintptr_t)prev_node ^ (uintptr_t)element);
    element->both = current_node;
  }
}


node * get(int index, node * list_root) {
  node * previous_node = list_root;
  node * current_node = list_root->both;
  node * tmp_node;
  if (index == 0) {
    return previous_node;
  } else {
    for (int i = 1; i < index; i++) {
      tmp_node = current_node;
      current_node = (node *) ((uintptr_t)previous_node ^ (uintptr_t)current_node->both);
      previous_node = tmp_node;
    }
  }
  return current_node;
}


int main() {
  // this code should ensure that our solution works correctly
  int retval;

  node * my_linked_list = create_node(666);

  add(create_node(777), my_linked_list);
  add(create_node(888), my_linked_list);
  add(create_node(999), my_linked_list);
  add(create_node(1111), my_linked_list);

  if (get(0, my_linked_list)->value == 666 &&
      get(1, my_linked_list)->value == 777 &&
      get(2, my_linked_list)->value == 888 &&
      get(3, my_linked_list)->value == 999 &&
      get(4, my_linked_list)->value == 1111) {
    printf("XOR linked list implementation passes test cases!\n");
    retval = 0;
  } else {
    retval = -1;
  }

  return retval;
}
