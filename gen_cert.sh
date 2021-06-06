openssl req -newkey rsa:4096 \
            -x509 \
            -sha256 \
            -days 3650 \
            -nodes \
            -out `hostname`.crt \
            -keyout `hostname`.key
