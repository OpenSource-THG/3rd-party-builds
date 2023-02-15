# HAProxy
This container will build HAProxy from source along with OpenSSL and Lua

## Execution
If you're using podman, you need to ssh into your podman machine 
```podman machine ssh``` 
and navigate into this directory from there before running the next step.

Build the container which will compile, build and output the haproxy executable:
`docker build .`