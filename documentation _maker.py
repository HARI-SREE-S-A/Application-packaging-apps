import openai

input_text = str(input("Enter the query"))

openai.api_key = "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"

model_engine = "text-davinci-003"
prompt = input_text

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
