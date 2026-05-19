from flask import Flask

from routes.pacientes_routes import pacientes_bp
from routes.citas_routes import citas_bp

app = Flask(__name__)

app.register_blueprint(pacientes_bp)

app.register_blueprint(citas_bp)

@app.route("/")
def inicio():
    return "API Hospitalaria funcionando 🚀"


if __name__ == "__main__":
    app.run(debug=True)

   