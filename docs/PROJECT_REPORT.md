# EduAssist Project Report

## 1. Title
**EduAssist: An Industry-Specific Large Language Model for Student Academic and Campus Support**

## 2. Industry
Education and Training.

## 3. Problem Statement
Students often need quick answers to academic and administrative questions. Relevant information can be distributed across institutional resources. EduAssist is designed as a conversational assistant for education-related student support.

## 4. Objectives
1. Collect education-domain data.
2. Clean and prepare the dataset.
3. Select a pretrained Hugging Face language model.
4. Fine-tune it using a resource-efficient approach.
5. Develop a chatbot interface.
6. Evaluate the chatbot on unseen questions and out-of-domain questions.
7. Document the complete development process.

## 5. Dataset
The repository contains a generic starter dataset covering Admissions, Academics, Attendance, Examinations, Library, Certificates, Student Services, and Campus Facilities.

**Important:** Before submission, replace or augment generic examples with verified, cited sources appropriate to the chosen educational context.

## 6. Methodology
Data collection → cleaning → instruction formatting → train/test split → pretrained model → LoRA/QLoRA fine-tuning → evaluation → Gradio chatbot.

## 7. Evaluation
Use an unseen test set. Report actual measurements only. Suggested dimensions:
- response relevance
- factual correctness
- completeness
- domain adherence
- out-of-domain refusal/redirect

## 8. Limitations
- Generic starter data does not represent one institution's official policies.
- A generative model can produce incorrect information.
- Model quality depends on data quality and training configuration.
- Official institutional information should be preferred for operational decisions.

## 9. Future Scope
- Retrieval-augmented generation
- multilingual student support
- voice interface
- institution-specific knowledge bases
- authentication
- student-portal integration
