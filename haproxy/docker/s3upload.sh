#!/bin/sh
aws s3 cp /build/haproxy-2.0.14/haproxy s3://$1/2.0.14/haproxy --profile "${2:-default}"