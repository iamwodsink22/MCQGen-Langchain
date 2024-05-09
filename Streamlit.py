import streamlit as st
import pandas as pd
import json
from src.utils import get_mcq,read_pdf
from src.mcq_gen import generate_evaluate_chain
with open('D:/MCQGen/Response.json','r') as file:
    RESPONSE_JSON=json.load(file)
st.title("MCQ GENERATOR USING LANGCHAIN")
with st.form("user_inputs"):
    file=st.file_uploader(label="Upload your pdf file")
    number=st.number_input(label="Number of MCQ",min_value=2,max_value=10)
    subject=st.text_input(label="Subject")
    difficulty=st.text_input(label="Difficulty")
    button=st.form_submit_button(label='Submit')
    
    if button and file is not None and number and subject and difficulty:
        with st.spinner():
            
                text=read_pdf(file)
                response=generate_evaluate_chain({'text':text,'number':number,'subject':subject,'difficulty':difficulty,'responsejson':json.dumps(RESPONSE_JSON)})
                if isinstance(response,dict):
                    print(response)
                    quiz=response.get('quiz',None)
                    my_arr=get_mcq(quiz)
                    if my_arr is not None:
                        df=pd.DataFrame(my_arr)
                        df.index=df.index+1
                        st.table(df)
                        st.text_area(label="Review",value=response['review'],height=150)
                    else:
                        st.error("Error in the table data")
                else:
                    st.write(response)
            
                
                