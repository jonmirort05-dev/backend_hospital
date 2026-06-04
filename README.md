# Sistema Hospitalario - Backend

## Descripción

Backend desarrollado en Flask para la gestión de un sistema hospitalario.

Incluye los siguientes módulos:

- Pacientes
- Médicos
- Citas
- Estudios
- Órdenes de laboratorio
- Detalles de órdenes
- Resultados

Todos los módulos cuentan con operaciones CRUD completas.

---

## Tecnologías utilizadas

- Python 3.12
- Flask 3.1.3
- MySQL 8
- mysql-connector-python 9.7.0

---

## Instalación

### 1. Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Entrar al proyecto

```bash
cd backend_flask
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Base de datos

Importar el archivo:

```text
hospital.sql
```

en MySQL Workbench.

El script crea automáticamente la base de datos y las tablas necesarias.

---

## Configuración

Modificar las credenciales de conexión en:

```text
db.py
```

Ejemplo:

```python
host="localhost"
user="root"
password="root123"
database="hospital"
```

---

## Ejecutar proyecto

```bash
python app.py
```

Servidor:

```text
http://127.0.0.1:5000
```

---

## Endpoints principales

### Pacientes

```text
GET     /pacientes
GET     /pacientes/<id>
POST    /pacientes
PUT     /pacientes/<id>
DELETE  /pacientes/<id>
```

### Médicos

```text
GET     /medicos
GET     /medicos/<id>
POST    /medicos
PUT     /medicos/<id>
DELETE  /medicos/<id>
```

### Estudios

```text
GET     /estudios
GET     /estudios/<id>
POST    /estudios
PUT     /estudios/<id>
DELETE  /estudios/<id>
```

### Órdenes de laboratorio

```text
GET     /ordenes
GET     /ordenes/<id>
POST    /ordenes
PUT     /ordenes/<id>
DELETE  /ordenes/<id>
```

### Detalles de orden

```text
GET     /detalles
GET     /detalles/<id>
POST    /detalles
PUT     /detalles/<id>
DELETE  /detalles/<id>
```

### Resultados

```text
GET     /resultados
GET     /resultados/<id>
POST    /resultados
PUT     /resultados/<id>
DELETE  /resultados/<id>
```

---

## Autor

Jonathan Eduardo Miranda Ortega
ESCOM - IPN
