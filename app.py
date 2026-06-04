from flask import Flask

from routes.pacientes_routes import pacientes_bp
from routes.citas_routes import citas_bp
from routes.medicos_routes import medicos_bp
from routes.estudios_routes import estudios_bp
from routes.ordenes_routes import ordenes_bp
from routes.detalles_routes import detalles_bp
from routes.resultados_routes import resultados_bp

app = Flask(__name__)

app.register_blueprint(pacientes_bp)

app.register_blueprint(citas_bp)

app.register_blueprint(medicos_bp)

app.register_blueprint(estudios_bp)

app.register_blueprint(resultados_bp)

app.register_blueprint(ordenes_bp)

app.register_blueprint(detalles_bp)

@app.route("/")
def inicio():
    return "API Hospitalaria funcionando 🚀"


if __name__ == "__main__":
    app.run(debug=True)

   