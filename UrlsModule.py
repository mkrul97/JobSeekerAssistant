import tkinter as tk
from tkinter import ttk
from DataManager import DataManager

class UrlsModule:
    def __init__(self, root):
        
        # Create a graphical user interface (GUI) with Entry widgets for entering URLs
        self.root = root

        self.data_manager = DataManager()
        self.data = self.data_manager.load_data()

        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        self.canvas = tk.Canvas(self.main_frame, height=220, width=300)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0,200), window=self.frame, anchor="n")

        self.url_inputs = []

        self.add_url()  # Adds the first Entry widget

        self.add_button = ttk.Button(root, text="Add URL", command=lambda: self.add_url())
        self.add_button.pack(padx=5, pady= 5)

        self.remove_button = ttk.Button(root, text="Remove URL", command=lambda: self.remove_url())
        self.remove_button.pack(padx=5, pady= 5)

        self.populate_urls()  # Load user's search details from saved data if it exists

    # Adjust the scroll region of the canvas to fit its contents 
    def on_canvas_configure(self, event):
        
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # Add up to 20 Entry widgets for entering URLs
    def add_url(self):
        
        if len(self.url_inputs) < 20:
            url_input = ttk.Entry(self.frame, width=45)
            url_input.pack(pady=1, padx=2, fill=tk.X, expand=True)
            self.url_inputs.append(url_input)
            self.on_canvas_configure(None)

    # Delete the last Entry widget for entering URLs until only one remains
    def remove_url(self):
        
        if len(self.url_inputs) > 1:
            url_input = self.url_inputs.pop()
            url_input.pack_forget()
            self.on_canvas_configure(None)

    # Retrieve URLs provided by the user
    def return_urls(self):
        
        urls = []
        for url in self.url_inputs:
            urls.append(url.get())

        return urls
    
    # Populate Entry widgets with saved data
    def populate_urls(self):
        
        # Add Entry widgets until their count matches the number of saved URLs
        while len(self.url_inputs) < len(self.data['urls']):
            self.add_url()

        for i, value in enumerate(self.data['urls']):
            self.url_inputs[i].delete(0, tk.END)
            self.url_inputs[i].insert(0, value)