from flask import Blueprint

from controllers.detalles_controller import (
    crear_detalle,
    obtener_detalles,
    obtener_detalle,
    actualizar_detalle,
    eliminar_detalle
)

detalles_bp = Blueprint("detalles_bp", __name__)

# CREATE
detalles_bp.route(
    "/detalles",
    methods=["POST"]
)(crear_detalle)

# READ TODOS
detalles_bp.route(
    "/detalles",
    methods=["GET"]
)(obtener_detalles)

# READ UNO
detalles_bp.route(
    "/detalles/<int:id>",
    methods=["GET"]
)(obtener_detalle)

# UPDATE
detalles_bp.route(
    "/detalles/<int:id>",
    methods=["PUT"]
)(actualizar_detalle)

# DELETE
detalles_bp.route(
    "/detalles/<int:id>",
    methods=["DELETE"]
)(eliminar_detalle)