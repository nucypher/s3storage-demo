import zerodb
import transaction
from BTrees.OOBTree import BTree

PASSPHRASE = "very insecure passphrase - never use it"
SOCKET = ("localhost", 8001)

db = zerodb.DB(SOCKET, username="root", password=PASSPHRASE)

root = db._root

tree = BTree({str(i): str(i + 1) for i in range(1000)})
root['test_tree'] = tree
transaction.commit()
