from openai import OpenAI

api_key = "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"

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

completion = client.chat.completions.create(
  model="deepseek/deepseek-r1:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)
