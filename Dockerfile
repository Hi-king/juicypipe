# Python juicypipe
FROM centos
MAINTAINER Keisuke Ogaki

RUN yum install -y python-setuptools
RUN easy_install pip

ADD . /app/juicypipe
WORKDIR /app/juicypipe
RUN python setup.py install
CMD nosetests -sv test
