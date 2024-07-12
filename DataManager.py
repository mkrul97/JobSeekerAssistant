from tkinter import messagebox
import json
import os

class DataManager:
    # Creating a save data file in the %appdata% directory to store user's search details
    def __init__(self):
        
        self.appdata_dir = self.get_appdata_directory()
        self.data_file = os.path.join(self.appdata_dir, "profile.json")

    # Retrieving the %appdata% path on Windows or the Share folder on macOS or Unix systems
    def get_appdata_directory(self):
        
        if os.name == 'nt':
            return os.getenv('APPDATA')
        else:
            return os.path.expanduser('~/.local/share')

    # Writing the user's search details into a JSON file
    def save_data(self, tags_list, urls_list):
        
        data = {
            'tags': tags_list,
            'urls': urls_list
        }

        with open(self.data_file, "w") as file:
            json.dump(data, file)

        messagebox.showinfo("Info", "Entries saved successfully")

    # Reading the saved user's search details from a JSON file 
    def load_data(self):

        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                data = json.load(file)
        else:
            data = {'tags':[], 'urls':[]}

        return data