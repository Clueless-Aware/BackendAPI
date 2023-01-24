#!/bin/bash

set -e
KEY=./.env.pass

if [ -f "$KEY" ]; then
    npx senv decrypt .env.encrypted > .env
    echo "Decription successful"
else
    echo "Missing pass file make sure you have file name '.env.pass'"
fi
