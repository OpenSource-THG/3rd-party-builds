# HAProxy
This container will build HAProxy from source along with OpenSSL and Lua

## Execution
If you're using podman, you need to ssh into your podman machine using
```podman machine ssh``` 
and navigate into this directory from there before running the next step. 

If you've mounted the Users directory to your podman machine then you'll probably have to run something like
```cd /Users/[your machine username]/[path to this directory]```

Build the container which will compile, build and output the haproxy executable:
`docker build .`