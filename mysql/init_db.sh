#!/bin/bash

mysql -u root --password="$DB_PASSWORD"  << EOF
USE ${DBDATABASE};
GRANT ALL PRIVILEGES ON  test${DB_DATABASE}.* TO '${DB_USERNAME}';
EOF
