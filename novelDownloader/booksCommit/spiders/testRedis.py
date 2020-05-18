import redis

r = redis.StrictRedis(host='localhost',port=6379)
r.set("name","zsj")
str1 = r.get("name")
print(str1)