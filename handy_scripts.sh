#!/usr/bin/env bash
#CONNECT SINK
curl -X POST -H "Content-Type: application/json" \
  --data '{"name": "file-sink", "config": {"connector.class":"org.apache.kafka.connect.file.FileStreamSinkConnector", "tasks.max":"1", "topics":"twitter", "file": "/tmp/twitter.txt"}}' \
  http://localhost:8083/connectors


curl -sX GET localhost:8083/connectors/file-sink/status

#PEAK STREAM
kafka-console-consumer --bootstrap-server localhost:9092 --topic twitter