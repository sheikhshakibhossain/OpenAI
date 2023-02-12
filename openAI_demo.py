import openai
openai.api_key = "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"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=60
    )
    message = completions.choices[0].text
    return message.strip()

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024,
        n=1, stop=None, temperature=0.7,
    )
    message = completions.choices[0].text
    return message.strip()

def chat():
    print("Hi, I'm a chatbot. What can I help you with today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: Goodbye!")
            break
        prompt = f"You: {user_input}\nChatbot:"
        response = generate_response(prompt)
        print(f"Chatbot: {response}")

# example usage
generated_text = generate_text("Hello, how are you today?")
print(generated_text)
print("<--------------------------------------------------------------------------------------------------------------------------------------------->")
print()
print()

chat()