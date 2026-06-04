from flask import jsonify, request
from db import get_connection


# POST CREAR ESTUDIO
def crear_estudio():

    data = request.get_json()

    campos_obligatorios = [
        "nombre"
    ]

    for campo in campos_obligatorios:
        if campo not in data or not data[campo]:
            return jsonify({
                "error": f"El campo {campo} es obligatorio"
            }), 400

    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT id_estudio
        FROM estudio
        WHERE nombre = %s
        """,
        (data["nombre"],)
    )

    estudio_existente = cursor.fetchone()

    if estudio_existente:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "El estudio ya existe"
        }), 400

    query = """
    INSERT INTO estudio
    (
        nombre,
        descripcion
    )
    VALUES
    (
        %s,
        %s
    )
    """

    valores = (
        data["nombre"],
        data.get("descripcion")
    )

    cursor.execute(query, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Estudio registrado"
    }), 201


# GET TODOS LOS ESTUDIOS
def obtener_estudios():

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
    SELECT *
    FROM estudio
    """)

    estudios = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(estudios)


# GET ESTUDIO POR ID
def obtener_estudio(id):

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM estudio
        WHERE id_estudio = %s
        """,
        (id,)
    )

    estudio = cursor.fetchone()

    cursor.close()
    conexion.close()

    if not estudio:
        return jsonify({
            "error": "Estudio no encontrado"
        }), 404

    return jsonify(estudio)


# PUT ACTUALIZAR ESTUDIO
def actualizar_estudio(id):

    data = request.get_json()

    if "nombre" not in data or not data["nombre"]:
        return jsonify({
            "error": "El nombre es obligatorio"
        }), 400

    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT id_estudio
        FROM estudio
        WHERE id_estudio = %s
        """,
        (id,)
    )

    estudio = cursor.fetchone()

    if not estudio:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Estudio no encontrado"
        }), 404

    cursor.execute(
        """
        SELECT id_estudio
        FROM estudio
        WHERE nombre = %s
        AND id_estudio <> %s
        """,
        (
            data["nombre"],
            id
        )
    )

    estudio_existente = cursor.fetchone()

    if estudio_existente:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "El estudio ya existe"
        }), 400

    query = """
    UPDATE estudio
    SET
        nombre = %s,
        descripcion = %s
    WHERE id_estudio = %s
    """

    valores = (
        data["nombre"],
        data.get("descripcion"),
        id
    )

    cursor.execute(query, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Estudio actualizado"
    })


# DELETE ESTUDIO
def eliminar_estudio(id):

    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT id_estudio
        FROM estudio
        WHERE id_estudio = %s
        """,
        (id,)
    )

    estudio = cursor.fetchone()

    if not estudio:
        cursor.close()
        conexion.close()

        return jsonify({
            "error": "Estudio no encontrado"
        }), 404

    cursor.execute(
        """
        DELETE FROM estudio
        WHERE id_estudio = %s
        """,
        (id,)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Estudio eliminado"
    })