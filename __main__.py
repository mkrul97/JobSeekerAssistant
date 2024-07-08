import Scraper
from DataManager import DataManager
from TagsModule import TagsModule
from UrlsModule import UrlsModule
import tkinter as tk

def scrape(tags, urls):
    result = {}

    for url in urls:    
        ws = Scraper.WebScraper(headless=True)
        links = ws.scrape(url, tags)

        for key, value in links.items():
            
            result.update({key: value})
    
    for key, value in result.items():
        print(key.replace("\n", "") + ": " + value)

if __name__ == "__main__":

    data_manager = DataManager()

    root = tk.Tk()
    root.title("Job Seeker Assistant")
    root.geometry("800x600")

    main_frame = tk.Frame(root)
    main_frame.pack()

    tags_module = TagsModule(main_frame)

    urls_module = UrlsModule(main_frame)

    save_button = tk.Button(text="Save", command=lambda: data_manager.save_data(tags_module.return_tags(), urls_module.return_urls()))
    save_button.pack()

    scraper_button = tk.Button(text="Find Jobs", command=lambda: scrape(tags_module.return_tags(), urls_module.return_urls()))
    scraper_button.pack()

    root.mainloop()