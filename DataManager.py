from tkinter import messagebox
import json
import os

class DataManager:
    def __init__(self):
        self.appdata_dir = self.get_appdata_directory()
        self.data_file = os.path.join(self.appdata_dir, "profile.json")

    def get_appdata_directory(self):
        if os.name == 'nt':
            return os.getenv('APPDATA')
        else:
            return os.path.expanduser('~/.local/share')

    def save_data(self, tags_list, urls_list):
        data = {
            'tags': tags_list,
            'urls': urls_list
        }

        with open(self.data_file, "w") as file:
            json.dump(data, file)

        messagebox.showinfo("Info", "Entries saved successfully")

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                data = json.load(file)
        else:
            data = {'tags':[], 'urls':[]}

        return data
    
    def delete_profile(self):
        os.remove(f"{self.data_file}")