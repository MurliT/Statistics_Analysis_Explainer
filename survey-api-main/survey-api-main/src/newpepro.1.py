import gradio as gr
import google.generativeai as genai
import matplotlib.pyplot as plt
import random

# Configure Gemini API key
genai.configure(api_key="AIzaSyCi1iX_IVSRoSumBzQxw3u8rHUDWffGMwg")  # Replace with your real key

# Load Gemini Pro model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Sample data generator for visualization (optional demo)
def generate_pie_chart_for_concept(question):
    fig, ax = plt.subplots()
    
    # Basic placeholder categories for demonstration
    categories = ['Group A', 'Group B', 'Group C']
    values = [random.randint(20, 50) for _ in categories]

    ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
    ax.set_title("Sample Data Distribution (Illustrative Only)")

    return fig

# Function to generate explanation
def explain_statistics(question, level):
    prompt = f"""
Explain the following statistical question to a {level} level student:
"{question}"
Include simple language, key concepts, and a real-world example if possible.
"""
    try:
        response = model.generate_content(prompt)
        explanation = response.text
        chart = generate_pie_chart_for_concept(question)
        return explanation, chart
    except Exception as e:
        return f"⚠️ Error: {e}", None

# Interface Design
with gr.Blocks(theme=gr.themes.Base()) as demo:
    gr.Markdown("""
    <h1 style="text-align: center; color: #4e8cff;">
        📊 Statistical Analysis Explainer
    </h1>
    <p style="text-align: center;">
        Ask any statistics-related question and get a clear, example-based explanation with visual aids powered by Gemini AI.
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
                lines=12
            )
            chart_output = gr.Plot(label="📈 Visual Aid (Sample Chart)")

    submit_btn.click(fn=explain_statistics, inputs=[question_input, level_input], outputs=[output, chart_output])

    gr.Markdown("""
    <div style="text-align: center; font-size: 0.9em; color: #888;">
        Built using Google Gemini API, Gradio & Matplotlib ⚡
    </div>
    """)

# Run app
demo.launch()
