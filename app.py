from flask import Flask, render_template, request

app = Flask(__name__) # So that this is run instead of any other library code we write on initialization


@app.route("/")
def index():        
    if 'name' in request.args:              
        name = request.args["name"]         # Check if name is a key in arg dict, if yes, set name to provided request (like in servlet)
    else:
        name = "World"                      # No param? name's value becomes World
    return render_template("index.html", name = name)    # Flask will use render_template to find the page, dynamic variable assignment in the brackets