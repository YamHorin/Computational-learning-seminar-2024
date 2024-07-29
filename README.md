# Computational learning seminar project 2024 
## readme not done 

System name: Checkly

Some system for checking (evaluating) grades of tests / exercises / closed/open questions - automatically.

* The 5 important requirements for the project, what people expect the system to do
* Entering questions by the author of the test and collecting correct answers to the questions.
* Preparation of a bank of answers similar to the answers entered by the author of the test / keywords for identification used in the answer.
* Calculating the similarity between the answer of the examinee and the author of the test (use of AI features) and giving an estimated score for each question
* Giving a score according to the similarity percentages obtained from the calculation.
* Possibility of sharing an exam for students and receiving the results.

## tools that we use in the project 
## Auto gen 

* Input - instructions to agents.
* The first agent will receive the exam questions, the second will create a bank of correct answers, the third will check the correctness of the answers compared to the answers entered by the test author and check the correctness of the students' answers compared to the answer bank
* Output - a bank of correct answers for the exam and the students' grades.
* Quality measurement: The quality of the answers in the answer bank and checking the students' answers will be done by cosine similarity metric. From each string, create a numerical vector and calculate the similarity by calculate the cosine similarity between these vectors.

<div align="center">
 <img alt="ollama" height="200px" src="https://github.com/ollama/ollama/assets/3325447/0d0b44e2-8f4a-4e99-9b52-a5c1c741c8f7">
</div>

## Ollama

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

### Docker

The official [Ollama Docker image](https://hub.docker.com/r/ollama/ollama) `ollama/ollama` is available on Docker Hub.

### Libraries

- [ollama-python](https://github.com/ollama/ollama-python)
- [ollama-js](https://github.com/ollama/ollama-js)
