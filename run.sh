#!/bin/bash
set -m
USERNAME=jankybank
PASSWORD=jankyland5
/usr/bin/entrypoint &

while true
do
  gitea_status_code=$(curl --write-out %{http_code} --silent --output /dev/null localhost:3000/ )
  if [ "$gitea_status_code" -eq 200 ]; then
    echo "Gitea ready. Continue with setup..."
    break
  fi
  echo "Gitea is not ready. Waiting 5 seconds..."
  sleep 5
done
cd /setup
python3 -m giteacasc /setup/gitea.yaml -u $USERNAME -p $PASSWORD
fg #/usr/bin/entrypoint
