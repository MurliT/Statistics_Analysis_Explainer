import google.generativeai as genai
import gradio as gr

# Setup API key
genai.configure(api_key="AIzaSyDgH-QiGGQQTndZISHV81w8_9xy2hpXYP4")  # Replace with your Gemini API key

# Use correct model (v1)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

def explain_statistics(user_query, level):
    prompt = f"""
You are an expert AI tutor in statistics.
Explain the following concept to a {level} level student:
"{user_query}"
Make the explanation simple, clear, and friendly.
Include one practical example if possible.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Gradio UI
def chatbot_interface(query, level):
    return explain_statistics(query, level)

iface = gr.Interface(
    fn=chatbot_interface,
    inputs=[
        gr.Textbox(label="Ask a statistical question"),
        gr.Radio(["beginner", "intermediate", "advanced"], label="Select your level")
    ],
    outputs="text",
    title="📊 Statistical Analysis Explainer",
    description="Ask any statistics-related question and get a clear, example-based explanation!"
)

if __name__ == "__main__":
    iface.launch()
