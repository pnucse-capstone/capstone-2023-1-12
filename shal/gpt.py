import openai

openai.api_key = "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"

messages = []
# user_content = input("user : ")
question = "한국의 수도는?"
messages.append({"role": "user", "content": f"{question}"})
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
assistant_content = completion.choices[0].message["content"].strip()
messages.append({"role": "assistant", "content": f"{assistant_content}"})
print(f"GPT : {assistant_content}")