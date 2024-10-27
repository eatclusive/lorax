import pytest
from .controller_interface import ControllerCommands  # Import the ControllerCommands class or enum
from .customer import Customer  # Import the mock Customer class or data used for testing
from datetime import datetime, timedelta

# Fixture to create a sample order
@pytest.fixture
def sample_order():
    """Fixture to create a sample Customer instance."""
    return Customer(
        customer_name="Test Customer",
        microgreen_type="basil",
        microgreen_amount=5.0,
        estimated_time=timedelta(hours=48)
    )

def test_get_amount(sample_order):
    """Test the GET_AMOUNT command."""
    result = ControllerCommands.GET_AMOUNT.execute(sample_order)
    assert result == sample_order.microgreen_amount, f"Expected {sample_order.microgreen_amount} but got {result}"

def test_get_type_of_mg(sample_order):
    """Test the GET_TYPE_OF_MG command."""
    result = ControllerCommands.GET_TYPE_OF_MG.execute(sample_order)
    assert result == sample_order.microgreen_type, f"Expected {sample_order.microgreen_type} but got {result}"

def test_get_time(sample_order):
    """Test the GET_TIME command."""
    result = ControllerCommands.GET_TIME.execute(sample_order)
    assert result == sample_order.estimated_time, f"Expected {sample_order.estimated_time} but got {result}"

def test_invalid_command(sample_order):
    """Test an invalid command and ensure it raises an error or returns a fallback."""
    with pytest.raises(NotImplementedError):
        # Attempting to execute a non-existent command should raise an error
        ControllerCommands.execute("INVALID_COMMAND", sample_order)