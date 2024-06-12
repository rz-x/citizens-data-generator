#!/bin/bash

# config
HOST="localhost"
DB_NAME="your_database_name"
USER="your_username"
PASSWORD="your_password"

DUMP_FILE="fake_citizen_data.dump"

mysql -h $HOST -u $USER -p$PASSWORD $DB_NAME < $DUMP_FILE

echo "MySQL export complete"
