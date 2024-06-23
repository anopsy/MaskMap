# MaskMap: Decoding the Hidden Spectrum
#### Magdalena Kowalczuk - Data and ML
#### Bartosz Kordaszewski - Frontend
## 1. Description
Creating a prototype of a diagnosis support tool using the power of NLP to gather data about common masking behaviors to extend the database of masking behaviors in female ASD patients and to help patients and doctors identify them.

A recent study suggested that 80% of autistic women remain undiagnosed at the age of 18. This can be due to two main reasons: They tend to “mask” their symptoms, suppressing their own behaviors and imitating others to blend in, leading to late or no diagnosis. We will further refer to this as AM - Autistic Masking. The anxiety and depression resulting from this long-term masking can lead to misdiagnosis, as these mental health conditions might be diagnosed instead of the underlying autism. Our solution, MaskMap, will help identify symptoms of AM and enable both medical staff and patients to better discern between anxiety, depression symptoms, and the long-term effects of AM. MaskMap is based on recent research that suggests that LLM-based models can be better at diagnosing than human doctors.

#### Our approach:
During our project, we successfully developed a prototype of a diagnosis support tool called MaskMap. This tool aims to identify symptoms of Autistic Masking (AM) and help medical staff and patients differentiate between anxiety, depression, and the long-term effects of AM. Here's how we achieved this:

We started by gathering textual data related to AM, anxiety, and depression from social media, specifically using the Reddit API. This allowed us to collect a diverse range of real-life experiences and symptoms shared by individuals.

Next, we processed the collected data using NLTK (Natural Language Toolkit). This involved cleaning and preparing the data for analysis, ensuring that it was in a suitable format for building our model.

With the processed data, we built a classification model capable of distinguishing between AM, anxiety, and depression. This model leverages the power of NLP to provide accurate predictions and insights.

Finally, we created a website with an intuitive interface for both prediction and data collection. This platform allows users to input their experiences and receive feedback, while also contributing to our growing database of masking behaviors.
   
## 2. Next Steps
The following steps could further enhance the MaskMap project :

First, we could consult with domain and ethics experts. This consultation is crucial to ensure that our project is based on methodologically collected patient data and that patients' privacy and interests are protected throughout the process.

Next, we'd aim to improve our data collection process by collaborating with specialists. This cooperation would help us work with high-quality labeled data, which is essential for the accuracy and reliability of our model.

We could also conduct experiments with textual data processing, vectorization, and embeddings. These experiments will help us refine our techniques and improve the overall performance of our model.

Finally, we would rigorously evaluate our model's performance metrics. This evaluation would provide insights into the effectiveness of our model and identify areas for further improvement.



## 3. Lessons learned
Throughout this project, I gained several valuable insights and skills:

Firstly, designing a prototype of a tool taught me that I am capable of creating a functional prototype of a data-based tool. This experience was both challenging and rewarding.

Using the Reddit API and YTTranscriptAPI, I discovered that these platforms are excellent free resources for gathering textual data. This realization has broadened my understanding of available data sources that I can utilize in future projects.

In performing basic textual data processing, I delved deeper into the use of vectorizers. This enhanced my ability to transform and manipulate text data effectively.

Building a simple API using FastAPI revealed that it is an excellent and easy-to-use framework for constructing REST APIs. This knowledge will be highly beneficial for future API development.

Integrating the API with the frontend was a particularly satisfying experience. While I had some experience with this process using Golang, successfully accomplishing it with a Python-based API added to my skill set.

Finally, brainstorming, decision-making, and cooperating on a project highlighted the importance of quick decision-making and scope management. We had to make rapid decisions and limit the scope of our project to ensure we completed the hackathon with a simple yet functional solution.










![image](https://github.com/anopsy/hackher/assets/74981211/b865640f-4068-466c-bead-5a02e4f08140)




## Description: 
We’re addressing the significant issue of undiagnosed autism in women, particularly those over 18. The current diagnostic process often overlooks autistic masking, leading to misdiagnoses and untreated autism.

## Solution Details: 
Our solution, MaskMap, leverages machine learning and data from over 14,000 tokens of user experiences on Reddit. It uses LinearSVC and XGBClassifier models to decode the hidden spectrum of autism.

## Stakeholders/Engagement: 
This solution benefits autistic women, their families, and medical specialists. It also opens opportunities for collaboration with data scientists, AI experts, and mental health advocates.

## Benchmark & Alternatives: 
Current industry benchmarks focus on traditional diagnostic methods. Our solution is innovative as it uses AI and data analysis, a largely unexplored area in autism diagnosis.

## Relevance & Alignment: 
Our approach directly addresses the issue of undiagnosed autism in women, contributing to broader efforts to improve women’s mental health.

## Value & Success Criteria: 
MaskMap offers a new avenue for autism diagnosis, potentially reducing misdiagnoses and improving mental health outcomes. Its success can be measured by its accuracy and its adoption by medical professionals.

## Ethical, Inclusion, Diversity & Equality (IDE): 
MaskMap aligns with IDE principles by addressing a gender disparity in autism diagnosis. We’ll measure this through user feedback and diagnostic outcomes.

## Feasibility and Scalability: 
The solution is feasible, given the availability of data and AI technology. It’s scalable, with potential for multilingual support and application to other mental health conditions.

## Assumptions and Dependencies: 
The solution assumes access to clean, anonymized data. It depends on technological infrastructure and acceptance by the medical community.

## Potential Future Development and Direction: 
We envision MaskMap evolving to include more diverse data sources and improved AI models. We aim for broader adoption within the medical community and expansion to other underdiagnosed conditions.

This project represents a significant step towards more inclusive and accurate autism diagnosis, harnessing the power of AI for better mental health outcomes. 
