# MaxHeap Priority Queue (Python)

This project implements a **Max Heap** data structure in Python, commonly used for **priority queues**. It maintains elements in an array-based binary heap where each parent has a higher priority than its children.

## 📁 Files

- `maxheap.py` – Contains the `heap_node` and `heap` classes with core heap operations.
- `heap_ui.py` – A simple graphical interface built with `tkinter` to interact with the heap.
- `README.md` – Project overview and usage instructions.

---

## ⚙️ Heap Class Methods

### `insert(id, priority)`
Adds a new node to the heap with the given ID and priority.

### `increase_priority(id, new_priority)`
Increases the priority of a node with the given ID (if higher than current).

### `delete_maximum()`
Removes and returns the node with the highest priority (root of the heap).

### `delete_by_id(id)`
Deletes the node identified by the given ID.

### `process(bst=None)`
Removes the max node and optionally deletes it from a provided BST.

### `level_order()`
Prints nodes in level-order (breadth-first traversal of the heap).

---

## 🖥 Graphical User Interface (Optional)

A basic GUI built with `tkinter` is included to perform heap operations through a user-friendly interface. It supports:

- Inserting nodes
- Increasing priority
- Deleting the maximum node
- Deleting by ID
- Viewing the heap in level-order

To run the interface:

```bash
python heap_ui.py
