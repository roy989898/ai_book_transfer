# 📚 EPUB Language Level Transfer

Transform any EPUB book into different English proficiency levels using AI! Perfect for language learners who want to enjoy their favorite books while improving their English skills.

## ✨ Features

- 🔄 **Smart Text Processing**: Converts EPUB files to different English proficiency levels (A1, A2, B1, B2, C1, C2)
- 🧠 **AI-Powered Translation**: Uses advanced AI models to maintain story coherence while adjusting language complexity
- 📖 **EPUB Support**: Handles standard EPUB format with proper HTML content extraction
- 🌐 **Multi-language Support**: Special handling for Chinese text with custom sentence tokenization
- ⚡ **Token-Aware Chunking**: Intelligently splits text while preserving sentence boundaries
- 📝 **Clean Output**: Generates processed text files ready for reading

## 🚀 Quick Start

### Prerequisites

```bash
pip install ebooklib beautifulsoup4 nltk tiktoken requests rich
```

### Basic Usage

```python
from epub_transfer import process_epub_file

# Process an EPUB file to B1 level English
results = process_epub_file(
    epub_path="your_book.epub",
    level="b1",
    max_tokens=4000,
    is_chinese=False  # Set to True for Chinese books
)

# Save the result
with open("output_book_b1.txt", "w") as f:
    f.write("".join(results))
```

## 📋 How It Works

1. **📖 Text Extraction**: Reads EPUB files and extracts clean text content
2. **✂️ Smart Chunking**: Splits text into manageable chunks while preserving sentence structure
3. **🤖 AI Processing**: Sends each chunk to an AI model for language level conversion
4. **📝 Output Generation**: Combines processed chunks into a coherent final text

## 🎯 Language Levels

| Level | Description | Target Audience |
|-------|-------------|-----------------|
| **A1** | Beginner | Basic words and phrases |
| **A2** | Elementary | Simple sentences and common topics |
| **B1** | Intermediate | Clear standard language on familiar topics |
| **B2** | Upper-Intermediate | Complex texts and abstract topics |
| **C1** | Advanced | Flexible and effective language use |
| **C2** | Proficient | Near-native fluency |

## 🛠️ Configuration

### Token Limits
Adjust the `max_tokens` parameter based on your AI model's capabilities:
```python
token_limit = 4000  # Standard limit
token_limit = 8000  # For more context-aware processing
```

### Chinese Text Support
For Chinese books, enable special sentence tokenization:
```python
process_epub_file(
    epub_path="chinese_book.epub",
    level="b1",
    is_chinese=True  # Enables Chinese sentence splitting
)
```




```

## 📊 Token Counting

The tool uses `tiktoken` for accurate token counting, ensuring chunks stay within AI model limits:

```python
from epub_transfer import count_tokens

text = "Your sample text here"
token_count = count_tokens(text)
print(f"Text contains {token_count} tokens")
```

## 🤝 Contributing

We welcome contributions! Here are some ways you can help:

- 🐛 **Bug Reports**: Found an issue? Let us know!
- 💡 **Feature Requests**: Have ideas for improvements?
- 🔧 **Code Contributions**: Submit pull requests
- 📚 **Documentation**: Help improve our docs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [ebooklib](https://github.com/aerkalov/ebooklib) for EPUB processing
- Uses [NLTK](https://www.nltk.org/) for natural language processing
- Powered by [tiktoken](https://github.com/openai/tiktoken) for token counting
- Enhanced with [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing


---

⭐ **Star this repo if you find it helpful!** ⭐

*Transform your reading experience, one book at a time.* 📖✨