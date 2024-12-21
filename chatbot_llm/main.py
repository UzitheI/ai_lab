import requests
import os

API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"

API_TOKEN = "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"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def clean_response(text):
    text = text.capitalize()
    if not text.endswith(('.', '!', '?')):
        text += '.'
    
    return text

def chat_bot(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 30, "return_full_text": False, "temperature": 0.7}
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        full_response = response.json()[0]['generated_text']
        
        return clean_response(full_response)
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    print("Chatbot: Hello! I'm a chatbot powered by the BLOOM model. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chat_bot(user_input)
        print("Chatbot:", response)