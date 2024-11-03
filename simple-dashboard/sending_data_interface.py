import time
import random

class SendingDataInterface:
    def getPamfStatus(self, pamf_machine):
        """Returns the state of the specified PAMF machine."""
        return pamf_machine['state']
    
    def sendCmd(self, pamf_machine, cmd):
        """Sends a command to the specified PAMF machine. /Currently a simulation/"""
        print(f"Sending command {cmd} to {pamf_machine}...")
        time.sleep(1) # simulate delay
        print(f"Successfully sent command {cmd} to {pamf_machine}.")
    
    def readCmd(self, pamf_machine):
        """Reads the last command sent to the specified PAMF machine. /Currently a simulation/"""
        print(f"Reading command from {pamf_machine}...")
        time.sleep(1) # simulate delay
        response = random.randint(0, 100)
        print(f"Successfully read command {response} from {pamf_machine}.")
    
    