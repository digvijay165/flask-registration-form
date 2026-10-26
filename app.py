"""
Flask Registration Form
------------------------
A simple Flask web application that displays a user registration form,
accepts the user's name, city, and phone number, and shows the submitted
details on a confirmation page.

Author: Deen Bandhu Singh
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def registration_form():
    """Display the registration form."""
    return render_template("register.html")


@app.route("/submit", methods=["POST"])
def submit():
    """Handle form submission and show the confirmation page."""
    name = request.form.get("name")
    city = request.form.get("city")
    phone = request.form.get("phone")

    return render_template(
        "confirmation.html",
        name=name,
        city=city,
        phone=phone,
    )


if __name__ == "__main__":
    app.run(debug=True)
