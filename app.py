"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request, render_template
from models import db, connect_db, Cupcake
from forms import CupcakeForm
import pdb

app = Flask(__name__, template_folder = "templates")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

connect_db(app)

app.config['SECRET_KEY'] = "hellothere"

@app.route('/')
def index_page():
    """return home page"""
    cupcakes = Cupcake.query.all()
    form = CupcakeForm()
    return render_template('index.html', cupcakes=cupcakes, form=form)

@app.route('/api/cupcakes')
def list_cupcakes():
    """Return JSON all cupcakes"""
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<cupcake_id>')
def list_single_cupcake(cupcake_id):
    """Return JSON of single cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def make_cupcake():
    """Make a cupcake"""
    new_cupcake = Cupcake(
        flavor = request.json['flavor'],
        size = request.json['size'],
        rating = request.json['rating'],
        image = request.json.get('image', 'none')
    )
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<cupcake_id>', methods=['PATCH'] )
def update_cupcake(cupcake_id):
    """update a single cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor),
    cupcake.size = request.json.get('size', cupcake.size),
    cupcake.rating = request.json.get('rating', cupcake.rating),
    cupcake.image = request.json.get('image', cupcake.image)

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<cupcake_id>', methods=['DELETE'] )
def delete_cupcake(cupcake_id):
    """update a single cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    
    return jsonify(message="deleted")