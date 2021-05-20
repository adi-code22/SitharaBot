from flask import Flask,render_template,url_for,request


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    my_prediction = 1
    return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)