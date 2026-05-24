
import streamlit as st
import random
import time

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AWS AI Practitioner Prep",
    page_icon="☁️",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
}

h1, h2, h3 {
    font-family: 'IBM Plex Mono', monospace !important;
}

/* Dark card feel */
.stApp {
    background-color: #0f1117;
    color: #e8eaf0;
}

/* Progress bar */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #FF9900, #FFB84D);
}

/* Radio buttons */
div[data-testid="stRadio"] label {
    font-size: 1rem;
    padding: 8px 0;
}

/* Buttons */
.stButton > button {
    font-family: 'IBM Plex Mono', monospace;
    font-weight: 600;
    letter-spacing: 0.05em;
    background: #FF9900;
    color: #000;
    border: none;
    border-radius: 4px;
    padding: 0.6rem 1.4rem;
    transition: all 0.15s ease;
}
.stButton > button:hover {
    background: #FFB84D;
    transform: translateY(-1px);
}

/* Domain badge */
.domain-badge {
    display: inline-block;
    background: #1a1f2e;
    border: 1px solid #FF9900;
    color: #FF9900;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    padding: 3px 10px;
    border-radius: 2px;
    margin-bottom: 12px;
    text-transform: uppercase;
}

/* Answer feedback boxes */
.correct-box {
    background: #0d2b1a;
    border-left: 4px solid #00c853;
    border-radius: 4px;
    padding: 14px 18px;
    margin-top: 12px;
    color: #b9f6ca;
}
.wrong-box {
    background: #2b0d0d;
    border-left: 4px solid #ff1744;
    border-radius: 4px;
    padding: 14px 18px;
    margin-top: 12px;
    color: #ff8a80;
}

/* Score card */
.score-card {
    background: #1a1f2e;
    border: 1px solid #2d3352;
    border-radius: 8px;
    padding: 28px;
    text-align: center;
    margin: 20px 0;
}

/* Question counter */
.q-counter {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.8rem;
    color: #6b7280;
    margin-bottom: 6px;
}

