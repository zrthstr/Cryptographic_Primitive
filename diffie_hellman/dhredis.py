#!/usr/bin/env python3

import redis
import sys
import time

REDIS_EXPIRE = 5 # sec

WAIT_BETWEEN_TRYS = 500  # ms
MAX_TRY_SEC = 3 # ms


def init_redis():
	return redis.StrictRedis(host='localhost', port=6379, db=0)

def set(key, value):
	print("Setting '%s' to: %d" %(key, value))
	r = init_redis()
	return r.setex(key, REDIS_EXPIRE, int(value))


def get(key):
	r = init_redis()
	stop_time = int(time.time()) + MAX_TRY_SEC
	while int(time.time()) < stop_time:
		value = r.get(key)
		if value == None:
			time.sleep(WAIT_BETWEEN_TRYS / 1000)
		else:
			print("Found key '%s': %d" %(key, int(value)))
			return(int(value))

	sys.exit("failed to get value: %s. Stoppping." % key )

if __name__ == "__main__":
	main()
