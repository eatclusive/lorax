# An implementation of a utility function that simulates the receiving and unpacking data from NeoNet.
# This dummy data simulates orders coming in over a network

import random
from datetime import timedelta

def generate_dummy_order():
    customer_names = ["Khulan", "Faiz", "Taite", "Hangal", "Khaliun", "Noe"]
    microgreens = ["brocolli", "basil", "celery", "arugula", "cilantro", "spinach"]

    customer_name = random.choice(customer_names)
    microgreen_type = random.choice(microgreens)
    microgreen_amount = round(random.uniform(1.0, 5.0), 2) # The amount of microgreens in grams rounded to the 2nd decimal
    estimated_time = timedelta(hours=random.randint(24, 72))

    customer_data = {
        "customer_name": customer_name,
        "microgreen_type": microgreen_type,
        "microgreen_amount": microgreen_amount,
        "estimated_time": estimated_time
    }

    return customer_data