from enum import Enum

class ControllerCommands(Enum):
    GET_AMOUNT = "getAmount"
    GET_TYPE_OF_MG = "getTypeOfMg"
    GET_TIME = "getTime"

    def execute(self, order_details):
        """Execute commands to retrieve order details."""
        if self == ControllerCommands.GET_AMOUNT:
            return order_details.microgreen_amount
        elif self == ControllerCommands.GET_TYPE_OF_MG:
            return order_details.microgreen_type
        elif self == ControllerCommands.GET_TIME:
            return order_details.estimated_time
        else:
            raise NotImplementedError("Command not implemented for this action")


# class ControllerInterface:
    # def __init__(self, prep_stage_manager):
        # Initialize with a reference to the prep_stage_manager for real-time info
        # self.prep_stage_manager = prep_stage_manager
    
    # # Sending Data Interface
    # def get_pamf_state(self) -> bool:
    #     # Retrieve the current status of the PAMF (true = processing, false = idle)
    #     current_machine = self.prep_stage_manager.get_current_machine()
    #     if current_machine:
    #         is_processing = current_machine['state'] == 'PROCESSING'
    #         print(f"PAMF status: {'Processing' if is_processing else 'Idle'}")
    #         return is_processing
    #     else:
    #         print("No machine currently assigned.")
    #         return False

    # def send_cmd(self, cmd: int):
    #     print(f"Sending command {cmd} to ESP32...")
    #     time.sleep(1) # simulate delay
    #     print(f"Successfully sent command {cmd} to ESP32.")

    # def read_cmd(self) -> int:
    #     print(f"Reading command from ESP32...")
    #     time.sleep(1) # simulate delay
    #     response = random.randint(0, 100)
    #     print(f"Successfully read command {response} from ESP32.")

    # def current_stage(self) -> str:
    #     current_machine = self.prep_stage_manager.get_current_machine()
    #     if current_machine:
    #         stage = current_machine['state']
    #         print(f"Current machine stage: {stage}")
    #         return stage
    #     else:
    #         print(f"No machine currently assigned")
    #         return "IDLE"

    # Controller Interface
    # def get_amount(self) -> float:
    #     # Retrieve the amount required from the current order
    #     current_order = self.prep_stage_manager.get_current_order()
    #     if current_order:
    #         amount = float(current_order.microgreen_amount)
    #         print(f"Retrieved microgreen amount: {amount}")
    #         return amount
    #     else:
    #         print(f"No current microgreen order available right now.")
    
    # def get_type_of_mg(self) -> str:
    #     current_order = self.prep_stage_manager.get_current_order()
    #     if current_order:
    #         mg_type = current_order.microgreen_type
    #         print(f"Retrieved microgreen amount: {mg_type}")
    #         return mg_type
    #     else:
    #         print(f"No current microgreen order available right now.")
    
    # def get_time(self) -> str:
    #     current_order = self.prep_stage_manager.get_current_order()
    #     if current_order:
    #         amount = float(current_order.microgreen_amount)
    #         print(f"Retrieved microgreen amount: {amount}")
    #         return amount
    #     else:
    #         print(f"No current microgreen order available right now.")
    
    # def get_current_customer(self) -> str:
    #     current_order = self.prep_stage_manager.get_current_order()
    #     if current_order:
    #         current_customer = current_order.customer_name
    #         print(f"Current customer name: {current_customer}")
    #         return current_customer
    #     else:
    #         print(f"")
