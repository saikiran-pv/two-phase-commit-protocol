from sys import argv
import xmlrpc.client

server_url = "http://localhost:8000"
transaction_coordinator = xmlrpc.client.ServerProxy(server_url)
transaction_coordinator.begin_transaction(int(argv[1]))