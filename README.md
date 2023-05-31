<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/fffiloni/langchain-chat-with-pdf.png" alt="Logo" width="290" height="160">
  <h3 align="center">PDFChat: Chat with Any PDF</h3>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project


PDFChat is a simple application developed by leveraging the capability of LLM (chatgpt) to generate humanlike text, answer questions based on context.

Steps followed:

> DataBase Creation
* Read and extract the content of the given pdf file
* Get emebddings of the given file using OpenAI Ada model and store them in Chroma base.

> Inference
* For the user query get user embeddings using Ada
* Perform doc search to extract top 3 paragraphs which are semantically similar to the query
* Pass the extracted docs as Context and user query to ChatGPT to formulate the answer.

### Built With

This section should list any major frameworks/libraries used to bootstrap the project. 

![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


<!-- GETTING STARTED -->
## Getting Started

To run the application you need the following pre-requisites

### Prerequisites

* Docker installed on your system. You can follow the instructions [here](https://docs.docker.com/engine/install/) to download it for your system.
* OpenAI API Key. You can get it from [here](https://openai.com/blog/openai-api). Add your API key to `.env` file.

### Installation

Run the below commands for installation 

1. Build Docker Image

```shell
docker build --tag PDFChat --file Dockerfile .
```

2. Run the Docker Image

```shell
docker run -it --env-file .env --name gpt-gateway gpt-gateway
```
