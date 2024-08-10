import os
from ai import getSuggestion

import panel as pn  # GUI

context = [ {'role':'system', 'content':"""
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer according to current day and time and ask about his mood, then collects the order, \
Make the welcome message more professional keeping in mind the time of the day while saying Good morning/afternoon/evening. \             
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
create a json summary of the previous food order. Itemize the price for each item\
The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size   4) list of sides include size  5)total price
"""} ]  # accumulate messages

panels = [] # collect display 
input = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

def collect_messages(_):
    prompt = input.value_input
    input.value = ''

    context.append({'role':'user', 'content':f"{prompt}"})
    # response = get_completion_from_messages(context) 
    response = getSuggestion(prompt)
    context.append({'role':'assistant', 'content':f"{response}"})

    panels.append(pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(pn.Row('Assistant:', pn.pane.Markdown(response, width=600, styles={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)


interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Row(
    pn.Column(
       
      pn.panel(interactive_conversation, loading_indicator=True),
      pn.Row(button_conversation),
      input)

)

pn.state.template.param.update(title="Pizza Order Assistant")
pn.extension(sizing_mode="stretch_width", template="fast")
pn.panel(dashboard).servable()


