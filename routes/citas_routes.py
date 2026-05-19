from flask import Blueprint
from controllers.citas_controller import (
    obtener_citas,
    crear_cita,
    obtener_cita,
    actualizar_cita,
    eliminar_cita
)

citas_bp = Blueprint("citas", __name__)

# GET TODAS LAS CITAS
@citas_bp.route("/citas", methods=["GET"])
def get_citas():
    return obtener_citas()

# POST CREAR CITA
@citas_bp.route("/citas", methods=["POST"])
def post_cita():

    from flask import request

    data = request.get_json()

    return crear_cita(data)

# GET CITA POR ID
@citas_bp.route("/citas/<int:id>", methods=["GET"])
def get_cita(id):

    return obtener_cita(id)

# PUT ACTUALIZAR CITA
@citas_bp.route("/citas/<int:id>", methods=["PUT"])
def put_cita(id):

    from flask import request

    data = request.get_json()

    return actualizar_cita(id, data)

# DELETE ELIMINAR CITA
@citas_bp.route("/citas/<int:id>", methods=["DELETE"])
def delete_cita(id):

    return eliminar_cita(id)