import streamlit as st
from data_loader import load_data
from llm_interaction import graph_generator,summary_generator,question_generator
from code_executor import graph_execution,graph_improviser,summary_execution,question_execution

def main():
    st.title("DATA ANALYSER")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:

        if("button_pressed" not in st.session_state):
            
            df, iniPrompt = load_data(uploaded_file)
            # st.text(iniPrompt)
            
            # Get the code from LLM
            graph,prompt = graph_generator(iniPrompt)
            # print(graph)
            # st.text(prompt)
            # st.code(graph, language="python")
            fiGraph=graph_improviser(graph,df)
            # st.text("Generated Code:")
            # st.code(fiGraph, language="python")
            # print(df.head())
            graph_execution(fiGraph, df)
            
            summary,prompt=summary_generator(iniPrompt)
            # st.text(prompt)
            # st.text(summary)
            summary_execution(summary,df)
        
        input=st.text_input("Ask Question")
        st.button("Get Response")
        
        if("button_pressed" in st.session_state):
            iniPrompt=""
            iniPrompt=st.session_state.button_pressed[0]
            df=st.session_state.button_pressed[1]
            query,prompt=question_generator((input),iniPrompt)
            # st.text(iniPrompt)
            # st.text(query)
            question_execution(query,df)
        else:
            st.session_state.button_pressed=[iniPrompt]
            st.session_state.button_pressed.append(df)

if __name__ == "__main__":
    main()
