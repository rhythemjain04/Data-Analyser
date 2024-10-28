import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
def graph_improviser(code,df):
    # Modify code to include only numeric DataFrame operations
    
    modified_code = code.replace("df.corr()", "numeric_df.corr()")
    modified_code = code.replace("plt.show()", "st.pyplot(plt.gcf())")
    
    lines = modified_code.strip().split('\n')
    if lines[0].startswith('```python'):
        lines.pop(0)  # Remove the first line
        lines.pop()  # Remove the last line

    modified_code = '\n'.join(lines)
    
    return modified_code

def graph_execution(code,df):
    try:
        numeric_df = df.select_dtypes(include='number')
        exec(code, {'df': df, 'st': st, 'plt': plt, 'numeric_df': numeric_df, 'pd': pd})
    except Exception as e:
        print(f"Error: {e}")

def summary_execution(code,df):
    try:
        cleaned_code = '\n'.join(line for line in code.splitlines()[:-1] if '```' not in line)
        exec(cleaned_code,{'df':df})
    except Exception as e:
        print(f"Error: {e}")
        
def question_execution(code,df):
    try:
        cleaned_code = '\n'.join(line for line in code.splitlines()[:-1] if '```' not in line)
        exec(cleaned_code,{'df':df,'pd':pd,"st":st})
    except Exception as e:
        print(f"Error: {e}")
    


