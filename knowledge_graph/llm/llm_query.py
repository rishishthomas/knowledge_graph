import requests


openai_api_key = ""  # put your api key here


def get_results_open_ai(results):
    "send the wiki context to openai GPT api and ask it to recognize entities and relationships"
    responses = []
    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    for result in results:
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f"""<|im_start|>system
            You are a friendly assistant. You answer questions from users.<|im_end|>
            <|im_start|>user
            Extract an entity relationship graph from the following text. Output as JSON
        
            Nodes must have label and type attributes. Edges must have source, target and relationship attributes.
        
            text: {result['text']} <|im_end|>
            <|im_start|>assistant
            """
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            print("Response from OpenAI:", response.json())
            print('\n')
            print('##################################################')
            print(response.json()['choices'][0]['message']['content'])
            responses.append(response.json()['choices'][0]['message']['content'])
        else:
            print("Error:", response.status_code, response.text)
    print('##################################################')
    return responses