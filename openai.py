import openai


OPENAI_API_KEY = "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"

MODEL = "gpt-4"

PROMPT = """"""


def prompt_request(client: OpenAI, user_prompt, sys_prompt=None, model=MODEL) -> str:
    messages = []

    if sys_prompt:
        messages.append({"role": "system", "content": sys_prompt})

    messages.append({"role": "user", "content": user_prompt})

    response = client.chat.completions.create(
        messages=[messages],
        model=MODEL,
    )

    return response.choices[0].message.content

