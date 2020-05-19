import redis
import json

ITEM_KEY = "books:items"


def process_item(item):
    with open('books.json', 'a', encoding='utf-8') as json_file:
        json.dump(item, json_file, ensure_ascii=False)


def main():
    r = redis.StrictRedis(host="192.168.125.131", port=6379)
    for _ in range(r.llen(ITEM_KEY)):
        data = r.lpop(ITEM_KEY)
        item = json.loads(data.decode('utf8'))
        process_item(item)


if __name__ == '__main__':
    main()
