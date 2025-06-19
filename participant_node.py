from sys import argv
from participant.transaction_participant import initialize_participant

if __name__ == "__main__":
    port = int(argv[1])
    initialize_participant(port)