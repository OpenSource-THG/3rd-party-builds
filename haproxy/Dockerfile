#
# Copyright 2020 The Hut Group
# 
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
FROM centos:7 as build-stage
LABEL Josh Blease<Josh.Blease@thehutgroup.com>

WORKDIR /build

RUN yum update -y && \
    yum install -y make gcc perl pcre-devel zlib-devel wget perl-Test-Harness perl-Module-Load-Conditional perl-core make gcc gcc-c++ pcre-devel readline-devel systemd-devel zlib-devel
RUN wget https://www.openssl.org/source/openssl-1.1.1l.tar.gz && \
    tar zxf openssl-1.1.1l.tar.gz
RUN wget https://www.lua.org/ftp/lua-5.4.3.tar.gz && \
    tar zxf lua-5.4.3.tar.gz
RUN wget http://www.haproxy.org/download/2.4/src/haproxy-2.4.4.tar.gz && \
    tar zxf haproxy-2.4.4.tar.gz
RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py && \
    python /build/get-pip.py && \
    pip install awscli boto3


WORKDIR /build/openssl-1.1.1l
RUN ./config --prefix=/usr/local/ssl --libdir=lib no-shared zlib && \
    make && \
    make test && \
    make install

WORKDIR /build/lua-5.4.3
RUN make linux test && \
    make linux install

WORKDIR /build/haproxy-2.4.4
RUN make TARGET=linux-glibc USE_PTHREAD_PSHARED=1 USE_OPENSSL=1 USE_PCRE=1 USE_SYSTEMD=1 USE_LIBCRYPT=1 USE_GETADDRINFO=1 USE_TFO=1 USE_NS=1 USE_ZLIB=1 USE_LUA=1 USE_PROMEX=1 SSL_LIB=/usr/local/ssl/lib SSL_INC=/usr/local/ssl/include LUA_LIB=/usr/local/lib/ LUA_INC=/usr/local/include/

FROM scratch AS export-stage
COPY --from=build-stage /build/haproxy-2.0.14/haproxy /
