from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever # Assuming this module is correctly defined

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
  print("\n\n-------------------------------")
  question = input("Ask your question(q to quit):")
  print("\n\n")
  if question == "q":
    break

  # --- DEBUGGING PRINT STATEMENTS ---
  print("\n--- DEBUGGING INPUT TO LLM ---")
  print(f"User's Question: '{question}'")
  print(f"Attempting to retrieve reviews for question: '{question}'")
  reviews = retriever.invoke(question) # This calls your 'vector' module
  print(f"Retrieved Reviews (Type: {type(reviews)}):\n'{reviews}'") # Print the reviews
  print(f"Full Prompt Template being used: {template}")
  print(f"Constructed Input Dictionary: {{'reviews': '{reviews}', 'question': '{question}'}}")
  print("----------------------------\n")
  # --- END DEBUGGING PRINT STATEMENTS ---

  result = chain.invoke({"reviews": reviews, "question": question})
  print(f"Model Result:\n'{result}'") # Print the actual result from the model