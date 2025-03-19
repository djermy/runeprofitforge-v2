#!/bin/sh

docker exec -it RS-psql bash -c 'psql -h localhost -U postgres RS'