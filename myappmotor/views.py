import matplotlib
matplotlib.use('Agg')

from django.shortcuts import render
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse, JsonResponse
from .mqtt_client import client, connect_to_broker, disconnect_from_broker
from rest_framework import viewsets
from .models import Device, Sensor
from .serializers import DeviceSerializer, SensorSerializer
# myappmotor/mqtt_client.py
import paho.mqtt.client as mqtt

client = mqtt.Client()

def connect_to_broker():
    client.connect("localhost", 1883, 60)
    client.loop_start()

def disconnect_from_broker():
    client.loop_stop()
    client.disconnect()

# Initialize the client connection
connect_to_broker()

def publish_message(request):
    topic = request.GET.get('topic')
    message = request.GET.get('message')
    
    if not topic or not message:
        return JsonResponse({'error': 'Missing topic or message'}, status=400)
    
    client.publish(topic, message)
    return JsonResponse({'status': 'Message published'})

def subscribe_topic(request):
    topic = request.GET.get('topic')
    
    if not topic:
        return JsonResponse({'error': 'Missing topic'}, status=400)
    
    client.subscribe(topic)
    return JsonResponse({'status': f'Subscribed to {topic}'})

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

def plot_motor_speed(times, speeds):
    """Generate a plot image for motor speed."""
    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Plot data
    ax.plot(times, speeds, marker='o')

    # Add labels and title
    ax.set_xlabel('Time')
    ax.set_ylabel('Speed')
    ax.set_title('Motor Speed Over Time')

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf.getvalue()

def button_page(request):
    return render(request, 'button_page.html')

def motor_plot_view(request):
    # Sample data
    times = [0, 1, 2, 3, 4, 5]
    speeds = [0, 10, 20, 30, 40, 50]

    # Generate plot
    plot_image = plot_motor_speed(times, speeds)

    # Return the plot as an HTTP response
    return HttpResponse(plot_image, content_type='image/png')

