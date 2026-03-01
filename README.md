# 🚀 AI Engineering Masterclass (2026 Edition)

Welcome to the definitive **34-Notebook AI Engineering Curriculum**. 

This repository is strictly designed to bridge the chasm between *learning ML concepts on a laptop* and *deploying scalable, cost-efficient AI systems in production*. It transforms junior AI developers into senior AI Architects.

This is not just another "Learn PyTorch" tutorial. This curriculum focuses heavily on the hardest problems in the field today: **Inference Optimization (vLLM), On-Device Edge LLMs, Agent-to-Agent Protocols, AI Safety Guardrails, and Distributed Computing (Ray).**

---

## 🎓 The "Junior to Senior" Difference

Every single notebook in this repository features a unique **Junior to Senior: Concept Bridge**. 

Rather than just showing you the code, this curriculum explicitly teaches:
- **The Senior Perspective:** *Why* a specific architecture was chosen for production.
- **The Mental Model:** Clear analogies to help you intuitively grasp complex distributed systems.
- **The Common Junior Pitfall:** The #1 mistake beginners make with that technology (and how to avoid it).

Additionally, the most complex notebooks (like Ray, vLLM Inference, and LangGraph Agent Orchestration) contain highly-targeted, line-by-line manual code annotations explaining *why* certain production architectural choices are made.

---

## 📚 Curriculum Structure

The curriculum is divided into 8 linear tracks, taking you from zero to a production-hardened AI Architect.

### 🛠️ Track 1: Foundations
*Learn where AI runs before learning how it runs. GPU economics and infrastructure.*
* `01_python_ai_primer.ipynb` - Decorators, Async/Await, Type Hints
* `02_infrastructure_orchestration.ipynb` - Docker & Kubernetes
* `03_cloud_platforms_ai_infrastructure.ipynb` - AWS/GCP/Azure, GPU Economics, Terraform

### 💾 Track 2: Data Engineering
*AI is only as good as its data. Lakehouses, Streaming, and Feature Stores.*
* `04_data_lakehouse.ipynb` - Iceberg, Delta Lake
* `05_data_management.ipynb` - lakeFS, Great Expectations
* `06_spark_declarative_pipelines.ipynb` - Spark 4.1
* `07_realtime_streaming.ipynb` - Kafka & Flink
* `08_feature_engineering.ipynb` - Feast Feature Store
* `09_ray_distributed_compute.ipynb` - Ray Tasks, Actors, Ray Data

### 🧠 Track 3: Model Development & Alignment
*Fine-tuning and teaching models human preferences.*
* `10_ml_fundamentals.ipynb` - Scikit-Learn to Deep Learning
* `11_model_development.ipynb` - PEFT/LoRA, MLflow, W&B
* `12_alignment_dpo_data_prep.ipynb` - DPO, RLHF, HuggingFace Hub

### 🔄 Track 4: CI/CD & Testing
*Applying rigorous software engineering to non-deterministic AI.*
* `13_cicd_automation.ipynb` - Kubeflow Pipelines, GitHub Actions
* `14_testing_ai_applications.ipynb` - LLM Mocking, Snapshot & Contract Testing

### 🚀 Track 5: Serving & Deployment
*How to serve millions of users without going bankrupt on GPU costs.*
* `15_http_apis_fundamentals.ipynb` - REST & JSON
* `16_async_serving_streaming.ipynb` - FastAPI, Server-Sent Events (SSE)
* `17_model_deployment.ipynb` - Dockerizing Models
* `18_inference_optimization_gpu.ipynb` - vLLM, Continuous Batching, PagedAttention
* `19_on_device_edge_llms.ipynb` - llama.cpp, CoreML, ExecuTorch, WebGPU
* `20_model_context_protocol.ipynb` - MCP (Model Context Protocol)

### 🛡️ Track 6: Monitoring & Governance
*Ensuring your models remain safe, fair, and accurate in the real world.*
* `21_monitoring_feedback.ipynb` - EvidentlyAI, Drift Detection
* `22_governance_security.ipynb` - SHAP, Bias Auditing
* `23_ai_safety_guardrails.ipynb` - Prompt Injection Defense, NeMo/Guardrails AI

### 🤖 Track 7: LLMOps & Agentic Systems
*Building autonomous, structured, and multi-modal AI applications.*
* `24_prompt_engineering.ipynb` - Few-Shot, Chain-of-Thought
* `25_structured_output_function_calling.ipynb` - Pydantic, Instructor
* `26_llmops_context_engineering.ipynb` - LiteLLM, Context Windows
* `27_vector_databases_embeddings.ipynb` - ChromaDB, HNSW/IVF Indexing
* `28_rag_pipeline.ipynb` - Advanced RAG (Retrieval-Augmented Generation)
* `29_multimodal_ai.ipynb` - Vision APIs, Whisper Audio, CLIP Embeddings
* `30_agentic_orchestration.ipynb` - LangGraph, State Machines
* `31_a2a_multi_agent_protocols.ipynb` - CrewAI, Agent-to-Agent Protocols

### 🏗️ Track 8: Production Hardening
*Taking prototypes to enterprise scale.*
* `32_ai_gateways_resilience.ipynb` - Caching, Rate Limiting, Fallbacks
* `33_llm_observability_cost.ipynb` - Langfuse, Token Budgeting
* `34_llm_evaluation.ipynb` - DeepEval, LLM-as-a-Judge

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
   *(Note: Specific libraries like `vllm`, `ray`, or `langgraph` are installed within the individual notebooks as needed to prevent massive dependency conflicts).*

3. **Start Jupyter Lab:**
   ```bash
   jupyter lab
   ```

4. **Begin with Notebook 01.** Even if you know Python, read through `01_python_ai_primer.ipynb` to familiarize yourself with the specific syntax patterns used heavily in later MLOps frameworks.

---

## 🤝 Contributing

The AI landscape changes rapidly. If you find a new optimization technique, a better mental model, or a shift in industry standard protocols, pull requests are heavily encouraged! Please ensure any new notebooks include the standard `🎓 Junior to Senior: Concept Bridge` format.
