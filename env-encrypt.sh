#!/bin/bash

set -e
KEY=./.env.pass

if [ -f "$KEY" ]; then
    npx senv encrypt .env > .env.encrypted
    echo "Encription successful"
else
    echo "Missing pass file make sure you have file name '.env.pass'"
fi
