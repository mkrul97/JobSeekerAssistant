from DataManager import DataManager
import tkinter as tk

class TagsModule:
    def __init__(self, root):
        self.tag_inputs = []

        self.data_manager = DataManager()
        self.data = self.data_manager.load_data()

        self.tags_frame = tk.Frame(root)
        self.tags_frame.pack(side=tk.LEFT)

        self.add_tag_button = tk.Button(self.tags_frame, text="+", command=self.add_tag)
        self.add_tag_button.pack(side=tk.LEFT)
        
        self.delete_tag_button = tk.Button(self.tags_frame, text="-", command=self.delete_tag)
        self.delete_tag_button.pack(side=tk.LEFT)

        self.add_tag()

        self.populate_tags()

    def add_tag(self):
        if len(self.tag_inputs) < 5:
            tag_input = tk.Entry(self.tags_frame)
            tag_input.pack(side=tk.LEFT)
            self.tag_inputs.append(tag_input)
            self.reposition_buttons()

    def delete_tag(self):
        if len(self.tag_inputs) > 1:
            tag_input = self.tag_inputs.pop()
            tag_input.destroy()
            self.reposition_buttons()

    def reposition_buttons(self):
        for widget in self.tags_frame.winfo_children():
            if widget not in [self.add_tag_button, self.delete_tag_button]:
                widget.pack_forget()

        for tag_input in self.tag_inputs:
            tag_input.pack(side=tk.LEFT)

        self.add_tag_button.pack_forget()
        self.delete_tag_button.pack_forget()
        self.add_tag_button.pack(side=tk.LEFT)
        self.delete_tag_button.pack(side=tk.LEFT)

    def return_tags(self):
        tags = []
        for tag in self.tag_inputs:
            tags.append(tag.get())

        return tags
    
    def populate_tags(self):
        
        while len(self.tag_inputs) < len(self.data['tags']):
            self.add_tag()
        
        i = 0
        for value in self.data['tags']:
            self.tag_inputs[i].delete(0, tk.END)
            self.tag_inputs[i].insert(0, value)
            i += 1