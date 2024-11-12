from datetime import datetime, timedelta
from .customer import Customer
from .prep_stage import PrepStageManager
from .sending_data_interface import SendingDataInterface
import time

def get_user_input():
    print("Enter the following details of the user order: ")
    customer_name = input("Customer Name: ")
    microgreen_type = input("Microgreen Type (e.g., basil, spinach): ")
    microgreen_amount = float(input("Microgreen Amount (in grams): "))
    estimated_hours = int(input("Estimated Processing Time (in hours): "))

    return Customer(
        customer_name=customer_name,
        order_date=datetime.now(),
        microgreen_type=microgreen_type,
        microgreen_amount=microgreen_amount,
        estimated_time=timedelta(hours=estimated_hours)
    )

def process_order(prep_stage_manager, sending_data_inter, customer_order):
    """Process a single order through the stages using the different managers"""

    print("\nOrder Received. Processing begins...\n")

    # Add order to the prep stage and attempt to assign it to a PAMF machine
    result = prep_stage_manager.add_order_and_process(customer_order)
    if "error" in result:
        print(f"Error in processing: {result['error']}")
        return
    
    assigned_machine = prep_stage_manager.get_current_machine()
    print(f"Order assigned to machine: {assigned_machine.machine_id}")

    # Retrieve order details and print it out
    current_order = prep_stage_manager.get_current_order()
    print("\nOrder details:\n")
    print(f"Customer Name: {current_order.customer_name}")
    print(f"Microgreen Type: {current_order.microgreen_type}")
    print(f"Microgreen Amount: {current_order.microgreen_amount} grams")
    print(f"Estimated Processing Time: {current_order.estimated_time}") 

    # Simulate ESP32 communication and processing in the PAMF machine
    if assigned_machine:
        print("\nChecking machine status...\n")
        status = sending_data_inter.getPamfStatus(vars(assigned_machine))
        print(f"Current status of machine {assigned_machine.machine_id}: {status}")

        # Send start command to the machine
        sending_data_inter.sendCmd(vars(assigned_machine), cmd=1)  # Command 1 simulates a start command

        # Simulate reading a response from the machine
        sending_data_inter.readCmd(vars(assigned_machine))

        # Update machine to processing state
        prep_stage_manager.update_machine_state(assigned_machine.machine_id, "PROCESSING")

        # Simulate processing time 
        time.sleep(2)

        # Update machine state to FINISHED, which resets to IDLE
        prep_stage_manager.update_machine_state(assigned_machine.machine_id, "FINISHED")
        
        # Print the final state of the machine
        final_state = assigned_machine.state
        print(f"Machine {assigned_machine.machine_id} has finished processing the order and now in {final_state} state.")
    
    # Display final state of the PAMF machines
    print("\nFinal state of all PAMF machines:\n")
    for machine in prep_stage_manager.get_all_machines():
        print(machine)


def main():
    # Initialize PrepStageManager, SendingDataInterface
    prep_stage_manager = PrepStageManager()
    sending_data_inter = SendingDataInterface()

    while True:
        # Capture user input to create new customer order
        customer_order = get_user_input()

        # Process the order
        process_order(prep_stage_manager, sending_data_inter, customer_order)

        # Ask if the user wants to add another order
        cont = input("\nDo you want to add another order? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

    print("\nAll orders have been processed. Exiting.")

if __name__ == "__main__":
    main()


