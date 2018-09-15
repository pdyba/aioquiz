#!/bin/bash
cd /opt/backup
logrotate -fv /etc/logrotate.d/aioquizdb.conf 2>/dev/null
DUMP_CMD="pg_dump aioquizdb > /opt/backup/aioquizdb.sql"
sudo -u postgres bash -c "$DUMP_CMD"
chmod 640 /opt/backup/aioquiz*