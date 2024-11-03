class PAMFMachine:
    def __init__(self, machine_id, health=100, seeds=100, water=100):
        self.machine_id = machine_id
        self.health = health
        self.seeds = seeds
        self.water = water
        self.processing_customers = {}  # Dictionary to store customer orders and their current stage
        self.state = "IDLE"
    
    def check_resources(self, required_seeds, required_water):
        """Check if the machine has enough resources to process an order."""
        if self.seeds < required_seeds:
            return "Insufficient seeds"
        if self.water < required_water:
            return "Insufficient water"
        return "Resources sufficient"
    
    def assign_order(self, customer_id, order_details):
        """Assign a new order to the machine and set initial processing state."""
        resource_check = self.check_resources(order_details['microgreen_amount'], 10)  # Assume 10 units water needed
        if resource_check != "Resources sufficient":
            return {"error": resource_check}
        
        # Deduct resources and update state
        self.seeds -= order_details['microgreen_amount']
        self.water -= 10
        self.processing_customers[customer_id] = "PROCESSING"
        self.state = "PROCESSING"
        
        return {"success": f"Order for customer {customer_id} assigned to machine {self.machine_id}"}

    def update_order_state(self, customer_id, new_state):
        """Update the processing state of a specific order."""
        if customer_id in self.processing_customers:
            self.processing_customers[customer_id] = new_state
            if new_state == "FINISHED":
                self.state = "IDLE"  # Reset machine to idle if all orders are complete
            return {"success": f"Order for customer {customer_id} updated to {new_state}"}
        return {"error": "Customer order not found"}

    def check_health(self):
        """Check the health of the machine."""
        return self.health

    def add_resources(self, seeds, water):
        """Replenish resources."""
        self.seeds += seeds
        self.water += water
        return {"success": "Resources added successfully"}