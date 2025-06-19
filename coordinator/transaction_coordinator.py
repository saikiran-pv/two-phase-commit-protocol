from setup_logger import Logg
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import time
from setup_logger import Logg


logger = Logg(name ="transaction_coordinator.log").logger

class ThreadedXMLRPCServer(ThreadingMixIn,SimpleXMLRPCServer):
    pass

class TransactionCoordinator():
    def __init__(self, participants, timeout= 1.):
        self.participants = participants
        self.t_count = 0
        self.time_out = timeout

    def begin_transaction(self, fail_scenario):
        self.t_count += 1
        transaction_id = self.t_count

        logger.info(f"New transaction started: [transaction id{transaction_id}]")

        # self.fail_scenario = fail_scenario

        if self.prepare_participants(transaction_id, fail_scenario):
            proceed_to_commit = "OK"
        else:
            proceed_to_commit = "Failed"
        print(proceed_to_commit)
        transaction_committed = self.commit_transaction(transaction_id, fail_scenario, proceed_to_commit)

        return transaction_committed
    
    def prepare_participants(self, transaction_id, fail_scenario):
        participant_votes = {}
        if fail_scenario == 1:
            temp = self.emulate_failure()
        for participant in self.participants:
            temp = participant.failure_check(fail_scenario)
            
            participant_votes[participant] = (participant.prepare_transaction(transaction_id) == b"yes")
            logger.info(f"{participant} voted {participant_votes[participant]}")
        return all(participant_votes.values())

    def commit_transaction(self, transaction_id, fail_scenario, proceed_to_commit):
        commits = {}
        for participant in self.participants:
            commits[participant] = (participant.commit_transaction(transaction_id, proceed_to_commit) == b"committ")

            if fail_scenario == 3:
                self.emulate_failure()
            if fail_scenario == 4:
                participant.emulate_failure(fail_scenario)
                logger.info("committing the transaction after recovery")
        print(logger)
        if proceed_to_commit == "OK":
            logger.info(f"Transaction-{transaction_id} is committed")
        else:
            logger.info(f"Transaction-{transaction_id} is aborted")
        
        return all(commits.values())
    
    def emulate_failure(self):
        logger.info(f"Coordinator failed waiting for recovery")
        time.sleep(self.time_out + 0.5)
        logger.info("coordinator recovered")
        return int(time.time())

        

def initialize_coordinator(port="8000", t_participants = None):
    hostname = "localhost"

    transaction_coordinator = TransactionCoordinator(t_participants)

    server = ThreadedXMLRPCServer((hostname, port))

    server.register_instance(transaction_coordinator)

    logger.info(f"Coordinator: Listening at {hostname}:{port}")

    server.serve_forever()
