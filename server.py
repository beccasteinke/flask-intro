"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    
    <!doctype html>
    <html>Hi! This is the home page.
    <p><a href="http://localhost:5000/hello">Click here to be complimented!</a></p>
    <p><a href="http://localhost:5000/insulter">Click here to get insulted!</a></p>
    </html>
   """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          <p>
          How are you feeling today? 
            <select name="user_choice">
              <option value="beautiful">Beautiful</option>
              <option value="creative">Creative</option>
              <option value="funny">Funny</option>
              <option value="intelligent">Intelligent</option>
            </select>
          </p>

        </form>
      </body>
    </html>
    """

@app.route('/insulter')
def say_insult_hello():
    """Say hello and prompt for user's name and insult."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          <p>
          How are you feeling today? 
            <select name="insult">
                <option value="ugly">Ugly</option>
                <option value="mean">Mean</option>
                <option value="dorky">Dorky</option>
                <option value="lazy">Lazy</option>
            </select>
          </p>

        </form>
      </body>
    </html>
    """

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("user_choice")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route('/diss')
def insult_person():
  """Insult a person"""

  player = request.args.get("person")

  diss = request.args.get("insult")
  return """
      <!doctype html>
      <html>
        <head>
        <title>An Insult</title>
        </head>
        <body>
          Hi, {}! I think you're {}!
        </body>
      </html>
    """.format(player, diss)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
