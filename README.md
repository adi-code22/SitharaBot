
# Paatukari.ml
A custom song lyric generator that generates song lyrics based on user input.

http://paatukari.herokuapp.com/

![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Paatukari.ml

In this project, I built a flask web application that uses the lyrics of songs by sithara and then predict the lyrics based on user input.
This project is divided to two parts:

##### Part 1 - Developing an ml model in colab

In this first part of the project, I trained an ml model using google colab.
##### Part 2 - Building the flask application

Build a flask webapp to take input from the user and to predict new images using the trained model.

## Team members :raising_hand:
1. Adith P Anandhan [https://github.com/cloneartist]
2. Adityakrishnan  [https://github.com/adi-code22]

## Team Id :key:

     BFH/recF8NlSP3G7kZDkA/2021

## Link to product walkthrough :tv:
<!-- ![Watch the video](https://bit.ly/2SnecIg) -->
(https://bit.ly/2SnecIg)

## Live URL :satellite:
We have deployed the current model to Heroku
You can See the webapp here:http://paatukari.herokuapp.com/
## Libraries used :books:
This project requires  **Python 3.x**  and the following Python libraries installed:
-   [TensorFlow](https://www.tensorflow.org/)
-   [Numpy](https://www.numpy.org/)
# How to configure :wrench:
## How to Run


### Local Installation

It's easy to install and run it on your computer.

```shell
# 1. First, clone the repo
$ git clone https://github.com/adi-code22/SitharaBot.git

# 2. Install Python packages
$ pip install -r requirements.txt

# 3. Run!
$ python app.py
```

Open http://localhost:5000 and have fun. :smiley:

## Customization :computer:

It's also easy to customize the ui and include your own models in this app.

<details>
 <summary>Details</summary>

### Use your own model

Place your trained `.h5` file saved by `model.save()`.

### UI Modification

Modify files in `templates` and `static` directory.

`index.html`and `style.css`  for the UI of webapp

</details>

