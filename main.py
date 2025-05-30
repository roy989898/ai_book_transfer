import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re
import nltk
from nltk.tokenize import sent_tokenize
import tiktoken
import requests
from rich.pretty import pprint

from robot import Robot


def strip_html_tags(html_content):
    """Remove HTML tags and get text content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()


def get_epub_text(epub_path):
    """Extract all text from an EPUB file."""
    book = epub.read_epub(epub_path)
    all_text = []

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = item.get_content().decode('utf-8')
            text = strip_html_tags(content)
            all_text.append(text)

    return ' '.join(all_text)


def count_tokens(text, encoding_name="cl100k_base"):
    """Count tokens in text using tiktoken."""
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))


def sent_tokenize_cn(text: str) -> list[str]:
    r = text.split("。")
    new_r = []
    for sentence in r:
        d = sentence + "。"
        new_r.append(d)
    return new_r


# 。
def split_text_by_tokens(text: str, max_tokens=4000, for_chinese=False):
    """Split text by token count while preserving complete sentences."""
    sentences = []
    if for_chinese:
        sentences = sent_tokenize_cn(text)
    else:
        sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_token_count = 0

    for sentence in sentences:
        sentence_tokens = count_tokens(sentence)

        # If a single sentence exceeds the max token limit, we might need to split it
        if sentence_tokens > max_tokens:
            # Add the current chunk if it's not empty
            if current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_token_count = 0

            # Add the long sentence as its own chunk
            chunks.append(sentence)
            continue

        # Check if adding this sentence would exceed the token limit
        if current_token_count + sentence_tokens > max_tokens:
            # Save the current chunk and start a new one
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
            current_token_count = sentence_tokens
        else:
            # Add the sentence to the current chunk
            current_chunk.append(sentence)
            current_token_count += sentence_tokens

    # Add the last chunk if there's anything left
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks


def send_to_ai_model(text_chunk: str, level: str,
                     ):
    """Send text chunk to an AI model API."""
    # print(text_chunk)
    # level = 'b2'

    try:
        r = Robot.transfer_book(text_chunk, level)

        return r
    except:
        print("An exception occurred re try")
        r = Robot.transfer_book(text_chunk, level)

        return r

    # headers = {
    #     "Authorization": f"Bearer {api_key}",
    #     "Content-Type": "application/json"
    # }
    #
    # data = {
    #     "model": "your-model-name",
    #     "prompt": text_chunk,
    #     "max_tokens": 1000
    # }
    #
    # try:
    #     response = requests.post(api_url, headers=headers, json=data)
    #     return response.json()
    # except Exception as e:
    #     return {"error": str(e)}


def process_epub_file(epub_path, level: str, max_tokens=4000, is_chinese=False):
    """Process EPUB file and send chunks to AI model."""
    # Extract text from EPUB
    print(f"Extracting text from {epub_path}...")
    full_text = get_epub_text(epub_path)

    # Split text into chunks by token count
    print("Splitting text into chunks...")
    chunks = split_text_by_tokens(full_text, max_tokens, is_chinese)
    print(f"Split into {len(chunks)} chunks.")

    # Process each chunk with AI model
    results = []
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i + 1}/{len(chunks)}...")
        result = send_to_ai_model(chunk, level)
        results.append(result)

    return results


def to_text_file(string: str, file_name: str):
    with open(file_name, "w") as file:
        file.write(string)


if __name__ == "__main__":
    # Download NLTK data if not already present
    nltk.download('punkt_tab')
    # Example usage
    epub_file_path = "book/night_fast_1.epub"
    token_limit = 50000  # Adjust based on your AI model's requirements

    results = process_epub_file(epub_file_path, "b1", token_limit, is_chinese=True)
    joined_result = "".join(results)

    to_text_file(joined_result, 'book/night_fast_1_b1_v2.txt')
    print(f"Processed {len(results)} chunks with the AI model.")
