from flask import request, jsonify
from db import get_connection


# CREATE
def crear_resultado():

    data = request.json

    id_detalle = data["id_detalle"]
    resultado = data["resultado"]
    fecha_resultado = data["fecha_resultado"]

    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM detalle_orden WHERE id_detalle = %s",
        (id_detalle,)
    )

    detalle = cursor.fetchone()

    if not detalle:
        cursor.close()
        conexion.close()
        return jsonify({"error": "Detalle no encontrado"}), 404

    cursor.execute(
        """
        INSERT INTO resultado
        (id_detalle, resultado, fecha_resultado)
        VALUES (%s, %s, %s)
        """,
        (id_detalle, resultado, fecha_resultado)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({"mensaje": "Resultado registrado"}), 201


# READ ALL
def obtener_resultados():

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM resultado")

    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(resultados)


# READ ONE
def obtener_resultado(id):

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM resultado WHERE id_resultado = %s",
        (id,)
    )

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    if not resultado:
        return jsonify({"error": "Resultado no encontrado"}), 404

    return jsonify(resultado)


# UPDATE
def actualizar_resultado(id):

    data = request.json

    id_detalle = data["id_detalle"]
    resultado = data["resultado"]
    fecha_resultado = data["fecha_resultado"]

    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM resultado WHERE id_resultado = %s",
        (id,)
    )

    existe = cursor.fetchone()

    if not existe:
        cursor.close()
        conexion.close()
        return jsonify({"error": "Resultado no encontrado"}), 404

    cursor.execute(
        "SELECT * FROM detalle_orden WHERE id_detalle = %s",
        (id_detalle,)
    )

    detalle = cursor.fetchone()

    if not detalle:
        cursor.close()
        conexion.close()
        return jsonify({"error": "Detalle no encontrado"}), 404

    cursor.execute(
        """
        UPDATE resultado
        SET id_detalle = %s,
            resultado = %s,
            fecha_resultado = %s
        WHERE id_resultado = %s
        """,
        (id_detalle, resultado, fecha_resultado, id)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({"mensaje": "Resultado actualizado"})


# DELETE
def eliminar_resultado(id):

    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM resultado WHERE id_resultado = %s",
        (id,)
    )

    existe = cursor.fetchone()

    if not existe:
        cursor.close()
        conexion.close()
        return jsonify({"error": "Resultado no encontrado"}), 404

    cursor.execute(
        "DELETE FROM resultado WHERE id_resultado = %s",
        (id,)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({"mensaje": "Resultado eliminado"})