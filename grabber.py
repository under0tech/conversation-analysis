import time
import requests

def grabber_go(
        max_time, prefix, 
        broadcastify_url, 
        output_folder, 
        stop_command):
    
    while not stop_command.is_set():

        start_time = time.time()
        response = requests.get(broadcastify_url, stream=True)

        with open(f'{output_folder}/{prefix}_{start_time}.mp3', 'wb') as f:
            try:
                for block in response.iter_content(512):
                    f.write(block)
                    if (time.time() - start_time) > max_time or stop_command.is_set():
                        break
            except Exception as e:
                print(f"An error occurred: {e}")
    
    stopped_time = time.strftime("%H:%M:%S, %Y, %d %B", time.localtime())
    print(f'thread \033[93mGrabber\033[0m, DONE at {stopped_time}.')