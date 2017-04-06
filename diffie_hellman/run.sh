#!/bin/bash
set -ex

rm dump.rdb || True 
pgrep redis-server || redis-server redis.conf &

./eve.py &

./alice.py &
./bob.py 
pkill redis-server
