from flask import Blueprint

from controllers.resultados_controller import (
    crear_resultado,
    obtener_resultados,
    obtener_resultado,
    actualizar_resultado,
    eliminar_resultado
)

resultados_bp = Blueprint("resultados", __name__)

resultados_bp.route("/resultados", methods=["POST"])(crear_resultado)
resultados_bp.route("/resultados", methods=["GET"])(obtener_resultados)
resultados_bp.route("/resultados/<int:id>", methods=["GET"])(obtener_resultado)
resultados_bp.route("/resultados/<int:id>", methods=["PUT"])(actualizar_resultado)
resultados_bp.route("/resultados/<int:id>", methods=["DELETE"])(eliminar_resultado)