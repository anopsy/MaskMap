![image](https://github.com/anopsy/hackher/assets/74981211/474514db-17e2-46a4-b2ff-21d944bdd44a)

Using the power of NLP to gather data about most common masking behaviours in order to extend the database of masking behaviours in female ASD patients and to help patients and doctors identify them

A recent study suggested that 80% of Autistic women remain undiagnosed at the age of 18. It can be due to two main reasons:
 They tend to “mask” their symptoms, suppressing their own behaviors and imitating others to blend in, leading to late or no diagnosis. We will further refer to it as AM - Autistic Masking. 
The anxiety and depression resulting from this long-term masking can lead to misdiagnosis, as these mental health conditions might be diagnosed instead of the underlying autism.
Our Solution - MaskMap will help identify symptoms of AM and enable both medical staff as patients to better discern between anxiety, depression symptoms and long-term effects of AM. 
MaskMap is based on recent research that implicated that LLM-based models can be better at diagnosing than human doctors.
Our approach:
We will gather textual data of AM, anxiety and depression experiences by scraping it from social media, fully anonymizing it and feeding it into a classification model:
Our goals are: 
1) to create a tool, where you can get a probability of the symptom being AM/anxiety/depression. 
2) to gather clean data from diagnosed female patients to improve the model in the future
3) create more awareness about the AM symptoms and consequences of AM

Description: We’re addressing the significant issue of undiagnosed autism in women, particularly those over 18. The current diagnostic process often overlooks autistic masking, leading to misdiagnoses and untreated autism.

Solution Details: Our solution, MaskMap, leverages machine learning and data from over 14,000 tokens of user experiences on Reddit. It uses LinearSVC and XGBClassifier models to decode the hidden spectrum of autism.

Stakeholders/Engagement: This solution benefits autistic women, their families, and medical specialists. It also opens opportunities for collaboration with data scientists, AI experts, and mental health advocates.

Benchmark & Alternatives: Current industry benchmarks focus on traditional diagnostic methods. Our solution is innovative as it uses AI and data analysis, a largely unexplored area in autism diagnosis.

Relevance & Alignment: Our approach directly addresses the issue of undiagnosed autism in women, contributing to broader efforts to improve women’s mental health.

Value & Success Criteria: MaskMap offers a new avenue for autism diagnosis, potentially reducing misdiagnoses and improving mental health outcomes. Its success can be measured by its accuracy and its adoption by medical professionals.

Ethical, Inclusion, Diversity & Equality (IDE): MaskMap aligns with IDE principles by addressing a gender disparity in autism diagnosis. We’ll measure this through user feedback and diagnostic outcomes.

Feasibility and Scalability: The solution is feasible, given the availability of data and AI technology. It’s scalable, with potential for multilingual support and application to other mental health conditions.

Assumptions and Dependencies: The solution assumes access to clean, anonymized data. It depends on technological infrastructure and acceptance by the medical community.

Potential Future Development and Direction: We envision MaskMap evolving to include more diverse data sources and improved AI models. We aim for broader adoption within the medical community and expansion to other underdiagnosed conditions.

This project represents a significant step towards more inclusive and accurate autism diagnosis, harnessing the power of AI for better mental health outcomes. 
