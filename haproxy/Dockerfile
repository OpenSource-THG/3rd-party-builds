#
# Copyright 2023 The Hut Group
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
FROM rockylinux:9 as build-stage
LABEL Josh Blease<Josh.Blease@thehutgroup.com>

WORKDIR /build

RUN yum update -y && \
    yum install -y make gcc perl pcre-devel zlib-devel wget perl-Test-Harness perl-Module-Load-Conditional perl-core make gcc gcc-c++ pcre-devel readline-devel systemd-devel zlib-devel
RUN wget https://github.com/quictls/openssl/archive/refs/tags/OpenSSL_1_1_1t-quic1.tar.gz && \
    tar zxf OpenSSL_1_1_1t-quic1.tar.gz
RUN wget https://www.lua.org/ftp/lua-5.4.4.tar.gz && \
    tar zxf lua-5.4.4.tar.gz
RUN wget https://www.haproxy.org/download/2.8/src/haproxy-2.8.3.tar.gz && \
    tar zxf haproxy-2.8.3.tar.gz


WORKDIR /build/openssl-OpenSSL_1_1_1t-quic1
RUN mkdir -p /opt/quictls && \
    ./config --libdir=lib --prefix=/opt/quictls no-shared no-pinshared && \
    make && \
    make install

WORKDIR /build/lua-5.4.4
RUN make linux test && \
    make linux install

WORKDIR /build/haproxy-2.8.3
RUN make TARGET=linux-glibc USE_PTHREAD_PSHARED=1 USE_OPENSSL=1 USE_PCRE=1 USE_SYSTEMD=1 USE_LIBCRYPT=1 USE_GETADDRINFO=1 USE_TFO=1 USE_NS=1 USE_ZLIB=1 USE_LUA=1 USE_PROMEX=1 USE_QUIC=1 USE_OPENSSL=1 SSL_LIB=/opt/quictls/lib SSL_INC=/opt/quictls/include LDFLAGS="-Wl,-rpath,/opt/quictls/lib" LUA_LIB=/usr/local/lib/ LUA_INC=/usr/local/include/ ADDLIB="-Wl,-rpath,/opt/quictls/lib"

FROM scratch AS export-stage
COPY --from=build-stage /build/haproxy-2.8.3/haproxy /
