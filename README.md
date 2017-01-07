## Nginx monitor agent
The monitoring agent collects state information by uses the [ngx_http_reqstat_module](http://tengine.taobao.org/document/http_reqstat.html) module provide by [Tengine](https://github.com/alibaba/tengine), and sends it to [Graphite](http://graphite.readthedocs.io/en/latest), and views metrics through [Grafana](https://github.com/grafana/grafana).

### Requirements
- Python (>=2.7)
- Tengine

### Installation and Configuration
1. Install the module in the `requirements.text` file
2. Edit `conf/settings.py` and `statsd.yaml` you want to replace, in particular URL address

### Usage
1. Agent can be started as a daemon in a virtual environment using the following command: `python nginx-monitor-agent start` or `systemctl start nginx-monitor-agent.service`
2. The daemon can be stopped by running: `python nginx-monitor-agent stop` or `systemctl stop nginx-monitor-agent.service`
3. The daemon can be restarted by running: python `nginx-monitor-agent restart` or `systemctl restart nginx-monitor-agent.service`

### Systemd example
> \# vi /etc/systemd/system/nginx-monitor-agent.service


```yaml
[Unit]
Description=Monitor agent for nginx
After=network.target

[Service]
Type=forking
WorkingDirectory=/opt/nginx-monitor-agent
PIDFile=/var/run/nginx-monitor-agent/nginx-monitor-agent.pid
ExecStart=/opt/nginx-monitor-agent/server.sh start
ExecReload=/opt/nginx-monitor-agent/server.sh restart
ExecStop=/opt/nginx-monitor-agent/server.sh stop
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

### Started script for virtual envirnoment

```bash
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
```