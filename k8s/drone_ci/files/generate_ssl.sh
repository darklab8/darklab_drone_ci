openssl req -x509 -nodes -days 3650 -newkey rsa:4096 -keyout ssl.key -out ssl.crt -config ssl.cfg -extensions v3_req