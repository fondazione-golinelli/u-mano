#!/usr/bin/env bash
cd /Users/mini || exit
source .bash_profile
export PYTHONPATH=/Users/mini/projects/u-mano/:/Users/mini/projects/u-mano/umano
cd /Users/mini/projects/u-mano/ || exit
supervisord -c supervisor/hal.cfg
