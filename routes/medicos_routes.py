from flask import Blueprint
from flask import request

from controllers.medicos_controller import (
    obtener_medicos,
    obtener_medico,
    crear_medico,
    actualizar_medico,
    eliminar_medico
)

medicos_bp = Blueprint("medicos", __name__)


# GET TODOS LOS MEDICOS
@medicos_bp.route("/medicos", methods=["GET"])
def get_medicos():

    return obtener_medicos()


# GET MEDICO POR ID
@medicos_bp.route("/medicos/<int:id>", methods=["GET"])
def get_medico(id):

    return obtener_medico(id)


# POST CREAR MEDICO
@medicos_bp.route("/medicos", methods=["POST"])
def post_medico():

    data = request.get_json()

    return crear_medico(data)


# PUT ACTUALIZAR MEDICO
@medicos_bp.route("/medicos/<int:id>", methods=["PUT"])
def put_medico(id):

    data = request.get_json()

    return actualizar_medico(id, data)


# DELETE MEDICO
@medicos_bp.route("/medicos/<int:id>", methods=["DELETE"])
def delete_medico(id):

    return eliminar_medico(id)