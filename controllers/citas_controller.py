from flask import jsonify
from db import get_connection


# GET TODAS LAS CITAS
def obtener_citas():

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    query = """
    SELECT 
        c.id_cita,
        p.nombre AS paciente,
        c.fecha,
        CAST(c.hora AS CHAR) AS hora,
        c.estado
    FROM cita c
    INNER JOIN paciente p
        ON c.id_paciente = p.id_paciente
    """

    cursor.execute(query)

    citas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(citas)


# GET CITA POR ID
def obtener_cita(id):

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    query = """
    SELECT 
        c.id_cita,
        p.nombre AS paciente,
        c.fecha,
        CAST(c.hora AS CHAR) AS hora,
        c.estado
    FROM cita c
    INNER JOIN paciente p
        ON c.id_paciente = p.id_paciente
    WHERE c.id_cita = %s
    """

    cursor.execute(query, (id,))

    cita = cursor.fetchone()

    cursor.close()
    conexion.close()

    if cita:
        return jsonify(cita)

    return jsonify({
        "error": "Cita no encontrada"
    }), 404


# POST CREAR CITA
def crear_cita(data):

    # VALIDAR CAMPOS OBLIGATORIOS
    campos_obligatorios = [
        "id_paciente",
        "id_medico",
        "fecha",
        "hora",
        "motivo"
    ]

    for campo in campos_obligatorios:
        if campo not in data or not data[campo]:
            return jsonify({
                "error": f"El campo {campo} es obligatorio"
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
        (data["id_paciente"],)
    )

    paciente = cursor.fetchone()

    if not paciente:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "El paciente no existe"
        }), 400

    # VALIDAR MEDICO EXISTE
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
            "error": "El médico no existe"
        }), 400

    # VALIDAR HORARIO DISPONIBLE
    cursor.execute(
        """
        SELECT id_cita
        FROM cita
        WHERE id_medico = %s
        AND fecha = %s
        AND hora = %s
        """,
        (
            data["id_medico"],
            data["fecha"],
            data["hora"]
        )
    )

    cita_existente = cursor.fetchone()

    if cita_existente:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "El horario ya está ocupado"
        }), 400

    # INSERTAR CITA
    query = """
    INSERT INTO cita
    (id_paciente, id_medico, fecha, hora, motivo)
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        data["id_paciente"],
        data["id_medico"],
        data["fecha"],
        data["hora"],
        data["motivo"]
    )

    cursor.execute(query, valores)

    conexion.commit()

    nueva_cita = cursor.lastrowid

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Cita creada",
        "id_cita": nueva_cita
    }), 201



# PUT ACTUALIZAR CITA
def actualizar_cita(id, data):

    # VALIDAR CAMPOS OBLIGATORIOS
    campos_obligatorios = [
        "id_paciente",
        "id_medico",
        "fecha",
        "hora",
        "motivo",
        "estado"
    ]

    for campo in campos_obligatorios:
        if campo not in data or not data[campo]:
            return jsonify({
                "error": f"El campo {campo} es obligatorio"
            }), 400

    # VALIDAR ESTADO
    estados_validos = [
        "Programada",
        "Atendida",
        "Cancelada"
    ]

    if data["estado"] not in estados_validos:
        return jsonify({
            "error": "Estado inválido"
        }), 400

    conexion = get_connection()
    cursor = conexion.cursor()

    # VALIDAR CITA EXISTE
    cursor.execute(
        """
        SELECT id_cita
        FROM cita
        WHERE id_cita = %s
        """,
        (id,)
    )

    cita = cursor.fetchone()

    if not cita:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Cita no encontrada"
        }), 404

    # VALIDAR PACIENTE EXISTE
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
            "error": "El paciente no existe"
        }), 400

    # VALIDAR MEDICO EXISTE
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
            "error": "El médico no existe"
        }), 400

    # VALIDAR HORARIO DISPONIBLE
    cursor.execute(
        """
        SELECT id_cita
        FROM cita
        WHERE id_medico = %s
        AND fecha = %s
        AND hora = %s
        AND id_cita <> %s
        """,
        (
            data["id_medico"],
            data["fecha"],
            data["hora"],
            id
        )
    )

    cita_existente = cursor.fetchone()

    if cita_existente:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "El horario ya está ocupado"
        }), 400

    # ACTUALIZAR CITA
    query = """
    UPDATE cita
    SET
        id_paciente = %s,
        id_medico = %s,
        fecha = %s,
        hora = %s,
        motivo = %s,
        estado = %s
    WHERE id_cita = %s
    """

    valores = (
        data["id_paciente"],
        data["id_medico"],
        data["fecha"],
        data["hora"],
        data["motivo"],
        data["estado"],
        id
    )

    cursor.execute(query, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Cita actualizada"
    })




# DELETE CITA
def eliminar_cita(id):

    conexion = get_connection()
    cursor = conexion.cursor()

    query = "DELETE FROM cita WHERE id_cita = %s"

    cursor.execute(query, (id,))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas_afectadas == 0:
        return jsonify({
            "error": "Cita no encontrada"
        }), 404

    return jsonify({
        "mensaje": "Cita eliminada"
    })