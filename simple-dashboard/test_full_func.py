import pytest
from .prep_stage import PrepStageManager
from .fifo_queue import OrderQueueManager
from .pamf_machine_manager import PAMFMachineManager
from .customer import Customer
from .utils import generate_dummy_order

@pytest.fixture
def prep_stage():
    """Fixture to create a PrepStageManager instance for each test."""
    return PrepStageManager()

@pytest.fixture
def machine_manager():
    """Fixture to create a PAMFMachineManager instance for each test."""
    return PAMFMachineManager(max_machines=5)

@pytest.fixture
def order_queue():
    """Fixture to create an OrderQueueManager instance for each test."""
    return OrderQueueManager(max_orders=10)

def test_add_order_and_process(prep_stage):
    """Test adding an order to the queue and processing it."""
    order_data = generate_dummy_order()
    result = prep_stage.add_order_and_process(order_data)
    
    if "error" in result:
        assert "No available PAMF machines in IDLE state to handle the order." in result["error"]
    else:
        assert "success" in result
        assert result["machine"].state == "PROCESSING"

def test_queue_overflow(prep_stage):
    """Test adding more orders than the queue can handle, triggering overflow."""
    # Only add orders to the queue without processing, to simulate a full queue.
    for _ in range(10):
        prep_stage.queue_manager.add_order(generate_dummy_order())  # Directly add to queue to fill it up
    result = prep_stage.add_order_and_process(generate_dummy_order())
    
    assert "error" in result
    assert "The FIFO Queue is full. Cannot add more orders" in result["error"]

def test_process_next_order(prep_stage):
    """Test processing the next order and assigning it to an idle machine."""
    order_data = generate_dummy_order()
    result = prep_stage.add_order_and_process(order_data)
    
    if "error" in result:
        assert "No available PAMF machines in IDLE state to handle the order." in result["error"]
    else:
        # Check if the order was assigned to a machine and the machine is in PROCESSING state
        assert prep_stage.get_current_machine() is not None
        assert prep_stage.get_current_machine().state == "PROCESSING"

def test_get_all_machines(machine_manager):
    """Test retrieving the status of all machines."""
    machines = machine_manager.get_all_machines()
    assert len(machines) == 5
    assert all(machine["state"] == "IDLE" for machine in machines)

def test_assign_order_to_machine(prep_stage):
    """Test assigning an order to a machine through the prep stage."""
    order_data = generate_dummy_order()
    result = prep_stage.add_order_and_process(order_data)
    
    if "error" in result:
        assert "No available PAMF machines in IDLE state to handle the order." in result["error"]
    else:
        assert "success" in result
        assigned_machine = prep_stage.get_current_machine()
        assert assigned_machine.state == "PROCESSING"

def test_update_order_state(prep_stage):
    """Test updating the state of an order within a machine."""
    # Reset all machines to IDLE before starting the test
    prep_stage.reset_machines()
    order_data = generate_dummy_order()
    result = prep_stage.add_order_and_process(order_data)
    
    if "error" in result:
        pytest.fail(f"Failed to assign order to a machine: {result['error']}")
    
    current_machine = prep_stage.get_current_machine()

    if current_machine is not None:
        # Update order state to FINISHED
        result = prep_stage.machine_manager.set_machine_state(current_machine.machine_id, "FINISHED")
        assert "success" in result
        assert prep_stage.machine_manager.machines[0].state == "IDLE"  # Ensure the machine returned to IDLE
    else:
        pytest.fail("No machine available to update order state")  # Fail the test with a descriptive message
        
def test_resource_management(prep_stage):
    """Test that resources are managed correctly after an order is processed."""
    order_data = generate_dummy_order()
    order_data['microgreen_amount'] = 10  # Set a specific amount of seeds needed
    initial_seeds = prep_stage.machine_manager.machines[0].seeds
    initial_water = prep_stage.machine_manager.machines[0].water
    
    result = prep_stage.add_order_and_process(order_data)
    if "success" in result:
        # Check if seeds and water have been deducted properly
        assigned_machine = prep_stage.get_current_machine()
        assert assigned_machine.seeds == initial_seeds - 10
        assert assigned_machine.water == initial_water - 10

def test_health_check(machine_manager):
    """Test that the health status of the machines can be retrieved and is correct."""
    for machine in machine_manager.machines:
        assert machine.check_health() == 100  # Initial health of all machines should be 100

def test_replenish_resources(machine_manager):
    """Test replenishing resources for a specific machine."""
    machine = machine_manager.machines[0]
    initial_seeds = machine.seeds
    initial_water = machine.water
    
    # Replenish resources
    result = machine.add_resources(seeds=20, water=15)
    assert "success" in result
    assert machine.seeds == initial_seeds + 20
    assert machine.water == initial_water + 15
