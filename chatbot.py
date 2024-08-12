import os
from ai import getSuggestion
from prompt import system_prompt

import panel as pn  # GUI

context = [ {'role':'system', 'content':system_prompt} ]  # accumulate messages

messages = [] # collect display 

def send_message(_):
    prompt = text_input.value_input
    text_input.value = ''

    context.append({'role':'user', 'content':f"{prompt}"})
    
    # get results from LLM
    response = getSuggestion(prompt)

    # append the response to the context
    context.append({'role':'assistant', 'content':f"{response}"})

    # update the UI
    content = "\n\n".join([f"**{entry['role'].capitalize()}:** {entry['content']}" for entry in context])
    conversation_panel.object = content
    
    # Inject JavaScript to scroll to the bottom
    conversation_panel.param.watch(lambda event: conversation_panel.append(pn.pane.HTML("""
        <script>
            var panel = document.querySelector('.conversation-panel');
            if (panel) {
                panel.scrollTop = panel.scrollHeight;
            }
        </script>
    """)), 'object')
   
# Create conversation panel
conversation_panel = pn.pane.Markdown("Assistant: How may I help you.\n\n", 
                                      height=400,
                                      css_classes=['conversation-panel'])
conversation_panel.style = {
    'overflow-y': 'auto',
    'max-height': 'calc(100vh - 100px)'  # Adjust this value to fit your layout
}

# Create Chat Box (Input + Button)
text_input = pn.widgets.TextInput()
chat_button = pn.widgets.Button(name="Chat!")
chat_button.on_click(send_message)
chat_box = pn.Row (text_input, chat_button)

# Create template to arrange all components
template = pn.template.FastListTemplate(title='Pizza Order Assistant')

# Add the conversation pane to the template's main area
template.main.append(conversation_panel)

# Add the text input and button to the template's sidebar
template.main.append(chat_box)

# Display the template
template.servable()

