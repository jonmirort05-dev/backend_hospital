# Sistema Hospitalario - Backend

Backend desarrollado en Flask y MySQL para la gestión de pacientes, médicos y citas.

## Tecnologías utilizadas

- Python
- Flask
- MySQL
- MySQL Connector

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/jonmirort05-dev/backend_hospital.git
```

Entrar al proyecto:

```bash
cd backend_hospital
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecutar servidor

```bash
python app.py
```

Servidor disponible en:

```text
http://127.0.0.1:5000
```

---

# Endpoints

## Pacientes

### Obtener todos los pacientes

```http
GET /pacientes
```

### Obtener paciente por ID

```http
GET /pacientes/<id>
```

### Crear paciente

```http
POST /pacientes
```

### Actualizar paciente

```http
PUT /pacientes/<id>
```

### Eliminar paciente

```http
DELETE /pacientes/<id>
```

---

## Médicos

### Obtener todos los médicos

```http
GET /medicos
```

### Obtener médico por ID

```http
GET /medicos/<id>
```

### Crear médico

```http
POST /medicos
```

### Actualizar médico

```http
PUT /medicos/<id>
```

### Eliminar médico

```http
DELETE /medicos/<id>
```

---

## Citas

### Obtener todas las citas

```http
GET /citas
```

### Obtener cita por ID

```http
GET /citas/<id>
```

### Crear cita

```http
POST /citas
```

### Actualizar cita

```http
PUT /citas/<id>
```

### Eliminar cita

```http
DELETE /citas/<id>
```

---

# Funcionalidades implementadas

- CRUD de pacientes
- CRUD de médicos
- CRUD de citas
- Validación de CURP única
- Validación de cédula profesional única
- Validación de sexo
- Validación de existencia de pacientes y médicos
- Validación de horarios ocupados
- Validación de estados de cita
- Manejo de errores y registros inexistentes

---

# Autor

Jonathan Eduardo Miranda Ortega
ESCOM - IPN
