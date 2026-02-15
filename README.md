# 🐍 Python Learning Journey

> From basics to practical projects - a hands-on Python learning experience

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 👨‍💻 About

This repository documents my journey learning Python from scratch. It's structured as both a learning resource and a portfolio of practical projects, progressing from fundamental concepts to real-world applications.

## 📁 Repository Structure

```
python/
├── README.md                  # This file
├── basics/                    # Python fundamentals overview
│   └── README.md             # Detailed guide to basics
├── fundamentals/             # Core Python concepts with examples
│   ├── dictonaries           # Dictionary examples
│   ├── functions             # Function basics
│   ├── lists                 # List operations
│   ├── loops                 # Loop examples
│   ├── parameters            # Function parameters
│   └── README.md             # Guide to intermediate topics
└── projects/                 # Practical applications
    ├── Pickalator/           # Cricket match predictor project
    │   ├── Pickalator.md    # Project documentation
    │   └── Pickalator.py    # Main application
    └── Wordcount/            # Text frequency analyzer project
        ├── Word Counter.md   # Project documentation
        └── wordcount.py      # Main application
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/master-coder1998/python.git
cd python
```

### 2. Set Up Python Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*Note: Current projects use only Python's standard library, so no external packages are required yet.*

## 📚 Learning Path

### 📖 Stage 1: Python Basics (`basics/`)

Foundational Python concepts with hands-on examples.

**Topics Covered:**
- **Variables & Data Types** - Understanding Python's type system
- **Dictionaries** - Key-value pair operations and dynamic building
- **Functions** - Creating reusable code blocks
- **Lists** - Working with ordered collections
- **Loops** - Iteration patterns and control flow
- **Parameters** - Passing data to functions

**Quick Start:**
```bash
cd fundamentals
python dictonaries
python functions
python lists
python loops
python parameters
```

**📘 See [basics/README.md](basics/README.md) for detailed explanations and examples.**

---

### 🔧 Stage 2: Fundamentals (`fundamentals/`)

Intermediate Python concepts and best practices (planned content).

**Planned Topics:**
- List and dictionary comprehensions
- Object-oriented programming
- File I/O and data processing
- Error handling and exceptions
- Modules and packages
- Decorators and generators

**📘 See [fundamentals/README.md](fundamentals/README.md) for learning roadmap.**

---

### 🎯 Stage 3: Projects (`projects/`)

Real-world applications demonstrating Python concepts in action.

#### 🏏 Pickalator - Cricket Match Predictor

A fun prediction tool that calculates team winning probabilities based on rankings with randomization.

**Features:**
- Team ranking algorithm
- Random chance factor
- Suspenseful output with delays
- Probability visualization

**Files:**
- [Pickalator.md](projects/Pickalator/Pickalator.md) - Project documentation and details
- [Pickalator.py](projects/Pickalator/Pickalator.py) - Main application

**Usage:**
```bash
python projects/Pickalator/Pickalator.py
```

**Key Concepts:** Variables, arithmetic, random module, time delays, conditionals, f-strings

---

#### 📊 Word Counter - Text Frequency Analyzer

Sophisticated text analysis tool that processes lyrics/text and generates word frequency statistics.

**Features:**
- Text preprocessing and cleaning
- Case-insensitive word counting
- Frequency-based sorting
- Statistical output

**Files:**
- [Word Counter.md](projects/Wordcount/Word%20Counter.md) - Project documentation and details
- [wordcount.py](projects/Wordcount/wordcount.py) - Main application
- [README.md](projects/Wordcount/README.md) - Complete project guide

**Usage:**
```bash
python projects/Wordcount/wordcount.py
```

**Key Concepts:** String manipulation, dictionaries, sorting, operator module, data processing

---

#### 🎮 Rock Paper Scissors - Interactive Game

Play the classic Rock, Paper, Scissors game against a computer opponent over multiple rounds.

**Features:**
- Multi-round gameplay with score tracking
- Smart input handling (accepts full words or single letters)
- Real-time score updates
- Input validation
- Random computer AI

