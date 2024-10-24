# 🛡️ LLM Switcher: Ensuring Reliability in AI Model Operations

The **LLM Switcher** project provides a resilient solution to handle rate limits, failures, or unavailability in Large Language Models (LLMs). Rather than allowing an application to crash due to a rate limit or model error, the switcher automatically moves to the next available model, ensuring that no work is lost and operations continue seamlessly. This prevents wasted effort and keeps your AI-driven systems running smoothly. 🔄💡

## 🎯 Purpose

Many AI systems rely on single LLMs, and extended usage can cause rate limits, downtime, or other failures. Without a backup plan, this could lead to wasted computational resources and time. The **LLM Switcher** addresses this by:

- 🌐 **Switching Models on Failure**: When an LLM hits a rate limit or becomes unavailable, the system automatically switches to another available LLM, ensuring no downtime.
- 🛠️ **Preserving Work**: Work in progress isn't wasted—by switching models, ongoing tasks continue, making the process failure-proof.
- 🧠 **Adaptability**: Whether you're using the LLM Switcher in an agent, an API call, or any other application, it ensures that long-running tasks won't be derailed by model-specific issues.

In short, this project guarantees that your AI systems keep running, saving you from losing hours of processing due to a single point of failure.

## 🛠️ Features

- **🔄 Automatic Model Switching**: Effortlessly switch between LLMs when one encounters an error.
- **💾 Work Preservation**: Prevents the loss of intermediate results due to LLM failures.
- **⚙️ Configurable Retry System**: Adjust retry limits to customize fault tolerance.
- **🧩 Extensible for New LLMs**: Integrate new models easily by subclassing the `BaseInference` class.

## 🚀 Getting Started

### Installation

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 🧠 What Makes LLM Switcher Unique?

1. **Failure-Resistant**: Whether it's hitting rate limits, API unavailability, or other errors, the switcher guarantees that work continues without interruption. Your application won't collapse just because one LLM becomes unavailable.
   
2. **Versatility**: The switcher is flexible—whether you're running an AI agent, building an API, or deploying a more complex AI system, this project ensures that your operation will remain unaffected by any individual LLM failure.

3. **Plug and Play**: Easily add new LLMs by subclassing the `BaseInference` class—making it adaptable to your growing AI needs.

This ensures that the model-switching logic and failover mechanisms work as expected under different failure conditions.

## 🤝 Contributing

We welcome contributions to make the **LLM Switcher** even more robust! If you find any bugs, feel free to open an issue. Contributions can be made via pull requests—just fork the repository and submit your changes.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
