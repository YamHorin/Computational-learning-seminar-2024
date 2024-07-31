# Computational learning seminar project 2024 
### readme not done 

System name: Checkly

Some system for checking (evaluating) grades of tests / exercises / closed/open questions - automatically.
### The 5 important requirements for the project, what people expect the system to do
* Entering questions by the author of the test and collecting correct answers to the questions.
* Preparation of a bank of answers similar to the answers entered by the author of the test / keywords for identification used in the answer.
* Calculating the similarity between the answer of the examinee and the author of the test (use of AI features) and giving an estimated score for each question
* Giving a score according to the similarity percentages obtained from the calculation.
* Possibility of sharing an exam for students and receiving the results.
## setup
* after installing ollama and docker , do the following
* build the docker image of auto gen:
 ```bash
docker build -f .devcontainer/Dockerfile -t autogen_base_img https://github.com/microsoft/autogen.git#main
``` 
* and run the setup file:
 ```bash
python3 setup.py
```
and finally run main.py

 ```bash
python3 main.py
```

## tools that we use in the project AND NEEDED TO BE INSTALLED IN ORDER TO RUN  

## DOCKER

</p>
<div align="center">
 <img alt="docker" height="200px" src="https://pbs.twimg.com/card_img/1813758439010742272/v9FtXldC?format=jpg&name=4096x4096">
</div>

### Docker Installation
1. Visit the official [Docker website](https://www.docker.com/).
2. Choose the appropriate Docker version for your operating system. For macOS or Linux, hover over the download button, and two options for installation will show up.
3. Open the download link and run the installation on your computer.
4. Once the installation is complete, Docker should be ready to use.
5. Before running the server of the program, make sure Docker is running on your computer.

## Auto gen 
</p>
<div align="center">
 <img alt="autogen" height="200px" src="https://microsoft.github.io/autogen/img/ag.svg">
</div>
* Input - instructions to agents.
* The first agent will receive the exam questions, the second will create a bank of correct answers, the third will check the correctness of the answers compared to the answers entered by the test author and check the correctness of the students' answers compared to the answer bank
* Output - a bank of correct answers for the exam and the students' grades.
* Quality measurement: The quality of the answers in the answer bank and checking the students' answers will be done by cosine similarity metric. From each string, create a numerical vector and calculate the similarity by calculate the cosine similarity between these vectors.

### What is AutoGen

AutoGen is an open-source programming framework for building AI agents and facilitating cooperation among multiple agents to solve tasks. AutoGen aims to streamline the development and research of agentic AI, much like PyTorch does for Deep Learning. It offers features such as agents capable of interacting with each other, facilitates the use of various large language models (LLMs) and tool use support, autonomous and human-in-the-loop workflows, and multi-agent conversation patterns.

**Open Source Statement**: The project welcomes contributions from developers and organizations worldwide. Our goal is to foster a collaborative and inclusive community where diverse perspectives and expertise can drive innovation and enhance the project's capabilities. Whether you are an individual contributor or represent an organization, we invite you to join us in shaping the future of this project. Together, we can build something truly remarkable.

The project is currently maintained by a [dynamic group of volunteers](https://butternut-swordtail-8a5.notion.site/410675be605442d3ada9a42eb4dfef30?v=fa5d0a79fd3d4c0f9c112951b2831cbb&pvs=4) from several different organizations. Contact project administrators Chi Wang and Qingyun Wu via auto-gen@outlook.com if you are interested in becoming a maintainer.

### Quickstart
The easiest way to start playing is
1. Click below to use the GitHub Codespace

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/autogen?quickstart=1)

 2. Copy OAI_CONFIG_LIST_sample to ./notebook folder, name to OAI_CONFIG_LIST, and set the correct configuration.
 3. Start playing with the notebooks!

*NOTE*: OAI_CONFIG_LIST_sample lists GPT-4 as the default model, as this represents our current recommendation, and is known to work well with AutoGen. If you use a model other than GPT-4, you may need to revise various system prompts (especially if using weaker models like GPT-3.5-turbo). Moreover, if you use models other than those hosted by OpenAI or Azure, you may incur additional risks related to alignment and safety. Proceed with caution if updating this default.

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
  <a href="#readme-top" style="text-decoration: none; color: blue; font-weight: bold;">
    ↑ Back to Top ↑
  </a>
</p>

### [Installation](https://microsoft.github.io/autogen/docs/Installation)
#### Option 1. Install and Run AutoGen in Docker

Find detailed instructions for users [here](https://microsoft.github.io/autogen/docs/installation/Docker#step-1-install-docker), and for developers [here](https://microsoft.github.io/autogen/docs/Contribute#docker-for-development).

#### Option 2. Install AutoGen Locally

AutoGen requires **Python version >= 3.8, < 3.13**. It can be installed from pip:

```bash
pip install pyautogen
```

Minimal dependencies are installed without extra options. You can install extra options based on the feature you need.

<!-- For example, use the following to install the dependencies needed by the [`blendsearch`](https://microsoft.github.io/FLAML/docs/Use-Cases/Tune-User-Defined-Function#blendsearch-economical-hyperparameter-optimization-with-blended-search-strategy) option.
```bash
pip install "pyautogen[blendsearch]"
``` -->

Find more options in [Installation](https://microsoft.github.io/autogen/docs/Installation#option-2-install-autogen-locally-using-virtual-environment).

<!-- Each of the [`notebook examples`](https://github.com/microsoft/autogen/tree/main/notebook) may require a specific option to be installed. -->

Even if you are installing and running AutoGen locally outside of docker, the recommendation and default behavior of agents is to perform [code execution](https://microsoft.github.io/autogen/docs/FAQ/#code-execution) in docker. Find more instructions and how to change the default behaviour [here](https://microsoft.github.io/autogen/docs/Installation#code-execution-with-docker-(default)).

For LLM inference configurations, check the [FAQs](https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints).

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
  <a href="#readme-top" style="text-decoration: none; color: blue; font-weight: bold;">
    ↑ Back to Top ↑
  </a>

## Ollama
</p>
<div align="center">
 <img alt="ollama" height="200px" src="https://github.com/ollama/ollama/assets/3325447/0d0b44e2-8f4a-4e99-9b52-a5c1c741c8f7">
</div>
* the autogen needs a language model that he can work on, we chose llama 3.
* to install ollama:

[![Discord](https://dcbadge.vercel.app/api/server/ollama?style=flat&compact=true)](https://discord.gg/ollama)

Get up and running with large language models.

### macOS

[Download](https://ollama.com/download/Ollama-darwin.zip)

### Windows preview

[Download](https://ollama.com/download/OllamaSetup.exe)

### Linux

```
curl -fsSL https://ollama.com/install.sh | sh
```

[Manual install instructions](https://github.com/ollama/ollama/blob/main/docs/linux.md)



* after installation pull the llama 3 model in the command line:
```bash
ollama pull llama 3
```

## MYSQL

</p>
<div align="center">
 <img alt="my sql" height="200px" src="https://pbs.twimg.com/profile_images/1255113654049128448/J5Yt92WW_400x400.png">
</div>

* the program use database of my sql
### how to install mysql:
### macOS

[Download](https://dev.mysql.com/doc/refman/8.4/en/macos-installation.html)

### Windows system

[Download](https://dev.mysql.com/downloads/installer/)

### Linux

```
mysql -u username -p
```

[Manual install instructions](https://dev.mysql.com/doc/refman/8.4/en/linux-installation.html)

