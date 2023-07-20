# novelGPT

## Introduction 
A web novel QA bot developed for my brother's task, based on the OpenAI API.

🛠 Tech Stack: Python, Flask, OpenAI API  
⏰ Duration: Three days (Mar 2023)  
👥 Team: Alone

## [Eng]   
The project involves crawling web novel content from a site, downloading it as files, then embedding this content using OpenAI's Ada model. A Flask web application is then set up, allowing users to pose questions and get answers based on this content.  

🌐 Data Crawler.ipynb  
Logs in to a website and downloads web novel content based on episode numbers.  

🌐 Data Embedding.ipynb  
Loads a dataset, computes embeddings for each text entry using OpenAI's Ada model, and saves the results to a new CSV.  

🌐 Data processing.py  
Breaks downloaded novels into sentences, counts tokens for each, and then visualizes token distribution.  

🌐 app.py (FLASK)  
A Flask web app allowing users to ask questions and get answers based on embeddings of a novel.

## [KOR]
웹 소설 사이트에서 내용을 크롤링하여 파일로 다운로드 받은 후, 이 내용들을 OpenAI의 Ada 모델로 임베딩 처리합니다. 이후 Flask 웹 애플리케이션을 통해 사용자가 질문을 할 수 있게 하여 해당 내용에 기반한 응답을 제공합니다.

🌐 Data Crawler.ipynb  
웹 사이트에 로그인하여 특정 에피소드 번호를 기반으로 웹 소설 내용을 다운로드합니다.  

🌐 Data Embedding.ipynb  
데이터셋을 로드하고, 각 텍스트 항목에 대한 임베딩을 계산한 다음, 결과를 새로운 CSV로 저장합니다. 이 과정에서 OpenAI의 Ada 모델을 활용합니다.  

🌐 Data processing.py  
다운로드 받은 소설들을 문장으로 분할하고, 각각에 대한 토큰 수를 계산한 다음 토큰 분포를 시각화합니다.  

🌐 app.py (FLASK)  
사용자가 질문을 할 수 있도록 하는 Flask 웹 앱으로, 소설의 임베딩을 기반으로 응답을 제공합니다.
