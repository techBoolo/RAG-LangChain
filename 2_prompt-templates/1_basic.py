from langchain.prompts import ChatPromptTemplate

template = "Tell me {number} jokes about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"topic": "cats", "number": 3})
print(prompt)