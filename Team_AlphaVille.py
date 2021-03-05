##### DELAWARE CHALLENGE - STUDENT GAME - TEAM ALPHAVILLE #####
                    ####### COPYWRITR ###########

import moviepy.editor as mpe
import speech_recognition as sr
import fasttext as ft
import os
import numpy as np
from tika import parser
import difflib

CURRENT_PATH = os.getcwd()
PATH_TRAINED_MODULE = os.path.join(CURRENT_PATH, 'lid.176.ftz')
PATH_VIDEOS = os.path.join(CURRENT_PATH,'videos')
PATH_AUDIOS = os.path.join(PATH_VIDEOS, 'audios')
PATH_TEXTS = os.path.join(PATH_VIDEOS, 'texts')
PATH_SCRIPTS_PDFS = os.path.join(PATH_VIDEOS, 'pdfs')

### SPEECH TO AUDIO
if not os.path.isdir(PATH_AUDIOS):
    os.mkdir(PATH_AUDIOS)
elif os.path.isdir(PATH_AUDIOS):
    for i in os.listdir(PATH_AUDIOS):
        if not i.startswith("."):
            for j in os.listdir(os.path.join(PATH_AUDIOS, i)):
                if not j.startswith("."):
                    os.remove(os.path.join(PATH_AUDIOS, i, j))

videos = np.array([i for i in os.listdir(PATH_VIDEOS) if ((not i.startswith('.')) and (i.endswith(".mp4")))])
videos = np.sort(videos)
# videos = np.flip(videos)
for i in range(len(videos)):
# for i in range(3, 4):
    print(f"{i + 1} Video: ")
    print("\n")
    if not os.path.isdir(os.path.join(PATH_AUDIOS, ('audios' + str(i + 1)))):
        os.mkdir(os.path.join(PATH_AUDIOS, ('audios' + str(i + 1))))
        
    elif os.path.isdir(os.path.join(PATH_AUDIOS, ('audios' + str(i + 1)))):
        for i in os.listdir(os.path.join(PATH_AUDIOS, ('audios' + str(i + 1)))):
            os.remove(os.path.join(PATH_AUDIOS, ('audios' + str(i + 1))))
    
    clip_audios_folder = os.path.join(PATH_AUDIOS, ('audios' + str(i + 1)))                   
    clip_name = videos[i]
    clip = mpe.VideoFileClip(os.path.join(PATH_VIDEOS, clip_name))
    start_t = 0
    end_t = 1
    delta_t = 50
    clip_length= clip.duration
    clip_parts = np.ceil(clip_length/delta_t).astype(np.uint16)
    clip_segments = np.linspace(start_t, clip_length, clip_parts)
    count = 0
    while count != clip_segments.size - 1:
        clip_sound= os.path.join(clip_audios_folder, "audio") + str(count + 1) + ".wav"
        clip_cut = clip.subclip(clip_segments[start_t], clip_segments[end_t])
        clip_cut.audio.write_audiofile(clip_sound)
        start_t += 1
        end_t += 1
        count += 1
        # print(f"{count} Part(s) Done!")
        print("\n==================================================================\n")
        
    print(f"\n ============== All Audio Files for {i + 1} Video Extracted ==============\n")
    print("AUDIO EXTRACTION DONE")
    print("\n==================================================================\n")
    
    
### AUDIO TO TEXT
# 1 - portuguese (pt)
# 2 - dutch (nl)
# 3 - english
# 4 - dutch (nl)

# check if texts folder exists and if yes, empty it, else make one
if not os.path.isdir(PATH_TEXTS):
    os.mkdir(PATH_TEXTS)
elif os.path.isdir(PATH_TEXTS):
    for i in os.listdir(PATH_TEXTS):
        if not i.startswith("."):
            os.remove(os.path.join(PATH_TEXTS, i))

model = ft.load_model(PATH_TRAINED_MODULE)
r = sr.Recognizer()
lang_code = {'1': 'pt',
             '2': 'nl',
             '3': 'en',
             '4': 'nl'}
