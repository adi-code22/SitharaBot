from flask import Flask, render_template, request
from keras.models import model_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow import keras
import tensorflow as tf
import numpy as np
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('model.h5')
model = loaded_model
data = open('Dataset1-Sithara.txt').read()
# open('enter location of dataset')
# print(data)

corpus = data.lower().split("\n")
corpus = list(set(corpus))
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1
# print(tokenizer.word_index)
input_sequences = []
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():



    for line in corpus:
        token_list = tokenizer.texts_to_sequences([line])[0]

        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i + 1]
            input_sequences.append(n_gram_sequence)
        # print(n_gram_sequence)
    max_sequence_len = max([len(x) for x in input_sequences])


    if request.method == 'POST':
        seed_text = request.form['message']
        next_words = int(request.form['number_count'])

        for _ in range(next_words):
            token_list = tokenizer.texts_to_sequences([seed_text])[0]
            token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
            # predicted = model.predict_classes(token_list, verbose=0)
            predicted = np.argmax(model.predict(token_list), axis=-1)
            output_word = ""
            for word, index in tokenizer.word_index.items():
                if index == predicted:
                    output_word = word
                    break
            seed_text += " " + output_word
        my_prediction=seed_text
        return render_template('result.html', prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)
