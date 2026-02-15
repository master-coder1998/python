# 📰 Daily News Feeds Scraper

A web scraper that fetches the latest news from Hacker News and saves it to organized text files.

## 📋 Description

This project fetches news articles from Hacker News (https://news.ycombinator.com) and extracts detailed information including article rank, title, source, URL, author, score, and posting time. The data is saved to text files organized by page number.

## ✨ Features

- **Multi-page Scraping** - Fetch up to 20 pages of Hacker News
- **Detailed Extraction** - Extracts rank, title, source, URL, author, score, and timestamp
- **Error Handling** - Gracefully handles connection errors and exceptions
- **Organized Output** - Creates HackerNews folder with separate files for each page
- **Verbose Mode** - Optional console output for progress tracking
- **Input Validation** - Limits maximum pages to 20 and validates user input

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
python "Daily news feeds.py"
```

## 🚀 Usage

```bash
python "Daily news feeds.py"
```

When prompted:
```
Enter number of pages that you want the HackerNews for (max 20): 5
Want verbose output y/[n] ?: y
```

The script will:
1. Create a `HackerNews` folder in the current directory
2. Fetch 5 pages of news from Hacker News
3. Save each page to `NewsPageX.txt` format
4. Display progress if verbose mode is enabled

## 📁 Files

- `Daily news feeds.py` - Main scraper application
- `HackerNews/` - Output directory (created automatically)
  - `NewsPage1.txt`
  - `NewsPage2.txt`
  - ... and so on

## 📊 Output Format

Each text file contains formatted article information:

```
────────────────────────────────────────────────────────────────────────────────
Page 1
────────────────────────────────────────────────────────────────────────────────

Article Number: 1
Article Title: [Title of the article]
Source Website: [Domain name]
Source URL: [Full URL to article]
Article Author: [Author name]
Article Score: [Score with points]
Posted: [Time ago]
────────────────────────────────────────────────────────────────────────────────
```

## 🔧 Key Functions

### `fetch(page_no, verbose=False)`
- **Parameters:**
  - `page_no` - Page number to fetch (1-20)
  - `verbose` - Enable console output (optional)
- **Functionality:**
  - Fetches HTML from Hacker News
  - Parses and extracts article data
  - Saves to text file with error handling

## 💡 Learning Concepts

- **Web Scraping** - Using BeautifulSoup for HTML parsing
- **HTTP Requests** - Making requests with requests library
- **HTML Parsing** - Extracting specific elements from DOM
- **File I/O** - Writing data to files
- **Error Handling** - Managing network exceptions
- **Data Extraction** - Finding and formatting data

## ⚠️ Notes

- Maximum of 20 pages can be fetched
- Uses CSS class selectors to find articles
- Handles both HTTPS and relative URLs
- Connection errors are logged to console
- Invalid input triggers re-prompt

## 🌟 Potential Enhancements

- [ ] Add filtering by category or score threshold
- [ ] Implement database storage (SQLite)
- [ ] Schedule automatic daily scraping
- [ ] Export to JSON/CSV format
- [ ] Build a simple web interface
- [ ] Add duplicate detection
- [ ] Implement parallel scraping with multiprocessing

## 📚 Related Topics

- Web Scraping and Data Extraction
- HTML/CSS Selectors
- HTTP Requests and APIs
- File Operations
- Error Handling
- Data Processing and Formatting

## 📈 Potential Improvements

1. **Multiprocessing** - Mentioned in comments as a future feature
2. **Caching** - Store fetched data to avoid redundant requests
3. **Real-time Updates** - Push notifications for new articles
4. **Analytics** - Track trending topics and authors
