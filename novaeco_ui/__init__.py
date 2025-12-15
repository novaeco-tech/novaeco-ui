from flask import Blueprint

# Create a Blueprint that knows where its 'static' and 'templates' folders are
novaeco_ui_bp = Blueprint(
    'novaeco_ui', 
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/novaeco_ui'
)