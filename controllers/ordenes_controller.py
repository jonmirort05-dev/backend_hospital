from flask import request, jsonify
from db import get_connection


# POST CREAR ORDEN
def crear_orden():

    data = request.get_json()

    campos_obligatorios = [
        "id_paciente",
        "id_medico",
        "fecha"
    ]

    for campo in campos_obligatorios:
        if campo not in data or not data[campo]:
            return jsonify({
                "error": f"El campo {campo} es obligatorio"
            }), 400

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    # VALIDAR PACIENTE
    cursor.execute(
        """
        SELECT id_paciente
        FROM paciente
        WHERE id_paciente = %s
        """,
        (data["id_paciente"],)
    )

    paciente = cursor.fetchone()

    if not paciente:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Paciente no encontrado"
        }), 404

    # VALIDAR MEDICO
    cursor.execute(
        """
        SELECT id_medico
        FROM medico
        WHERE id_medico = %s
        """,
        (data["id_medico"],)
    )

    medico = cursor.fetchone()

    if not medico:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Medico no encontrado"
        }), 404

    query = """
    INSERT INTO orden_laboratorio
    (
        id_paciente,
        id_medico,
        fecha
    )
    VALUES
    (
        %s,
        %s,
        %s
    )
    """

    valores = (
        data["id_paciente"],
        data["id_medico"],
        data["fecha"]
    )

    cursor.execute(query, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Orden registrada"
    }), 201


# GET TODAS LAS ORDENES
def obtener_ordenes():

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM orden_laboratorio
        """
    )

    ordenes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(ordenes)


# GET ORDEN POR ID
def obtener_orden(id):

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM orden_laboratorio
        WHERE id_orden = %s
        """,
        (id,)
    )

    orden = cursor.fetchone()

    cursor.close()
    conexion.close()

    if not orden:
        return jsonify({
            "error": "Orden no encontrada"
        }), 404

    return jsonify(orden)


# PUT ACTUALIZAR ORDEN
def actualizar_orden(id):

    data = request.get_json()

    campos_obligatorios = [
        "id_paciente",
        "id_medico",
        "fecha"
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
        SELECT id_orden
        FROM orden_laboratorio
        WHERE id_orden = %s
        """,
        (id,)
    )

    orden = cursor.fetchone()

    if not orden:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Orden no encontrada"
        }), 404

    query = """
    UPDATE orden_laboratorio
    SET
        id_paciente = %s,
        id_medico = %s,
        fecha = %s
    WHERE id_orden = %s
    """

    valores = (
        data["id_paciente"],
        data["id_medico"],
        data["fecha"],
        id
    )

    cursor.execute(query, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Orden actualizada"
    })


# DELETE ORDEN
def eliminar_orden(id):

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT id_orden
        FROM orden_laboratorio
        WHERE id_orden = %s
        """,
        (id,)
    )

    orden = cursor.fetchone()

    if not orden:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Orden no encontrada"
        }), 404

    cursor.execute(
        """
        DELETE FROM orden_laboratorio
        WHERE id_orden = %s
        """,
        (id,)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Orden eliminada"
    })