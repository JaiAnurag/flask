from flask import Flask
app = Flask(__name__)

# Home route
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")
if __name__ == '__main__':
    app.run(debug=True)
