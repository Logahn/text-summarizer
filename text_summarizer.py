from rake_nltk import Rake
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import string
from heapq import nlargest

"""### Text Data Preparation"""

data = 'sample.txt'
with open(data, "r", encoding="utf-8") as f:
    text = f.read()
print(text)

"""### Data Pre-processing

**Cloud image generation**
"""


print("Word count in text: {}".format(len(text)))

WC = WordCloud(stopwords=STOPWORDS, background_color="white").generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(WC, interpolation='bilinear')
plt.axis("off")
plt.show()

"""**Keyword Extraction**"""

nltk.download('stopwords')
nltk.download('punkt')

rk = Rake()
rk.extract_keywords_from_text(text)
extract_keyword = rk.get_ranked_phrases()
# extract_keyword

"""### Text Summarization"""

# print(text.count("."))
# print(string.punctuation)
nopuch = [char for char in text if char not in string.punctuation]
nopuch = "".join(nopuch)
# print(nopuch)

# Elimination of stopwords
process_text = [word for word in nopuch.split() if word.lower()
                not in nltk.corpus.stopwords.words('english')]
# print(process_text)

# Creating word frequency
word_freq = {}
for word in process_text:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] = word_freq[word] + 1

dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))

max_freq = max(word_freq.values())
for word in word_freq.keys():
    word_freq[word] = (word_freq[word]/max_freq)

# Creating sentence frequency
sent_list = nltk.sent_tokenize(text)

sent_score = {}
for sent in sent_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_freq.keys():
            if sent not in sent_score.keys():
                sent_score[sent] = word_freq[word]
            else:
                sent_score[sent] = sent_score[sent]+word_freq[word]

# dict(sorted(sent_score.items(),key=lambda item:item[1], reverse=True))

summary_sent = nlargest(6, sent_score, key=sent_score.get)
summary = " ".join(summary_sent)
summary
