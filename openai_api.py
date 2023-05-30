import os
import openai
import time


openai.api_key = os.getenv("RBH_OpenAI_Token")
# 'text-ada-001'
# 'text-curie-001'
# 'text-davinci-001'
model_engine = "text-davinci-003"
stop_symbols = "###"
model = openai.Model(engine=model_engine)


def get_answer(user_id, rq, last_rq='', last_prompt_time=0):
    if not rq or len(rq) == 0:
        raise ValueError("Empty request provided. Please, enter valid request to the bot!")
    if len(rq) > 1000:
        rq = rq[:1000]

    print(f">>> Request: ({user_id}) - {rq}")

    # truncate to 1000 symbols from the end
    prompt = f"{last_rq} Q: {rq} ->"[-2000:]
    messages = [{'role': 'user', 'content': rq}]
    print("Sending to OpenAI: " + prompt)
    completion = openai.Completion.create(
        #engine=model,
        model=model_engine,
        prompt=prompt,
        #messages=messages,
        max_tokens=1024,
        #stop=[stop_symbols],
        temperature=0.7)
    eng_ans = completion['choices'][0]['text'].strip()
    print("OpenAI Answer: " + eng_ans)
    print("Tokens: " + str(completion['usage']))
    if "->" in eng_ans:
        eng_ans = eng_ans.split("->")[0].strip()
    ans = eng_ans
    print(f"<<< ({user_id}) {ans}")
    return ans
