# TG Auth
Authorization in telegramm and return last login code.

Use Docker, Flask and Telegram MTProto API: [Pyrogram](https://github.com/pyrogram/pyrogram/).

## Docker
```
docker build -t tg_code .
docker run -p 80:80 tg_code
```

## Auth
```
docker ps # get CONTAINER_ID
docker exec -it {CONTAINER_ID} python telega.py
>First name: Skip
>Last name: Skip
>Enter code: 12345
```


## Test

Get code from console:
```
docker exec -it {CONTAINER_ID} python telega.py
```

Get code from web:
```
http http://localhost/code
http http://localhost/detail
```

