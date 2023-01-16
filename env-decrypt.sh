#!/bin/bash

set -e

npx senv decrypt .env.encrypted > .env
