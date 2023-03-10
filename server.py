from flask import Flask, render_template

app = Flask(__name__)

# providing a welcome message to users coming to the webpage!
@app.route('/')
def hello_world():
    return "Welcome to the world of boxes! "

#  this route renders a constant box number of 3
@app.route('/play')
def play():
    return render_template('play.html', x = 3, color="#9EC5F8")

# this route outputs the given amount of boxes
@app.route('/play/<int:x>')
def multiply(x):
    return render_template('play.html', x=x, color="#9EC5F8")

# renders the given amount of boxes and color 
@app.route('/play/<int:x>/<color>')
def colors(x, color):
    return render_template('play.html', x=x, color=color)

if __name__=="__main__":
    app.run(debug=True)
