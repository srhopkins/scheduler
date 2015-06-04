FROM python:2.7
ADD init.sh /
RUN chmod +x /init.sh

ENTRYPOINT ["/init.sh"] 
