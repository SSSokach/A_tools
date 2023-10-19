import os
import time
import openai

openai.api_key = 'sk-*****'
os.environ['http_proxy']= "http://127.0.0.1:7890"
os.environ['https_proxy']= "http://127.0.0.1:7890"
def use_openai_api(input_str, model="gpt-3.5-turbo",system_prompt="You are a helpful assistant.", temperature=1, max_tokens=512, verbose=True):
    # if len(input_str)>4090:
    #     input_str=input_str[:4090]
    while True:
        try:
            completion = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system","content": system_prompt},
                    {"role": "user", "content": input_str}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            output_str=completion.choices[0].message['content']
            break

        except openai.error.RateLimitError:
            print('RateLimitError wait 5s !')
            time.sleep(5)
        except openai.error.ServiceUnavailableError:
            print('ServiceUnavailableError wait 120s !')
            time.sleep(120)
        except openai.error.Timeout:
            print('Timeout wait 120s !')
            time.sleep(120)
        except openai.error.APIError:
            print('Server shutdown wait 300s !')
            time.sleep(300)
    if verbose:
        print('============system==========')
        print(system_prompt)
        print('============input===========')
        print(input_str)
        print('============output===========')
        print(output_str)
    return output_str