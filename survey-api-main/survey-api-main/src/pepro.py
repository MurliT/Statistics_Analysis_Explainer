import google.generativeai as genai
from boat.llms import GoogleLLM
from boat.agents import ChatAgent
from boat.tools import SimpleTool

# Replace with your Google API key
GEMINI_API_KEY = "AIzaSyCi1iX_IVSRoSumBzQxAIzaSyCi1iX_IVSRoSumBzQxw3u8rHUDWffGMwg"
genai.configure(api_key=GEMINI_API_KEY)

# Create a Gemini LLM model for BOAT
llm = GoogleLLM("models/gemini-1.5-pro-latestm")

# Define a simple tool to generate smart city plan
@SimpleTool
def smart_city_generator_tool(budget: str, terrain: str, climate: str, priorities: str) -> str:
    prompt = f"""
You are a futuristic smart city planner AI. Based on the following:
- Budget: {budget}
- Terrain: {terrain}
- Climate: {climate}
- Priorities: {priorities}

Design a smart city with:
1. Architecture
2. Transport system
3. Energy sources
4. Infrastructure
5. Water & waste management
6. Futuristic features

Respond in bullet points.
"""
    response = llm(prompt)
    return response

# Create the agent with the tool
agent = ChatAgent(tools=[smart_city_generator_tool])

# CLI Chatbot interface
def run_chatbot():
    print("🚀 Smart City System Generator using Gemini + BOAT\n")
    budget = input("Enter Budget (Low/Medium/High): ")
    terrain = input("Enter Terrain (Mountainous/Coastal/Desert/Plain): ")
    climate = input("Enter Climate (Tropical/Temperate/Arid/Cold): ")
    priorities = input("Enter Priorities (e.g., Sustainability, Smart Mobility, etc): ")

    print("\n⏳ Generating your Smart City plan...\n")
    query = f"smart_city_generator_tool(budget='{budget}', terrain='{terrain}', climate='{climate}', priorities='{priorities}')"
    result = agent(query)
    print(result)

if __name__ == "__main__":
    run_chatbot()
