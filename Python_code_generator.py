
import openai

input_text = str(input("Enter the query"))
prompt = ("give a python code to " + input_text)

openai.api_key = "sk-lbkFJPi2sZK42vy2u0uAWd7rK---***(changed)"

model_engine = "text-davinci-003"
#prompt = input_text

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=550,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