.metric-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    color: #9ca3af;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
</style>
""", unsafe_allow_html=True)

# ── Question bank ─────────────────────────────────────────────────────────────
QUESTIONS = [
    # Domain 1
    {"domain": "Domain 1: Fundamentals of AI & ML", "q": "What is the primary difference between AI and ML?",
     "options": ["AI is a subset of ML", "ML is a subset of AI", "They are completely unrelated fields", "AI and ML are the same thing"],
     "answer": 1, "explanation": "ML is a subset of AI. Understanding the similarities and differences between AI, ML, and deep learning is a key concept (Task Statement 1.1)."},
    {"domain": "Domain 1: Fundamentals of AI & ML", "q": "Which of the following is NOT a type of machine learning?",
     "options": ["Supervised learning", "Unsupervised learning", "Reinforcement learning", "Diagnostic learning"],
     "answer": 3, "explanation": "Diagnostic learning is not a standard ML type. The standard types are supervised, unsupervised, and reinforcement learning (Task Statement 1.1)."},
    {"domain": "Domain 1: Fundamentals of AI & ML", "q": "What type of data is most suitable for training a computer vision model?",
     "options": ["Tabular data", "Time-series data", "Image data", "Text data"],
     "answer": 2, "explanation": "Image data is most suitable for computer vision models (Task Statement 1.1)."},
    {"domain": "Domain 1: Fundamentals of AI & ML", "q": "Which AWS service is best suited for natural language processing tasks?",
     "options": ["Amazon SageMaker", "Amazon Comprehend", "Amazon Polly", "Amazon Transcribe"],
     "answer": 1, "explanation": "Amazon Comprehend is specifically designed for NLP tasks (Task Statement 1.2)."},
    {"domain": "Domain 1: Fundamentals of AI & ML", "q": "What is the primary purpose of exploratory data analysis (EDA)?",
     "options": ["To train the model", "To deploy the model", "To understand the characteristics of the data", "To monitor the model in production"],
     "answer": 2, "explanation": "EDA is used to understand data characteristics before model training (Task Statement 1.3)."},
    {"domain": "Domain 1: Fundamentals of AI & ML", "q": "What does AUC stand for in model performance metrics?",
     "options": ["Average User Cost", "Area Under the Curve", "Automated Universal Calculation", "Augmented Use Case"],
     "answer": 1, "explanation": "AUC stands for Area Under the Curve (ROC curve) (Task Statement 1.3)."},
    {"domain": "Domain 1: Fundamentals of AI & ML", "q": "Which type of learning is most appropriate with a large dataset of labeled examples?",
     "options": ["Unsupervised learning", "Reinforcement learning", "Supervised learning", "Semi-supervised learning"],
     "answer": 2, "explanation": "Supervised learning is most appropriate when you have labeled data (Task Statement 1.1)."},
    {"domain": "Domain 1: Fundamentals of AI & ML", "q": "What does MLOps stand for?",
     "options": ["Machine Learning Operations", "Multiple Learning Optimizations", "Model Learning Objectives", "Managed Learning Outputs"],
     "answer": 0, "explanation": "MLOps stands for Machine Learning Operations (Task Statement 1.3)."},
    {"domain": "Domain 1: Fundamentals of AI & ML", "q": "What is the primary purpose of model monitoring in production?",
     "options": ["To train new models", "To collect more data", "To detect issues like model drift or data drift", "To perform feature engineering"],
     "answer": 2, "explanation": "Model monitoring is primarily used to detect model drift or data drift (Task Statement 1.3)."},
    {"domain": "Domain 1: Fundamentals of AI & ML", "q": "Which AWS service is best suited for converting text to speech?",
     "options": ["Amazon Comprehend", "Amazon Translate", "Amazon Transcribe", "Amazon Polly"],
     "answer": 3, "explanation": "Amazon Polly is designed for text-to-speech conversion (Task Statement 1.2)."},

    # Domain 2
    {"domain": "Domain 2: Fundamentals of Generative AI", "q": "What is a token in the context of generative AI?",
     "options": ["A security feature", "A unit of text processed by the model", "A type of neural network", "A model evaluation metric"],
     "answer": 1, "explanation": "A token is a unit of text processed by the model (Task Statement 2.1)."},
    {"domain": "Domain 2: Fundamentals of Generative AI", "q": "What is a hallucination in generative AI?",
     "options": ["A visual output produced by the model", "A type of model architecture", "An incorrect or fabricated output presented as fact", "A method of model training"],
     "answer": 2, "explanation": "Hallucinations are incorrect or fabricated outputs presented as fact — a key disadvantage (Task Statement 2.2)."},
    {"domain": "Domain 2: Fundamentals of Generative AI", "q": "Which AWS service is designed specifically for developing generative AI applications?",
     "options": ["Amazon EC2", "Amazon S3", "Amazon Bedrock", "Amazon RDS"],
     "answer": 2, "explanation": "Amazon Bedrock is the AWS service for developing generative AI applications (Task Statement 2.3)."},
    {"domain": "Domain 2: Fundamentals of Generative AI", "q": "What is a foundation model in generative AI?",
     "options": ["A model that can only generate text", "A large, pre-trained model that can be adapted for various tasks", "A model specifically designed for image generation", "A model that requires no training data"],
     "answer": 1, "explanation": "A foundation model is a large, pre-trained model adaptable for various tasks (Task Statement 2.1)."},
    {"domain": "Domain 2: Fundamentals of Generative AI", "q": "What is prompt engineering in generative AI?",
     "options": ["A method of hardware optimization", "Designing the physical structure of AI models", "The process of crafting effective input prompts to guide model outputs", "A way to reduce energy consumption"],
     "answer": 2, "explanation": "Prompt engineering is crafting effective input prompts to guide model outputs (Task Statement 2.1)."},
    {"domain": "Domain 2: Fundamentals of Generative AI", "q": "What is a multi-modal model in generative AI?",
     "options": ["A model that can only process text", "A model that works with multiple types of data (text, images, audio)", "A model that requires multiple GPUs", "A model that can only generate images"],
     "answer": 1, "explanation": "Multi-modal models can process multiple types of data such as text, images, and audio (Task Statement 2.1)."},
    {"domain": "Domain 2: Fundamentals of Generative AI", "q": "What is nondeterminism in generative AI?",
     "options": ["A type of model architecture", "A method of data preprocessing", "The property of producing different outputs for the same input", "A technique for improving model accuracy"],
     "answer": 2, "explanation": "Nondeterminism means the model can produce different outputs for the same input — a potential disadvantage (Task Statement 2.2)."},
    {"domain": "Domain 2: Fundamentals of Generative AI", "q": "What is chunking in the context of generative AI?",
     "options": ["A method of data compression", "Breaking down large inputs into smaller, manageable pieces", "A type of model architecture", "A way to increase model accuracy"],
     "answer": 1, "explanation": "Chunking refers to breaking large inputs into smaller, manageable pieces (Task Statement 2.1)."},
    {"domain": "Domain 2: Fundamentals of Generative AI", "q": "What is a diffusion model in generative AI?",
     "options": ["A model that only works with textual data", "A type of generative model often used for image generation", "A model that requires no training data", "A model designed for NLP"],
     "answer": 1, "explanation": "Diffusion models are generative models commonly used for image generation (Task Statement 2.1)."},
    {"domain": "Domain 2: Fundamentals of Generative AI", "q": "What is the primary purpose of embeddings in generative AI?",
     "options": ["To compress data for storage", "To represent data in a high-dimensional space", "To encrypt sensitive information", "To generate random numbers"],
     "answer": 1, "explanation": "Embeddings represent data in a high-dimensional space for semantic meaning (Task Statement 2.1)."},

    # Domain 3
    {"domain": "Domain 3: Applications of Foundation Models", "q": "What is Retrieval Augmented Generation (RAG)?",
     "options": ["A technique for generating new data", "A method of combining retrieved information with model generation", "A type of model architecture", "A data compression algorithm"],
     "answer": 1, "explanation": "RAG combines retrieved information with model generation to improve accuracy (Task Statement 3.1)."},
    {"domain": "Domain 3: Applications of Foundation Models", "q": "What is the primary purpose of adjusting the temperature parameter in inference?",
     "options": ["To control the physical temperature of the server", "To adjust the creativity or randomness of the model's output", "To increase processing speed", "To reduce energy consumption"],
     "answer": 1, "explanation": "Temperature controls the randomness/creativity of model outputs (Task Statement 3.1)."},
    {"domain": "Domain 3: Applications of Foundation Models", "q": "What is a chain-of-thought prompt?",
     "options": ["A physical chain used in AI hardware", "A prompt that encourages the model to show its reasoning process", "A method of linking multiple AI models", "A technique for encrypting prompts"],
     "answer": 1, "explanation": "Chain-of-thought prompting encourages the model to show its step-by-step reasoning (Task Statement 3.2)."},
    {"domain": "Domain 3: Applications of Foundation Models", "q": "What is the ROUGE metric used for?",
     "options": ["Measuring the redness of model output", "Evaluating the quality of generated summaries", "Calculating energy efficiency", "Determining processing speed"],
     "answer": 1, "explanation": "ROUGE (Recall-Oriented Understudy for Gisting Evaluation) evaluates generated summaries (Task Statement 3.4)."},
    {"domain": "Domain 3: Applications of Foundation Models", "q": "What is the primary purpose of RLHF in foundation model training?",
     "options": ["To reduce energy consumption", "To improve the model's performance based on human evaluations", "To increase model size", "To translate the model into different languages"],
     "answer": 1, "explanation": "RLHF (Reinforcement Learning from Human Feedback) improves models based on human evaluations (Task Statement 3.3)."},
    {"domain": "Domain 3: Applications of Foundation Models", "q": "What is prompt hijacking?",
     "options": ["A method of optimizing prompts", "A technique for stealing prompts from competitors", "An attack where the model is tricked into ignoring the intended prompt", "A way to speed up prompt processing"],
     "answer": 2, "explanation": "Prompt hijacking tricks the model into ignoring the original intended prompt (Task Statement 3.2)."},
    {"domain": "Domain 3: Applications of Foundation Models", "q": "What is the BLEU score used for?",
     "options": ["Measuring energy efficiency", "Evaluating the quality of machine translations", "Calculating processing speed", "Determining market value"],
     "answer": 1, "explanation": "BLEU (Bilingual Evaluation Understudy) evaluates machine translation quality (Task Statement 3.4)."},
    {"domain": "Domain 3: Applications of Foundation Models", "q": "What is the primary advantage of few-shot learning in prompt engineering?",
     "options": ["It requires no examples in the prompt", "It allows the model to learn from a small number of examples", "It always produces perfect results", "It reduces energy consumption"],
     "answer": 1, "explanation": "Few-shot learning lets the model generalize from a small number of examples in the prompt (Task Statement 3.2)."},
    {"domain": "Domain 3: Applications of Foundation Models", "q": "What is continuous pre-training in foundation models?",
     "options": ["A method of constantly retraining the model on new data", "A technique for training models 24/7", "A way to train models using continuous mathematics", "Training models on a continuous physical surface"],
     "answer": 0, "explanation": "Continuous pre-training involves ongoing retraining on new data to keep the model current (Task Statement 3.3)."},
    {"domain": "Domain 3: Applications of Foundation Models", "q": "What is prompt poisoning?",
     "options": ["A method of optimizing prompts", "A technique for improving prompt quality", "An attack where malicious content is inserted into training data or prompts", "A way to speed up prompt processing"],
     "answer": 2, "explanation": "Prompt poisoning inserts malicious content into training data or prompts to manipulate model behavior (Task Statement 3.2)."},

    # Domain 4
    {"domain": "Domain 4: Responsible AI", "q": "Which of the following is NOT a feature of responsible AI?",
     "options": ["Fairness", "Robustness", "Profitability", "Inclusivity"],
     "answer": 2, "explanation": "Profitability is not listed as a feature of responsible AI. Fairness, robustness, and inclusivity are (Task Statement 4.1)."},
    {"domain": "Domain 4: Responsible AI", "q": "Which AWS tool is used to detect and monitor bias in ML models?",
     "options": ["Amazon EC2", "Amazon S3", "Amazon SageMaker Clarify", "Amazon RDS"],
     "answer": 2, "explanation": "Amazon SageMaker Clarify is designed to detect and monitor bias in ML models (Task Statement 4.1)."},
    {"domain": "Domain 4: Responsible AI", "q": "What is overfitting in the context of AI models?",
     "options": ["A model performs too well on training data but poorly on new data", "A model is too large to fit in memory", "A model generates outputs that are too long", "A model consumes too much energy"],
     "answer": 0, "explanation": "Overfitting means the model memorizes training data but fails to generalize to new data (Task Statement 4.1)."},
    {"domain": "Domain 4: Responsible AI", "q": "What is the primary purpose of Amazon Augmented AI (A2I)?",
     "options": ["To replace human workers with AI", "To facilitate human review of AI predictions", "To increase the AI model's size", "To reduce energy consumption"],
     "answer": 1, "explanation": "Amazon A2I facilitates human review of AI predictions for responsible oversight (Task Statement 4.1)."},
    {"domain": "Domain 4: Responsible AI", "q": "What is veracity in responsible AI?",
     "options": ["The speed at which the AI operates", "The truthfulness and accuracy of the AI system's outputs", "The size of the AI model", "The cost of running the AI system"],
     "answer": 1, "explanation": "Veracity refers to the truthfulness and accuracy of AI system outputs (Task Statement 4.1)."},
    {"domain": "Domain 4: Responsible AI", "q": "What is underfitting in AI models?",
     "options": ["A model is too small to fit in memory", "A model performs poorly on both training and new data", "A model generates outputs that are too short", "A model consumes too little energy"],
     "answer": 1, "explanation": "Underfitting means the model is too simple to capture patterns, performing poorly on all data (Task Statement 4.1)."},
    {"domain": "Domain 4: Responsible AI", "q": "Which tool documents model information for transparency?",
     "options": ["Amazon SageMaker Model Cards", "Amazon EC2", "Amazon S3", "Amazon RDS"],
     "answer": 0, "explanation": "Amazon SageMaker Model Cards document model information to support transparency (Task Statement 4.2)."},
    {"domain": "Domain 4: Responsible AI", "q": "What is the primary purpose of subgroup analysis in responsible AI?",
     "options": ["To divide the development team into subgroups", "To analyze model performance across different demographic groups", "To reduce model size", "To increase processing speed"],
     "answer": 1, "explanation": "Subgroup analysis evaluates model fairness across different demographic groups (Task Statement 4.1)."},
    {"domain": "Domain 4: Responsible AI", "q": "What is a potential consequence of using biased datasets in AI training?",
     "options": ["Improved model performance for all groups", "Unfair or discriminatory outcomes for certain groups", "Reduced energy consumption", "Faster model training times"],
     "answer": 1, "explanation": "Biased datasets can lead to unfair or discriminatory outcomes for certain groups (Task Statement 4.1)."},
    {"domain": "Domain 4: Responsible AI", "q": "What is the primary purpose of human audits in responsible AI systems?",
     "options": ["To replace AI systems with human workers", "To verify and validate AI system outputs and processes", "To increase processing speed", "To reduce energy consumption"],
     "answer": 1, "explanation": "Human audits verify and validate AI system outputs and processes (Task Statement 4.1)."},

    # Domain 5
    {"domain": "Domain 5: Security, Compliance & Governance", "q": "Which AWS service is primarily used for managing access and permissions for AI systems?",
     "options": ["Amazon S3", "AWS IAM", "Amazon EC2", "Amazon RDS"],
     "answer": 1, "explanation": "AWS IAM manages roles, policies, and permissions for AI systems (Task Statement 5.1)."},
    {"domain": "Domain 5: Security, Compliance & Governance", "q": "What is the primary purpose of Amazon Macie in AI security?",
     "options": ["To generate AI models", "To discover and protect sensitive data", "To increase model performance", "To reduce energy consumption"],
     "answer": 1, "explanation": "Amazon Macie discovers and protects sensitive data (Task Statement 5.1)."},
    {"domain": "Domain 5: Security, Compliance & Governance", "q": "What does the AWS shared responsibility model refer to?",
     "options": ["Sharing AI models between customers", "Division of security responsibilities between AWS and the customer", "Sharing costs between AWS and the customer", "Dividing AI tasks between humans and machines"],
     "answer": 1, "explanation": "The shared responsibility model divides security duties between AWS and the customer (Task Statement 5.1)."},
    {"domain": "Domain 5: Security, Compliance & Governance", "q": "What is prompt injection in AI security?",
     "options": ["A method of improving prompt quality", "A security vulnerability where malicious input manipulates the AI's behavior", "A technique for speeding up AI processing", "A way to reduce AI energy consumption"],
     "answer": 1, "explanation": "Prompt injection is a security vulnerability where malicious input manipulates AI behavior (Task Statement 5.1)."},
    {"domain": "Domain 5: Security, Compliance & Governance", "q": "What is the primary purpose of AWS CloudTrail in AI governance?",
     "options": ["To generate AI models", "To log API calls and account activity", "To increase model performance", "To reduce energy consumption"],
     "answer": 1, "explanation": "AWS CloudTrail logs API calls and account activity for auditing (Task Statement 5.2)."},
    {"domain": "Domain 5: Security, Compliance & Governance", "q": "What is data residency in AI governance?",
     "options": ["The physical location where data is stored", "The duration for which data is kept", "The speed at which data is processed", "The format in which data is stored"],
     "answer": 0, "explanation": "Data residency refers to the physical location where data is stored (Task Statement 5.2)."},
    {"domain": "Domain 5: Security, Compliance & Governance", "q": "What is the primary purpose of AWS Audit Manager?",
     "options": ["To generate AI models", "To continuously audit AWS usage for compliance", "To increase model performance", "To reduce energy consumption"],
     "answer": 1, "explanation": "AWS Audit Manager continuously audits AWS usage for compliance (Task Statement 5.2)."},
    {"domain": "Domain 5: Security, Compliance & Governance", "q": "Which AWS service is used for automated security assessments?",
     "options": ["Amazon EC2", "Amazon Inspector", "Amazon S3", "Amazon RDS"],
     "answer": 1, "explanation": "Amazon Inspector performs automated security assessments (Task Statement 5.2)."},
    {"domain": "Domain 5: Security, Compliance & Governance", "q": "What is data lineage in AI security?",
     "options": ["A method of data encryption", "Tracking the origin and transformations of data", "A type of AI model architecture", "A way to increase data processing speed"],
     "answer": 1, "explanation": "Data lineage tracks the origin and transformations of data (Task Statement 5.1)."},
    {"domain": "Domain 5: Security, Compliance & Governance", "q": "What is the primary purpose of encryption at rest in AI security?",
     "options": ["To protect data while it's being transmitted", "To protect stored data", "To increase data processing speed", "To reduce energy consumption"],
     "answer": 1, "explanation": "Encryption at rest protects stored data from unauthorized access (Task Statement 5.1)."},
]

DOMAIN_COLORS = {
    "Domain 1: Fundamentals of AI & ML": "#3b82f6",
    "Domain 2: Fundamentals of Generative AI": "#a855f7",
    "Domain 3: Applications of Foundation Models": "#22c55e",
    "Domain 4: Responsible AI": "#f59e0b",
    "Domain 5: Security, Compliance & Governance": "#ef4444",
}

# ── Session state init ────────────────────────────────────────────────────────
def init_state():
    if "mode" not in st.session_state:
        st.session_state.mode = "home"         # home | quiz | review | results
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "idx" not in st.session_state:
        st.session_state.idx = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}          # {idx: chosen_index}
    if "revealed" not in st.session_state:
        st.session_state.revealed = False
    if "domain_filter" not in st.session_state:
        st.session_state.domain_filter = "All Domains"

init_state()

# ── Helpers ───────────────────────────────────────────────────────────────────
def start_quiz(n, domain):
    pool = QUESTIONS if domain == "All Domains" else [q for q in QUESTIONS if q["domain"] == domain]
    random.shuffle(pool)
    st.session_state.questions = pool[:n]
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.answers = {}
    st.session_state.revealed = False
    st.session_state.mode = "quiz"

def submit_answer(chosen):
    q = st.session_state.questions[st.session_state.idx]
    st.session_state.answers[st.session_state.idx] = chosen
    if chosen == q["answer"]:
        st.session_state.score += 1
    st.session_state.revealed = True

def next_question():
    st.session_state.idx += 1
    st.session_state.revealed = False
    if st.session_state.idx >= len(st.session_state.questions):
        st.session_state.mode = "results"

def reset():
    for k in ["mode", "questions", "idx", "score", "answers", "revealed"]:
        del st.session_state[k]
    init_state()

# ── HOME ──────────────────────────────────────────────────────────────────────
if st.session_state.mode == "home":
    st.markdown("# ☁️ AWS AI Practitioner")
    st.markdown("### Exam Prep Quiz")
    st.markdown("---")

    domain_options = ["All Domains"] + sorted(set(q["domain"] for q in QUESTIONS))
    domain = st.selectbox("📂 Filter by domain", domain_options)

    pool_size = len(QUESTIONS) if domain == "All Domains" else len([q for q in QUESTIONS if q["domain"] == domain])
    n = st.slider(f"Number of questions (max {pool_size})", min_value=5, max_value=pool_size, value=min(10, pool_size), step=5)

    st.markdown("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Start Quiz", use_container_width=True):
            start_quiz(n, domain)
            st.rerun()
    with col2:
        if st.button("📋 Review All Q&A", use_container_width=True):
            st.session_state.mode = "review"
            st.rerun()

    st.markdown("---")
    st.markdown("**Domains covered:**")
    for d, color in DOMAIN_COLORS.items():
        count = len([q for q in QUESTIONS if q["domain"] == d])
        st.markdown(f"- **{d}** — {count} questions")

# ── QUIZ ──────────────────────────────────────────────────────────────────────
elif st.session_state.mode == "quiz":
    qs = st.session_state.questions
    idx = st.session_state.idx
    total = len(qs)

    if idx >= total:
        st.session_state.mode = "results"
        st.rerun()

    q = qs[idx]
    progress = (idx) / total
    st.progress(progress)

    st.markdown(f'<div class="q-counter">Question {idx + 1} of {total} · Score: {st.session_state.score}/{idx}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="domain-badge">{q["domain"]}</div>', unsafe_allow_html=True)
    st.markdown(f"### {q['q']}")

    if not st.session_state.revealed:
        chosen = st.radio("Choose your answer:", q["options"], key=f"radio_{idx}", index=None)
        st.markdown("")
        if st.button("Submit Answer", disabled=(chosen is None)):
            chosen_idx = q["options"].index(chosen)
            submit_answer(chosen_idx)
            st.rerun()
    else:
        chosen_idx = st.session_state.answers[idx]
        correct_idx = q["answer"]

        # Show options with result indicators
        for i, opt in enumerate(q["options"]):
            if i == correct_idx:
                st.markdown(f"✅ **{opt}**")
            elif i == chosen_idx and chosen_idx != correct_idx:
                st.markdown(f"❌ ~~{opt}~~")
            else:
                st.markdown(f"○ {opt}")

        if chosen_idx == correct_idx:
            st.markdown(f'<div class="correct-box">✅ <strong>Correct!</strong><br><br>{q["explanation"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="wrong-box">❌ <strong>Incorrect.</strong> The correct answer was: <strong>{q["options"][correct_idx]}</strong><br><br>{q["explanation"]}</div>', unsafe_allow_html=True)

        st.markdown("")
        label = "Finish Quiz →" if idx + 1 >= total else "Next Question →"
        if st.button(label):
            next_question()
            st.rerun()

    if st.button("⟵ Quit Quiz"):
        reset()
        st.rerun()

# ── RESULTS ───────────────────────────────────────────────────────────────────
elif st.session_state.mode == "results":
    qs = st.session_state.questions
    score = st.session_state.score
    total = len(qs)
    pct = int((score / total) * 100)

    st.markdown("# Results")

    grade = "🏆 Excellent!" if pct >= 85 else ("👍 Good progress!" if pct >= 65 else "📚 Keep studying!")
    st.markdown(f'<div class="score-card"><h1 style="font-size:3.5rem;margin:0;color:#FF9900">{pct}%</h1><p style="font-size:1.1rem;margin:8px 0 0">{grade}</p><p style="color:#6b7280;font-size:0.9rem">{score} correct out of {total} questions</p></div>', unsafe_allow_html=True)

    # Domain breakdown
    domain_scores = {}
    for i, q in enumerate(qs):
        d = q["domain"]
        correct = 1 if st.session_state.answers.get(i) == q["answer"] else 0
        if d not in domain_scores:
            domain_scores[d] = {"correct": 0, "total": 0}
        domain_scores[d]["correct"] += correct
        domain_scores[d]["total"] += 1

    if len(domain_scores) > 1:
        st.markdown("### Domain Breakdown")
        for d, s in domain_scores.items():
            dpct = int((s["correct"] / s["total"]) * 100)
            st.markdown(f"**{d}**")
            st.progress(dpct / 100)
            st.markdown(f"<small>{s['correct']}/{s['total']} correct ({dpct}%)</small>", unsafe_allow_html=True)

    # Review wrong answers
    wrong = [(i, qs[i]) for i in range(total) if st.session_state.answers.get(i) != qs[i]["answer"]]
    if wrong:
        st.markdown("### ❌ Questions to Review")
        for i, q in wrong:
            with st.expander(f"Q{i+1}: {q['q'][:80]}..."):
                st.markdown(f"**Your answer:** {q['options'][st.session_state.answers[i]]}")
                st.markdown(f"**Correct answer:** {q['options'][q['answer']]}")
                st.markdown(f"*{q['explanation']}*")

    st.markdown("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Try Again", use_container_width=True):
            reset()
            st.rerun()
    with col2:
        if st.button("🏠 Home", use_container_width=True):
            reset()
            st.rerun()

# ── REVIEW ────────────────────────────────────────────────────────────────────
elif st.session_state.mode == "review":
    st.markdown("# 📋 Full Question Review")
    st.markdown("Browse all questions and answers by domain.")

    domain_options = ["All Domains"] + sorted(set(q["domain"] for q in QUESTIONS))
    selected = st.selectbox("Filter by domain:", domain_options)

    pool = QUESTIONS if selected == "All Domains" else [q for q in QUESTIONS if q["domain"] == selected]

    for i, q in enumerate(pool):
        with st.expander(f"**Q{i+1}:** {q['q']}"):
            st.markdown(f'<div class="domain-badge">{q["domain"]}</div>', unsafe_allow_html=True)
            for j, opt in enumerate(q["options"]):
                if j == q["answer"]:
                    st.markdown(f"✅ **{opt}**")
                else:
                    st.markdown(f"○ {opt}")
            st.info(f"💡 {q['explanation']}")

    st.markdown("")
    if st.button("🏠 Back to Home"):
        st.session_state.mode = "home"
        st.rerun()
