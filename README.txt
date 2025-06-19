
-> Make sure python is installed on your Pc. Version: 3.11.0

-> Open four terminals at the project folder.

	* transaction coordinator
	* participant-1
	* participant-2
	* transaction initializer i.e client
-> Run the following commands in their corresponding terminals.
	* python3 coordinator_node.py
	* python3 participant_node.py 8001
	* python3 participant_node.py 8002
	* python3 start_transaction.py fail_scenario

-> fail scenario can be 0 to 4.
