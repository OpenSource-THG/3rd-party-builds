FROM centos:7
LABEL Josh Blease<Josh.Blease@thehutgroup.com>

WORKDIR /build

RUN yum update -y && \
    yum install -y make gcc perl pcre-devel zlib-devel wget perl-Test-Harness perl-Module-Load-Conditional perl-core make gcc gcc-c++ pcre-devel readline-devel systemd-devel zlib-devel
RUN wget https://www.openssl.org/source/openssl-1.1.1g.tar.gz && \
    tar zxf openssl-1.1.1g.tar.gz
RUN wget http://www.lua.org/ftp/lua-5.3.5.tar.gz && \
    tar zxf lua-5.3.5.tar.gz
RUN wget http://www.haproxy.org/download/2.0/src/haproxy-2.0.14.tar.gz && \
    tar zxf haproxy-2.0.14.tar.gz
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python /build/get-pip.py && \
    pip install awscli


WORKDIR /build/openssl-1.1.1g
RUN ./config --prefix=/usr/local/ssl --libdir=lib no-shared zlib && \
    make && \
    make test && \
    make install

WORKDIR /build/lua-5.3.5
RUN make linux test && \
    make linux install

WORKDIR /build/haproxy-2.0.14
RUN make TARGET=linux-glibc USE_PTHREAD_PSHARED=1 USE_OPENSSL=1 USE_PCRE=1 USE_SYSTEMD=1 USE_LIBCRYPT=1 USE_GETADDRINFO=1 USE_TFO=1 USE_NS=1 USE_ZLIB=1 USE_LUA=1 SSL_LIB=/usr/local/ssl/lib SSL_INC=/usr/local/ssl/include LUA_LIB=/usr/local/lib/ LUA_INC=/usr/local/include/ EXTRA_OBJS="contrib/prometheus-exporter/service-prometheus.o"

WORKDIR /build
COPY docker/* ./