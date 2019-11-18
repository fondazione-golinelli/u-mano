#!/usr/bin/env bash
cd /Users/mini1 || exit
source .bash_profile
export PYTHONPATH=/Users/mini/projects/u-mano/:/Users/mini/projects/u-mano/umano
cd /Users/mini/projects/u-mano/ || exit
supervisord -c supervisor/manosola.cfg
python umano/services/dubio.py --hands=1 --video=0
