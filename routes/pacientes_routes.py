from flask import Blueprint

from controllers.pacientes_controller import (
    obtener_pacientes,
    obtener_paciente,
    crear_paciente,
    actualizar_paciente,
    eliminar_paciente
)

pacientes_bp = Blueprint("pacientes", __name__)


# GET TODOS
@pacientes_bp.route("/pacientes", methods=["GET"])
def get_pacientes():
    return obtener_pacientes()


# GET POR ID
@pacientes_bp.route("/pacientes/<int:id>", methods=["GET"])
def get_paciente(id):
    return obtener_paciente(id)


# POST
@pacientes_bp.route("/pacientes", methods=["POST"])
def post_paciente():
    return crear_paciente()

# PUT
@pacientes_bp.route("/pacientes/<int:id>", methods=["PUT"])
def put_paciente(id):
    return actualizar_paciente(id)

# DELETE
@pacientes_bp.route("/pacientes/<int:id>", methods=["DELETE"])
def delete_paciente(id):
    return eliminar_paciente(id)

