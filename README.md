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
*   `02_ml_math_and_data_foundations.ipynb` - Linear Algebra, Calculus, and Statistics for ML

---

### 📉 Phase 2: Classical Machine Learning
*Walking before running. Learning core learning paradigms sequentially builds the intuition needed to understand neural landscapes.*
*   `03_01_linear_models_and_optimization.ipynb` - Linear & Logistic Regression, Gradient Descent
*   `03_02_distance_and_kernel_methods.ipynb` - KNN, SVMs, and the Kernel Trick
*   `03_03_tree_based_models_and_ensembles.ipynb` - Decision Trees, Random Forests, XGBoost
*   `03_04_unsupervised_and_manifold_learning.ipynb` - K-Means, PCA, t-SNE, UMAP
*   `03_05_ml_bayesian_machine_learning.ipynb` - Naive Bayes, Gaussian Processes
*   `03_06_ml_model_evaluation_and_diagnostics.ipynb` - Cross-Validation, ROC/AUC, Bias-Variance Tradeoff
*   `03_07_causal_inference_and_uplift.ipynb` - A/B Testing, Propensity Scores, Pearl's Do-Calculus

---

### 🧠 Phase 3: Deep Learning Foundations
*The core of modern AI. Understanding PyTorch, gradients, and optimization forms the backbone for building advanced models.*
*   `04_pytorch_fundamentals.ipynb` - The Gateway to DL (Tensors, Autograd, DataLoaders)
*   `05_01_neural_network_mathematics.ipynb` - Matrix Multiplications, Backpropagation Calculus
*   `05_02_activation_functions_and_gradients.ipynb` - ReLU, GELU, Sigmoid, Vanishing Gradients
*   `05_03_weight_initialization_theory.ipynb` - Xavier, He, Orthogonal Initialization
*   `05_04_advanced_optimizers_and_loss_landscapes.ipynb` - SGD with Momentum, RMSprop, AdamW
*   `05_05_regularization_and_normalization.ipynb` - Dropout, BatchNorm, LayerNorm, Weight Decay
*   `06_graph_neural_networks.ipynb` - Message Passing, GCNs, GraphSAGE

---

### ⚙️ Phase 4: Data Engineering & Infrastructure [The Scale]
*With modeling intuition built, we introduce the massive data engines and orchestration systems that keep models fed.*
*   `07_eda_data_preprocessing.ipynb` - Data Cleaning Pipelines & Pandas Mastery
*   `08_sql_databases_for_ai.ipynb` - PostgreSQL, Window Functions, Query Optimization
*   `09_data_lakehouse.ipynb` - Apache Iceberg, Delta Lake Data Formats
*   `10_data_management.ipynb` - Data Branching and Versioning with lakeFS
*   `11_spark_declarative_pipelines.ipynb` - Distributed Processing Architecture with Spark
*   `12_feature_engineering.ipynb` - Feature Stores and Feast Integration
*   `13_infrastructure_orchestration.ipynb` - Docker Containers & Kubernetes Services
*   `14_cloud_platforms_ai_infrastructure.ipynb` - Cloud Economics (AWS/GCP/Azure)
*   `15_data_orchestration_pipelines.ipynb` - Airflow DAGs & Dagster TaskFlow
*   `16_realtime_streaming.ipynb` - Distributed Event Streaming with Kafka & Flink
*   `17_ray_distributed_compute.ipynb` - Scaling Compute with Ray Tasks, Actors, and Data
*   `18_distributed_training.ipynb` - Data Parallelism, FSDP, and DeepSpeed

---

