from flask import jsonify, request
from db import get_connection


# GET TODOS LOS PACIENTES
def obtener_pacientes():

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    query = "SELECT * FROM paciente"
    cursor.execute(query)

    pacientes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(pacientes)


# GET PACIENTE POR ID
def obtener_paciente(id):

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    query = "SELECT * FROM paciente WHERE id_paciente = %s"
    cursor.execute(query, (id,))

    paciente = cursor.fetchone()

    cursor.close()
    conexion.close()

    if paciente:
        return jsonify(paciente)

    return jsonify({"error": "Paciente no encontrado"}), 404


# POST CREAR PACIENTE
def crear_paciente():

    data = request.get_json()

    # VALIDAR CAMPOS OBLIGATORIOS
    campos_obligatorios = [
        "nombre",
        "apellido_paterno",
        "apellido_materno",
        "curp",
        "fecha_nacimiento",
        "sexo"
    ]

    for campo in campos_obligatorios:
        if campo not in data or not data[campo]:
            return jsonify({
                "error": f"El campo {campo} es obligatorio"
            }), 400

    # VALIDAR SEXO
    if data["sexo"] not in ["M", "F"]:
        return jsonify({
            "error": "El sexo debe ser M o F"
        }), 400

    conexion = get_connection()
    cursor = conexion.cursor()

    # VALIDAR CURP DUPLICADA
    cursor.execute(
        "SELECT id_paciente FROM paciente WHERE curp = %s",
        (data["curp"],)
    )

    existe = cursor.fetchone()

    if existe:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "La CURP ya está registrada"
        }), 400

    # INSERTAR PACIENTE
    query = """
    INSERT INTO paciente
    (nombre, apellido_paterno, apellido_materno, curp, fecha_nacimiento, sexo)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (
        data["nombre"],
        data["apellido_paterno"],
        data["apellido_materno"],
        data["curp"],
        data["fecha_nacimiento"],
        data["sexo"]
    )

    cursor.execute(query, valores)

    conexion.commit()

    nuevo_id = cursor.lastrowid

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Paciente creado",
        "id": nuevo_id
    }), 201


# PUT ACTUALIZAR PACIENTE
def actualizar_paciente(id):

    data = request.get_json()

    conexion = get_connection()
    cursor = conexion.cursor()

    query = """
    UPDATE paciente
    SET nombre = %s
    WHERE id_paciente = %s
    """

    valores = (
        data["nombre"],
        id
    )

    cursor.execute(query, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Paciente actualizado"
    })

# DELETE PACIENTE
def eliminar_paciente(id):

    conexion = get_connection()
    cursor = conexion.cursor()

    query = "DELETE FROM paciente WHERE id_paciente = %s"

    cursor.execute(query, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Paciente eliminado"
    })
            