from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3")

message = [
  ("system", "You are an expert product reviewer. You have a great understanding of the product and its features."),
  # HumanMessage(content="Tell me 3 joks").   # if we use variable we have to use tuple instead of HumanMessage
  ("user", "List the main features of the product {product_name}.")
]
prompt_template = ChatPromptTemplate.from_messages(message)

def analyze_pros(features):
    pros_template = ChatPromptTemplate.from_messages([
      ("system", "You are an expert product reviewer. You have a great understanding of the product and its features."),
      ("user", "Given these {features}, list the pros of these features.")
    ])

    return pros_template.format_prompt(features=features)

def analyze_cons(features):
    cons_template = ChatPromptTemplate.from_messages([
      ("system", "You are an expert product reviewer. You have a great understanding of the product and its features."),
      ("user", "Given these {features}, list the cons of these features.")
    ])

    return cons_template.format_prompt(features=features)

def combine_pros_cons(pros, cons):
    return f"Pros: \n{pros}\n\nCons:\n{cons}"


pros_branch_chain = (
  RunnableLambda(lambda x: analyze_pros(x)) | llm | StrOutputParser()
)

cons_branch_chain = (
  RunnableLambda(lambda x: analyze_cons(x)) | llm | StrOutputParser()
)

chain = (
  prompt_template 
  | llm 
  | StrOutputParser()   # here we have all the features of the produdct
  | RunnableParallel(branches={"pros": pros_branch_chain, "cons": cons_branch_chain})
  # | RunnableParallel(branchs=[pros_branch, cons_branch])
  | RunnableLambda(lambda x: combine_pros_cons(x["branches"]["pros"], x["branches"]["cons"]))
  )

result = chain.invoke({"product_name": "Macbook Pro"})
print(result)