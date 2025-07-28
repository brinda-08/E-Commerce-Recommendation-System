from flask import Flask, request, render_template

app = Flask('__name__')

# routes
@app.route("/")
def index():
    return render_template('index.html')

if '__name__' == '_main_':
    app.run(debug=True)