import os
import ast
import json
import PyPDF2
import traceback
import pandas as pd


def read_pdf(file):
    if file.name.endswith(".pdf"):
        pdf_reader=PyPDF2.PdfReader(file)
        text=''
        for pages in pdf_reader.pages:
            text+=pages.extract_text()
        return text
    elif file.name.endswith('.txt'):
        return file.read.decode('utf-8')
    else:
        raise Exception("UnSupported format")
def get_mcq(quiz):
    try:
      quiz=ast.literal_eval(quiz)
      print(quiz)
      my_arr=[]
      for key,value in quiz.items():
        mcq=value['question']
        options='|'.join([
        f"{option}:{option_value}" for option,option_value in value['options'].items()
    ])
        answers=value['answer']
        my_arr.append({'question':mcq,'options':options,'answer':answers})
      return my_arr
    except Exception as e:
        raise Exception("Error reading quiz")
        