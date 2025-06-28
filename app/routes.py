from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Lead

@app.route("/")
def index():
    leads = Lead.query.order_by(Lead.created_at.desc()).all()
    return render_template("dashboard.html", leads=leads)

@app.route("/add-lead", methods=["GET", "POST"])
def add_lead():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        status = request.form.get("status")
        new_lead = Lead(name=name, email=email, phone=phone, status=status)
        db.session.add(new_lead)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_lead.html")