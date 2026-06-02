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
# PUT ACTUALIZAR PACIENTE
# PUT ACTUALIZAR PACIENTE
def actualizar_paciente(id):

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

    # VALIDAR PACIENTE EXISTE
    cursor.execute(
        """
        SELECT id_paciente
        FROM paciente
        WHERE id_paciente = %s
        """,
        (id,)
    )

    paciente = cursor.fetchone()

    if not paciente:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Paciente no encontrado"
        }), 404

    # VALIDAR CURP DUPLICADA
    cursor.execute(
        """
        SELECT id_paciente
        FROM paciente
        WHERE curp = %s
        AND id_paciente <> %s
        """,
        (
            data["curp"],
            id
        )
    )

    curp_existente = cursor.fetchone()

    if curp_existente:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "La CURP ya está registrada"
        }), 400

    # ACTUALIZAR PACIENTE
    query = """
    UPDATE paciente
    SET
        nombre = %s,
        apellido_paterno = %s,
        apellido_materno = %s,
        curp = %s,
        fecha_nacimiento = %s,
        sexo = %s
    WHERE id_paciente = %s
    """

    valores = (
        data["nombre"],
        data["apellido_paterno"],
        data["apellido_materno"],
        data["curp"],
        data["fecha_nacimiento"],
        data["sexo"],
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

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas_afectadas == 0:
        return jsonify({
            "error": "Paciente no encontrado"
        }), 404

    return jsonify({
        "mensaje": "Paciente eliminado"
    })