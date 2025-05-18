import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os
import re


def epub_to_text(epub_path, output_txt_path):
    # Read the EPUB file
    book = epub.read_epub(epub_path)

    all_text = []

    # Process each chapter/item
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Get the content as HTML
            content = item.get_content().decode('utf-8')

            # Parse HTML with BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')

            # Extract text with better formatting
            chapter_text = []

            # Process headings specially
            for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                heading_level = int(heading.name[1])
                heading_text = heading.get_text().strip()
                # Add formatting for headings
                chapter_text.append(
                    "\n" + "=" * (7 - heading_level) + " " + heading_text + " " + "=" * (7 - heading_level) + "\n")

            # Process paragraphs
            for para in soup.find_all('p'):
                para_text = para.get_text().strip()
                if para_text:
                    chapter_text.append(para_text + "\n")

            # Process lists
            for ul in soup.find_all('ul'):
                for li in ul.find_all('li'):
                    li_text = li.get_text().strip()
                    if li_text:
                        chapter_text.append("• " + li_text + "\n")

            # Join all text in this chapter
            if chapter_text:
                all_text.extend(chapter_text)
                all_text.append("\n" + "-" * 40 + "\n")  # Chapter separator

    # Join all chapters and write to file
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(all_text))

    print(f"Conversion complete. Text saved to {output_txt_path}")


# Example usage
epub_file = "book/1698.epub"
output_file = "book/1698.txt"
epub_to_text(epub_file, output_file)