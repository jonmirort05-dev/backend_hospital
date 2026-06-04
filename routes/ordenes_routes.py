from flask import Blueprint, request
from controllers.ordenes_controller import (
    crear_orden,
    obtener_ordenes,
    obtener_orden,
    actualizar_orden,
    eliminar_orden
)

ordenes_bp = Blueprint("ordenes", __name__)


# POST
@ordenes_bp.route("/ordenes", methods=["POST"])
def post_orden():
    return crear_orden()


# GET TODOS
@ordenes_bp.route("/ordenes", methods=["GET"])
def get_ordenes():
    return obtener_ordenes()


# GET POR ID
@ordenes_bp.route("/ordenes/<int:id>", methods=["GET"])
def get_orden(id):
    return obtener_orden(id)


# PUT
@ordenes_bp.route("/ordenes/<int:id>", methods=["PUT"])
def put_orden(id):
    return actualizar_orden(id)


# DELETE
@ordenes_bp.route("/ordenes/<int:id>", methods=["DELETE"])
def delete_orden(id):
    return eliminar_orden(id)