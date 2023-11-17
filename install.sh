#!/usr/bin/env bash

set -e

REPO_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

mkdir -p ~/bin

ln -s "${REPO_DIR}/todos.py" ~/bin/todos || true
