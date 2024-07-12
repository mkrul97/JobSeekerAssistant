import tkinter as tk
from tkinter import font
import webbrowser
import Scraper

class OutputWindow:
    # Displaying a popup window with hyperlinks to the found job offers
    def __init__(self, tags, urls):
        
        self.job_offers = {}  # Storing the job title and link to the offer
        self.tags = tags
        self.urls = urls

        self.popup = tk.Toplevel()
        self.popup.title("Job Offers")

        self.get_job_offers()
        self.print_job_offers()
    
    # Retrieving job offers from links provided by the user and adding them to the dictionary
    def get_job_offers(self):
        
        for url in self.urls:    
            ws = Scraper.WebScraper(headless=True)
            links = ws.scrape(url, self.tags)

            for key, value in links.items():
                
                self.job_offers.update({key: value})

    # Displaying job titles as headers with hyperlinks to the offers and separators between them      
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
