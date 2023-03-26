def generate_response(prompt, model="text-davinci-003", max_tokens=500):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.01,
    )
    return response.choices[0].text.strip()
