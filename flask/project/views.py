from flask import render_template
from flask_flatpages import FlatPages
from app import app, pages

@app.route('/')
def home():
  posts = [page for page in pages]
  sorted_posts = sorted(posts, key=lambda page: page.meta['order'])
  return render_template('index.html', pages=sorted_posts)

@app.route('/<path:path>/')
def page(path):
  # Path is the filename of a page, without the file extension e.g. "first-post"
  page = pages.get_or_404(path)
  return render_template('page.html', page=page)
