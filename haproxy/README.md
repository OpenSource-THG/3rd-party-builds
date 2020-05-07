# HAProxy
This container will build HAProxy from source along with OpenSSL and Lua

## Execution
Build the container which will compile everything:
`docker build -t 3rd-party-builds/haproxy .`

Upload the compiled HAProxy to an S3 bucket of your choosing:
`docker run --rm 3rd-party-builds/haproxy ./s3upload.sh my-asset-bucket`

If you are running out of EC2, mount your credentials folder and optionally pass in an AWS CLI profile
`docker run --rm -it -v ~/.aws/:/root/.aws 3rd-party-builds/haproxy ./s3upload.sh my-asset-bucket my-aws-profile`