# 📊 Word Counter - Text Analysis Tool

A sophisticated word frequency analyzer that processes text, cleans it, and generates detailed word statistics sorted by frequency.

## 📝 Description

This tool analyzes song lyrics (or any text) to count word occurrences, identify unique words, and display frequency statistics. It demonstrates text processing, data cleaning, and dictionary manipulation in Python.

## ✨ Features

- **Text Preprocessing**: Removes special characters and brackets
- **Case Normalization**: Converts all text to lowercase for accurate counting
- **Word Frequency Analysis**: Counts occurrences of each word
- **Sorted Output**: Displays words from most to least frequent
- **Statistics**: Shows total unique word count
- **Formatted Display**: Clean, readable output with word/count pairs

## 🚀 How It Works

### Processing Pipeline

1. **Text Input**: Large text block (song lyrics in example)
2. **Character Removal**: Remove brackets, quotes, newlines
3. **Normalization**: Convert to lowercase
4. **Tokenization**: Split into individual words
5. **Counting**: Build frequency dictionary
6. **Sorting**: Order by frequency (descending)
7. **Output**: Display formatted results

### Algorithm

```python
# 1. Remove special characters
for char in remove_chars:
    full_text = full_text.replace(char, ' ')

# 2. Tokenize and normalize
word_list = full_text.lower().split()

# 3. Count frequencies
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# 4. Sort by frequency
sorted_word_count = dict(sorted(word_count.items(), 
                               key=operator.itemgetter(1), 
                               reverse=True))
```

## 💻 Usage

### Run the Script

```bash
python wordcount.py
```

### Customize the Text

Replace the `full_text` variable with your own content:

```python
full_text = '''
Your text here
Can be multiple lines
Song lyrics, articles, etc.
'''
```

### Sample Output

```
['baby', 'baby', 'baby', 'oh', 'like', 'baby', ...]

there are 87 unique words in the text.
word: "BABY", count: 54
word: "I", count: 31
word: "YOU", count: 28
word: "MY", count: 18
word: "AND", count: 17
...
```

## 🎮 Code Breakdown

### Imports
```python
import operator  # For sorting dictionary by values
```

### Text Cleaning
```python
# Characters to remove
remove_chars = ['[', ']', '(', ')', '\n', '"', "'", '?']

# Remove each character
for char in remove_chars:
    full_text = full_text.replace(char, ' ')
```

### Word Processing
```python
# Convert to lowercase and split into words
word_list = full_text.lower().split()
```

### Frequency Counting
```python
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1  # Increment existing
    else:
        word_count[word] = 1   # Initialize new
```

### Sorting by Frequency
```python
sorted_word_count = dict(
    sorted(word_count.items(), 
           key=operator.itemgetter(1),  # Sort by value (count)
           reverse=True)                 # Highest first
)
```

### Output
```python
print(f'there are {len(sorted_word_count)} unique words in the text.')

for word_tuple in sorted_word_count.items():
    print(f'word: "{word_tuple[0].upper()}", count: {word_tuple[1]}')
```

## 🎯 Learning Concepts

This project demonstrates:

- **String Methods**: `replace()`, `lower()`, `split()`
- **Lists**: Building and iterating
- **Dictionaries**: Key-value storage and manipulation
- **Conditionals**: Checking key existence
- **Sorting**: Using `sorted()` with custom keys
- **Operator Module**: `itemgetter()` for tuple access
- **f-strings**: Advanced formatting
- **Iteration**: Looping through dictionary items

## 🔧 Enhancement Ideas

### 1. Ignore Common Words (Stop Words)
```python
stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at'}

word_count = {}
for word in word_list:
    if word not in stop_words:  # Skip stop words
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
```

### 2. Read from File
```python
def analyze_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        full_text = f.read()
    # Process as before...
```

### 3. Export Results
```python
import json

with open('word_count.json', 'w') as f:
    json.dump(sorted_word_count, f, indent=2)
```

### 4. Visualization
```python
import matplotlib.pyplot as plt

# Get top 10 words
top_10 = dict(list(sorted_word_count.items())[:10])

plt.bar(top_10.keys(), top_10.values())
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Frequent Words')
plt.xticks(rotation=45)
plt.show()
```

### 5. Advanced Statistics
```python
def text_statistics(word_count):
    total_words = sum(word_count.values())
    unique_words = len(word_count)
    avg_frequency = total_words / unique_words
    
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print(f"Average frequency: {avg_frequency:.2f}")
```

### 6. Command-Line Arguments
```python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        full_text = f.read()
else:
    # Use default text
    full_text = '''...'''
```

## 📊 Use Cases

- **Lyric Analysis**: Find most repeated words in songs
- **Document Analysis**: Identify key terms in articles
- **Code Analysis**: Find common variable names
- **SEO**: Analyze keyword density
- **Literature Study**: Examine word usage in books
- **Social Media**: Analyze trending topics

## 🐛 Potential Improvements

### Better Word Boundary Detection
```python
import re

# Use regex for better word extraction
word_list = re.findall(r'\b[a-zA-Z]+\b', full_text.lower())
```

### Handle Contractions
```python
# Expand contractions before counting
contractions = {
    "don't": "do not",
    "can't": "cannot",
    "won't": "will not"
}

for contraction, expansion in contractions.items():
    full_text = full_text.replace(contraction, expansion)
```

### Stemming/Lemmatization
```python
# Requires nltk library
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
word_list = [stemmer.stem(word) for word in word_list]
```

## 📚 Dependencies

**Current:**
- `operator` (built-in)

**For Enhancements:**
```bash
pip install nltk          # Natural language processing
pip install matplotlib    # Visualization
pip install wordcloud     # Word cloud generation
```

## 🎓 Educational Value

Perfect for learning:
- Text processing fundamentals
- Dictionary operations
- Sorting complex data structures
- Data cleaning techniques
- Frequency analysis
- String manipulation

## 🔍 Sample Analysis

**Input**: "Baby" by Justin Bieber (lyrics)

**Key Findings**:
- Most frequent word: "baby" (54 times)
- Second most: "I" (31 times)
- Total unique words: 87
- Demonstrates repetitive chorus structure

## 📝 License

Part of the personal learning repository. Feel free to use and modify!

## 🚀 Next Steps

1. Add GUI with Tkinter
2. Support multiple file formats (PDF, DOCX)
3. Build word cloud visualization
4. Add sentiment analysis
5. Create web interface with Flask
6. Compare multiple documents
7. Export to various formats (CSV, JSON, HTML)

---

**Made with ❤️ for text analysis enthusiasts!** 📖