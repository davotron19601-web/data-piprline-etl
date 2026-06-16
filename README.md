# Data Pipeline ETL

Este proyecto demuestra la construcción de un **pipeline ETL (Extract, Transform, Load)** orientado a **Ingeniería de Datos y Análisis de Datos**, utilizando **PySpark**, **Delta Lake** y **SQL**. El objetivo es mostrar cómo diseñar procesos modulares y robustos para transformar datos crudos en información lista para análisis.

## 🎯 Objetivo
El pipeline procesa datos de clientes, cuentas y transacciones, aplicando:
- **Ingesta** desde archivos CSV.
- **Transformación** con tipificación, estandarización y enriquecimiento de variables.
- **Validación** para eliminar nulos y duplicados.
- **Carga** en formato Parquet, organizado en capas Silver y Gold.

Este proyecto sirve como portafolio para demostrar habilidades en **data engineering**, **data analytics** y **arquitectura de datos en la nube**.

## 🚀 Tecnologías utilizadas
- **Lenguajes**: Python, SQL
- **Frameworks**: PySpark, Pandas
- **Data Lakehouse**: Delta Lake
- **Infraestructura**: Databricks / Google Cloud
- **Visualización**: Matplotlib, Seaborn

## 📂 Estructura del repositorio
- `src/`: código modular (ingest, transform, validate, load).
- `notebooks/`: demo interactiva con ejecución paso a paso.
- `diagrams/`: visualización del flujo ETL y modelos de datos.
- `data/`: datasets de ejemplo (clientes, cuentas, transacciones).

## ▶️ Ejecución
Instala dependencias:
```bash
pip install -r requirements.txt
