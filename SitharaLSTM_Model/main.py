import tensorflow as tf

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional,Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow import keras
import numpy as np


# tokenizer = Tokenizer()
# data = open('').read()
data = open('/content/sample_data/Dataset1-Sithara.txt').read()
#open('enter location of dataset')
# print(data)

corpus = data.lower().split("\n")
corpus = list(set(corpus))
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1
# print(tokenizer.word_index)
input_sequences = []
