import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re
import nltk
from nltk.tokenize import sent_tokenize
import tiktoken
import requests
from rich.pretty import pprint

from main import to_text_file
from robot import Robot


def read_file_to_string(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


if __name__ == "__main__":
    # Example usage

    file_path = "book/1698_en_b2.txt"
    text_content = read_file_to_string(file_path)

    r = Robot.get_better_format(text_content)
    to_text_file(r, '1698_en_b2_format.txt')
    print(f"Processed .")
