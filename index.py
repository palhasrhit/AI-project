from urllib import response
import openai
openai.api_key="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"
def get_responce(prompt:str) -> str|None:
    text:str | None=None
    # Create a chat completion request
    try:
        response: dict = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=1,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["Human:","AI:"]
)
        print(response)
    except Exception as e:
        print("error",e)

prompt = "the following us a conversation with an AI assistant"
get_responce(prompt)

