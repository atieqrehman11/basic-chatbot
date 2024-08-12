import os
from processor import process, conversation, append_to_context

import panel as pn  # GUI

def send_message(_):
    prompt = text_input.value_input
    text_input.value = ''
    process_input(prompt)

def on_enter_press(event):
    prompt = event.new
    process_input(prompt)

def process_input(input):
    append_to_context('user', input)
                              
    # update the UI
    conversation_panel.object = "\n\n".join(conversation)

    process(input)

    # update the UI
    conversation_panel.object = "\n\n".join(conversation)
    
    
    # Inject JavaScript to scroll to the bottom
    # conversation_panel.param.watch(lambda event: conversation_panel.append(pn.pane.HTML("""
    #     <script>
    #         var panel = document.querySelector('.conversation-panel');
    #         if (panel) {
    #             panel.scrollTop = panel.scrollHeight;
    #         }
    #     </script>
    # """)), 'object')

# Create conversation panel
conversation_panel = pn.pane.Markdown(height=400, css_classes=['conversation-panel'])
conversation_panel.style = {
    'overflow-y': 'auto',
    'max-height': 'calc(100vh - 100px)'  # Adjust this value to fit your layout
}

# Create Chat Box (Input + Button)
text_input = pn.widgets.TextInput()
# text_input.param.watch(send_message, parameter_names = 'value')

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

