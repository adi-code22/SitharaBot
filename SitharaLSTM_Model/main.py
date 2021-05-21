import tensorflow as tf

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow import keras
import numpy as np


# tokenizer = Tokenizer()
# data = open('').read()
data = open('/content/sample_data/Dataset1-Sithara.txt').read()
# open('enter location of dataset')
# print(data)

corpus = data.lower().split("\n")
corpus = list(set(corpus))
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1
# print(tokenizer.word_index)
input_sequences = []
for line in corpus:
    token_list = tokenizer.texts_to_sequences([line])[0]
    
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
    
    input_sequences.append(n_gram_sequence)
    # print(n_gram_sequence)
max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences,
                       maxlen = max_sequence_len, padding='pre'))
predictors, label = input_sequences[:,:-1],input_sequences[:,-1]
# label=ku.to_categorical(label,num_classes=total_words)
label=tf.keras.utils.to_categorical(
    label, num_classes=total_words, dtype='float32'
)

model = Sequential()
model.add(Embedding(total_words, 50, input_length=max_sequence_len-1))
model.add(Bidirectional(LSTM(150, return_sequences=True)))  
model.add(Dropout(0.2))
model.add(LSTM(100)) 
model.add(Dense(total_words/2, activation='relu'))  
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics='accuracy')  
print(model.summary())

history = model.fit(predictors, label, epochs= 100, verbose=1)

model_json = model.to_json()
with open("model.json",'w') as json_file:
  json_file.write(model_json)

model.save_weights("model.h5")



