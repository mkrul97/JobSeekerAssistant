from DataManager import DataManager
from TagsModule import TagsModule
from UrlsModule import UrlsModule
import tkinter as tk
import Output

if __name__ == "__main__":

    data_manager = DataManager()

    root = tk.Tk()
    root.title("Job Seeker Assistant")
    root.geometry("360x400")
    root.resizable(False, False)

    main_frame = tk.Frame(root)
    main_frame.pack()

    tags_frame = tk.Frame(main_frame)
    tags_frame.pack(pady=10)
    tags_module = TagsModule(tags_frame)

    urls_frame = tk.Frame(main_frame)
    urls_frame.pack(pady=10)
    urls_module = UrlsModule(urls_frame)

    buttons_frame = tk.Frame(main_frame)
    buttons_frame.pack()

    scraper_button = tk.Button(buttons_frame, text="Find Jobs", command=lambda: Output.OutputWindow(tags_module.return_tags(), urls_module.return_urls()))
    scraper_button.pack(side=tk.RIGHT, padx=5)

    save_button = tk.Button(buttons_frame, text="Save", command=lambda: data_manager.save_data(tags_module.return_tags(), urls_module.return_urls()))
    save_button.pack(side=tk.RIGHT, padx=5)

    root.mainloop()