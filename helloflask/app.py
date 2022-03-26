from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        return f'Hello, {name}!'
    return 'Hello, world!'

#create another route like "/square/<number>" so the web app will display the square of the number
@app.route('/square/') #will trigger square() -) square(none)
@app.route('/square/<number>') #will trigger square(number)
def square(number=None):
    if number is None:
        return "Provide a number pls"
    return str(int(number) ** 2)


if __name__ == "__main__":
    app.run()