#!/usr/bin/env python3
"""
Clean source texts for The Kindled Path.
Removes page numbers, fixes ALL CAPS headers, and cleans OCR artifacts.
"""

import re
import sys

def clean_attar(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove page numbers like (10), (13), ( 14 ), (i6), (^ 7 ), (lO, etc.
    text = re.sub(r'\n\s*\(\s*[0-9iIlOo\^\s]+\s*\)?\s*\n', '\n', text)
    text = re.sub(r'\(\s*[0-9iIlOo\^\s]+\s*\)', '', text)

    # Remove standalone single letters that are artifacts (like "c", "B")
    text = re.sub(r'\n\s*[a-zA-Z]\s*\n\n', '\n\n', text)
    text = re.sub(r'\n\s*[a-zA-Z]\s*\n(?=\n)', '\n', text)

    # Convert ALL CAPS section headers to Title Case
    def title_case_header(match):
        text = match.group(1)
        # Convert to title case
        words = text.lower().split()
        titled = []
        small_words = {'a', 'an', 'the', 'and', 'or', 'but', 'of', 'to', 'in', 'for', 'on', 'with', 'at', 'by', 'from'}
        for i, word in enumerate(words):
            if i == 0 or word not in small_words:
                titled.append(word.capitalize())
            else:
                titled.append(word)
        return '\n\n' + ' '.join(titled) + '\n\n'

    # Match ALL CAPS headers (lines that are entirely uppercase letters and spaces)
    text = re.sub(r'\n\s*([A-Z][A-Z\s,\'\-]+[A-Z])\s*\n', title_case_header, text)

    # Fix common OCR errors
    text = text.replace('^', "'")
    text = text.replace("''", "'")  # double single-quotes to apostrophe
    text = text.replace('Ever^^one', 'Everyone')
    text = text.replace("Everyone", "Everyone")
    text = text.replace("w'orld", 'world')
    text = text.replace('ever}^one', 'everyone')
    text = text.replace('tilings', 'things')
    text = text.replace('forv\'ard', 'forward')
    text = text.replace("ferv'ent", 'fervent')
    text = text.replace('dervdsh', 'dervish')
    text = text.replace('der\\ush', 'dervish')
    text = text.replace('rela>', 'rela-')
    text = text.replace(' Mv ', ' My ')
    text = text.replace('resdess', 'restless')
    text = text.replace('everlasdng', 'everlasting')
    text = text.replace('per\'erse', 'perverse')
    text = text.replace("ligh'-", "light")
    text = text.replace(" 1 \"", "!\"")  # OCR error: "1" for "!"

    # Fix hyphenated words at line breaks (word- \nnext -> wordnext)
    text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)

    # Clean up excessive whitespace
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    text = re.sub(r' +', ' ', text)

    # Remove leading/trailing whitespace from lines
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Cleaned {input_path} -> {output_path}")

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        clean_attar(sys.argv[1], sys.argv[2])
    else:
        # Default paths
        clean_attar(
            'attar-conference-of-birds/raw.txt',
            'attar-conference-of-birds/cleaned.txt'
        )
