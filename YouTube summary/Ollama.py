import ollama
import os # I use this to clear the terminal, idk if there's a better way to do it

def get_user_information():
    botModelOptions = [model.model for model in ollama.list().models]
    while True:
        botModel = input(f'Enter the model, your installed models are: {botModelOptions}: ').lower()
        if botModel in botModelOptions:
            break
        print("Invalid model. Please enter a valid model name.")
    return botModel

def summaryOllama(Transcription, Title, prompt):
    model = get_user_information()

    # changePrompt = input(f"The default prompt is: {prompt}, do you want to change it with a custom one? (y, n): ")
   
    # if changePrompt == "y":
    #     prompt = input("Type your new prompt here: ")      # <------------ Not yet to be included, I'll do it sometime later.
    # else changePrompt == "n":
    #     pass

    response: ChatResponse = ollama.chat(model=model, messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{Title}\n\n{response['message']['content']}")