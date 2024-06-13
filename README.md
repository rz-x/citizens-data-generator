# Fake Citizen Data Generator 

This script generates fake citizen data in various formats (CSV, JSON, SQL dump). 

## Contents

1. **generatorpy** - Python script to generate synthetic data.
2. **mysql_exporter.sh** - Helper script to export a SQL dump into MySQL.

## Features

- Generate synthetic citizen data with configurable parameters.
- Export data in multiple formats: CSV, JSON, or SQL dump.
- Export SQL data dumps into a MySQL database using a Bash script.

## Requirements

- Python 3.6 or higher.
- Python libraries: `pandas`, `faker`.
- MySQL Client (for the Bash script) - in case of MySQL export.

## Before exec

Scripts contain some configuration options (eg. credentials for MySQL server, etc.)
