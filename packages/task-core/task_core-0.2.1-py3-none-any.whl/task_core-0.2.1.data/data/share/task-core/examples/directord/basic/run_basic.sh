#!/bin/bash
# NOTE: edit basic_inventory.yaml and basic_options.yaml with your evironment
# defaults before continuing

SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
# we must be in the services dir because the services ADD commands
# assume we're in services/
pushd $SCRIPT_DIR/../services
set -ex
task-core -s . -i ../basic/basic_inventory.yaml -r ../basic/basic_roles.yaml -d
popd
