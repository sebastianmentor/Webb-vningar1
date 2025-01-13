from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        title = request.form.get("title")
        email = request.form.get("email")
        message = request.form.get("message")
        # fake save to database and sending email
        return redirect(url_for('tack', title=title))

    return render_template('contact.html')

@app.route("/tack/<title>")
def tack(title):
    return render_template('tack.html', title=title)


if __name__ == "__main__":
    app.run(debug=True)
