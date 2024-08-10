from openai import OpenAI
import os

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI()

llmModel = os.environ.get('LLM_MODEL')

def getSuggestion(prompt): 
    messages = [{"role": "user", "content": prompt}]

    print("LLM Model: ", llmModel)

    # make completion
    completion = client.chat.completions.create(
        model = llmModel, 
        messages = messages)

    # print response
    return completion.choices[0].message.content

# def createEmbedding(text):
#     #text = 'the quick brown fox jumped over the lazy dog'
#     model = 'text-embedding-ada-002'

#     embedding = openai.Embedding.create(input = [text], model=model)
    
#     return embedding.data[0].embedding