"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

import string
from collections import Counter

def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    """
    Count total words in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    # découpe sur les espaces/  blancs
    return len(text.split())


def count_lines(filename):
    """
    Count total lines in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)


def count_characters(filename, include_spaces=True):
    """
    Count characters in the file.
    include_spaces=False => on retire tous les caractères d'espacement.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    if include_spaces:
        return len(text)
    # retire espaces, tabulations, retours ligne, etc.
    no_space = ''.join(ch for ch in text if not ch.isspace())
    return len(no_space)


def find_longest_word(filename):
    """
    Find and return the longest word in the file.
    On retire la ponctuation pour éviter les apostrophes/points.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    table = str.maketrans('', '', string.punctuation)
    words = text.translate(table).split()
    return max(words, key=len) if words else ""


def word_frequency(filename):
    """
    Return a dictionary of word frequencies.
    Convert words to lowercase and remove punctuation.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    table = str.maketrans('', '', string.punctuation)
    words = text.translate(table).split()
    return dict(Counter(words))


def analyze_file(filename):
    """
    Perform complete analysis of the file.
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)
    try:
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        print("\nTop 5 most common words:")
        freq = word_frequency(filename)
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()
