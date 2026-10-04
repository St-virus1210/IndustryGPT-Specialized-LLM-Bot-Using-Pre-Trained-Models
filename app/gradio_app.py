import os
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_PATH = os.getenv("EDUASSIST_MODEL", "./models/eduassist-adapter")

tokenizer = None
model = None

def load_model():
    global tokenizer, model
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None
    )

def respond(message, history):
    if model is None:
        return "Model is not loaded. Set EDUASSIST_MODEL to your fine-tuned model path and restart the app."
    prompt = f"""You are EduAssist, an education-support assistant.
Answer only education and student-support questions. If a question is outside this domain, politely say that it is outside your scope.

Student: {message}
EduAssist:"""
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=180, do_sample=True, temperature=0.3)
    text = tokenizer.decode(out[0], skip_special_tokens=True)
    return text.split("EduAssist:")[-1].strip()

with gr.Blocks(title="EduAssist") as demo:
    gr.Markdown("# 🎓 EduAssist\n### Education & Training Industry Student Support Assistant")
    gr.ChatInterface(respond, title="Ask EduAssist")

if __name__ == "__main__":
    # Uncomment after placing a trained model in MODEL_PATH:
    # load_model()
    demo.launch()