**Files:**
- [README.md](projects/Rock%20Paper%20Scissors/README.md) - Project guide
- [Rock Paper Scissors.py](projects/Rock%20Paper%20Scissors/Rock%20Paper%20Scissors.py) - Main game

**Usage:**
```bash
python projects/"Rock Paper Scissors.py"
```

**Key Concepts:** Random module, conditional logic, loops, input validation, dictionaries

---

#### 🔐 Hashing Password - Password Hash Generator

Command-line utility for generating cryptographic hashes of passwords using SHA-256, SHA-512, or MD5.

**Features:**
- Multiple hash algorithms (SHA-256, SHA-512, MD5)
- Command-line argument parsing
- Secure default algorithm
- Hexadecimal output
- Simple and secure password hashing

**Files:**
- [README.md](projects/Hashing%20Password/README.md) - Complete documentation
- [Hashing Password.py](projects/Hashing%20Password/Hashing%20Password.py) - Main application

**Usage:**
```bash
python "Hashing Password.py" mypassword -t sha256
```

**Key Concepts:** Cryptography, hashlib module, argparse, command-line tools

---

#### 🔗 Get All Links - Web Link Extractor

Web scraper that extracts all hyperlinks from a given website and displays them.

**Features:**
- URL input validation with protocol detection
- Extracts all hyperlinks from webpage
- Automatic https:// protocol handling
- Simple command-line interface
- Error handling for network issues

**Files:**
- [README.md](projects/Get%20all%20links/README.md) - Project documentation
- [Get all links.py](projects/Get%20all%20links/Get%20all%20links.py) - Main scraper

**Usage:**
```bash
python "Get all links.py"
# Enter URL: google.com
```

**Key Concepts:** Web scraping, BeautifulSoup, HTTP requests, HTML parsing

---

#### 📰 Daily News Feeds - Hacker News Scraper

Web scraper that fetches the latest news from Hacker News and saves organized article data to text files.

**Features:**
- Multi-page scraping (up to 20 pages)
- Detailed article extraction (title, URL, author, score, timestamp)
- Organized file output with HackerNews folder
- Error handling and connection management
- Optional verbose output mode

**Files:**
- [README.md](projects/Daily%20news%20feeds/README.md) - Full documentation
- [Daily news feeds.py](projects/Daily%20news%20feeds/Daily%20news%20feeds.py) - Main scraper

**Usage:**
```bash
python "Daily news feeds.py"
# Enter pages: 5
# Verbose mode: y
```

**Key Concepts:** Web scraping, BeautifulSoup, requests, file I/O, error handling

---

#### 🔐 CAPTCHA - Verification System

CAPTCHA image generator with GUI for user verification using Tkinter.

**Features:**
- Random 6-digit CAPTCHA generation
- Graphical user interface with Tkinter
- Image verification against input
- Refresh functionality
- Visual feedback with message boxes

**Files:**
- [README.md](projects/Captcha/README.md) - Complete guide
- [Captcha.py](projects/Captcha/Captcha.py) - Main application

**Usage:**
```bash
python projects/Captcha/Captcha.py
```

**Prerequisites:**
```bash
pip install captcha
```

**Key Concepts:** GUI development with Tkinter, image generation, event handling, file I/O

---

## 🎯 Learning Goals

### Completed ✅
- [x] Master Python syntax and fundamentals
- [x] Understand data structures (lists, dictionaries)
- [x] Create functions with parameters
- [x] Build working mini-projects
- [x] Text processing and analysis
- [x] Algorithm implementation

### In Progress 🚧
- [ ] Object-oriented programming
- [ ] File I/O operations
- [ ] Error handling best practices
- [ ] Code organization and modules

### Planned 📋
- [ ] Build web applications with Flask
- [ ] Data analysis with pandas
- [ ] API integration and web scraping
- [ ] Database operations
- [ ] Testing with pytest
- [ ] Command-line tools

## 📊 Current Projects

