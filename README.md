# 🚀 AI Engineering Masterclass (2026 Edition)

Welcome to the definitive **AI Engineering Curriculum** — now expanded to **43 notebooks** plus 6 deep-theory sub-tracks.

This repository bridges the chasm between *learning ML concepts on a laptop* and *deploying scalable, cost-efficient AI systems in production*. It transforms junior AI developers into senior AI Architects.

This is not just another "Learn PyTorch" tutorial. This curriculum focuses on: **Inference Optimization (vLLM), Transformer Internals, RAG with Hybrid Search, Agent Orchestration (LangGraph), AI Safety Guardrails, and Distributed Computing (Ray).**

---

## 🎓 The "Junior to Senior" Difference

Every notebook features a unique **Junior to Senior: Concept Bridge**:

- **The Senior Perspective:** *Why* a specific architecture was chosen for production.
- **The Mental Model:** Clear analogies to intuitively grasp complex distributed systems.
- **The Common Junior Pitfall:** The #1 mistake beginners make (and how to avoid it).
- **Knowledge Check:** Quiz questions to test understanding.
- **Practical Practice:** Coding exercises with solutions.

---

## 📚 Curriculum Structure

### Phase I: The Data & The Math (The Input)

**🛠️ Track 1: Foundations**
*Learn where AI runs before learning how it runs. GPU economics and infrastructure.*
* `01_python_ai_primer.ipynb` - Decorators, Async/Await, Type Hints
* `02_infrastructure_orchestration.ipynb` - Docker & Kubernetes
* `03_cloud_platforms_ai_infrastructure.ipynb` - AWS/GCP/Azure, GPU Economics, Terraform
* `04_eda_data_preprocessing.ipynb` - EDA, Pandas Mastery, Data Cleaning Pipelines
* `05_sql_databases_for_ai.ipynb` - Advanced SQL, Window Functions, PostgreSQL

**💾 Track 2: Data Engineering & Orchestration**
*AI is only as good as its data. Lakehouses, Streaming, and Feature Stores.*
* `06_data_lakehouse.ipynb` - Iceberg, Delta Lake
* `07_data_management.ipynb` - lakeFS, Great Expectations
* `08_spark_declarative_pipelines.ipynb` - Spark 4.1 Distributed Processing
* `09_data_orchestration_pipelines.ipynb` - Airflow, Dagster, TaskFlow API
* `10_realtime_streaming.ipynb` - Kafka & Flink
* `11_feature_engineering.ipynb` - Feast Feature Store
* `12_ray_distributed_compute.ipynb` - Ray Tasks, Actors, Ray Data

---

### Phase II: Building the AI (The Core)

**🧠 Track 3: Traditional ML & DL Development**
*From ML theory to fine-tuning and alignment.*
* `13_ml_fundamentals.ipynb` - Scikit-Learn to Deep Learning
* `14_pytorch_fundamentals.ipynb` - Tensors, Autograd, nn.Module, Training Loops
* `15_model_development.ipynb` - PEFT/LoRA, MLflow, W&B
* `16_alignment_dpo_data_prep.ipynb` - DPO, RLHF, HuggingFace Hub

**🤖 Track 4: Generative AI & Agentic Systems**
*Building autonomous, structured, and multi-modal AI applications.*
* `17_prompt_engineering.ipynb` - Few-Shot, Chain-of-Thought
* `18_structured_output_function_calling.ipynb` - Pydantic, Instructor
* `19_llmops_context_engineering.ipynb` - LiteLLM, Context Windows
* `20_vector_databases_embeddings.ipynb` - ChromaDB, HNSW/IVF Indexing
* `21_rag_pipeline.ipynb` - Advanced RAG, Hybrid Search, Re-Ranking
* `22_multimodal_ai.ipynb` - Vision APIs, Whisper Audio, CLIP Embeddings
* `23_agentic_orchestration.ipynb` - LangGraph State Machines, Checkpointing
* `24_a2a_multi_agent_protocols.ipynb` - CrewAI, Agent-to-Agent Protocols
* `25_model_context_protocol.ipynb` - MCP (Model Context Protocol)

---

### Phase III: Shipping the AI (The Output)

**🚀 Track 5: Backend Serving & APIs**
*How to serve millions of users without going bankrupt on GPU costs.*
* `26_http_apis_fundamentals.ipynb` - REST & JSON
* `27_async_serving_streaming.ipynb` - FastAPI, Server-Sent Events (SSE)
* `28_task_queues_async_jobs.ipynb` - Celery, Redis, Priority Queues, Webhooks
* `29_inference_optimization_gpu.ipynb` - vLLM, Continuous Batching, PagedAttention
* `30_on_device_edge_llms.ipynb` - llama.cpp, CoreML, ExecuTorch, WebGPU

