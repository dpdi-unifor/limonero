FROM ubuntu:16.04
MAINTAINER Vinicius Dias <viniciusvdias@dcc.ufmg.br>

# Install python and jdk
RUN apt-get update \
   && apt-get install -qy python-pip

# Install juicer
ENV LIMONERO_HOME /usr/local/limonero
ENV LIMONERO_CONFIG $LIMONERO_HOME/conf/limonero-config.yaml
RUN mkdir -p $LIMONERO_HOME/conf
RUN mkdir -p $LIMONERO_HOME/sbin
RUN mkdir -p $LIMONERO_HOME/limonero
ADD sbin $LIMONERO_HOME/sbin
ADD limonero $LIMONERO_HOME/limonero
ADD migrations $LIMONERO_HOME/migrations
ADD logging_config.ini $LIMONERO_HOME/logging_config.ini

# Install juicer requirements and entrypoint
ADD requirements.txt $LIMONERO_HOME
RUN pip install -r $LIMONERO_HOME/requirements.txt
EXPOSE 5000
CMD ["/usr/local/limonero/sbin/limonero-daemon.sh", "startf"]
