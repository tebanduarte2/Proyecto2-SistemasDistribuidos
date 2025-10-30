from flask import Flask, render_template
from extensions import db, login_manager
from models.user import User
import os

app = Flask(__name__)

# ========================================
# CONFIGURACIÓN DESDE VARIABLES DE ENTORNO
# ========================================
# Secret Key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secretkey')

# Base de datos - Leer de variables de entorno
DB_HOST = os.getenv('DB_HOST', 'db')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_NAME = os.getenv('DB_NAME', 'bookstore')
DB_USER = os.getenv('DB_USER', 'bookstore_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'bookstore_pass')

# Construir URI de MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ========================================
# INICIALIZACIÓN
# ========================================
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Importar blueprints
from controllers.auth_controller import auth
from controllers.book_controller import book
from controllers.purchase_controller import purchase
from controllers.payment_controller import payment
from controllers.delivery_controller import delivery
from controllers.admin_controller import admin

# Registrar blueprints
app.register_blueprint(auth)
app.register_blueprint(book, url_prefix='/book')
app.register_blueprint(purchase)
app.register_blueprint(payment)
app.register_blueprint(delivery)
app.register_blueprint(admin)

from models.delivery import DeliveryProvider

def initialize_delivery_providers():
    with app.app_context():
        if DeliveryProvider.query.count() == 0:
            providers = [
                DeliveryProvider(name="DHL", coverage_area="Internacional", cost=50.0),
                DeliveryProvider(name="FedEx", coverage_area="Internacional", cost=45.0),
                DeliveryProvider(name="Envia", coverage_area="Nacional", cost=20.0),
                DeliveryProvider(name="Servientrega", coverage_area="Nacional", cost=15.0),
            ]
            db.session.bulk_save_objects(providers)
            db.session.commit()

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    # OJO: Este contexto crea las tablas e inicia los proveedores de entrega
    # Se debe ejecutar cada vez que se reinstala y ejecuta la aplicación Bookstore
    with app.app_context():
        db.create_all()
        initialize_delivery_providers()
    
    # Cambiar debug=False en producción
    app.run(host="0.0.0.0", port=5000, debug=False)