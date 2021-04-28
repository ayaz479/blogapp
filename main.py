from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps


# kullanci adi dicureter

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Please login to view this page", "danger")
            return redirect(url_for("login"))

    return decorated_function


class RegisterForm(Form):
    name = StringField("Name and Surname", validators=[validators.Length(min=5, max=25)])
    username = StringField("Username", validators=[validators.Length(min=5, max=25)])
    email = StringField("E-mail", validators=[validators.Email()])
    password = PasswordField("password:", validators=[validators.DataRequired(message="please enter a password"),
                                                      validators.EqualTo(fieldname="confirm",
                                                                         message="password does not match")])

    confirm = PasswordField("password verification")


class Loginform(Form):
    username = StringField("Username")
    password = PasswordField("Password")


app = Flask(__name__)
app.secret_key = "horbax"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "horbax company"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def homepage():
    return render_template("Homepage.html")


@app.route("/dashboard")
@login_required
def control_panel():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From article where author = %s"
    result = cursor.execute(sorgu, (session["username"],))
    if result > 0:
        article = cursor.fetchall()
        return render_template("dashboard.html", article=article)

    else:
        return render_template("dashboard.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From article"
    result = cursor.execute(sorgu)
    if result > 0:
        articles = cursor.fetchall()

        return render_template("service.html", articles=articles)

    else:
        return render_template("service.html")


@app.route("/Contact")
def contact():
    return render_template("contact.html")


@app.route("/join", methods=["GET", "POST"])
def joinus():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)
        cursor = mysql.connection.cursor()
        sorgu = "Insert into userss(name,username,password,email) VALUES(%s,%s,%s,%s)"
        cursor.execute(sorgu, (name, username, password, email))
        mysql.connection.commit()
        cursor.close()
        flash("You have successfully registered", "success")

        return redirect(url_for("login"))
    else:
        return render_template("join.html", form=form)


@app.route("/Login", methods=["GET", "POST"])
def login():
    form = Loginform(request.form)
    if request.method == "POST":
        username = form.username.data
        password_enterd = form.password.data
        cursor = mysql.connection.cursor()
        sorgu = "Select * From userss where username = %s"
        result = cursor.execute(sorgu, (username,))
        if result > 0:
            data = cursor.fetchone()
            real_pass = data["password"]
            if sha256_crypt.verify(password_enterd, real_pass):
                flash("You have successfully logged in", "success")
                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("homepage"))
            else:
                flash("password is wrong", "danger")
                return redirect(url_for("login"))
        else:
            flash("There is no such user", "danger")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)


@app.route("/Logout")
def logout():
    session.clear()
    return redirect(url_for("homepage"))


@app.route("/addarticle", methods=["GET", "POST"])
def addarticle():
    form = Articleform(request.form)
    if request.method == "POST":
        title = form.title.data
        content = form.content.data
        cursor = mysql.connection.cursor()
        sorgu = "Insert into article(title,author,content) VALUES(%s,%s,%s) "
        cursor.execute(sorgu, (title, session["username"], content))
        mysql.connection.commit()
        cursor.close()
        flash("article successfully added")
        return redirect(url_for("control_panel"))

    return render_template("Addarticle.html", form=form)


class Articleform(Form):
    title = StringField("Article title", validators=[validators.Length(min=5, max=10)])
    content = TextAreaField("Article content", validators=[validators.Length(min=10, max=30)])


@app.route("/article/<string:id>")
def article(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select * From article where id = %s"
    result = cursor.execute(sorgu, (id,))
    if result > 0:
        article = cursor.fetchone()
        return render_template("article.html", article=article)
    else:
        return render_template("article.html")


# article delete
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor()
    sorgu = "Select * from article where author = %s and id =%s"
    result = cursor.execute(sorgu, (session["username"], id))
    if result > 0:
        sorgu1 = "Delete from article where id = %s"
        cursor.execute(sorgu1, (id,))
        mysql.connection.commit()
        return redirect(url_for("control_panel"))
    else:
        flash("There is no such article or we do not have the authority to process such an article.", "danger")
        return redirect(url_for("homepage"))
# Article update
@app.route("/edit/<string:id>",methods=["GET","POST"])
@login_required
def update(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "Select * from article where id = %s and author = %s"
        result = cursor.execute(sorgu,(id,session["username"]))
        if result == 0 :
            flash("There is no such article or we do not have the authority to process such an article.", "danger")
            return redirect(url_for("homepage"))
        else:
            article = cursor.fetchone()
            form = Articleform()
            form.title.data = article["title"]
            form.content.data = article["content"]
            return render_template("update.html",form=form)
    else:
        form = Articleform(request.form)
        newTitle = form.title.data
        newContent = form.content.data
        sorgu1 = "Update article Set title = %s,content = %s where id = %s"
        cursor = mysql.connection.cursor()
        cursor.execute(sorgu1,(newTitle,newContent,id))
        mysql.connection.commit()
        flash("the article has been successfully updated","success")
        return redirect(url_for("control_panel"))
#search url
@app.route("/search",methods = ["GET","POST"])
def search():
    if request.method == "GET":
        return redirect(url_for("homepage"))
    else:
        keyword = request.form.get("keyword")
        cursor = mysql.connection.cursor()
        sorgu = "Select * from article where title Like '%" + keyword + "%'"
        result = cursor.execute(sorgu)
        if result == 0 :
            flash("There is no such article","warning")
            return redirect(url_for("services"))
        else:
            articles = cursor.fetchall()
            return render_template("service.html",articles=articles)
if __name__ == "__main__":
    app.run(debug=True)
