from langchain_ollama import ChatOllama
models = [
    "llama2",
    "gemma4"
]
question = input("question: ")
for model in models:
    try:
        llm  = ChatOllama(model=model)
        response = llm.invoke(question)
        print("="*70)
        print("MODEL:",model)
        print("="*70)
        print(response.content)
    except Exception as e:
        print(model,"not installed")
