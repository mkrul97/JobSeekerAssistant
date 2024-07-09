import tkinter as tk
from tkinter import font
import webbrowser
import Scraper

class OutputWindow:
    def __init__(self, tags, urls):
        
        self.job_offers = {}
        self.tags = tags
        self.urls = urls

        self.popup = tk.Toplevel()
        self.popup.title("Job Offers")

        self.get_job_offers()
        self.print_job_offers()
        
    def get_job_offers(self):
        
        for url in self.urls:    
            ws = Scraper.WebScraper(headless=True)
            links = ws.scrape(url, self.tags)

            for key, value in links.items():
                
                self.job_offers.update({key: value})
            
    def print_job_offers(self):
        header_font = font.Font(family="Helvetica", size=12, weight="bold")
        link_font = font.Font(family="Helvetica", size=11)
        separator_font = font.Font(family="Helvetica", size=9)

        for key, value in self.job_offers.items():
            job_header = tk.Label(self.popup, text=f"{key.replace("\n", "")}", font=header_font)
            job_link = tk.Label(self.popup, text=value, font=link_font)
            separator = tk.Label(self.popup, text="------------", font=separator_font, fg="grey")
            
            job_header.pack()
            job_link.pack()
            separator.pack()

            job_link.bind("<Enter>", lambda e, lbl=job_link: lbl.config(font=('Helvetica', 11, 'underline')))
            job_link.bind("<Leave>", lambda e, lbl=job_link: lbl.config(font=('Helvetica', 11, 'normal')))
            job_link.bind("<Button-1>", lambda e, url=value: webbrowser.open(url))
