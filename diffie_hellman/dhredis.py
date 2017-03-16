import redis
import sys
import time

REDIS_EXPIRE = 4 # sec

WAIT_BETWEEN_TRYS = 200  # ms
MAX_TRY_TIME = 3000 # ms


def init_redis():
	return redis.StrictRedis(host='localhost', port=6379, db=0)

def set(key, value):
	r = init_redis()
	return r.setex(key, REDIS_EXPIRE, int(value))


def get(key):
	r = init_redis()
	stop_time = int(time.time()  + MAX_TRY_TIME / 1000 )
	while int(time.time()) < stop_time:
		value = r.get(key)
		if value == None:
			time.sleep(WAIT_BETWEEN_TRYS / 1000)
		else:
			return(int(value))

	sys.exit("failed to get value: %s. Stoppping." % key )

if __name__ == "__main__":
	main()