**🔄 Track 6: MLOps, CI/CD & Deployment**
*Applying rigorous software engineering to non-deterministic AI.*
* `31_cicd_automation.ipynb` - Kubeflow Pipelines, GitHub Actions
* `32_testing_ai_applications.ipynb` - LLM Mocking, Snapshot & Contract Testing
* `33_model_deployment.ipynb` - BentoML, Kubernetes HPA, Load Testing

---

### Phase IV: Productionizing the AI (The Guardrails)

**🛡️ Track 7: Observability & Hardening**
*Taking prototypes to enterprise scale.*
* `34_system_observability_apm.ipynb` - Prometheus, Grafana, Structured Logging
* `35_monitoring_feedback.ipynb` - EvidentlyAI, Drift Detection
* `36_llm_observability_cost.ipynb` - Langfuse, Token Budgeting
* `37_llm_evaluation.ipynb` - DeepEval, LLM-as-a-Judge
* `38_ai_gateways_resilience.ipynb` - Caching, Rate Limiting, Fallbacks

**🔐 Track 8: Governance & Security**
*Ensuring your models remain safe, fair, and secure in the real world.*
* `39_api_security_authentication.ipynb` - JWTs, OAuth2, RBAC, API Gateways
* `40_ai_safety_guardrails.ipynb` - Prompt Injection Defense, NeMo/Guardrails AI
* `41_governance_security.ipynb` - SHAP, Bias Auditing

**🎯 Track 9: Career Readiness**
*Interview prep and system design skills.*
* `42_ml_system_design.ipynb` - 7-Step Framework, Fraud Detection, Search, LLMs
* `43_interview_prep.ipynb` - 60 Interview Questions Mapped to Curriculum

---

## 📖 Deep Theory Tracks (`traditional_ai_domains/`)

For learners who want to go deeper into the theory behind the tools:

| Track | Notebooks | Topics |
|-------|:---------:|--------|
| **Machine Learning** (`ML/`) | 9 | Linear algebra, optimization, trees, kernels, evaluation, system design |
| **Deep Learning** (`DL/`) | 7 | Backprop, activations, initialization, optimizers, **Transformer architecture** |
| **Computer Vision** (`CV/`) | 18 | CNNs, detection, segmentation, ViT, 3DGS, Diffusion, OCR, Tracking, **Anomaly Detection** |
| **NLP** (`NLP/`) | 6 | **[NEW]** Tokenization (BPE), Word2Vec, RNNs/LSTMs, Attention, BERT, HuggingFace |
| **Reinforcement Learning** (`RL/`) | 6 | **[NEW]** MDPs, Q-Learning, DQN, Policy Gradient, **PPO**, **RLHF alignment** |
| **Recommender Systems** (`RS/`) | 4 | **[NEW]** Content/CF, Matrix Factorization, Neural CF/Two-Tower, Production Systems |

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-engineering-masterclass.git
   cd ai-engineering-masterclass
   ```

2. **Set up your environment:**
   We recommend using `conda` or `venv` with Python 3.11+.
   ```bash
   conda create -n ai-masterclass python=3.11
   conda activate ai-masterclass
   pip install jupyterlab
   ```
   *(Note: Specific libraries are installed within individual notebooks to prevent dependency conflicts).*

3. **Start Jupyter Lab:**
   ```bash
   jupyter lab
   ```

4. **Begin with Notebook 01.** Even if you know Python, read through `01_python_ai_primer.ipynb` to familiarize yourself with the patterns used throughout.

### 📋 Recommended Learning Paths

| Goal | Path | Estimated Time |
|------|------|:---:|
| **Full AI Engineer** | NB01 → NB43 (sequential) | 8-12 weeks |
| **LLM/GenAI Engineer** | NB01-03 → NB13-25 → NB29-30 → NB36-37 | 4-6 weeks |
| **MLOps Engineer** | NB01-12 → NB31-35 → NB38-41 | 5-7 weeks |
| **Interview Prep** | NB13 → 14 → NB42 → NB43 | 2-3 weeks |

---

## 🤝 Contributing

The AI landscape changes rapidly. If you find a new optimization technique, a better mental model, or a shift in industry standard protocols, pull requests are heavily encouraged! Please ensure any new notebooks include the standard `🎓 Junior to Senior: Concept Bridge` format with Knowledge Checks and Practical Exercises.
