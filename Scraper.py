from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import time
import re

class WebScraper:
    def __init__(self, headless=True):
        self.headless = headless
        self.driver = self.setup_driver()

    def setup_driver(self):
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    
    def get_source_page(self, url):
        self.driver.get(url)
        time.sleep(5)
        self.click_show_more_buttons()
        page_source = self.driver.page_source
        return page_source
    
    def click_show_more_buttons(self):
        try:
            while True:
                show_more_buttons = self.driver.find_elements("class name", "show-more")
                if not show_more_buttons:
                    break
                for button in show_more_buttons:
                    try:
                        a_tag = button.find_element("tag name", "a")
                        if a_tag:
                            self.driver.execute_script("arguments[0].click();", a_tag)
                            time.sleep(2)  # Wait for content to load
                    except Exception as e:
                        print(f"Error clicking show more button: {e}")
        except Exception as e:
            print(f"No more 'show more' buttons to click or an error occurred: {e}")
    
    def parse_links(self, page_source, base_url, tags):
        soup = BeautifulSoup(page_source, 'html.parser')
        list_all_a = soup.find_all('a')
        
        links = {}
        text_counts = {}

        for tag in tags:
            for a_tag in list_all_a:
                text = str(a_tag.get_text()).strip()
                href = str(a_tag.get('href')).strip()
                
                if self.match_tags(tag)(href) or self.match_tags(tag)(text):
                    if href.startswith('http'):
                        full_url = href
                    else:
                        full_url = urljoin(base_url, href)
                    
                    # Manage adding a number suffix to text if needed
                    if text in links:
                        # Check if the exact (text, href) pair is already in links
                        if any(full_url == v for k, v in links.items() if k == text):
                            continue  # Skip adding if the exact pair already exists
                        else:
                            # Add a number suffix to text if href is different
                            if text in text_counts:
                                text_counts[text] += 1
                            else:
                                text_counts[text] = 1
                            links[f"{text}{text_counts[text]}"] = full_url
                    else:
                        links[text] = full_url

        return links

    def scrape(self, url, tags):
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"  # Extract base URL
        page_source = self.get_source_page(url)
        links = self.parse_links(page_source, base_url, tags)
        self.driver.quit()
        return links
       
    def match_tags(self, tag):
        return re.compile(r'\b({0})\b'.format(tag), flags=re.IGNORECASE).search
    