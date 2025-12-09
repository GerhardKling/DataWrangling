import PyPDF2
import re
from collections import Counter
from gensim.parsing.preprocessing import remove_stopwords

def word_rank(file_name: str, top_num: int = 10):
    """
    file_name: name of pdf file
    Returns: list of tuples -> (keyword, count)
    """
    # Read PDF
    doc = PyPDF2.PdfFileReader(file_name)
    pages = doc.getNumPages()

    all_words = []

    for i in range(pages):
        current_page = doc.getPage(i)
        text = current_page.extractText().lower()

        # Remove stopwords
        text_filtered = remove_stopwords(text)

        # Split into words
        words = text_filtered.split()
        all_words.extend(words)

    # Keep only alphanumeric tokens
    words_alnum = [w for w in all_words if w.isalnum()]

    # Ignore-list (lowercase to match processed words)
    ignore_list = ['the', 'year', 'financial', 'marks', 'spencer']

    words_filtered = [w for w in words_alnum if w not in ignore_list]

    # Return list of tuples like: [('keyword1', 30), ('keyword2', 48), ...]
    top_words = Counter(words_filtered).most_common(top_num)

    return top_words
