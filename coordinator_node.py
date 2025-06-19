import xmlrpc.client
from coordinator.transaction_coordinator import initialize_coordinator

p1_url = "http://localhost:8001"
p2_url = "http://localhost:8002"

participant1 = xmlrpc.client.ServerProxy(p1_url)
participant2 = xmlrpc.client.ServerProxy(p2_url)

participants = [participant1, participant2]

if __name__ == "__main__":
    initialize_coordinator(8000, participants)