import os # I use this to clear the terminal, idk if there's a better way to do it

def summaryGPT(Transcription, Title, prompt):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Hi! :3, not done yet, but here's info that everything works:\n\nTitle: {Title},\n\nTranscription: {Transcription}\n\nPrompt: {prompt}")