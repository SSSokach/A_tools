import json
import os
import openai
import time
import socket
socket.setdefaulttimeout(20)
openai.organization = "org-JFoFp31TiG7JO9OHPVa75tjc"
openai.api_key = 'sk-Kz....'

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False,indent=2)

def build_prompt(context):
    dialogue=''
    for i in context:
        dialogue+=f'\"{i}\"\n'

    prompt=f'''
Assuming that you are a highly empathetic person, generate a concise (no more than 20 words), relevant and empathetic response for the following conversation.

You can take these as examples.

Conversation:
"i there , dont know what to do , jst broke up with my girlfirned , we were 8 years together",
"sorry to hear ! do you have any idea about the break up ? did you think about it ?",
"yes we decided together with our minds , and know i come home and feel so distant from the world"

Response: "sorry again ! hope you will get relief from this sadness . please concentrate on your interests to divert your mind from this ."

Conversation:
"i could not wait to go to the concert .",
"which concert ?",
"the u2 concert . tickets were really expensive and i never thought we would be able to go , but somehow we did ! ! !"

Response: "wow , that is awesome ! i have never been to an actual concert ."

Now generate a concise (no more than 20 words), relevant and empathetic response for the following conversation.

Conversation:
{dialogue}

Response:
    '''
    return prompt
path='E:\workplace\Empathy_test.json'

dataset=load_json(path)

for index,one_data in enumerate(dataset):
    context=one_data['context']
    if one_data['in-Context Learning']!='':
        continue
    prompt=build_prompt(context)

    print(prompt)
    print(index)
    while True:
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            output=completion.choices[0].message
            break

        except openai.error.RateLimitError:
            print('wait 10s !')
            time.sleep(10)
        
    one_data['in-Context Learning']=output['content']
    time.sleep(3)
    if index % 10 ==0:
        write_json(path,dataset)
write_json(path,dataset)