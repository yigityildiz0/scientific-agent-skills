# ai-research-skills

[English](ai-research-skills.en.md) · [Türkçe](ai-research-skills.tr.md) · [Library](../../README.tr.md)

**Eğitim, RAG, değerlendirme ve deneyler için geniş ML mühendisliği kütüphanesini yönlendirir.**

## Örnek istek

> Türkçe RAG sistemi için veri sızıntısını gözeten değerlendirme tasarla.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

AI/ML engineering and research library: 98 modules for model training, RAG, evaluation, experiments, research ideas, papers and plots. TR: AI araştır, model eğit, RAG kur, ML makalesi, deney planla.

</details>

## Çalışma mantığı

İlgili teknik modülü seçer; donanım/veri sınırlarını inceler; temel karşılaştırma ve bağımsız değerlendirme kurar; belirsizliği raporlar.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/ai-research-skills/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Modül | Kaynak kapsamı |
|---|---|
| [a-evolve](../../skills/common/ai-research-skills/modules/a-evolve/MODULE.md) | Provides guidance for automatically evolving and optimizing AI agents across any domain using LLM-driven evolution algorithms. Use when building self-improving agents, optimizing a |
| [academic-plotting](../../skills/common/ai-research-skills/modules/academic-plotting/MODULE.md) | Generates publication-quality figures for ML papers from research context. Given a paper section or description, extracts system components and relationships to generate architectu |
| [accelerate](../../skills/common/ai-research-skills/modules/accelerate/MODULE.md) | Simplest distributed training API. 4 lines to add distributed support to any PyTorch script. Unified API for DeepSpeed/FSDP/Megatron/DDP. Automatic device placement, mixed precisio |
| [audiocraft](../../skills/common/ai-research-skills/modules/audiocraft/MODULE.md) | PyTorch library for audio generation including text-to-music (MusicGen) and text-to-sound (AudioGen). Use when you need to generate music from text descriptions, create sound effec |
| [autogpt](../../skills/common/ai-research-skills/modules/autogpt/MODULE.md) | Autonomous AI agent platform for building and deploying continuous agents. Use when creating visual workflow agents, deploying persistent autonomous agents, or building complex mul |
| [autoresearch](../../skills/common/ai-research-skills/modules/autoresearch/MODULE.md) | Orchestrates end-to-end autonomous AI research projects using a two-loop architecture. The inner loop runs rapid experiment iterations with clear optimization targets. The outer lo |
| [awq](../../skills/common/ai-research-skills/modules/awq/MODULE.md) | Activation-aware weight quantization for 4-bit LLM compression with 3x speedup and minimal accuracy loss. Use when deploying large models (7B-70B) on limited GPU memory, when you n |
| [axolotl](../../skills/common/ai-research-skills/modules/axolotl/MODULE.md) | Expert guidance for fine-tuning LLMs with Axolotl - YAML configs, 100+ models, LoRA/QLoRA, DPO/KTO/ORPO/GRPO, multimodal support |
| [bigcode-evaluation-harness](../../skills/common/ai-research-skills/modules/bigcode-evaluation-harness/MODULE.md) | Evaluates code generation models across HumanEval, MBPP, MultiPL-E, and 15+ benchmarks with pass@k metrics. Use when benchmarking code models, comparing coding abilities, testing m |
| [bitsandbytes](../../skills/common/ai-research-skills/modules/bitsandbytes/MODULE.md) | Quantizes LLMs to 8-bit or 4-bit for 50-75% memory reduction with minimal accuracy loss. Use when GPU memory is limited, need to fit larger models, or want faster inference. Suppor |
| [blip-2](../../skills/common/ai-research-skills/modules/blip-2/MODULE.md) | Vision-language pre-training framework bridging frozen image encoders and LLMs. Use when you need image captioning, visual question answering, image-text retrieval, or multimodal c |
| [brainstorming-research-ideas](../../skills/common/ai-research-skills/modules/brainstorming-research-ideas/MODULE.md) | Guides researchers through structured ideation frameworks to discover high-impact research directions. Use when exploring new problem spaces, pivoting between projects, or seeking  |
| [chroma](../../skills/common/ai-research-skills/modules/chroma/MODULE.md) | Open-source embedding database for AI applications. Store embeddings and metadata, perform vector and full-text search, filter by metadata. Simple 4-function API. Scales from noteb |
| [clip](../../skills/common/ai-research-skills/modules/clip/MODULE.md) | OpenAI's model connecting vision and language. Enables zero-shot image classification, image-text matching, and cross-modal retrieval. Trained on 400M image-text pairs. Use for ima |
| [compiler](../../skills/common/ai-research-skills/modules/compiler/MODULE.md) | Compiles any research input — PDF papers, GitHub repositories, experiment logs, code directories, or raw notes — into a complete Agent-Native Research Artifact (ARA) with cognitive |
| [constitutional-ai](../../skills/common/ai-research-skills/modules/constitutional-ai/MODULE.md) | Anthropic's method for training harmless AI through self-improvement. Two-phase approach - supervised learning with self-critique/revision, then RLAIF (RL from AI Feedback). Use fo |
| [cosmos-policy](../../skills/common/ai-research-skills/modules/cosmos-policy/MODULE.md) | Evaluates NVIDIA Cosmos Policy on LIBERO and RoboCasa simulation environments. Use when setting up cosmos-policy for robot manipulation evaluation, running headless GPU evaluations |
| [creative-thinking-for-research](../../skills/common/ai-research-skills/modules/creative-thinking-for-research/MODULE.md) | Applies cognitive science frameworks for creative thinking to CS and AI research ideation. Use when seeking genuinely novel research directions by leveraging combinatorial creativi |
| [crewai](../../skills/common/ai-research-skills/modules/crewai/MODULE.md) | Multi-agent orchestration framework for autonomous AI collaboration. Use when building teams of specialized agents working together on complex tasks, when you need role-based agent |
| [deepspeed](../../skills/common/ai-research-skills/modules/deepspeed/MODULE.md) | deepspeed |
| [dspy](../../skills/common/ai-research-skills/modules/dspy/MODULE.md) | Build complex AI systems with declarative programming, optimize prompts automatically, create modular RAG systems and agents with DSPy - Stanford NLP's framework for systematic LM  |
| [faiss](../../skills/common/ai-research-skills/modules/faiss/MODULE.md) | Facebook's library for efficient similarity search and clustering of dense vectors. Supports billions of vectors, GPU acceleration, and various index types (Flat, IVF, HNSW). Use f |
| [flash-attention](../../skills/common/ai-research-skills/modules/flash-attention/MODULE.md) | Optimizes transformer attention with Flash Attention for 2-4x speedup and 10-20x memory reduction. Use when training/running transformers with long sequences (>512 tokens), encount |
| [gguf](../../skills/common/ai-research-skills/modules/gguf/MODULE.md) | GGUF format and llama.cpp quantization for efficient CPU/GPU inference. Use when deploying models on consumer hardware, Apple Silicon, or when needing flexible quantization from 2- |
| [gptq](../../skills/common/ai-research-skills/modules/gptq/MODULE.md) | Post-training 4-bit quantization for LLMs with minimal accuracy loss. Use for deploying large models (70B, 405B) on consumer GPUs, when you need 4× memory reduction with <2% perple |
| [grpo-rl-training](../../skills/common/ai-research-skills/modules/grpo-rl-training/MODULE.md) | Expert guidance for GRPO/RL fine-tuning with TRL for reasoning and task-specific model training |
| [guidance](../../skills/common/ai-research-skills/modules/guidance/MODULE.md) | Control LLM output with regex and grammars, guarantee valid JSON/XML/code generation, enforce structured formats, and build multi-step workflows with Guidance - Microsoft Research' |
| [hqq](../../skills/common/ai-research-skills/modules/hqq/MODULE.md) | Half-Quadratic Quantization for LLMs without calibration data. Use when quantizing models to 4/3/2-bit precision without needing calibration datasets, for fast quantization workflo |
| [huggingface-tokenizers](../../skills/common/ai-research-skills/modules/huggingface-tokenizers/MODULE.md) | Fast tokenizers optimized for research and production. Rust-based implementation tokenizes 1GB in <20 seconds. Supports BPE, WordPiece, and Unigram algorithms. Train custom vocabul |
| [instructor](../../skills/common/ai-research-skills/modules/instructor/MODULE.md) | Extract structured data from LLM responses with Pydantic validation, retry failed extractions automatically, parse complex JSON with type safety, and stream partial results with In |
| [knowledge-distillation](../../skills/common/ai-research-skills/modules/knowledge-distillation/MODULE.md) | Compress large language models using knowledge distillation from teacher to student models. Use when deploying smaller models with retained performance, transferring GPT-4 capabili |
| [lambda-labs](../../skills/common/ai-research-skills/modules/lambda-labs/MODULE.md) | Reserved and on-demand GPU cloud instances for ML training and inference. Use when you need dedicated GPU instances with simple SSH access, persistent filesystems, or high-performa |
| [langchain](../../skills/common/ai-research-skills/modules/langchain/MODULE.md) | Framework for building LLM-powered applications with agents, chains, and RAG. Supports multiple providers (OpenAI, Anthropic, Google), 500+ integrations, ReAct agents, tool calling |
| [langsmith](../../skills/common/ai-research-skills/modules/langsmith/MODULE.md) | LLM observability platform for tracing, evaluation, and monitoring. Use when debugging LLM applications, evaluating model outputs against datasets, monitoring production systems, o |
| [litgpt](../../skills/common/ai-research-skills/modules/litgpt/MODULE.md) | Implements and trains LLMs using Lightning AI's LitGPT with 20+ pretrained architectures (Llama, Gemma, Phi, Qwen, Mistral). Use when need clean model implementations, educational  |
| [llama-cpp](../../skills/common/ai-research-skills/modules/llama-cpp/MODULE.md) | GGUF inference on CPU, Apple Silicon, NVIDIA CUDA and supported AMD/Intel GPUs; local/offloaded deployment and quantization. Benchmark speed for the actual hardware and workload. |
| [llama-factory](../../skills/common/ai-research-skills/modules/llama-factory/MODULE.md) | Expert guidance for fine-tuning LLMs with LLaMA-Factory - WebUI no-code, 100+ models, 2/3/4/5/6/8-bit QLoRA, multimodal support |
| [llamaguard](../../skills/common/ai-research-skills/modules/llamaguard/MODULE.md) | Meta's 7-8B specialized moderation model for LLM input/output filtering. 6 safety categories - violence/hate, sexual content, weapons, substances, self-harm, criminal planning. 94- |
| [llamaindex](../../skills/common/ai-research-skills/modules/llamaindex/MODULE.md) | Data framework for building LLM applications with RAG. Specializes in document ingestion (300+ connectors), indexing, and querying. Features vector indices, query engines, agents,  |
| [llava](../../skills/common/ai-research-skills/modules/llava/MODULE.md) | Large Language and Vision Assistant. Enables visual instruction tuning and image-based conversations. Combines CLIP vision encoder with Vicuna/LLaMA language models. Supports multi |
| [lm-evaluation-harness](../../skills/common/ai-research-skills/modules/lm-evaluation-harness/MODULE.md) | Evaluates LLMs across 60+ academic benchmarks (MMLU, HumanEval, GSM8K, TruthfulQA, HellaSwag). Use when benchmarking model quality, comparing models, reporting academic results, or |
| [long-context](../../skills/common/ai-research-skills/modules/long-context/MODULE.md) | Extend context windows of transformer models using RoPE, YaRN, ALiBi, and position interpolation techniques. Use when processing long documents (32k-128k+ tokens), extending pre-tr |
| [mamba](../../skills/common/ai-research-skills/modules/mamba/MODULE.md) | State-space model with O(n) complexity vs Transformers' O(n²). 5× faster inference, million-token sequences, no KV cache. Selective SSM with hardware-aware design. Mamba-1 (d_state |
| [megatron-core](../../skills/common/ai-research-skills/modules/megatron-core/MODULE.md) | Trains large language models (2B-462B parameters) using NVIDIA Megatron-Core with advanced parallelism strategies. Use when training models >1B parameters, need maximum GPU efficie |
| [miles](../../skills/common/ai-research-skills/modules/miles/MODULE.md) | Provides guidance for enterprise-grade RL training using miles, a production-ready fork of slime. Use when training large MoE models with FP8/INT4, needing train-inference alignmen |
| [ml-paper-writing](../../skills/common/ai-research-skills/modules/ml-paper-writing/MODULE.md) | Write publication-ready ML/AI papers for NeurIPS, ICML, ICLR, ACL, AAAI, COLM. Use when drafting papers from research repos, structuring arguments, verifying citations, or preparin |
| [ml-training-recipes](../../skills/common/ai-research-skills/modules/ml-training-recipes/MODULE.md) | Battle-tested PyTorch training recipes for all domains — LLMs, vision, diffusion, medical imaging, protein/drug discovery, spatial omics, genomics. Covers training loops, optimizer |
| [mlflow](../../skills/common/ai-research-skills/modules/mlflow/MODULE.md) | Track ML experiments, manage model registry with versioning, deploy models to production, and reproduce experiments with MLflow - framework-agnostic ML lifecycle platform |
| [modal](../../skills/common/ai-research-skills/modules/modal/MODULE.md) | Serverless GPU cloud platform for running ML workloads. Use when you need on-demand GPU access without infrastructure management, deploying ML models as APIs, or running batch jobs |
| [model-merging](../../skills/common/ai-research-skills/modules/model-merging/MODULE.md) | Merge multiple fine-tuned models using mergekit to combine capabilities without retraining. Use when creating specialized models by blending domain-specific expertise (math + codin |
| [model-pruning](../../skills/common/ai-research-skills/modules/model-pruning/MODULE.md) | Reduce LLM size and accelerate inference using pruning techniques like Wanda and SparseGPT. Use when compressing models without retraining, achieving 50% sparsity with minimal accu |
| [moe-training](../../skills/common/ai-research-skills/modules/moe-training/MODULE.md) | Train Mixture of Experts (MoE) models using DeepSpeed or HuggingFace. Use when training large-scale models with limited compute (5× cost reduction vs dense models), implementing sp |
| [nanogpt](../../skills/common/ai-research-skills/modules/nanogpt/MODULE.md) | Educational GPT implementation in ~300 lines. Reproduces GPT-2 (124M) on OpenWebText. Clean, hackable code for learning transformers. By Andrej Karpathy. Perfect for understanding  |
| [nemo-curator](../../skills/common/ai-research-skills/modules/nemo-curator/MODULE.md) | GPU-accelerated data curation for LLM training. Supports text/image/video/audio. Features fuzzy deduplication (16× faster), quality filtering (30+ heuristics), semantic deduplicati |
| [nemo-evaluator](../../skills/common/ai-research-skills/modules/nemo-evaluator/MODULE.md) | Evaluates LLMs across 100+ benchmarks from 18+ harnesses (MMLU, HumanEval, GSM8K, safety, VLM) with multi-backend execution. Use when needing scalable evaluation on local Docker, S |
| [nemo-guardrails](../../skills/common/ai-research-skills/modules/nemo-guardrails/MODULE.md) | NVIDIA's runtime safety framework for LLM applications. Features jailbreak detection, input/output validation, fact-checking, hallucination detection, PII filtering and toxicity de |
| [nnsight](../../skills/common/ai-research-skills/modules/nnsight/MODULE.md) | Provides guidance for interpreting and manipulating neural network internals using nnsight with optional NDIF remote execution. Use when needing to run interpretability experiments |
| [openpi](../../skills/common/ai-research-skills/modules/openpi/MODULE.md) | Fine-tune and serve Physical Intelligence OpenPI models (pi0, pi0-fast, pi0.5) using JAX or PyTorch backends for robot policy inference across ALOHA, DROID, and LIBERO environments |
| [openrlhf](../../skills/common/ai-research-skills/modules/openrlhf/MODULE.md) | High-performance RLHF framework with Ray+vLLM acceleration. Use for PPO, GRPO, RLOO, DPO training of large models (7B-70B+). Built on Ray, vLLM, ZeRO-3. 2× faster than DeepSpeedCha |
| [openvla-oft](../../skills/common/ai-research-skills/modules/openvla-oft/MODULE.md) | Fine-tunes and evaluates OpenVLA-OFT and OpenVLA-OFT+ policies for robot action generation with continuous action heads, LoRA adaptation, and FiLM conditioning on LIBERO simulation |
| [outlines](../../skills/common/ai-research-skills/modules/outlines/MODULE.md) | Guarantee valid JSON/XML/code structure during generation, use Pydantic models for type-safe outputs, support local models (Transformers, vLLM), and maximize inference speed with O |
| [peft](../../skills/common/ai-research-skills/modules/peft/MODULE.md) | Parameter-efficient fine-tuning for LLMs using LoRA, QLoRA, and 25+ methods. Use when fine-tuning large models (7B-70B) with limited GPU memory, when you need to train <1% of param |
| [phoenix](../../skills/common/ai-research-skills/modules/phoenix/MODULE.md) | Open-source AI observability platform for LLM tracing, evaluation, and monitoring. Use when debugging LLM applications with detailed traces, running evaluations on datasets, or mon |
| [pinecone](../../skills/common/ai-research-skills/modules/pinecone/MODULE.md) | Managed vector database for production AI applications. Fully managed, auto-scaling, with hybrid search (dense + sparse), metadata filtering, and namespaces. Low latency (<100ms p9 |
| [presenting-conference-talks](../../skills/common/ai-research-skills/modules/presenting-conference-talks/MODULE.md) | Generates conference presentation slides (Beamer LaTeX PDF and editable PPTX) from a compiled paper with speaker notes and talk script. Use when preparing oral talks, spotlight pre |
| [prompt-guard](../../skills/common/ai-research-skills/modules/prompt-guard/MODULE.md) | Meta's 86M prompt injection and jailbreak detector. Filters malicious prompts and third-party data for LLM apps. 99%+ TPR, <1% FPR. Fast (<2ms GPU). Multilingual (8 languages). Dep |
| [pytorch-fsdp2](../../skills/common/ai-research-skills/modules/pytorch-fsdp2/MODULE.md) | Adds PyTorch FSDP2 (fully_shard) to training scripts with correct init, sharding, mixed precision/offload config, and distributed checkpointing. Use when models exceed single-GPU m |
| [pytorch-lightning](../../skills/common/ai-research-skills/modules/pytorch-lightning/MODULE.md) | High-level PyTorch framework with Trainer class, automatic distributed training (DDP/FSDP/DeepSpeed), callbacks system, and minimal boilerplate. Scales from laptop to supercomputer |
| [pyvene](../../skills/common/ai-research-skills/modules/pyvene/MODULE.md) | Provides guidance for performing causal interventions on PyTorch models using pyvene's declarative intervention framework. Use when conducting causal tracing, activation patching,  |
| [qdrant](../../skills/common/ai-research-skills/modules/qdrant/MODULE.md) | High-performance vector similarity search engine for RAG and semantic search. Use when building production RAG systems requiring fast nearest neighbor search, hybrid search with fi |
| [ray-data](../../skills/common/ai-research-skills/modules/ray-data/MODULE.md) | Scalable data processing for ML workloads. Streaming execution across CPU/GPU, supports Parquet/CSV/JSON/images. Integrates with Ray Train, PyTorch, TensorFlow. Scales from single  |
| [ray-train](../../skills/common/ai-research-skills/modules/ray-train/MODULE.md) | Distributed training orchestration across clusters. Scales PyTorch/TensorFlow/HuggingFace from laptop to 1000s of nodes. Built-in hyperparameter tuning with Ray Tune, fault toleran |
| [research-manager](../../skills/common/ai-research-skills/modules/research-manager/MODULE.md) | Records research provenance as a post-task epilogue, scanning conversation history at the end of a coding or research session to extract decisions, experiments, dead ends, claims,  |
| [rigor-reviewer](../../skills/common/ai-research-skills/modules/rigor-reviewer/MODULE.md) | Performs ARA Seal Level 2 semantic epistemic review on Agent-Native Research Artifacts, scoring six dimensions (evidence relevance, falsifiability, scope calibration, argument cohe |
| [rwkv](../../skills/common/ai-research-skills/modules/rwkv/MODULE.md) | RNN+Transformer hybrid with O(n) inference. Linear time, infinite context, no KV cache. Train like GPT (parallel), infer like RNN (sequential). Linux Foundation AI project. Product |
| [saelens](../../skills/common/ai-research-skills/modules/saelens/MODULE.md) | Provides guidance for training and analyzing Sparse Autoencoders (SAEs) using SAELens to decompose neural network activations into interpretable features. Use when discovering inte |
| [segment-anything](../../skills/common/ai-research-skills/modules/segment-anything/MODULE.md) | Foundation model for image segmentation with zero-shot transfer. Use when you need to segment any object in images using points, boxes, or masks as prompts, or automatically genera |
| [sentence-transformers](../../skills/common/ai-research-skills/modules/sentence-transformers/MODULE.md) | Framework for state-of-the-art sentence, text, and image embeddings. Provides 5000+ pre-trained models for semantic similarity, clustering, and retrieval. Supports multilingual, do |
| [sentencepiece](../../skills/common/ai-research-skills/modules/sentencepiece/MODULE.md) | Language-independent tokenizer treating text as raw Unicode. Supports BPE and Unigram algorithms. Fast (50k sentences/sec), lightweight (6MB memory), deterministic vocabulary. Used |
| [sglang](../../skills/common/ai-research-skills/modules/sglang/MODULE.md) | Fast structured generation and serving for LLMs with RadixAttention prefix caching. Use for JSON/regex outputs, constrained decoding, agentic workflows with tool calls, or when you |
| [simpo](../../skills/common/ai-research-skills/modules/simpo/MODULE.md) | Simple Preference Optimization for LLM alignment. Reference-free alternative to DPO with better performance (+6.4 points on AlpacaEval 2.0). No reference model needed, more efficie |
| [skypilot](../../skills/common/ai-research-skills/modules/skypilot/MODULE.md) | Multi-cloud orchestration for ML workloads with automatic cost optimization. Use when you need to run training or batch jobs across multiple clouds, leverage spot instances with au |
| [slime](../../skills/common/ai-research-skills/modules/slime/MODULE.md) | Provides guidance for LLM post-training with RL using slime, a Megatron+SGLang framework. Use when training GLM models, implementing custom data generation workflows, or needing ti |
| [speculative-decoding](../../skills/common/ai-research-skills/modules/speculative-decoding/MODULE.md) | Accelerate LLM inference using speculative decoding, Medusa multiple heads, and lookahead decoding techniques. Use when optimizing inference speed (1.5-3.6× speedup), reducing late |
| [stable-diffusion](../../skills/common/ai-research-skills/modules/stable-diffusion/MODULE.md) | State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. Use when generating images from text prompts, performing image-to-image translatio |
| [swanlab](../../skills/common/ai-research-skills/modules/swanlab/MODULE.md) | Provides guidance for experiment tracking with SwanLab. Use when you need open-source run tracking, local or self-hosted dashboards, and lightweight media logging for ML workflows. |
| [systems-paper-writing](../../skills/common/ai-research-skills/modules/systems-paper-writing/MODULE.md) | Comprehensive guide for writing systems papers targeting OSDI, SOSP, ASPLOS, NSDI, and EuroSys. Provides paragraph-level structural blueprints, writing patterns, venue-specific che |
| [tensorboard](../../skills/common/ai-research-skills/modules/tensorboard/MODULE.md) | Visualize training metrics, debug models with histograms, compare experiments, visualize model graphs, and profile performance with TensorBoard - Google's ML visualization toolkit |
| [tensorrt-llm](../../skills/common/ai-research-skills/modules/tensorrt-llm/MODULE.md) | Optimizes LLM inference with NVIDIA TensorRT for maximum throughput and lowest latency. Use for production deployment on NVIDIA GPUs (A100/H100), when you need 10-100x faster infer |
| [torchforge](../../skills/common/ai-research-skills/modules/torchforge/MODULE.md) | Provides guidance for PyTorch-native agentic RL using torchforge, Meta's library separating infra from algorithms. Use when you want clean RL abstractions, easy algorithm experimen |
| [torchtitan](../../skills/common/ai-research-skills/modules/torchtitan/MODULE.md) | Provides PyTorch-native distributed LLM pretraining using torchtitan with 4D parallelism (FSDP2, TP, PP, CP). Use when pretraining Llama 3.1, DeepSeek V3, or custom models at scale |
| [transformer-lens](../../skills/common/ai-research-skills/modules/transformer-lens/MODULE.md) | Provides guidance for mechanistic interpretability research using TransformerLens to inspect and manipulate transformer internals via HookPoints and activation caching. Use when re |
| [trl-fine-tuning](../../skills/common/ai-research-skills/modules/trl-fine-tuning/MODULE.md) | Fine-tune LLMs using reinforcement learning with TRL - SFT for instruction tuning, DPO for preference alignment, PPO/GRPO for reward optimization, and reward model training. Use wh |
| [unsloth](../../skills/common/ai-research-skills/modules/unsloth/MODULE.md) | Expert guidance for fast fine-tuning with Unsloth - 2-5x faster training, 50-80% less memory, LoRA/QLoRA optimization |
| [verl](../../skills/common/ai-research-skills/modules/verl/MODULE.md) | Provides guidance for training LLMs with reinforcement learning using verl (Volcano Engine RL). Use when implementing RLHF, GRPO, PPO, or other RL algorithms for LLM post-training  |
| [vllm](../../skills/common/ai-research-skills/modules/vllm/MODULE.md) | Serves LLMs with high throughput using vLLM's PagedAttention and continuous batching. Use when deploying production LLM APIs, optimizing inference latency/throughput, or serving mo |
| [weights-and-biases](../../skills/common/ai-research-skills/modules/weights-and-biases/MODULE.md) | Track ML experiments with automatic logging, visualize training in real-time, optimize hyperparameters with sweeps, and manage model registry with W&B - collaborative MLOps platfor |
| [whisper](../../skills/common/ai-research-skills/modules/whisper/MODULE.md) | OpenAI's general-purpose speech recognition model. Supports 99 languages, transcription, translation to English, and language identification. Six model sizes from tiny (39M params) |
