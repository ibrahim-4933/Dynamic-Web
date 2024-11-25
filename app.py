from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home", message="Welcome to my dynamic website!")

@app.route('/about')
def about():
    return render_template('about.html', title="About", message="This is the about page.")

if __name__ == '__main__':
    app.run(debug=True)
