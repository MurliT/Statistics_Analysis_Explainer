import gradio as gr
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyCi1iX_IVSRoSumBzQxw3u8rHUDWffGMwg")  # Replace with your real key

# Load Gemini Pro model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Function to generate explanation
def explain_statistics(question, level):
    prompt = f"""
Explain the following statistical question to a {level} level student:
"{question}"
Include simple language, key concepts, and a real-world example if possible.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

# Interface Design
with gr.Blocks(theme=gr.themes.Base()) as demo:
    gr.Markdown("""
    <h1 style="text-align: center; color: #4e8cff;">
        📊 Statistical Analysis Explainer
    </h1>
    <p style="text-align: center;">
        Ask any statistics-related question and get a clear, example-based explanation powered by Gemini AI.
    </p>
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            question_input = gr.Textbox(
                label="📌 Ask a statistical question",
                placeholder="E.g., How does sleep quality affect GPA across universities?",
                lines=6
            )
            level_input = gr.Radio(
                ["Beginner", "Intermediate", "Advanced"],
                label="🎓 Choose explanation level",
                value="Beginner"
            )
            submit_btn = gr.Button("🚀 Generate Explanation", variant="primary")
        
        with gr.Column(scale=1):
            output = gr.Textbox(
                label="🧠 Explanation Output",
                placeholder="The AI's response will appear here...",
                lines=18
            )

    submit_btn.click(fn=explain_statistics, inputs=[question_input, level_input], outputs=output)

    gr.Markdown("""
    <div style="text-align: center; font-size: 0.9em; color: #888;">
        Built using Google Gemini API & Gradio ⚡
    </div>
    """)

# Run app
demo.launch()
