import random
from .pamf_machine import PAMFMachine

# Define the states for a machine (Change it to three for the MVP)
# PAMF_STATES = ['IDLE', 'PROCESSING', 'FINISHED']

class PAMFMachineManager:
    def __init__(self, max_machines=5):
        # Initialize a list of PAMFMachine objects
        self.machines = [PAMFMachine(machine_id=i+1) for i in range(max_machines)]
    
    def get_idle_machines(self):
        """Retrieve all machines that are currently idle."""
        return [machine for machine in self.machines if machine['state'] == 'IDLE']

    def assign_machines(self, order):
        """Assign an order to an idle machine if available, and deduct resources."""
        idle_machines = [machine for machine in self.machines if machine.state == "IDLE"]
        
        if not idle_machines:
            print("No idle machines available.")
            return None
        
        assigned_machine = idle_machines[0]  # Assign the first available idle machine
        assigned_machine.state = "PROCESSING"
        assigned_machine.current_order = order
        
        # Deduct resources
        assigned_machine.seeds -= order['microgreen_amount']
        assigned_machine.water -= 10  # Assuming a set amount of water needed per order

        print(f"Assigned machine {assigned_machine.machine_id} to order with resources deducted.")
        return assigned_machine
    
    def set_machine_state(self, machine_id, new_state):
        """Set the state of a specific machine and reset to IDLE if finished."""
        for machine in self.machines:
            if machine.machine_id == machine_id:
                machine.state = new_state
                if new_state == "FINISHED":
                    machine.state = "IDLE"  # Automatically reset to IDLE
                    if hasattr(machine, 'current_order'):
                        del machine.current_order  # Clear the order on reset
                return {"success": f"Machine {machine_id} state updated to {new_state}"}
        return {"error": "Machine not found"}
    
    def get_all_machines(self):
        """Retrieve a list of all machines with their details."""
        return [{"id": machine.machine_id, "state": machine.state, "health": machine.health,
                 "seeds": machine.seeds, "water": machine.water} for machine in self.machines]
