from flask import Blueprint

from controllers.estudios_controller import (
    crear_estudio,
    obtener_estudios,
    obtener_estudio,
    actualizar_estudio,
    eliminar_estudio
)

estudios_bp = Blueprint("estudios", __name__)


# POST
estudios_bp.route(
    "/estudios",
    methods=["POST"]
)(crear_estudio)


# GET TODOS
estudios_bp.route(
    "/estudios",
    methods=["GET"]
)(obtener_estudios)


# GET POR ID
estudios_bp.route(
    "/estudios/<int:id>",
    methods=["GET"]
)(obtener_estudio)


# PUT
estudios_bp.route(
    "/estudios/<int:id>",
    methods=["PUT"]
)(actualizar_estudio)


# DELETE
estudios_bp.route(
    "/estudios/<int:id>",
    methods=["DELETE"]
)(eliminar_estudio)