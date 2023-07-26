# ISTAT_GPT Virtual Assistant

## Overview

ISTAT_GPT is a virtual assistant powered by GPT models, designed to provide improved answers based on a user-provided dataset. The assistant utilizes GPT-3.5 models and a user's collection of documents to offer accurate and informative responses to user queries.

## Instructions

1. **Prepare Your Documents**: Place your documents in the "Document" folder. The current version of the script supports PDF, DOC/DOCX, TXT, and LaTeX files.

2. **Obtain OpenAI API Key**: Visit https://openai.com/blog/openai-api to acquire your OpenAI API key.

3. **Configure Settings**: Open the "settings.txt" file in the main folder and customize it for your specific case.

4. **Prepare the Text Data**: Execute "ChopDocuments.py" to process the text data. The program will display your files one by one. Once completed, you will find a file named "xxx-originaltext.csv" in your virtual folder. Review the content to ensure proper scanning, especially for PDF files.

5. **Generate Text Embeddings**: In the same command window, run "EmbedDocuments.py." This process may take a few minutes if you have multiple documents. The script will convert sentences into 1500-dimensional vector representations using a rolling window of approximately 150 words. The primary objective is to find text chunks with similar meanings based on cosine similarity between the embedded query and text chunks. The virtual assistant will attempt to find the right text chunks to provide accurate answers to user queries.

6. **Create Final Data**: Execute "CreateFinalData.py." This step will combine all the text chunks and embeddings, creating two large files used by the AI to find the relevant text. If you want to add new content later, simply reprocess and embed the new files and run this step again.

7. **Run the Virtual Assistant**: Open a command prompt, navigate to the directory where your virtual TA is stored. Set up a virtual environment in Python. Then set `FLASK_APP=app` and press enter. Next, enter `flask run` and hit enter. You should see the following output:

```
Serving Flask app 'app'
Debug mode: off 
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
Running on http://127.0.0.1:5000 
Press CTRL+C to quit
```

8. **Access the Virtual Assistant**: Open a browser and enter http://localhost:5000/. Your Virtual Assistant should now be operational and ready to assist you.

Please note that this application is intended for development purposes and is not recommended for production deployments. For production environments, consider using a production WSGI server.

