from DataManager import DataManager
import tkinter as tk

class TagsModule:
    # Create a graphical user interface (GUI) with Entry widgets for entering tags
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

        self.add_tag()  # Adds the first Entry widget

        self.populate_tags()  # Load user's search details from saved data if it exists

    # Add up to 5 Entry widgets for entering tags
    def add_tag(self):
        
        if len(self.tag_inputs) < 5:
            tag_input = tk.Entry(self.tags_frame, width=10)
            tag_input.pack(side=tk.LEFT)
            self.tag_inputs.append(tag_input)
            self.reposition_buttons() # Updates widgets positions

    # Delete the last Entry widget for entering tags until only one remains
    def delete_tag(self):
        
        if len(self.tag_inputs) > 1:
            tag_input = self.tag_inputs.pop()
            tag_input.destroy()
            self.reposition_buttons()  # Updates widgets positions

    # Update widget positions to preserve the intended order
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

    # Retrieve tags provided by the user
    def return_tags(self):
        
        tags = []
        for tag in self.tag_inputs:
            tags.append(tag.get())

        return tags
    
    # Populate Entry widgets with saved data
    def populate_tags(self):
        
        # Add Entry widgets until their count matches the number of saved tags
        while len(self.tag_inputs) < len(self.data['tags']):
            self.add_tag()
        
        i = 0
        for value in self.data['tags']:
            self.tag_inputs[i].delete(0, tk.END)
            self.tag_inputs[i].insert(0, value)
            i += 1