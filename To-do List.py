import tkinter as tk
from tkinter import ttk, messagebox,font
from ttkbootstrap import Style

class TodoListApp(tk.Tk):
    def __init__(self, font=None):
        super().__init__()
        self.title("Todo List")
        self.geometry("500x500")
        style = Style(theme="flatly")
        style.configure("Custon.TEntry", foreground='gray')
        self.task_input = ttk.Entry(self, font=("TKDefaultFont", 16), width=30, style="Custon.TEntry")
        self.task_input.pack(pady=10)
        self.task_input.insert(0, "Enter your To-do")
        self.task_input.bind("<FocusIn>", self.clear_placeholder)
        self.task_input.bind("<FocusIn>", self.restore_placeholder)
        ttk.Button(self, text="ADD", command=self.add_task).pack(pady=5)
        self.task_list = tk.Listbox(self, font=("TKDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        ttk.Button(self, text="Done", style="sucess.TButton", command=self.mark_done).pack(side=tk.RIGHT, padx=10,
                                                                                           pady=10)
        ttk.Button(self, text="Delete", style="danger.TButton", command=self.delete_task).pack(side=tk.RIGHT, padx=10,
                                                                                               pady=10)

    def add_task(self):
        task = self.task_input.get()
        if task != "Enter your To-do":
            self.task_list.insert(tk.END, task)
            self.task_list.itemconfig(tk.END, fg="red")
            self.task_input.delete(0, tk.END)


    def mark_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, fg="green")

    def delete_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.delete(task_index)

    def clear_placeholder(self, event):
        if self.task_input.get() == "Todo List":
            self.task_input.delete(0, tk.END)
            self.task_input.configure(style="TEntry")

    def restore_placeholder(self, event):
        if self.task_input.get() == "":
            self.task_input.insert(0, "Enter your To-do")
            self.task_input.configure(style="Custom.TEntry")


if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop()
