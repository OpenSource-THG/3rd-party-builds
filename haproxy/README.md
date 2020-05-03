# HAProxy
This container will build HAProxy from source along with OpenSSL and Lua

## Execution
Build the container which will compile everything:
`docker build -t 3rd-party-builds/haproxy .`

Upload the compiled HAProxy to an S3 bucket of your choosing:
`docker run --rm 3rd-party-builds/haproxy ./s3upload.sh my-asset-bucket`