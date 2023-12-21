import g4f

def get_response_GPT(request_for_GPT):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=[{"role": "user", "content": request_for_GPT}],
        proxy="http://host:port",

    )
    # with open('answer.txt', 'w', encoding='utf-8') as file:
    #     file.write(response)
    return response
