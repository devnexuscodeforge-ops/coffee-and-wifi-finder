from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config["SECRET_KEY"] = "my-secret-key"


class CafeForm(FlaskForm):
    location = StringField(
        "Cafe Location on Google Maps (URL)",
        validators=[DataRequired(), URL(message="Invalid URL.")]
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file)
        list_of_rows = list(csv_data)

    return render_template("cafes.html", cafes=list_of_rows)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = CafeForm()

    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", newline="", encoding="utf-8") as csv_file:
            csv_file.write(
                f"\n{request.form['cafe']},"
                f"{form.location.data},"
                f"{request.form['open']},"
                f"{request.form['close']},"
                f"{request.form['coffee']},"
                f"{request.form['wifi']},"
                f"{request.form['power']}"
            )

        return redirect(url_for("cafes"))

    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)