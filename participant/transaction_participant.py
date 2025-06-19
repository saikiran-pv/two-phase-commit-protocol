from setup_logger import Logg
from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer
import time
from setup_logger import Logg


logger = Logg(name="transaction_participant.log").logger

class TransactionParticipant():

    def __init__(self, url, timeout= 1.):
        self.url = url
        self.time_out = timeout
        self.vote = "yes"

    def prepare_transaction(self, transaction_id) -> str:
        print(logger)

        vote = self.vote
        logger.info(f"Transaction[{transaction_id}] voted <{vote}>")
        return vote.encode()

    def commit_transaction(self, transaction_id, proceed_to_commit):
        message = "commit"
        print(proceed_to_commit)
        if proceed_to_commit != "OK":
            message = "abort"

        logger.info(f"Transaction[{transaction_id}] {message}ed")
        return message.encode()
    
    def emulate_failure(self, fail_scenario):
        logger.info(f"Participant node:{self} failed")
        time.sleep(self.time_out + 0.5)

        if fail_scenario == 4:
            logger.info(f"{self} backup is done")

        return int(time.time())

    def failure_check(self, fail_scenario):
        if fail_scenario == 1:
            self.vote = "no"
        elif fail_scenario == 2:
            self.vote = "no"
        else:
            self.vote = "yes"

        return int(time.time())

class ThreadedXMLRPCServer(ThreadingMixIn,SimpleXMLRPCServer):
    pass

def initialize_participant(port="8000"):
    hostname = "localhost"
    transaction_participant = TransactionParticipant(url=f"https://localhost:{port}")

    server = ThreadedXMLRPCServer((hostname, port))

    server.register_instance(transaction_participant)

    logger.info(f"Participant: Listening at {hostname}:{port}")

    server.serve_forever()

