# 🚀 AI Engineering Masterclass (2026 Edition)

Welcome to the definitive **AI Engineering Curriculum** — now expanded to **44 core notebooks** and 4 specialized tracks.

This repository follows a **"T-Shaped AI Engineer"** architecture: mastering the broad foundations of Data Engineering, ML, DL, and NLP first, before choosing a specialization track for deep expertise.

---

## 🎓 The "Junior to Senior" Difference

Every notebook in this curriculum features a unique **Junior to Senior: Concept Bridge**:

- **The Senior Perspective:** *Why* a specific architecture was chosen for production.
- **The Mental Model:** Clear analogies to intuitively grasp complex distributed systems.
- **The Common Junior Pitfall:** The #1 mistake beginners make (and how to avoid it).
- **Knowledge Check:** Quiz questions to test understanding.
- **Practical Practice:** Coding exercises with solutions.

---

## 📚 Curriculum Structure (The Main Track)

### 🧱 Phase I: Data & Systems Foundations
**Module 1: Infrastructure & Orchestration**
*   `01_python_ai_primer.ipynb` - Decorators, Async/Await, Type Hints
*   `02_infrastructure_orchestration.ipynb` - Docker & Kubernetes
*   `03_cloud_platforms_ai_infrastructure.ipynb` - Cloud Economics (AWS/GCP/Azure)
*   `04_eda_data_preprocessing.ipynb` - Data Cleaning Pipelines & Panda Mastery
*   `05_sql_databases_for_ai.ipynb` - PostgreSQL & Advanced SQL
*   `06_data_lakehouse.ipynb` - Apache Iceberg & Delta Lake
*   `07_data_management.ipynb` - versioning with `lakeFS`
*   `08_spark_declarative_pipelines.ipynb` - Distributed Processing with Spark
*   `09_data_orchestration_pipelines.ipynb` - Airflow & Dagster TaskFlow
*   `10_realtime_streaming.ipynb` - Kafka & Flink
*   `11_feature_engineering.ipynb` - Feast Feature Stores
*   `12_ray_distributed_compute.ipynb` - Ray Tasks, Actors, and Data

---

### 🧠 Phase II: Model Foundations
**Module 2: ML Engineering**
*   `13_01_ml_math_and_data_foundations.ipynb`
*   `13_02_linear_models_and_optimization.ipynb`
*   `13_03_distance_and_kernel_methods.ipynb`
*   `13_04_tree_based_models_and_ensembles.ipynb`
*   `13_05_unsupervised_and_manifold_learning.ipynb`
*   `13_06_ml_bayesian_machine_learning.ipynb`
*   `13_07_ml_model_evaluation_and_diagnostics.ipynb`
*   `13_08_causal_inference_and_uplift.ipynb`

**Module 3: Deep Learning Engineering**
*   `14_pytorch_fundamentals.ipynb` - The Gateway to DL
*   `15_01_neural_network_mathematics.ipynb`
*   `15_02_activation_functions_and_gradients.ipynb`
*   `15_03_weight_initialization_theory.ipynb`
*   `15_04_advanced_optimizers_and_loss_landscapes.ipynb`
*   `15_05_regularization_and_normalization.ipynb`
*   `15_06_transformer_architecture.ipynb`
*   `15_07_graph_neural_networks.ipynb`
*   `15_08_mixture_of_experts.ipynb`
*   `15_09_model_serialization_and_registry.ipynb` - ONNX & Model Registries
*   `15_10_experiment_tracking.ipynb` - MLflow & W&B

---

### 🤖 Phase III: Generative AI & Language
**Module 4: Language & Sequence Foundations**
*   `16_01_text_preprocessing_tokenization.ipynb`
*   `16_02_word_embeddings_and_word2vec.ipynb`
*   `16_03_recurrent_networks_and_lstms.ipynb`
*   `16_04_sequence_to_sequence_and_attention.ipynb`
*   `16_05_pretraining_objectives_and_bert.ipynb`
*   `16_06_huggingface_pipelines_and_transfer_learning.ipynb`
*   `16_07_model_development.ipynb` - Training Setup & Evaluation

