# AI Tutor

AI Tutor is a RAG system. The data are all the Harvard CS50 lectures saved in
a chroma db vector database (HARVARD_DATABASE).The LLM to create text from the
data is deepsek r1 (free version on open router). You can choose how many data
points you take under consideration to answer the query. You can also choose how
similar the data should be with your query (similarity distance). Furthermore
you can choose to show the ressources (Harvard CS50 youtube videos linked to the
timestamp, which is mostly related to your question). The answer of your question
is based on the most similar video chunks (1 min) from the Harvard CS50 lectures.

As an additional feature you can talk with deepseek, without calling the vector
database (Attention hallucination possible).

The third feature is an auto correction loop of deepseek. You can upload a
jupyter notebook or ask deepseek to code you something. If you uploaded a notebook
deepseek and type "Solve this" in the prompt, deepseek will correct that notebook
and give the pyton code back in the chat. If you asked deepseek to code something
(without uploaded notebook) deepseek will give the pyton code back in the chat. This
code can have errors. Therefore it is checked in a jupyter notebook API (JUPYTER_ENVIRONMENT).
When it is not possible to run the notebook, the error message will be redirected
to deepseek to create a new corrected notebook. This is done, until the notebook
can run without errors or the number of iterations is exceeded.

This is a great tool to learn more about the CS50 lectures and to automate coding
