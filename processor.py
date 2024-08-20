from ai import get_suggestion
from prompt import system_prompt

context = []
conversation = [] # collect display 

def append_to_context(role, message):
    context.append({'role':role, 'content':f"{message}"}) 
    
    if role != 'system':
        conversation.append(f"\n\n**{role.capitalize()}:** {message}") 

def process(input):
    response = get_suggestion(input)       
    append_to_context('assistant', response)
    
append_to_context('system', system_prompt)
#append_to_context('assistant', "How may I help you.")
