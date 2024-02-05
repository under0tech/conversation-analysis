import os
import time
import whisper
import utils

model = whisper.load_model("base")

def recognizer_go(
        wait_time, 
        broadcastify_title, 
        input_folder, 
        output_folder, 
        stop_command):
    
    while not stop_command.is_set():

        time.sleep(wait_time)
        files = os.listdir(input_folder)

        if len(files) > 1:
            print(f'\n\033[92m\033[1m{broadcastify_title}\033[0m')

        for file in files[:-1]:
            try:
                if stop_command.is_set():
                    break
                file_path = f'{input_folder}/{file}'
                audio = whisper.load_audio(file_path)
                result = model.transcribe(audio, fp16=False, language='English')
                if result["text"]:
                    print(f'{file}: {result["text"]}')
                    utils.move_file(file_path, output_folder)
                    utils.create_metadata(file_path, output_folder, result["text"])
                else:
                    print('...')
                    os.remove(file_path)
            except Exception as e:
                print(f"An error occurred: {e}")

    stopped_time = time.strftime("%H:%M:%S, %Y, %d %B", time.localtime())
    print(f'thread \033[93mSpeech recognizer\033[0m, DONE at {stopped_time}.')