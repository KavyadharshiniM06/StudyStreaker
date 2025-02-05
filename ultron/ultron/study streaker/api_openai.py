from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
