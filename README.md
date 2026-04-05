# 🚀 AI Engineering Masterclass (2026 Edition)

Welcome to the definitive **AI Engineering Curriculum** — now expanded to **45 core notebooks** and 4 specialized tracks.

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

### 🧱 Phase 1: Software & Mathematical Foundations
*Building the bedrock. A student must first understand code structure and mathematical primitives before training any AI model.*
*   `01_python_ai_primer.ipynb` - Decorators, Async/Await, Type Hints
*   `02_ml_math_and_data_foundations.ipynb`

---

### 📉 Phase 2: Classical Machine Learning
*Walking before running. Learning core learning paradigms sequentially builds the intuition needed to understand neural landscapes.*
*   `03_01_linear_models_and_optimization.ipynb`
*   `03_02_distance_and_kernel_methods.ipynb`
*   `03_03_tree_based_models_and_ensembles.ipynb`
*   `03_04_unsupervised_and_manifold_learning.ipynb`
*   `03_05_ml_bayesian_machine_learning.ipynb`
*   `03_06_ml_model_evaluation_and_diagnostics.ipynb`
*   `03_07_causal_inference_and_uplift.ipynb`

---

### 🧠 Phase 3: Deep Learning Foundations
*The core of modern AI. Understanding PyTorch, gradients, and optimization forms the backbone for building advanced models.*
*   `04_pytorch_fundamentals.ipynb` - The Gateway to DL
*   `05_01_neural_network_mathematics.ipynb`
*   `05_02_activation_functions_and_gradients.ipynb`
*   `05_03_weight_initialization_theory.ipynb`
*   `05_04_advanced_optimizers_and_loss_landscapes.ipynb`
*   `05_05_regularization_and_normalization.ipynb`
*   `06_graph_neural_networks.ipynb`

---

### ⚙️ Phase 4: Data Engineering & Infrastructure [The Scale]
*With modeling intuition built, we introduce the massive data engines and orchestration systems that keep models fed.*
*   `07_eda_data_preprocessing.ipynb` - Data Cleaning Pipelines & Panda Mastery
*   `08_sql_databases_for_ai.ipynb` - PostgreSQL & Advanced SQL
*   `09_data_lakehouse.ipynb` - Apache Iceberg & Delta Lake
*   `10_data_management.ipynb` - versioning with `lakeFS`
*   `11_spark_declarative_pipelines.ipynb` - Distributed Processing with Spark
*   `12_feature_engineering.ipynb` - Feast Feature Stores
*   `13_infrastructure_orchestration.ipynb` - Docker & Kubernetes
*   `14_cloud_platforms_ai_infrastructure.ipynb` - Cloud Economics
*   `15_data_orchestration_pipelines.ipynb` - Airflow & Dagster TaskFlow
*   `16_realtime_streaming.ipynb` - Kafka & Flink
*   `17_ray_distributed_compute.ipynb` - Ray Tasks, Actors, and Data
*   `18_distributed_training.ipynb`

---

### 🤖 Phase 5: Modern NLP & Generative AI [The State-of-the-Art]
*Moving from classical DL to large-scale generative modeling, spanning sequences, transformers, and agentic networks.*
*   `19_01_text_preprocessing_tokenization.ipynb`
*   `19_02_word_embeddings_and_word2vec.ipynb`
*   `19_03_recurrent_networks_and_lstms.ipynb`
*   `19_04_sequence_to_sequence_and_attention.ipynb`
*   `20_transformer_architecture.ipynb`
*   `21_pretraining_objectives_and_bert.ipynb`
*   `22_mixture_of_experts.ipynb`
*   `23_01_huggingface_pipelines_and_transfer_learning.ipynb`
*   `23_02_model_development.ipynb` - Training Setup & Evaluation
*   `23_03_sft_implementation.ipynb`
*   `24_01_alignment_dpo_data_prep.ipynb` - DPO & Alignment Data
*   `24_02_rlhf_alignment.ipynb` - PPO & Reward Models
*   `25_prompt_engineering.ipynb` - Advanced Reasoning & CoT
*   `26_structured_output_function_calling.ipynb` - Pydantic & Instructor
*   `27_llmops_context_engineering.ipynb` - LiteLLM & Context Windows
*   `28_vector_databases_embeddings.ipynb` - ChromaDB & HNSW Indexing
*   `29_rag_pipeline.ipynb` - Advanced RAG & Hybrid Search
*   `30_multimodal_ai.ipynb` - Vision APIs & CLIP
*   `31_01_agentic_orchestration.ipynb` - LangGraph State Machines
*   `31_02_a2a_multi_agent_protocols.ipynb` - CrewAI & Protocols
*   `32_model_context_protocol.ipynb` - MCP (Model Context Protocol)

---

### 🚀 Phase 6: MLOps, Serving & Deployment [The Production]
*Bringing state-of-the-art models out of isolation by heavily testing, packaging, and deploying them to highly concurrent edge or cloud APIs.*
*   `33_testing_ai_applications.ipynb` - LLM Mocking & Snapshot Testing
*   `34_cicd_automation.ipynb` - Kubeflow & GitHub Actions
*   `35_01_model_serialization_and_registry.ipynb` - ONNX & Model Registries
*   `35_02_experiment_tracking.ipynb` - MLflow & W&B
*   `36_http_apis_fundamentals.ipynb`
*   `37_async_serving_streaming.ipynb` - FastAPI & SSE
*   `38_task_queues_async_jobs.ipynb` - Celery & Redis
*   `39_inference_optimization_gpu.ipynb` - vLLM & PagedAttention
*   `40_on_device_edge_llms.ipynb` - llama.cpp & WebGPU
*   `41_model_deployment.ipynb` - BentoML & Kubernetes HPA

---

### 👁️ Phase 7: Observability, Governance & System Design [The Senior Lens]
*The true mark of a senior engineer: managing long-term lifecycle performance, securing end points, framing large system blueprints.*
*   `42_01_system_observability_apm.ipynb` - Prometheus & Grafana
*   `42_02_monitoring_feedback.ipynb` - EvidentlyAI & Drift
*   `42_03_llm_observability_cost.ipynb` - Langfuse & Token Tracking
*   `42_04_llm_evaluation.ipynb` - DeepEval & LLM-as-a-Judge
*   `42_05_ai_gateways_resilience.ipynb` - Rate Limiting & Fallbacks
*   `43_01_api_security_authentication.ipynb` - JWTs & RBAC
*   `43_02_ai_safety_guardrails.ipynb` - NeMo Guardrails
*   `43_03_governance_security.ipynb` - SHAP & Bias Auditing
*   `44_ml_system_design.ipynb` - Architecting Real-world AI
*   `45_interview_prep.ipynb` - 100 Technical Interview Questions

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
| **Full AI Architect** | Core Main Track (01-45) + 1 Specialization | 12-16 weeks |
| **Generative AI Expert** | 01-05 → 14 → 16_01-06 → 17-26 → 31-32 | 6-8 weeks |
| **MLOps & Infrastructure** | 01-12 → 33-40 → 44 | 6-8 weeks |
| **Career Jumpstart** | 13-15 → 28-29 → 44-45 | 4 weeks |

---

## 🤝 Contributing
The AI landscape shifts weekly. Pull requests are welcomed for new optimization techniques, better mental models, or architectural shifts!
