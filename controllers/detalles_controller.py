from flask import request, jsonify
from db import get_connection


# POST CREAR DETALLE
def crear_detalle():

    data = request.get_json()

    campos_obligatorios = [
        "id_orden",
        "id_estudio"
    ]

    for campo in campos_obligatorios:
        if campo not in data or not data[campo]:
            return jsonify({
                "error": f"El campo {campo} es obligatorio"
            }), 400

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    # VALIDAR ORDEN
    cursor.execute(
        """
        SELECT id_orden
        FROM orden_laboratorio
        WHERE id_orden = %s
        """,
        (data["id_orden"],)
    )

    orden = cursor.fetchone()

    if not orden:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Orden no encontrada"
        }), 404

    # VALIDAR ESTUDIO
    cursor.execute(
        """
        SELECT id_estudio
        FROM estudio
        WHERE id_estudio = %s
        """,
        (data["id_estudio"],)
    )

    estudio = cursor.fetchone()

    if not estudio:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Estudio no encontrado"
        }), 404

    # VALIDAR DUPLICADO
    cursor.execute(
        """
        SELECT id_detalle
        FROM detalle_orden
        WHERE id_orden = %s
        AND id_estudio = %s
        """,
        (
            data["id_orden"],
            data["id_estudio"]
        )
    )

    detalle_existente = cursor.fetchone()

    if detalle_existente:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Ese estudio ya fue agregado a la orden"
        }), 400

    query = """
    INSERT INTO detalle_orden
    (
        id_orden,
        id_estudio
    )
    VALUES
    (
        %s,
        %s
    )
    """

    valores = (
        data["id_orden"],
        data["id_estudio"]
    )

    cursor.execute(query, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Detalle registrado"
    }), 201


# GET TODOS
def obtener_detalles():

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM detalle_orden
        """
    )

    detalles = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(detalles)


# GET POR ID
def obtener_detalle(id):

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM detalle_orden
        WHERE id_detalle = %s
        """,
        (id,)
    )

    detalle = cursor.fetchone()

    cursor.close()
    conexion.close()

    if not detalle:
        return jsonify({
            "error": "Detalle no encontrado"
        }), 404

    return jsonify(detalle)


# PUT
def actualizar_detalle(id):

    data = request.get_json()

    campos_obligatorios = [
        "id_orden",
        "id_estudio"
    ]

    for campo in campos_obligatorios:
        if campo not in data or not data[campo]:
            return jsonify({
                "error": f"El campo {campo} es obligatorio"
            }), 400

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT id_detalle
        FROM detalle_orden
        WHERE id_detalle = %s
        """,
        (id,)
    )

    detalle = cursor.fetchone()

    if not detalle:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Detalle no encontrado"
        }), 404

    query = """
    UPDATE detalle_orden
    SET
        id_orden = %s,
        id_estudio = %s
    WHERE id_detalle = %s
    """

    valores = (
        data["id_orden"],
        data["id_estudio"],
        id
    )

    cursor.execute(query, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Detalle actualizado"
    })


# DELETE
def eliminar_detalle(id):

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT id_detalle
        FROM detalle_orden
        WHERE id_detalle = %s
        """,
        (id,)
    )

    detalle = cursor.fetchone()

    if not detalle:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Detalle no encontrado"
        }), 404

    cursor.execute(
        """
        DELETE FROM detalle_orden
        WHERE id_detalle = %s
        """,
        (id,)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Detalle eliminado"
    })