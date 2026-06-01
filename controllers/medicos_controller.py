from flask import jsonify
from db import get_connection


# GET TODOS LOS MEDICOS
def obtener_medicos():

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    query = """
    SELECT *
    FROM medico
    """

    cursor.execute(query)

    medicos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(medicos)


# GET MEDICO POR ID
def obtener_medico(id):

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    query = """
    SELECT *
    FROM medico
    WHERE id_medico = %s
    """

    cursor.execute(query, (id,))

    medico = cursor.fetchone()

    cursor.close()
    conexion.close()

    if medico:
        return jsonify(medico)

    return jsonify({
        "error": "Medico no encontrado"
    }), 404


# POST CREAR MEDICO
def crear_medico(data):

    # VALIDAR CAMPOS OBLIGATORIOS
    campos_obligatorios = [
        "nombre",
        "especialidad",
        "cedula_profesional"
    ]

    for campo in campos_obligatorios:
        if campo not in data or not data[campo]:
            return jsonify({
                "error": f"El campo {campo} es obligatorio"
            }), 400

    conexion = get_connection()
    cursor = conexion.cursor()

    # VALIDAR CEDULA DUPLICADA
    cursor.execute(
        """
        SELECT id_medico
        FROM medico
        WHERE cedula_profesional = %s
        """,
        (data["cedula_profesional"],)
    )

    existe = cursor.fetchone()

    if existe:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "La cédula profesional ya está registrada"
        }), 400

    # INSERTAR MEDICO
    query = """
    INSERT INTO medico
    (nombre, especialidad, cedula_profesional)
    VALUES (%s, %s, %s)
    """

    valores = (
        data["nombre"],
        data["especialidad"],
        data["cedula_profesional"]
    )

    cursor.execute(query, valores)

    conexion.commit()

    nuevo_medico = cursor.lastrowid

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Medico creado",
        "id_medico": nuevo_medico
    }), 201


# PUT ACTUALIZAR MEDICO
def actualizar_medico(id, data):

    conexion = get_connection()
    cursor = conexion.cursor()

    query = """
    UPDATE medico
    SET
        nombre = %s,
        especialidad = %s,
        cedula_profesional = %s
    WHERE id_medico = %s
    """

    valores = (
        data["nombre"],
        data["especialidad"],
        data["cedula_profesional"],
        id
    )

    cursor.execute(query, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Medico actualizado"
    })


# DELETE MEDICO
def eliminar_medico(id):

    conexion = get_connection()
    cursor = conexion.cursor()

    query = """
    DELETE FROM medico
    WHERE id_medico = %s
    """

    cursor.execute(query, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Medico eliminado"
    })