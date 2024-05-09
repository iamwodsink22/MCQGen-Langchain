import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from langchain.chat_models import ChatCohere
from langchain.chains import LLMChain,SequentialChain
from langchain.prompts import PromptTemplate
import PyPDF2
load_dotenv()
llm=ChatCohere(cohere_api_key=os.getenv("COHERE_API_KEY"))
TEMPLATE="""
Text:{text}
You are an expert MCQ generator. For  {subject} students, Generate {number} multiple choice questions of {difficulty} difficulty 
Make sure the quetions are not repeated and all the questions must be from the given text. Make sure to strictly format and return the response in given\
format : {responsejson} . Donot use any other words or anything like 'Here are ....' that might make difficult to extract the quiz.
"""
prompt=PromptTemplate(input_variables=['text','subject','number','difficulty','responsejson'],template=TEMPLATE)
quiz_chain=LLMChain(llm=llm,prompt=prompt,output_key="quiz",verbose=True)

TEMPLATE2="""
You are an expert english grammarian and writer. For a given mcq quiz for {subject} students, you need to evaluate the complexity of \
    problem and provide a complexity analysis of the quiz in 50 words. If the quiz is too difficult or too easy compared to congnitive \
    ability of students, you can change the difficulty to match the cognitive ability of students. 
    The Quiz:
    {quiz}
"""
quiz_evaluation_prompt=PromptTemplate(input_variables=['subject','quiz'],template=TEMPLATE2)
review_chain=LLMChain(llm=llm,prompt=quiz_evaluation_prompt,output_key='review',verbose=True)
generate_evaluate_chain=SequentialChain.invoke(chains=[quiz_chain,review_chain],input_variables=['text','subject','number','difficulty','responsejson'],output_variables=['quiz','review'],verbose=True)