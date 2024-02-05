import os
import threading as th
import grabber as gr
import recognizer as re
import analyzer as an

broadcastify_title = 'NYPD - 109th and 111th Precincts'
broadcastify_url = "https://broadcastify.cdnstream1.com/27526" 
grabber_output_folder = "grabbed"
recognizer_output_folder = "recognized"
alert_output_folder = "alert"

if not os.path.exists(grabber_output_folder):
    os.makedirs(grabber_output_folder)
if not os.path.exists(recognizer_output_folder):
    os.makedirs(recognizer_output_folder)
if not os.path.exists(alert_output_folder):
    os.makedirs(alert_output_folder)

stop_command = th.Event()

th_grabber = th.Thread(
    target=gr.grabber_go, 
    args=[60, 'NYPD', broadcastify_url, grabber_output_folder, stop_command])
th_recognizer = th.Thread(
    target=re.recognizer_go, 
    args=[10, broadcastify_title, grabber_output_folder, recognizer_output_folder, stop_command])
th_analyzer = th.Thread(
    target=an.analyzer_go, 
    args=[5, recognizer_output_folder, alert_output_folder, stop_command])

th_grabber.start()
th_recognizer.start()
th_analyzer.start()

os.system('clear')
print('\033[93m[CONVERSATION ANALYSIS: STARTED]\033[0m')
input('Press enter to stop process...')
print('\033[93m[STOPPING THREADS]\033[0m')
stop_command.set()

th_grabber.join()
th_recognizer.join()
th_analyzer.join()

print('\033[93m[CONVERSATION ANALYSIS: DONE]\033[0m')