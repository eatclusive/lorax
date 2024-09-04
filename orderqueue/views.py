# Implementation of views that simulate the order process.
# It includes the adding of orders into the FIFO queue and retrieving them.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .fifo_queue import OrderQueueManager
from .utils import generate_dummy_order

# Instantiate the queue manager with a limit of 10 orders
order_queue_manager = OrderQueueManager(max_orders=10)

class AddOrderView(APIView):
    def post(self, request):
        # Simulate receiving data from the NeoNet
        customer_data = generate_dummy_order()
        try:
            order_queue_manager.add_order(customer_data)
            return Response({"message": "Order added successfully.", "order": customer_data}, status=status.HTTP_201_CREATED)
        except OverflowError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GetNextOrderView(APIView):
    def get(self, request):
        try:
            next_order = order_queue_manager.get_next_order()
            return Response({"next order": next_order}, status=status.HTTP_200_OK)
        except IndexError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
