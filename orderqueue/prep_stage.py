from .fifo_queue import OrderQueueManager
from .pamf_machine_manager import PAMFMachineManager
from .customer import Customer

class PrepStageManager:
    def __init__(self):
        self.queue_manager = OrderQueueManager(max_orders=10)
        self.machine_manager = PAMFMachineManager(max_machines=5)
        self.current_order = None
        self.current_machine = None

    def add_order_and_process(self, order_data):
        try:
            self.queue_manager.add_order(order_data)
            return self.process_next_order()
        except OverflowError:
            return {"error": "The FIFO Queue is full. Cannot add more orders."}
    
    def process_next_order(self):
        try:
            next_order = self.queue_manager.get_next_order()
            assigned_machine = self.machine_manager.assign_machines(next_order)
            if not assigned_machine:
                return {"error": "No available PAMF machines in IDLE state to handle the order."}
            # Set the current order
            self.current_order = next_order
            self.current_machine = assigned_machine
            print(f"Order assigned to machine: {assigned_machine}")
            return {"success": "Order assigned to machine.", "machine": assigned_machine}
        except IndexError:
            return {"error": "The FIFO queue is empty."}
    
    def get_all_machines(self):
        return self.machine_manager.get_all_machines()
    
    def get_current_order(self):
        return self.current_order
    
    def get_current_machine(self):
        return self.current_machine
    
    def reset_machines(self):
        """Reset all machines to IDLE state and clear current order assignments."""
        for machine in self.machine_manager.machines:
            machine.state = "IDLE"  # Use dot notation
            if hasattr(machine, 'current_order'):
                del machine.current_order  # Clear any assigned orders if this attribute exists
        print("Machines have been reset to IDLE.")
    