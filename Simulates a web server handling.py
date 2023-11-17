import queue
import threading
import time
import random

request_types = ['GET', 'POST', 'PUT', 'DELETE']
processing_times = {'GET': 2, 'POST': 4, 'PUT': 3, 'DELETE': 5}

def process_request(request_type):
    time.sleep(processing_times[request_type])
    print(f"Processed {request_type} request in {processing_times[request_type]} seconds")

def web_server(queue):
    while True:
        if not queue.empty():
            request_type = queue.get()
            process_request(request_type)
        time.sleep(1)

def generate_requests(queue, num_requests):
    for _ in range(num_requests):
        request_type = random.choice(request_types)
        queue.put(request_type)
        print(f"Received {request_type} request")
        time.sleep(random.uniform(0.5, 1.5))

if __name__ == "__main__":
    request_queue = queue.Queue()

    server_thread = threading.Thread(target=web_server, args=(request_queue,))
    server_thread.start()

    request_generator_thread = threading.Thread(target=generate_requests, args=(request_queue, 10))
    request_generator_thread.start()

    request_generator_thread.join()
    server_thread.join()
