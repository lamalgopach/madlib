"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Greet user with compliment."""
    answer = request.args.get("answer")

    if answer == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    person = request.args.get("person")
    color1 = request.args.get("color1")    
    color2 = request.args.get("color2")
    color3 = request.args.get("color3")
    animal = request.args.get("animal")
    adj = request.args.get("adj")
    return render_template("madlib.html", person=person, 
                            color1=color1, color2=color2, color3=color3,
                             animal=animal, adj=adj)





if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
