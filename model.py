from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Define Article model
class Article(db.Model):

    
id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship("User", backref="articles")
    published_date = db.Column(db.DateTime, nullable=False)

# Route to create a new article
@app.route("/articles/new", methods=["GET", "POST"])
@login_required
def
 
create_article():

    
if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        # ...
        article = Article(title=title, content=content, author=current_user)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create_article.html")

# Route to edit an existing article
@app.route("/articles/<int:article_id>/edit", methods=["GET", "POST"])

@login_required

def
 
edit_article(article_id):
    article = Article.query.get_or_404(article_id)

    
if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        # ...
        article.title = title
        article.content = content
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_article.html", article=article)