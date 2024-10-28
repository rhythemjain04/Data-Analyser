import json
import requests
from header import url,headers

def graph_generator(prompt):
    start=(
    f"DO NOT INCLUDE CODE COMMENTS.\n"
    f"MINIMUM 10 CREATIVE GRAPHS. \n"
    f"write Python code using MATPLOTLIB OR SEABOARN\n"
    )
    end=(
    f"Consider output token length of {1500} tokens.\n"
    f"analyse the above provided data and provide python code for the all possible graphs generation with importing necessary libraries.\n"
    )
    prompt=start+prompt+end
    
    action= "Act as a data analyst, analyse the data summary and head. Provide suitable graphs code"
    response=get_response(prompt,action)
    return response

def summary_generator(prompt):
    start=(
    f"ONLY CODE FOR TEXT AND DATA, NO GRAPH"
    f"EXPAND CONTENT"
    )
    end=(
    f"write python code using streamlit(title, innovative heading, innovative subheadings) to WRITE UNDER MULTIPLE HEADINGS:\n"
    f"WRITE THEORITICAL DETAILED DISCRIPTION by considering the above provided data and write detailed LITERATURE on the data\n"
    f"write theory as long as you can write"

    )
    #f"DIAGNOSTIC ANALYSIS, PRIDICTIVE ANALYSIS, PRESPECTIVE ANALYSIS considering the above provided data details and write detailed LITERATURE on the data, explaining insights on the data.\n"
    #    f"Showing on whichs factors data is varying factors\n"
    prompt=start+prompt+end
    
    action= "Act as a data reviewer, write  insights on data information via PYTHON CODE using streamlit(title, innovative heading, innovative subheadings)."
    response=get_response(prompt,action,2000)
    return response

def question_generator(ques,prompt):
    start=(f"These the the ALREADY created df details:\n")
    mid=(
    f"provide ONLY QUERY IN PYTHON PANDAS to fetch data from df according to provided question:\n"
    )
    end=(
    f"\nWrite ANSWER USING STREAMLIT.write\n"

    )

    prompt=start+prompt+mid+ques+end
    
    action= "Act as a data retrival, convert normal language into pandas query."
    # return prompt
    response=get_response(prompt,action,1000)
    return response
    

def get_response(prompt,action,max_tokens=1500):
    payload = {
    "providers": "openai/gpt-3.5-turbo-0125",
    "text": prompt,
    "chatbot_global_action": action,
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": max_tokens,
    }
    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    code=result['openai/gpt-3.5-turbo-0125']['generated_text']
    return code,prompt








