# CryptFlows


<p align="center">
  <strong>Agentic Security Automation Framework</strong>
</p>


## 🚀 Overview

CryptFlows is a cutting-edge, Langchain-driven agent framework designed to provide intelligent assistance during various offensive security scenarios. By leveraging the power of Large Language Models (LLMs) and containerized applications, CryptFlows aims to revolutionize the way security professionals approach vulnerability assessment, exploitation, and reporting.

### 🔑 Key Features

- **Intelligent Agent Framework**: Utilizes Langchain for LLM & Agent orchestration
- **Modular Architecture**: Deploys containerized applications for individual tasks
- **Adaptive LLM Routing**: Uses the right model for each task, optimizing performance
- **Comprehensive Toolset**: Integrates Project Discovery's arsenal of network recon tools
- **Automated Reporting**: Generates detailed, accurate security reports

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/OTRLabs/CryptFlows.git

# Change to the project directory
cd CryptFlows

# Install dependencies using PDM
pdm install

# Set up the environment
pdm run setup

# start the WebUI
pdm run start-ui

# run a specific task
pdm run task <task_name>

# Generate a report
pdm run generate-report
```

## 🛠️ Development
CryptFlows is built using Python and leverages a powerful stack of technologies:

## Development Stack

CryptFlows is built using the following powerful technologies:

- **Package Manager**: [PDM](https://pdm.fming.dev/)
- **WebUI**: [Litestar](https://litestar.dev/) + [Vite](https://vitejs.dev/)
- **LLM & Agent Orchestration**: [Langchain](https://langchain.dev/)
- **Container Runtime**: [Podman](https://podman.io/)
- **Workflow Orchestration**: [Apache Airflow](https://airflow.apache.org/) (tentative)
- **Database**: [DuckDB](https://duckdb.org/)
- **Prompting**: [Fabric by Daniel M.](https://github.com/fabric/fabric)
- **ORM**: [Advanced_alchemy](https://github.com/NickKravis/advanced_alchemy) (SQLAlchemy extension for DuckDB)
- **LLM Runtime**: [Ollama](https://github.com/llm-foundation/ollama-server) + [Ollama HTTP API](https://github.com/llm-foundation/ollama-server#api)
- **Specialized LLM Models**: [Hugging Face](https://huggingface.co/)

## LLM Routing

CryptFlows implements an intelligent LLM routing system that optimizes computing power and ensures the "right tool for the job" is always used.

## Containerized Task Execution

The system's core logic is handled by Python, which deploys containerized applications to perform individual tasks. These containers return data to the main function for further processing and analysis.

## 🗺️ Roadmap

### Stage 1: CTF & Hack the Box Labs

Focus: Establishing base capabilities without external impact

- Accurate scope assessment
- Security research
- Vulnerability assessment & exploitation
- Logging and reporting systems development

### Stage 2: Open Bug Bounty Programs

Focus: Demonstrating potential vulnerabilities

- Implement video manipulation capabilities
- Create exploit demonstrations
- Develop human validation & verification processes

### Stage 3: Penetration Testing

Focus: Full-scale penetration testing capabilities

- Automated reconnaissance
- Exploit chaining
- Advanced reporting

### Stage 4: TBD

Future developments based on community feedback and emerging security trends

## 🤝 Contributing

We welcome contributions to CryptFlows! Please refer to our [Contributing Guidelines](https://github.com/yourusername/CryptFlows/blob/main/CONTRIBUTING.md) for details on how to submit pull requests, report issues, and suggest improvements.

## 📄 License

CryptFlows is released under the [MIT License](https://github.com/yourusername/CryptFlows/blob/main/LICENSE).

<p align="center">
  Made with ❤️ by the [OTR Labs](https://github.com/OTRLabs) Team
</p>
