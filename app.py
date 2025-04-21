from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='shreya_janu_28',
        database='data'
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/electronics')
def electronics():
    return render_template('electronics.html')

@app.route('/beauty')
def beauty():
    return render_template('beauty.html')

@app.route('/furniture')
def furniture():
    return render_template('furniture.html')

@app.route('/mobile_acc')
def mobile_acc():
    return render_template('mobile_acc.html')

@app.route('/grocery')
def grocery():
    return render_template('grocery.html')

@app.route('/footwear_bags')
def footwear_bags():
    return render_template('footwear_bags.html')

@app.route('/index-perfume')
def perfume():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT pro_id, pro_name, img_path FROM beauty_index')
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index-perfume.html', products=products)

@app.route('/product-perfume/<int:product_id>/<string:product_name>')

def pro_perfume(product_id, product_name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT *
        FROM beauty
        WHERE pro_id = %s
    ''', (product_id,))
    product_details = cursor.fetchall()
    cursor.close()
    connection.close()

    recommended_website = min(product_details, key=lambda x: x['price'])
    return render_template('product-perfume.html',produc_name=product_name,product_details=product_details,recommended_website=recommended_website)

@app.route('/index-lotion')
def lotion():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT p_id, pro_name, img_path FROM lotion_index')
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index-lotion.html', products=products)

@app.route('/product-lotion/<int:product_id>/<string:product_name>')
def pro_lotion(product_id,product_name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT *
        FROM lotion
        WHERE p_id = %s
    ''', (product_id,))
    product_details = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('product-lotion.html', product_name=product_name, product_details=product_details)

@app.route('/index-grooming')
def grooming():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT prod_id, pro_name, img_path FROM grooming_index')
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index-grooming.html', products=products)

@app.route('/product-grooming/<int:product_id>/<string:product_name>')
def pro_grooming(product_id,product_name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT *
        FROM grooming
        WHERE prod_id = %s
    ''', (product_id,))
    product_details = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('product-grooming.html', product_name=product_name, product_details=product_details)

@app.route('/index-makeup')
def makeup():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT pr_id, pro_name, img_path FROM makeup_index')
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index-makeup.html', products=products)

@app.route('/product-makeup/<int:product_id>/<string:product_name>')
def pro_makeup(product_id,product_name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT *
        FROM makeup
        WHERE pr_id = %s
    ''', (product_id,))
    product_details = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('product-makeup.html', product_name=product_name, product_details=product_details)

@app.route('/index-pack')
def pack():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT i_id, pro_name, img_path FROM pack_index')
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index-pack.html', products=products)

@app.route('/product-pack/<int:product_id>/<string:product_name>')
def pro_pack(product_id,product_name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT *
        FROM pack
        WHERE i_id = %s
    ''', (product_id,))
    product_details = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('product-pack.html', product_name=product_name, product_details=product_details)

@app.route('/index-acc')
def acc():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT product_id, pro_name, img_path FROM acc_index')
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index-acc.html', products=products)

@app.route('/product-acc/<int:product_id>/<string:product_name>')
def pro_acc(product_id,product_name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT *
        FROM acc
        WHERE product_id = %s
    ''', (product_id,))
    product_details = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('product-acc.html', product_name=product_name, product_details=product_details)

@app.route('/index-masala')
def masala():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT m_id, pro_name, img_path FROM masala_index')
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index-masala.html', products=products)

@app.route('/product-masala/<int:product_id>/<string:product_name>')

def pro_masala(product_id, product_name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT *
        FROM masala
        WHERE m_id = %s
    ''', (product_id,))
    product_details = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('product-masala.html', product_name=product_name, product_details=product_details)


if __name__ == '__main__':
    app.run(debug=True)

