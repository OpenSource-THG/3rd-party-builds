#
# Copyright 2024 The Hut Group
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
    yum groupinstall -y "Development Tools" && \
    yum install -y make gcc perl pcre-devel zlib-devel wget perl-Test-Harness perl-Module-Load-Conditional perl-core make gcc gcc-c++ pcre-devel readline-devel systemd-devel zlib-devel rpm-build rpmdevtools
RUN rpmdev-setuptree && \
    cd /root/rpmbuild/SOURCES/ && \
    wget https://github.com/jemalloc/jemalloc/releases/download/5.3.0/jemalloc-5.3.0.tar.bz2
COPY rpm.spec /root/rpmbuild/SPECS/jemalloc.spec
WORKDIR /root/rpmbuild
RUN rpmbuild -ba /root/rpmbuild/SPECS/jemalloc.spec

FROM scratch AS export-stage
COPY --from=build-stage /root/rpmbuild/RPMS/x86_64/jemalloc-5.3.0-3.el9.x86_64.rpm /