### 🤖 Phase 5: Modern NLP & Generative AI [The State-of-the-Art]
*Moving from classical DL to large-scale generative modeling, spanning sequences, transformers, and agentic networks.*
*   `19_01_text_preprocessing_tokenization.ipynb` - BPE, WordPiece, SentencePiece Tokenizers
*   `19_02_word_embeddings_and_word2vec.ipynb` - CBOW, Skip-Gram, GloVe Representations
*   `19_03_recurrent_networks_and_lstms.ipynb` - RNNs, Gradient Clipping, LSTMs
*   `19_04_sequence_to_sequence_and_attention.ipynb` - Encoder-Decoder Architecture and Attention
*   `20_transformer_architecture.ipynb` - Self-Attention, Multi-Head Attention, Positional Encoding
*   `21_pretraining_objectives_and_bert.ipynb` - Masked Language Modeling (MLM), Next Sentence Prediction
*   `22_mixture_of_experts.ipynb` - Sparse Architectures, Routing Algorithms, Switch Transformers
*   `23_01_huggingface_pipelines_and_transfer_learning.ipynb` - Model Hub, AutoClasses, Accelerate
*   `23_02_model_development.ipynb` - Casual LM Training Setup & Evaluation
*   `23_03_sft_implementation.ipynb` - LoRA, QLoRA, and Instruction Tuning
*   `24_01_alignment_dpo_data_prep.ipynb` - Preference Data Formatting for DPO
*   `24_02_rlhf_alignment.ipynb` - PPO, Reward Models, Proximal Policy Optimization
*   `25_prompt_engineering.ipynb` - Few-Shot, Chain-of-Thought, ReAct Prompting
*   `26_structured_output_function_calling.ipynb` - Pydantic schemas, Instructor, Tool Use
*   `27_llmops_context_engineering.ipynb` - LiteLLM, Context Window Management
*   `28_vector_databases_embeddings.ipynb` - ChromaDB, HNSW Indexing, Sentence Transformers
*   `29_rag_pipeline.ipynb` - Advanced RAG, Hybrid Search, Query Rewriting
*   `30_multimodal_ai.ipynb` - Vision APIs, CLIP, Image Bindings
*   `31_01_agentic_orchestration.ipynb` - Building Stateful Agents with LangGraph
*   `31_02_a2a_multi_agent_protocols.ipynb` - CrewAI, Autogen, Multi-Agent Communication
*   `32_model_context_protocol.ipynb` - MCP (Model Context Protocol) Implementation

---

### 🚀 Phase 6: MLOps, Serving & Deployment [The Production]
*Bringing state-of-the-art models out of isolation by heavily testing, packaging, and deploying them to highly concurrent edge or cloud APIs.*
*   `33_testing_ai_applications.ipynb` - Unit Tests, LLM Mocking & Snapshot Testing
*   `34_cicd_automation.ipynb` - Automated Pipelines locally, Kubeflow & GitHub Actions
*   `35_01_model_serialization_and_registry.ipynb` - ONNX Formats, Safetensors & Model Registries
*   `35_02_experiment_tracking.ipynb` - Parameter Logging with MLflow & W&B
*   `36_http_apis_fundamentals.ipynb` - RESTful Principles, Path Parameters, Payloads
*   `37_async_serving_streaming.ipynb` - FastAPI Concurrency, Starlette, SSE Streaming
*   `38_task_queues_async_jobs.ipynb` - Background Workers with Celery & Redis
*   `39_inference_optimization_gpu.ipynb` - Hardware Batching, vLLM & PagedAttention
*   `40_on_device_edge_llms.ipynb` - Quantization formats, llama.cpp & WebGPU Targeting
*   `41_model_deployment.ipynb` - BentoML Serving, Kubernetes HPA, Load Balancing

---

### 👁️ Phase 7: Observability, Governance & System Design [The Senior Lens]
*The true mark of a senior engineer: managing long-term lifecycle performance, securing end points, framing large system blueprints.*
*   `42_01_system_observability_apm.ipynb` - OpenTelemetry, Prometheus Metrics & Grafana
*   `42_02_monitoring_feedback.ipynb` - Data Drift detection with EvidentlyAI
*   `42_03_llm_observability_cost.ipynb` - Tracing workflows with Langfuse & Token Tracking
*   `42_04_llm_evaluation.ipynb` - Creating robust test sets, DeepEval & LLM-as-a-Judge
*   `42_05_ai_gateways_resilience.ipynb` - Rate Limiting, Semantic Caching & API Fallbacks
*   `43_01_api_security_authentication.ipynb` - OAuth2, JWTs & RBAC Authorization
*   `43_02_ai_safety_guardrails.ipynb` - Topic filtering with NeMo Guardrails
*   `43_03_governance_security.ipynb` - Interpretability with SHAP & Systematic Bias Auditing
*   `44_ml_system_design.ipynb` - Architecting end-to-end Real-world AI Systems
*   `45_interview_prep.ipynb` - 100 Technical AI Engineering Interview Questions

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
