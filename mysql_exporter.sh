#!/bin/bash

# config
HOST="mysql_host"
DB_NAME="database_name"
USER="mysql_username"
PASSWORD="mysql_passwd"

DUMP_FILE="fake_citizen_data.dump"

mysql -h $HOST -u $USER -p$PASSWORD $DB_NAME < $DUMP_FILE

echo "MySQL export complete"
