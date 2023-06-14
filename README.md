# Text Summarizer

This script is a Python implementation of a Text Summarizer. It automatically generates a summary of a given text.

## Libraries used

- [Rake](https://pypi.org/project/rake-nltk/): A Python implementation of the Rapid Automatic Keyword Extraction algorithm.
- [WordCloud](https://pypi.org/project/wordcloud/): A Python library for generating word clouds.
- [NumPy](https://numpy.org/): A Python library for the computation with arrays and matrices.
- [Pandas](https://pandas.pydata.org/): A Python library for data manipulation and analysis.
- [Matplotlib](https://matplotlib.org/): A Python library for creating visualizations in Python.
- [NLTK](https://www.nltk.org/): A Python library for natural language processing.

## Text Data Preparation

The script loads the text data from a file `sample.txt` and generates a word cloud image of the text.

## Data Pre-processing

The script performs the following pre-processing steps on the text data:

1. Elimination of punctuations
2. Elimination of stopwords
3. Creation of word frequency

## Text Summarization

The script generates a summary of the text using the following steps:

1. Creation of sentence frequency
2. Selection of top sentences based on sentence score

## How to use

To use this script, you need to have the following libraries installed:

- Rake
- WordCloud
- NumPy
- Pandas
- Matplotlib
- NLTK

You also need to provide the text data in a file `sample.txt`.

Run the script to generate the summary of the text. The summary will be displayed in the console.

## Link

Google colab file can be found [here](https://colab.research.google.com/drive/1_HW42gOYy8BbXnVqeQZoO9k7z79YjWX5 "Link to Colab File")
