#!/bin/bash

# Instalar dependencias
pip install -r requirements.txt

# Inicializar la base de datos (si usas Flask-Migrate)
flask db init
flask db migrate "Initial migration"
flask db upgrade