# num_words_text = []
audios = np.array([i for i in os.listdir(PATH_AUDIOS) if not i.startswith('.')])
audios = np.sort(audios)
# audios = np.flip(audios)
audio_symbols = {i[-1]: len(os.listdir(os.path.join(PATH_AUDIOS, i))) for i in np.sort(os.listdir(PATH_AUDIOS)) if not i.startswith('.')}
# len_audio_folders = [len(i) for i in os.listdir(audios) if not i.startswith('.') and (i.endswith(".wav"))]
for i in range(len(audios)):
# for i in range(1):
    print(f"{i + 1} Text: ")
    print("\n")
    actual_lang_code = audios[i - 1][-1]
    # actual_lang_code = audios[][-1]
    
    # create text file for each of the audio folders (4 here)
    if not os.path.exists(os.path.join(PATH_TEXTS, ('text' + str(i + 1) + '.txt'))):
        file = open(('text' + str(i + 1) + '.txt'), "w")
    
    elif os.path.exists(os.path.join(PATH_TEXTS, ('text' + str(i + 1)))):
        file = open(('text' + str(i + 1) + '.txt'), "r+")
        file.truncate(0)
        file.close()
    
    file_path = os.path.join(PATH_TEXTS, ('text' + str(i + 1) + '.txt'))
    
    # loop through all audios of a single audio folder
    # for j in range(1, audio_symbols[actual_lang_code] + 1):
    for j in range(1, len(audio_symbols) + 1):
        audio_path = os.path.join(PATH_AUDIOS,
                                   audios[i - 1],
                                  ('audio' + str(j) + ".wav")
                                  )
        audio = sr.AudioFile(audio_path)
        try:
            with audio as source:
                audio_file = r.record(source) 
            result = r.recognize_google(audio_file, language=lang_code[actual_lang_code])
            print(f"- Text Extracted from Audio File: {j}")
            with open(file_path, mode='a') as file:
                file.write(result)
        except sr.UnknownValueError:
            print("- Language Different from Preset Value!")
        except sr.RequestError as re:
            print("- No results from Google Speech Recognition service; {0}".format(re))
        
### Comparing with the original script
# num_words_original_script = []
for i in range(1, 5):
# for i in range(1, 2):
    if not os.path.exists(os.path.join(PATH_SCRIPTS_PDFS, ('original_script' + str(i) + '.txt'))):
        file = open(('text' + str(i + 1) + '.txt'), "w")
    
    elif os.path.exists(os.path.join(PATH_SCRIPTS_PDFS, ('original_script' + str(i)))):
        file = open(('text' + str(i + 1) + '.txt'), "r+")
        file.truncate(0)
        file.close()
    
    script_output_file_path = os.path.join(PATH_SCRIPTS_PDFS, ('original_script' + str(i + 1) + '.txt'))
    
    script_data = parser.from_file(os.path.join(PATH_SCRIPTS_PDFS, ('script_' + str(i + 1) + '.pdf')))
    original_text = script_data['content'].splitlines()
    original_text = np.asarray(list(set([i.strip().lower() for i in original_text if i != ''])))
    # num_words_original_script.append(original_text.size)
    # script_output_file_path = os.path.join(PATH_SCRIPTS_PDFS, 'rajat.txt')
    with open(script_output_file_path, 'a') as src:
        for i in original_text:
            src.write(i)
            
### Brief Comparison using the DiffLib Module
for i in range(1, 5):
    file_original_script = os.path.join(PATH_SCRIPTS_PDFS, ('original_script' + str(i + 1) + '.txt'))
    file_text = os.path.join(PATH_TEXTS, ('text' + str(i + 1) + '.txt'))
    text1 = open(file_original_script).readlines()
    text2 = open(file_text).readlines()
    
    for line in difflib.unified_diff(text1, text2):
        print(line)
        print("\n==================================================================\n")
        

