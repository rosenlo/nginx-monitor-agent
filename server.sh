#!/bin/bash

WORK_HOME="/opt/nginx-monitor-agent"
VENV_HOME="$WORK_HOME/.venv"


source $VENV_HOME/bin/activate

case $1 in
    start) $VENV_HOME/bin/python $WORK_HOME/nginx-monitor-agent start
        ;;
    stop) $VENV_HOME/bin/python $WORK_HOME/nginx-monitor-agent stop
        ;;
    restart) $VENV_HOME/bin/python $WORK_HOME/nginx-monitor-agent restart
        ;;
    *) $VENV_HOME/bin/python $WORK_HOME/nginx-monitor-agent
        ;;
esac


