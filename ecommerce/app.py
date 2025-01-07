import os
import random
from flask import Flask, render_template, redirect, url_for, request, session, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from python.forms import ContactForm

# Generate a random secret key
secret_key = os.urandom(24)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = secret_key

db = SQLAlchemy(app)

# Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    description = db.Column(db.Text, nullable=True)

@app.before_request
def create_tables():
    db.create_all()
    if not Product.query.first():
        products = [
            # Men's products
            Product(name='Men\'s T-shirt', price=19.99, category='Men', image_file='product1.jpg', description='A comfortable cotton T-shirt.'),
            Product(name='Men\'s Jeans', price=39.99, category='Men', image_file='product2.jpg', description='Stylish blue jeans.'),
            Product(name='Men\'s Jacket', price=59.99, category='Men', image_file='product3.jpg', description='Warm and cozy jacket.'),
            Product(name='Men\'s Sneakers', price=49.99, category='Men', image_file='product4.jpg', description='Comfortable running shoes.'),
            Product(name='Men\'s Watch', price=129.99, category='Men', image_file='product5.jpg', description='Elegant wrist watch.'),
            Product(name='Men\'s Hat', price=14.99, category='Men', image_file='product6.jpg', description='Cool summer hat.'),
            Product(name='Men\'s Sunglasses', price=24.99, category='Men', image_file='product7.jpg', description='Stylish sunglasses.'),
            Product(name='Men\'s Belt', price=19.99, category='Men', image_file='product8.jpg', description='Leather belt.'),
            Product(name='Men\'s Wallet', price=29.99, category='Men', image_file='product9.jpg', description='Genuine leather wallet.'),
            Product(name='Men\'s Gloves', price=19.99, category='Men', image_file='product10.jpg', description='Warm winter gloves.'),
            Product(name='Men\'s Tie', price=14.99, category='Men', image_file='product11.jpg', description='Formal tie.'),
            Product(name='Men\'s Shorts', price=24.99, category='Men', image_file='product12.jpg', description='Casual summer shorts.'),
            Product(name='Men\'s Sandals', price=29.99, category='Men', image_file='product13.jpg', description='Comfortable sandals.'),
            Product(name='Men\'s Socks', price=9.99, category='Men', image_file='product14.jpg', description='Pack of 3 socks.'),
            Product(name='Men\'s Hoodie', price=39.99, category='Men', image_file='product15.jpg', description='Cozy hoodie.'),
            Product(name='Men\'s Sweater', price=49.99, category='Men', image_file='product16.jpg', description='Warm sweater.'),
            Product(name='Men\'s Boots', price=89.99, category='Men', image_file='product17.jpg', description='Durable boots.'),
            Product(name='Men\'s Polo Shirt', price=29.99, category='Men', image_file='product18.jpg', description='Casual polo shirt.'),
            Product(name='Men\'s Blazer', price=99.99, category='Men', image_file='product19.jpg', description='Formal blazer.'),
            Product(name='Men\'s Scarf', price=14.99, category='Men', image_file='product20.jpg', description='Winter scarf.'),
            Product(name='Men\'s Beanie', price=9.99, category='Men', image_file='product21.jpg', description='Knitted beanie.'),
            Product(name='Men\'s Chinos', price=39.99, category='Men', image_file='product22.jpg', description='Stylish chinos.'),
            Product(name='Men\'s Trench Coat', price=149.99, category='Men', image_file='product23.jpg', description='Classic trench coat.'),
            Product(name='Men\'s Cap', price=14.99, category='Men', image_file='product24.jpg', description='Baseball cap.'),
            Product(name='Men\'s Swim Shorts', price=24.99, category='Men', image_file='product25.jpg', description='Swimming shorts.'),
            
            # Women's products
            Product(name='Women\'s Dress', price=49.99, category='Women', image_file='product26.jpg', description='Elegant evening dress.'),
            Product(name='Women\'s Skirt', price=29.99, category='Women', image_file='product27.jpg', description='Stylish skirt.'),
            Product(name='Women\'s Blouse', price=19.99, category='Women', image_file='product28.jpg', description='Casual blouse.'),
            Product(name='Women\'s Handbag', price=59.99, category='Women', image_file='product29.jpg', description='Designer handbag.'),
            Product(name='Women\'s Heels', price=79.99, category='Women', image_file='product30.jpg', description='High heels.'),
            Product(name='Women\'s Necklace', price=49.99, category='Women', image_file='product31.jpg', description='Elegant necklace.'),
            Product(name='Women\'s Earrings', price=19.99, category='Women', image_file='product32.jpg', description='Stylish earrings.'),
            Product(name='Women\'s Bracelet', price=29.99, category='Women', image_file='product33.jpg', description='Gold bracelet.'),
            Product(name='Women\'s Watch', price=129.99, category='Women', image_file='product34.jpg', description='Elegant wrist watch.'),
            Product(name='Women\'s Hat', price=14.99, category='Women', image_file='product35.jpg', description='Summer hat.'),
            Product(name='Women\'s Sunglasses', price=24.99, category='Women', image_file='product36.jpg', description='Stylish sunglasses.'),
            Product(name='Women\'s Scarf', price=14.99, category='Women', image_file='product37.jpg', description='Winter scarf.'),
            Product(name='Women\'s Gloves', price=19.99, category='Women', image_file='product38.jpg', description='Leather gloves.'),
            Product(name='Women\'s Belt', price=19.99, category='Women', image_file='product39.jpg', description='Fashion belt.'),
            Product(name='Women\'s Wallet', price=29.99, category='Women', image_file='product40.jpg', description='Leather wallet.'),
            Product(name='Women\'s Boots', price=89.99, category='Women', image_file='product41.jpg', description='Stylish boots.'),
            Product(name='Women\'s Sweater', price=49.99, category='Women', image_file='product42.jpg', description='Cozy sweater.'),
            Product(name='Women\'s Hoodie', price=39.99, category='Women', image_file='product43.jpg', description='Casual hoodie.'),
            Product(name='Women\'s Jeans', price=39.99, category='Women', image_file='product44.jpg', description='Blue jeans.'),
            Product(name='Women\'s Shorts', price=24.99, category='Women', image_file='product45.jpg', description='Casual shorts.'),
            Product(name='Women\'s Swimwear', price=29.99, category='Women', image_file='product46.jpg', description='Stylish swimwear.'),
            Product(name='Women\'s Cardigan', price=39.99, category='Women', image_file='product47.jpg', description='Warm cardigan.'),
            Product(name='Women\'s Jacket', price=59.99, category='Women', image_file='product48.jpg', description='Winter jacket.'),
            Product(name='Women\'s Sandals', price=29.99, category='Women', image_file='product49.jpg', description='Comfortable sandals.'),
            Product(name='Women\'s T-shirt', price=19.99, category='Women', image_file='product50.jpg', description='Casual T-shirt.'),
            
            # Children's products
            Product(name='Children\'s T-shirt', price=9.99, category='Children', image_file='product51.jpg', description='Cute T-shirt.'),
            Product(name='Children\'s Jeans', price=19.99, category='Children', image_file='product52.jpg', description='Durable jeans.'),
            Product(name='Children\'s Jacket', price=29.99, category='Children', image_file='product53.jpg', description='Warm jacket.'),
            Product(name='Children\'s Sneakers', price=24.99, category='Children', image_file='product54.jpg', description='Comfortable sneakers.'),
            Product(name='Children\'s Dress', price=29.99, category='Children', image_file='product55.jpg', description='Lovely dress.'),
            Product(name='Children\'s Hat', price=9.99, category='Children', image_file='product56.jpg', description='Cute hat.'),
            Product(name='Children\'s Socks', price=6.99, category='Children', image_file='product57.jpg', description='Pack of 5 socks.'),
            Product(name='Children\'s Gloves', price=9.99, category='Children', image_file='product58.jpg', description='Warm gloves.'),
            Product(name='Children\'s Scarf', price=7.99, category='Children', image_file='product59.jpg', description='Cozy scarf.'),
            Product(name='Children\'s Sunglasses', price=12.99, category='Children', image_file='product60.jpg', description='Cool sunglasses.'),
            Product(name='Children\'s Backpack', price=19.99, category='Children', image_file='product61.jpg', description='School backpack.'),
            Product(name='Children\'s Swimwear', price=14.99, category='Children', image_file='product62.jpg', description='Swimming costume.'),
            Product(name='Children\'s Shorts', price=14.99, category='Children', image_file='product63.jpg', description='Comfortable shorts.'),
            Product(name='Children\'s Hoodie', price=24.99, category='Children', image_file='product64.jpg', description='Cozy hoodie.'),
            Product(name='Children\'s Sweater', price=29.99, category='Children', image_file='product65.jpg', description='Warm sweater.'),
            Product(name='Children\'s Shoes', price=24.99, category='Children', image_file='product66.jpg', description='Comfortable shoes.'),
            Product(name='Children\'s Belt', price=9.99, category='Children', image_file='product67.jpg', description='Cute belt.'),
            Product(name='Children\'s Pajamas', price=19.99, category='Children', image_file='product68.jpg', description='Comfortable pajamas.'),
            Product(name='Children\'s Coat', price=39.99, category='Children', image_file='product69.jpg', description='Winter coat.'),
            Product(name='Children\'s Beanie', price=7.99, category='Children', image_file='product70.jpg', description='Warm beanie.'),
            Product(name='Children\'s Slippers', price=14.99, category='Children', image_file='product71.jpg', description='Cute slippers.'),
            Product(name='Children\'s Watch', price=19.99, category='Children', image_file='product72.jpg', description='Colorful watch.'),
            Product(name='Children\'s Hair Accessories', price=9.99, category='Children', image_file='product73.jpg', description='Pack of hair accessories.'),
            Product(name='Children\'s Books', price=14.99, category='Children', image_file='product74.jpg', description='Pack of story books.'),
            Product(name='Children\'s Toys', price=19.99, category='Children', image_file='product75.jpg', description='Fun toys.')
        ]
        db.session.add_all(products)
        db.session.commit()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shop')
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@app.route('/category/<category>')
def category(category):
    products = Product.query.filter_by(category=category).all()
    return render_template('category.html', products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    if product_id:
        product = Product.query.get(product_id)
        if product:
            cart = session.get('cart', {})
            if product_id in cart:
                cart[product_id]['quantity'] += 1
            else:
                cart[product_id] = {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'quantity': 1,
                    'image_file': product.image_file
                }
            session['cart'] = cart
            return jsonify({'success': True, 'cart': cart})
    return jsonify({'success': False})

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    if product_id:
        cart = session.get('cart', {})
        if product_id in cart:
            if cart[product_id]['quantity'] > 1:
                cart[product_id]['quantity'] -= 1
            else:
                del cart[product_id]
            session['cart'] = cart
            return jsonify({'success': True, 'cart': cart})
    return jsonify({'success': False})

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    return render_template('cart.html', cart=cart)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/complete_checkout', methods=['POST'])
def complete_checkout():
    # Logic to process payment and clear cart
    session.pop('cart', None)
    return redirect(url_for('home'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Process the form data (e.g., send email, store in database)
        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact'))  # Redirect to contact page or home page

    return render_template('contact.html', form=form)

@app.route('/send_message', methods=['POST'])
def send_message():
    # Logic to handle message sending
    return 'Message sent successfully'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
