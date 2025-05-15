from flask import Blueprint, render_template
from .models import Destination, Comment

# Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
destbp = Blueprint('destination', __name__, url_prefix='/destinations')

@destbp.route('/<id>')
def show(id):
    brazil = get_destination()
    return render_template('destinations/show.html', destination=brazil)

def get_destination():
  # creating the description of Brazil
  b_desc = """Brazil is considered an advanced emerging economy.
   It has the ninth largest GDP in the world by nominal, and eight by PPP measures. 
   It is one of the world\'s major breadbaskets, being the largest producer of coffee for the last 150 years."""
   # an image location
  image_loc = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag'
  destination = Destination('Brazil', b_desc,image_loc, 'R$10')
  # a comment
  comment = Comment("Sam", "Visited during the olympics, was great", '2023-08-12 11:00:00')
  destination.set_comments(comment)
  comment = Comment("Bill", "free food!", '2023-08-12 11:00:00')
  destination.set_comments(comment)
  comment = Comment("Sally", "free face masks!", '2023-08-12 11:00:00')
  destination.set_comments(comment)
  return destination