**Module 5: Generative AI & LLM Engineering**
*   `17_01_alignment_dpo_data_prep.ipynb` - DPO & Alignment Data
*   `17_02_rlhf_alignment.ipynb` - PPO & Reward Models
*   `18_prompt_engineering.ipynb` - Advanced Reasoning & CoT
*   `19_structured_output_function_calling.ipynb` - Pydantic & Instructor
*   `20_llmops_context_engineering.ipynb` - LiteLLM & Context Windows
*   `21_vector_databases_embeddings.ipynb` - ChromaDB & HNSW Indexing
*   `22_rag_pipeline.ipynb` - Advanced RAG & Hybrid Search
*   `23_multimodal_ai.ipynb` - Vision APIs & CLIP
*   `24_agentic_orchestration.ipynb` - LangGraph State Machines
*   `25_a2a_multi_agent_protocols.ipynb` - CrewAI & Protocols
*   `26_model_context_protocol.ipynb` - MCP (Model Context Protocol)

---

### 🚀 Phase IV: Production & MLOps
**Module 6: Backend Serving & APIs**
*   `27_http_apis_fundamentals.ipynb`
*   `28_async_serving_streaming.ipynb` - FastAPI & SSE
*   `29_task_queues_async_jobs.ipynb` - Celery & Redis
*   `30_inference_optimization_gpu.ipynb` - vLLM & PagedAttention
*   `31_on_device_edge_llms.ipynb` - llama.cpp & WebGPU

**Module 7: MLOps & CICD**
*   `32_cicd_automation.ipynb` - Kubeflow & GitHub Actions
*   `33_testing_ai_applications.ipynb` - LLM Mocking & Snapshot Testing
*   `34_model_deployment.ipynb` - BentoML & Kubernetes HPA

**Module 8: Observability & Hardening**
*   `35_system_observability_apm.ipynb` - Prometheus & Grafana
*   `36_monitoring_feedback.ipynb` - EvidentlyAI & Drift
*   `37_llm_observability_cost.ipynb` - Langfuse & Token Tracking
*   `38_llm_evaluation.ipynb` - DeepEval & LLM-as-a-Judge
*   `39_ai_gateways_resilience.ipynb` - Rate Limiting & Fallbacks

**Module 9: Governance & Security**
*   `40_api_security_authentication.ipynb` - JWTs & RBAC
*   `41_ai_safety_guardrails.ipynb` - NeMo Guardrails
*   `42_governance_security.ipynb` - SHAP & Bias Auditing

**Module 10: System Design & Career**
*   `43_ml_system_design.ipynb` - Architecting Real-world AI
*   `44_interview_prep.ipynb` - 100 Technical Interview Questions

---

## 🏆 Specialization Tracks (`/specialization_*`)
Choose your track for deep industry-standard performance.

| Specialization Track | Notebooks | Key Topics |
| :--- | :---: | :--- |
| **Computer Vision** | 17 | CNNs, ViT, Segmentation, 3DGS, Diffusion, Tracking |
| **Reinforcement Learning** | 5 | MDPs, Q-Learning, DQN, Policy Gradient, PPO |
| **Recommender Systems** | 4 | Collaborative Filtering, Matrix Factorization, Two-Tower |
| **Time Series** | 4 | Classical Forecasting, Modern DL for Time Series |

---

## 🚀 Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/ai-engineering-masterclass.git
    cd ai-engineering-masterclass
    ```
2.  **Set up your environment:**
    ```bash
    conda create -n ai-masterclass python=3.11
    conda activate ai-masterclass
    pip install jupyterlab
    ```
3.  **Start Jupyter Lab:**
    ```bash
    jupyter lab
    ```

### 📋 Recommended Learning Paths

| Goal | Path | Time |
| :--- | :--- | :---: |
| **Full AI Architect** | Core Main Track (01-44) + 1 Specialization | 12-16 weeks |
| **Generative AI Expert** | 01-05 → 14 → 16_01-06 → 17-26 → 30-31 | 6-8 weeks |
| **MLOps & Infrastructure** | 01-12 → 32-39 → 43 | 6-8 weeks |
| **Career Jumpstart** | 13-15 → 27-28 → 43-44 | 4 weeks |

---

## 🤝 Contributing
The AI landscape shifts weekly. Pull requests are welcomed for new optimization techniques, better mental models, or architectural shifts!
