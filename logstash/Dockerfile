FROM docker.elastic.co/logstash/logstash-oss:6.2.3

RUN rm -f /usr/share/logstash/pipeline/logstash.conf
ADD pipeline/ /usr/share/logstash/pipeline/

RUN mkdir -p /usr/share/logstash/logs
RUN chown -R logstash.logstash /usr/share/logstash/logs
RUN chmod -R 777 /usr/share/logstash/logs
