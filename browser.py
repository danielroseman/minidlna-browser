import os
import sqlite3

from flask import Flask, request, g, url_for, render_template
app = Flask(__name__)

app.config.from_object(__name__)
app.config.update(dict(
  DATABASE=os.path.join(app.root_path, 'files.db'),
  SECRET_KEY='development key',
  BASE_URL ='http://192.168.1.81:8200/MediaItems/',
  ROOT_ID='64',
  #USERNAME='admin',
  #PASSWORD='default'
))
app.config.from_envvar('BROWSER_SETTINGS', silent=True)

def connect_db():
  rv = sqlite3.connect(app.config['DATABASE'])
  rv.row_factory = sqlite3.Row
  return rv

def get_db():
  if not hasattr(g, 'sqlite_db'):
    g.sqlite_db = connect_db()
  return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
  if hasattr(g, 'sqlite_db'):
    g.sqlite_db.close()

@app.route('/')
@app.route('/browse/<object_id>/')
def browse(object_id=None):
  db = get_db()
  if object_id is None or object_id == app.config['ROOT_ID']:
    object_id = app.config['ROOT_ID']
    parent_id = path = None
  else:
    cur = db.execute('select PARENT_ID, PATH FROM OBJECTS JOIN DETAILS ON OBJECTS.DETAIL_ID=DETAILS.ID WHERE OBJECT_ID =?', [object_id])
    parent_id, path = cur.fetchone()
  cur = db.execute('select ID, CLASS, OBJECT_ID, NAME, DETAIL_ID FROM OBJECTS WHERE PARENT_ID=?', [object_id])
  items = cur.fetchall()
  return render_template('browse.html', items=items, BASE_URL=app.config['BASE_URL'], parent_id=parent_id, path=path)
