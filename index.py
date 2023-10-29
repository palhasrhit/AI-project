from urllib import response
import openai
openai.api_key="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"
def get_response(prompt:str) -> str|None:
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
        choices: dict = response.get('choices')[0]
        text = choices.get('text')
        
        
    except Exception as e:
        print("error",e)
        
        return text


def update_list(message:str, pl:list[str]):
    pl.append(message)
    
    def create_prompt(message:str , pl: list[str])->str:
        p_message: str = f'\nHuman:{message}'
        update_list(p_message,pl)
        prompt: str = ''.join(pl) 
        return prompt
    
    
    def get_bot_response(message:str , pl: list[str])-> str:
        prompt: str = create_prompt(message,pl)
        bot_response: str = get_response(prompt)
        
        
        if bot_response:
            update_list(bot_response,pl)
            pos: int = bot_response.find('\nAI: ')
            bot_response=bot_response[pos+5:]
           
        else :
            bot_response = 'somthhing went wrong...'
        
        return bot_response   
           
            
    def main():
        prompt_list: list[str] =[' you will pretend to be a naruto dude that ends every response with "bro"',
                                 '\nHuman: what your collage name?',
                                 '\nAI: It is BNCET,bro']
        
        while True:
            user_input: str = input('you: ')
            response: str = get_bot_response(user_input,prompt_list)
            print(f'Bot:{response}')
            
            
    if __name__=='__main__':
        main()