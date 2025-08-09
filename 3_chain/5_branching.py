from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnableBranch
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3")

message = [
  ("system", "You are a helpful assistant."),
  # HumanMessage(content="Tell me 3 joks").   # if we use variable we have to use tuple instead of HumanMessage
  ("user", "List the main features of the product {product_name}.")
]
prompt_template = ChatPromptTemplate.from_messages(message)

# positive feedback
postive_feedback_message =  [
  ("system", "You are a helpful assistant."),
  ("human", "Generate a brief, cheerful response for this positive feedback {feedback}")
]
positive_feedback_template = ChatPromptTemplate.from_messages(postive_feedback_message)

# negative feedback
negative_feedback_message =   [
    ("system", "You are a helpful assistant."),
    ("human", "Generate a brief, empathetic response acknowledging this negative feedback and promising to look into it {feedback}")
  ]
negative_feedback_template = ChatPromptTemplate.from_messages(negative_feedback_message)

# neutral feedback
neutral_feedback_message = [
  ("system", "You are a helpful assistant."),
  ("user", "Generate a polite request for more details for this neutral feedback {feedback}")
]
neutral_feedback_template = ChatPromptTemplate.from_messages(neutral_feedback_message)

# escaltle feedback
escalate_feedback_message = [
  ("system", "You are a helpful assistant"),
  ("human", "Generate a message to escalate this feedback to a human agent {feedback}.")
]
escalate_feedback_template = ChatPromptTemplate.from_messages(escalate_feedback_message)

branches = RunnableBranch(
  (
    lambda x: "positive" in x['classification'].lower(),   # lower() b/c the response could be 'Positive'
    positive_feedback_template 
    | llm 
    | StrOutputParser()
  ),
  (
    lambda x: "negative" in x['classification'].lower(),
    negative_feedback_template 
    | llm 
    | StrOutputParser()
  ),
  (
    lambda x: "neutral" in x['classification'].lower(),
    neutral_feedback_template 
    | llm 
    | StrOutputParser()
  ),
  escalate_feedback_template 
  | llm 
  | StrOutputParser()
) 

classification_template = ChatPromptTemplate.from_messages(
  [
    ("system", "You are a helpful assistant."),
    ("user", "Classify the sentiment of this feedback as positive, negative, neutral or escalate {feedback}")
  ]
)

classification_chain = classification_template | llm | StrOutputParser()
chain = { "classification": classification_chain, "feedback": lambda x: x["feedback"]} | branches

positive_review = f"The product is excellent, I really enjoy using it and found it very helpful."
negative_review = f"The product is terrible, It broke just after one use and the quality is very poor."
neutral_review = f"The product is Okay, It works as expected but nothing exceptional."
escalate_review = f"I am not sure about the product yet, can you tell me more about its feature."
escalate_review = f"the produdct is holographic."


result = chain.invoke({"feedback": escalate_review})
print(result)

