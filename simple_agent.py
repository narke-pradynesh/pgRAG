from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

Model = ChatOpenAI(
    model="nvidia/nemotron-3-nano-30b-a3b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

def get_water_footprint_advice(keyword: str) -> str:
    """ Give the user the water footprint of an appliance and guide them how to reduce their water consumption"""
    return f"The water footprint of {keyword} is "

agent = create_agent(
    model=Model, tools=[get_water_footprint_advice], 
    system_prompt="You are a water footprint bot advising the user about water footprint awareness. Keep a friendly, empathic tone." 
)

keyword = input("Chat: ")

result = agent.invoke({
    "messages": [{"role":"user", "content": f"What is the water footprint of {keyword}?"}]
})

print(result["messages"][-1].content)