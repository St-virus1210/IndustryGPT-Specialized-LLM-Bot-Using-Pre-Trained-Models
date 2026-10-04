# EduAssist Demo Video Script

## 0:00–0:30 — Introduction
Hello everyone. This project presents EduAssist, an industry-specific Large Language Model chatbot designed for the Education and Training industry.

## 0:30–1:15 — Problem
Students often need answers about academic procedures, examinations, attendance, certificates, library services, and student support. EduAssist provides a conversational interface for these education-related questions.

## 1:15–2:00 — Dataset
The dataset covers Admissions, Academics, Attendance, Examinations, Library, Certificates, Student Services, and Campus Facilities.

## 2:00–3:00 — Model
We start with a pretrained instruction-tuned language model and fine-tune it on education-domain examples using a parameter-efficient LoRA/QLoRA approach on Google Colab.

## 3:00–5:30 — Live Demo
Ask:
1. How can I request a transcript?
2. What is the attendance requirement?
3. How do I register for an examination?
4. How long can I borrow a library book?
5. How can I request a bonafide certificate?
6. How do I update my student information?
7. Ask one unrelated question to demonstrate domain handling.

## 5:30–6:30 — Evaluation
Show the actual held-out test results. Explain relevance, correctness, and out-of-domain handling.

## 6:30–7:00 — Conclusion
EduAssist demonstrates how a pretrained LLM can be adapted to a specific industry using domain-focused data and fine-tuning.
