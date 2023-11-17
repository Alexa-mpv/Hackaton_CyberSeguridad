import openai


def conexion(prompt):
    openai.api_key = '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'

    completion = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    print(completion)
    print(finish)
    
conexion("How do I connect my smart frigde to my phone")
