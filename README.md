# EduAssist — Education & Training Industry LLM Bot

## Project
**EduAssist: An Industry-Specific Large Language Model for Student Academic and Campus Support**

This repository is a complete starter project aligned to the supplied capstone brief. It includes:
- project documentation
- a starter education-domain Q&A dataset
- a Colab-ready fine-tuning notebook
- a Gradio chatbot application
- evaluation scripts
- presentation/video materials
- research-paper starter structure

## Important scope note
The supplied capstone brief requires students to gather relevant industry data, fine-tune a pretrained model, develop a bot, test it, and create a demonstration video. This package provides the project scaffold and a generic starter dataset. It does **not** claim institution-specific policies as facts. Replace/augment the starter data with verified official educational sources before final submission.

## Quick start
1. Open `notebooks/EduAssist_FineTuning_Colab.ipynb` in Google Colab.
2. Upload `data/eduassist_dataset.jsonl`.
3. Select a compatible small instruction-tuned Hugging Face model.
4. Fine-tune with LoRA/QLoRA on a T4 GPU.
5. Save the trained adapter/model into `models/`.
6. Run `app/gradio_app.py` after configuring the model path.
7. Run `src/evaluate.py` on a held-out test set.
8. Use `docs/PROJECT_REPORT.md`, `presentation/SLIDES_OUTLINE.md`, and `video/DEMO_VIDEO_SCRIPT.md` for submission preparation.

## Recommended workflow
- Start with 3–5 epochs and evaluate before increasing training.
- Keep the final test set separate from training.
- Report actual results; do not invent accuracy or quality scores.
- Cite and document every external dataset/source used in the final version.
