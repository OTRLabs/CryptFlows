# CryptFlows
Agentic Security Automation buzzword framework

----

---

Langchain driven agent framework designed to provide assistance during various types of offensive security situations 


The plan is to create a system that begins as follows:
Development 

The project will be built using python 
Libraries & Dependencies:

python package manager: PDM
WebUI: Litestar + Vite
Langchain: LLM & Agent orchestration + data access & analysis!
container runtime: podman
Workflow orchestration: Apache airflow?
Database: duckdb
ORM: advanced_alchemy, extension for SQLalchemy which allows use of DuckDB
Ollama + Ollama HTTP API : LLM runtime
Hugging face: specialized LLM runtime for more specific models
Techniques:

LLMRouting: using lighter models based on the question/prompt, allowing for computing power to be saved in the process. This can be done using Ollama as the platform supports many different models, and allows us to use the “right tool for the job”


The idea is: use python for the central “logic handler” or “main loop” of the system, and have it deploy containerized applications that can preform individual tasks as functions and return data to the main function for further processing and analysis 

For example: we will make heavy use of Project Discovery’s arsenal of network recon tools, each of which can be used as a docker (or in our case podman) container 


Milestones:
Stage 1: CTF & Hack the Box Labs

We intend to use simple, private CTF labs such as hack the box, TryHackMe, etc to train the system to perform basic vulnerability detection & analysis, and carry out basic exploits, as well as developing the most important part! The logging, and reporting systems

We will be using these CTFs as a way to establish the base capabilities of our agent framework without bothering anyone with unnecessary bullshit reports


The primary focus of this section will be achieving 

accurate scope assessment 
Accurate security research
Accurate vulnerability assessment & exploitation when relevant 

Stage 2: Open Bug bounty programs 

NOTICE: at no point should the system ever ever ever submit any type of report to any external service. We cannot guarantee 100% accuracy and the idea of wasting someone’s time with an unwarranted & unnecessary security issue is physically painful to think about. We do not want this thing to be submitting reports to hackerone without some human validation & verification 


Notice 2: the primary focus of these stages will be on demonstrating any potential vulnerabilities and issues found in systems. I would like to give the system some form of video manipulation abilities (pymovie?) and allow it to create demonstrations of the exploit, or whatever 

Stage 3: Penetration Testing 

Stage 4: TBD! 