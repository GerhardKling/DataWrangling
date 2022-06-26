"""
Common words in PDF file
Author: Gerhard Kling
"""

from rank import word_rank

#Arguments
file_name = "MS_2019.pdf"

#Call function
top_words = word_rank(file_name, 30)

print(top_words)