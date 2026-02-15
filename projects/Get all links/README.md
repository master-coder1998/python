# 🔗 Get All Links - Web Link Extractor

A simple web scraper that extracts all hyperlinks from a given website and displays them.

## 📋 Description

This project takes a URL as input and extracts all the hyperlinks found on that webpage. It uses BeautifulSoup to parse HTML and automatically handles URL formatting (adding https:// if needed).

## ✨ Features

- **URL Input Validation** - Automatically adds protocol if missing
- **Link Extraction** - Finds all hyperlinks on a webpage
- **Smart URL Handling** - Detects and handles http/https protocols
- **Simple Interface** - Interactive command-line prompts
- **Error Handling** - Manages network requests gracefully

## 🛠 Prerequisites

```bash
pip install requests beautifulsoup4
```

## 📦 Installation

1. Install required dependencies:
```bash
pip install requests beautifulsoup4
```

2. Run the script:
```bash
python "Get all links.py"
```

## 🚀 Usage

```bash
python "Get all links.py"
```

When prompted, enter a website URL:
```
Enter Link: google.com
```

Or with the protocol included:
```
Enter Link: https://www.google.com
```

The script will:
1. Fetch the webpage content
2. Parse the HTML
3. Extract all hyperlinks
4. Display the list of links

## 📁 Files

- `Get all links.py` - Main application file

## 🔧 Key Components

### URL Processing
```python
if ("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)
```
- Checks if protocol is included
- Adds https:// by default if missing

### Link Extraction
```python
soup = BeautifulSoup(data.text, "html.parser")
links = []
# Extracts all <a> tags to get links
```

## 💡 Learning Concepts

- **Web Scraping** - Fetching and parsing web content
- **HTML Parsing** - Using BeautifulSoup to navigate DOM
- **HTTP Requests** - Making requests with requests library
- **String Operations** - URL validation and formatting
- **List Operations** - Storing and managing extracted data
- **User Input** - Interactive command-line interface

## 📝 Output Example

```
https://www.google.com/search?q=python
https://www.google.com/intl/en/about/
https://www.google.com/intl/en/policies/privacy/
...
```

## ⚠️ Notes

- Works with both http and https protocols
- Automatic protocol detection for input URLs
- Requires active internet connection
- May encounter robots.txt restrictions on some sites
- Relative links are extracted as provided

## 🌟 Potential Enhancements

- [ ] Filter links by type (internal/external)
- [ ] Remove duplicate links
- [ ] Follow redirects
- [ ] Validate URLs for accessibility
- [ ] Export links to file (CSV, JSON)
- [ ] Build a link graph/tree structure
- [ ] Add recursive scraping (follow links)
- [ ] Implement link checking (404 detection)
- [ ] Add timeout and retry logic
- [ ] Support for JavaScript-rendered content

## 📚 Related Topics

- Web Scraping Fundamentals
- HTML/CSS Selectors
- HTTP Protocol
- Data Extraction and Processing
- File Export Formats (JSON, CSV)

## 🔒 Ethical Considerations

- Always check `robots.txt` before scraping
- Respect website terms of service
- Add delays between requests to avoid overloading servers
- Identify your scraper with proper User-Agent headers
