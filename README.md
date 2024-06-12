# Fake Citizen Data Generator 

Python script generates fake citizen data in various formats (CSV, JSON, SQL dump). 
Bash script is for exporting SQL dump into MySQL server.

## Contents

1. **generatorpy** - Python script to generate synthetic data.
2. **mysql_exporter.sh** - Bash script to import a SQL dump into MySQL.

## Features

- Generate synthetic citizen data with configurable parameters.
- Export data in multiple formats: CSV, JSON, or SQL dump.
- Import SQL data dumps into a MySQL database using a Bash script.

## Requirements

- Python 3.6 or higher.
- Python libraries: `pandas`, `faker`.
- MySQL Client (for the Bash script).

## Before exec

Edit both before use - each script contains some configuration options and requirements (eg. credentials for MySQL server, etc.)
