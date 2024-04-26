from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
   app.run()


# copy paste http://localhost:5000/