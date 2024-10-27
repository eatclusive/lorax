from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Customer:
    customer_name: str
    order_date: datetime = datetime.now()
    microgreen_type: str = "default"
    microgreen_amount: float = 1.0
    estimated_time: timedelta = timedelta(hours=48)

    def __str__(self):
        return f"{self.customer_name} - {self.microgreen_type}"