| Project | Status | Description | Key Skills |
|---------|--------|-------------|------------|
| Dictionary Examples | ✅ Complete | Key-value operations | Dictionaries, loops |
| Function Basics | ✅ Complete | Function creation | Functions, scope |
| List Operations | ✅ Complete | List manipulation | Lists, methods |
| Loop Patterns | ✅ Complete | Iteration techniques | For loops, ranges |
| Pickalator | ✅ Complete | Match predictor | Random, conditionals |
| Word Counter | ✅ Complete | Text analyzer | Dicts, sorting, strings |

## 🔮 Future Project Ideas

- **To-Do List Manager** - CLI task tracker with file persistence
- **File Organizer** - Automated file sorting by type/date
- **Weather App** - API integration with weather services
- **Web Scraper** - Extract data from websites
- **Budget Tracker** - Personal finance manager
- **Quiz Game** - Interactive learning application
- **Password Generator** - Secure random password creator
- **Markdown Converter** - Convert markdown to HTML

## 📚 Learning Resources

### Python Fundamentals
- [Official Python Tutorial](https://docs.python.org/3/tutorial/) - Comprehensive official guide
- [Real Python](https://realpython.com/) - In-depth tutorials and articles
- [Python for Everybody](https://www.py4e.com/) - Beginner-friendly course
- [Automate the Boring Stuff](https://automatetheboringstuff.com/) - Practical automation

### Practice Platforms
- [LeetCode](https://leetcode.com/) - Algorithm challenges
- [HackerRank](https://www.hackerrank.com/) - Coding practice
- [Codecademy](https://www.codecademy.com/learn/learn-python-3) - Interactive lessons
- [Project Euler](https://projecteuler.net/) - Mathematical problems

### Style & Best Practices
- [PEP 8](https://pep8.org/) - Python style guide
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/) - Best practices
- [Clean Code in Python](https://www.packtpub.com/product/clean-code-in-python/9781800560215) - Writing maintainable code

## 💡 Learning Tips

1. **Practice Daily** - Code for at least 30 minutes every day
2. **Build Projects** - Apply concepts in real applications
3. **Read Code** - Study well-written open-source projects
4. **Debug Actively** - Learn to troubleshoot effectively
5. **Write Tests** - Practice writing unit tests
6. **Document Code** - Write clear comments and docstrings
7. **Join Communities** - Participate in Python forums and discussions

## 🤝 Contributing

This is a personal learning repository, but I welcome:

- 🐛 Bug reports and fixes
- 💡 Suggestions for improvements
- 📚 Learning resource recommendations
- 🔄 Pull requests with enhancements

Feel free to open an issue or submit a PR!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Master Coder**
- Learning Focus: Python Programming & Software Development
- GitHub: [@master-coder1998](https://github.com/master-coder1998)
- Goal: Build practical skills through hands-on projects

## 📈 Progress Tracker

| Week | Focus Area | Status | Notes |
|------|------------|--------|-------|
| 1-2 | Python Basics | ✅ Complete | Variables, lists, dicts, functions |
| 3 | Mini Projects | ✅ Complete | Pickalator, Word Counter |
| 4 | OOP Concepts | 📋 Planned | Classes, inheritance |
| 5-6 | File Operations | 📋 Planned | Reading, writing, CSV, JSON |
| 7-8 | Web Development | 📋 Planned | Flask basics |
| 9+ | Advanced Projects | 📋 Planned | Real-world applications |

---

## 🌟 Highlights

### What Makes This Repository Useful?

- **Structured Learning** - Clear progression from basics to advanced
- **Practical Examples** - Real code you can run and modify
- **Detailed Documentation** - Comprehensive README files for each section
- **Project-Based** - Learning through building actual applications
- **Beginner-Friendly** - Clear explanations and commented code
- **Active Development** - Continuously adding new projects and concepts

---

**Last Updated:** January 26, 2026

⭐ **If you find this repository helpful for your Python learning journey, consider giving it a star!**

💬 **Questions or suggestions?** Open an issue or reach out!

🚀 **Happy Coding!**