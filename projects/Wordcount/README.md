# 📊 Word Count - Text Frequency Analyzer

A sophisticated text analysis tool that processes text/lyrics and generates word frequency statistics with sorting and visualization.

## 📋 Description

This project analyzes text content (such as song lyrics) and generates detailed word frequency information. It processes the text to count word occurrences, remove duplicates, and display statistics in various sorted formats.

## ✨ Features

- **Word Frequency Analysis** - Count occurrences of each word
- **Text Preprocessing** - Handle case normalization and cleaning
- **Multiple Sorting Options** - Sort by frequency or alphabetically
- **Statistical Output** - Display word counts and percentages
- **Duplicate Removal** - Identify unique words
- **Flexible Input** - Works with any text or lyrics

## 🛠 Prerequisites

- Python 3.x (uses standard library)

## 📦 Installation

No external dependencies required! The project uses Python's standard library:
- `operator` module for sorting

```bash
python wordcount.py
```

## 🚀 Usage

The script contains sample lyrics that are analyzed by default. You can modify the `full_text` variable in the code to analyze different text:

```python
full_text = '''
Your text here...
'''
```

Run the script:
```bash
python wordcount.py
```

## 📁 Files

- `wordcount.py` - Main application file

## 🔧 Key Components

### Text Analysis
```python
import _operator
# Text processing and word extraction
words = full_text.split()
# Count occurrences
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
```

### Sorting
- Sort by frequency (most common words first)
- Sort alphabetically (A-Z order)
- Display top N words

## 💡 Learning Concepts

- **String Manipulation** - Processing and cleaning text
- **Dictionaries** - Storing word-frequency pairs
- **Sorting** - Using operator module for custom sorting
- **Data Analysis** - Extracting patterns from text
- **File Operations** - Reading and analyzing text files
- **Regular Expressions** - Pattern matching for text cleaning
- **Statistical Analysis** - Word frequency distributions

## 📊 Output Example

```
Word Frequency Analysis
========================

Total Words: 287
Unique Words: 45
Average Frequency: 6.4

Top 10 Most Common Words:
1. the        - 28 occurrences (9.8%)
2. and        - 21 occurrences (7.3%)
3. to         - 15 occurrences (5.2%)
4. a          - 14 occurrences (4.9%)
...

Alphabetical Word List:
a - 14
about - 3
after - 2
...
```

## 📝 Sample Analysis

### Lyrics Example
Input: Song lyrics from "Baby" by Justin Bieber

Output includes:
- Word frequency distribution
- Repeated words
- Unique vocabulary count
- Statistical analysis

## ⚠️ Notes

- Case sensitivity can be controlled (uppercase vs lowercase)
- Punctuation handling depends on text preprocessing
- Empty strings and whitespace are handled
- Works best with larger text samples for meaningful statistics

## 🌟 Potential Enhancements

- [ ] Remove stop words (the, and, a, etc.)
- [ ] N-gram analysis (word pairs, phrases)
- [ ] Sentiment analysis
- [ ] Visualize with matplotlib (bar charts, word clouds)
- [ ] Export to CSV/JSON
- [ ] Compare multiple texts
- [ ] Readability metrics (Flesch-Kincaid)
- [ ] Text processing from files or URLs
- [ ] Web interface for analysis
- [ ] Natural Language Processing integration

## 📚 Related Topics

- Text Processing and Analysis
- Natural Language Processing (NLP)
- Data Visualization
- Statistical Analysis
- File I/O Operations
- Dictionary and List Operations
- Sorting Algorithms

## 🎯 Use Cases

1. **Content Analysis** - Understand writing style
2. **Language Learning** - Vocabulary frequency
3. **SEO Analysis** - Keyword frequency
4. **Literary Analysis** - Word patterns in literature
5. **Topic Modeling** - Identify main themes
6. **Plagiarism Detection** - Compare texts
7. **Readability Assessment** - Text complexity analysis

## 📖 Extensions You Could Try

### Stop Word Removal
Filter out common words (the, and, a, etc.) for more meaningful analysis

### Word Cloud Generation
Use matplotlib or PIL to create visual word clouds

### Sentiment Analysis
Determine positive/negative sentiment by word choice

### Comparative Analysis
Compare word frequency across multiple texts

### N-Gram Analysis
Find common word combinations and phrases

## 💻 Example: Using with Different Text

```python
# Analyze a file
with open('document.txt', 'r') as f:
    full_text = f.read()

# Or analyze from web content
import requests
url = 'http://example.com'
response = requests.get(url)
full_text = response.text
```

## 📈 Performance Tips

- Pre-process large texts for better performance
- Use sets for faster duplicate checking
- Consider chunking very large documents
- Cache results for repeated analysis

---

**Perfect for:** Text analysis projects, NLP learning, content research, literary analysis
