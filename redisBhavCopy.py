import redis
import os

REDIS_HOST="127.0.0.1"
REDIS_PORT=6379
BHAV_COPY_URL="https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx"

def get_redis_connection():
    res = {"status": 0, "data": ""}
    try:
        redis_url = os.environ.get("REDIS_URL", "redis://%s:%s" % (REDIS_HOST, REDIS_PORT))
        r = redis.from_url(redis_url ,charset="utf-8",decode_responses=True, db=0)
        res["status"]=1
        res["data"]=r
    except Exception as e:
        res["data"]="Redis connection error, Kindly contact administrator"
    return res
