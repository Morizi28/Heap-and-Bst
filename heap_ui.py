import tkinter as tk
from tkinter import messagebox
from maxheap import heap

class HeapUI:
    def __init__(self, master):
        self.master = master
        master.title("Max Heap Interface")

        self.h = heap()

        # ID and Priority
        self.label_id = tk.Label(master, text="ID:")
        self.label_id.grid(row=0, column=0)
        self.entry_id = tk.Entry(master)
        self.entry_id.grid(row=0, column=1)

        self.label_priority = tk.Label(master, text="Priority:")
        self.label_priority.grid(row=1, column=0)
        self.entry_priority = tk.Entry(master)
        self.entry_priority.grid(row=1, column=1)

        # Buttons
        self.insert_button = tk.Button(master, text="Insert", command=self.insert_node)
        self.insert_button.grid(row=2, column=0, columnspan=2)

        self.increase_button = tk.Button(master, text="Increase Priority", command=self.increase_priority)
        self.increase_button.grid(row=3, column=0, columnspan=2)

        self.delete_max_button = tk.Button(master, text="Delete Max", command=self.delete_max)
        self.delete_max_button.grid(row=4, column=0, columnspan=2)

        self.delete_by_id_button = tk.Button(master, text="Delete by ID", command=self.delete_by_id)
        self.delete_by_id_button.grid(row=5, column=0, columnspan=2)

        self.level_order_button = tk.Button(master, text="Level Order", command=self.display_level_order)
        self.level_order_button.grid(row=6, column=0, columnspan=2)

        self.output = tk.Text(master, height=10, width=40)
        self.output.grid(row=7, column=0, columnspan=2)

    def insert_node(self):
        try:
            ID = self.entry_id.get()
            priority = int(self.entry_priority.get())
            self.h.insert(ID, priority)
            messagebox.showinfo("Success", f"Inserted node with ID: {ID}")
        except ValueError:
            messagebox.showerror("Error", "Priority must be an integer")

    def increase_priority(self):
        try:
            ID = self.entry_id.get()
            new_priority = int(self.entry_priority.get())
            self.h.increase_priority(ID, new_priority)
            messagebox.showinfo("Success", f"Increased priority for ID: {ID}")
        except ValueError:
            messagebox.showerror("Error", "Priority must be an integer")

    def delete_max(self):
        node = self.h.delete_maximum()
        if node:
            messagebox.showinfo("Deleted", f"Deleted node ID: {node.id} with priority {node.priority}")
        else:
            messagebox.showinfo("Info", "Heap is empty")

    def delete_by_id(self):
        ID = self.entry_id.get()
        self.h.delete_by_id(ID)
        messagebox.showinfo("Deleted", f"Deleted node with ID: {ID}")

    def display_level_order(self):
        self.output.delete(1.0, tk.END)
        if self.h.size == 0:
            self.output.insert(tk.END, "Heap is empty.\n")
        else:
            for i, node in enumerate(self.h.arr[1:], start=1):
                self.output.insert(tk.END, f"{i}: ID: {node.id}, Priority: {node.priority}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = HeapUI(root)
    root.mainloop()
