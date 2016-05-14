#!/ust/bin/env python
from zerodb.storage import StorageServer
from s3storage import S3Storage
from zerodb.permissions import elliptic
import logging

logging.basicConfig(level=logging.DEBUG)
elliptic.register_auth()

SOCKET = ('localhost', 8001)
BUCKET_NAME = "zerodb-test"
S3_PREFIX = "zerodb-test-server-2"
POOL_SIZE = 10

options = {
        "read_only": False,
        "invalidation_queue_size": 100,
        "invalidation_age": None,
        "transaction_timeout": None,
        "monitor_address": None,
        "auth_protocol": "ecc_auth",
        "auth_database": "conf/authdb.conf",
        "auth_realm": "ZERO"}

if __name__ == "__main__":
    storage = S3Storage(BUCKET_NAME, S3_PREFIX, pool_size=POOL_SIZE)
    server = StorageServer(SOCKET, {'1': storage}, **options)
    server.loop()
