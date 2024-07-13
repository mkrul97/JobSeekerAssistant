# Job Seeker Assistant

Job Seeker Assistant is a Python application that helps users search for job offers by scraping specified websites using provided tags and URLs.

## Features

- **GUI**: Provides a graphical interface for easy interaction.
- **Web Scraping**: Scrapes websites to find job titles and links based on user-provided tags and URLs.
- **Save and Load Searches**: Allows users to save their search configurations for future use and load them on launch.

## Technologies

- Python
- Selenium

## How to Use

1. Clone the repository:
   ```
   git clone https://github.com/mkrul97/JobSeekerAssistant.git
   ```

2. Navigate into the directory:
   ```
   cd JobSeekerAssistant
   ```

3. Install dependencies (if any) using:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python __main__.py
   ```

5. Follow these steps within the GUI:
   - Add up to 5 tags to specify job types or categories.
   - Add up to 20 websites URLs where job offers should be searched.
   - Save your search details for later use.
   - Press 'Start' to initiate the job search.
   - Wait until the output window displays the results.

## Known Issues

- **Website Compatibility**: Some websites may not be compatible with the application due to their specific structure, anti-scraping measures, or terms of service prohibiting automated access to their content.

- **Application Unresponsiveness**: When starting the scraping process, the application may become unresponsive until the job is done. This is due to the nature of the scraping tasks being performed synchronously. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

**Disclaimer**: Some websites may prohibit or restrict automated scraping of their content. It is recommended to review and comply with the terms of service of each website before using this tool for scraping.
