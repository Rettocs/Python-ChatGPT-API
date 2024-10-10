import openai

# set project_api_key to a string containing your project's chatgpt api key
#project_api_key = 'thislongstringisanexampleofanapikeystringthatyouwoulduseasthevalueforthisvariable'
project_api_key = ''

# I have my api_key in a text file in a different folder so I don't accidentally upload it
api_key_location = "C:\\api_keys\\"
api_key_filename = "chatgpt-pythontesting.txt"
with open(api_key_location + api_key_filename, 'r') as keyfile:
    project_api_key = keyfile.read()

# add your api key into the openai object
client = openai.OpenAI(
    api_key = project_api_key
)

# prompt is the question you're asking to chatgpt
# model is the version of chatgpt you'll be asking
def get_chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

# this is formatting the command line to be user-friendly
# response is the string output of chatgpt's reply
prompt = input("What would you like to ask?\n\n Q> ")
response = get_chatgpt_response(prompt)
separator = f"\n{'-' * 50}\n"

# puts the reply onto the command line for you to view
print(
        f"{separator}{response}{separator}\n"
      )