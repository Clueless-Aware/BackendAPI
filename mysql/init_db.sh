#!/bin/bash

mysql -u root --password="$MYSQL_ROOT_PASSWORD"  << EOF
USE ${DBDATABASE};
GRANT ALL PRIVILEGES ON  test${DB_DATABASE}.* TO '${MYSQL_USER}';
EOF
