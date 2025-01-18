# Aviary.AI
AI-powered bird encyclopedia (Gen AI &amp; Langchain Project)
-- 
Here's the updated version of the project documentation with the `app.py` UI integration:

---

## Bird Encyclopedia Chatbot

This project implements a chatbot powered by Google’s Gemini model and Wikipedia, integrated with custom bird-related data from PDF encyclopedias. The chatbot answers user queries about birds and provides detailed information such as scientific names, habitats, diets, and more.

## Features

- **Wikipedia Integration**: Retrieves bird information from Wikipedia.
- **Custom PDF Data**: Extracts and processes bird-related content from PDF encyclopedias.
- **Generative AI**: Uses Google Gemini to generate factual responses.
- **FAISS Vectorstore**: Efficiently stores and retrieves embeddings for similarity search.
- **User Interface**: An intuitive UI built with Streamlit, allowing users to search for bird information easily.

## Requirements

Install dependencies from `requirements.txt`.

## Workflow

1. **API Configuration**: Set up Google Gemini API key for content generation.
2. **PDF Data Extraction**: Extracts bird-related data from PDFs using `PyPDF2`.
3. **Text Chunking**: Splits large texts into manageable chunks.
4. **Vectorstore Setup**: Converts text chunks into embeddings and stores them in a FAISS vector store.
5. **UI**: The user interface is built with Streamlit to provide an easy search experience for users.
6. **Prompting**: Creates dynamic prompts to generate concise, factual responses.
7. **User Interaction**: Handles user queries, and integrates custom data and Wikipedia to generate responses.

## `app.py` - User Interface

The user interface is built using [Streamlit](https://streamlit.io/). It allows users to input the name of a bird, search for information, and view detailed results in an organized format.

Key UI functionalities:
- **Search Bar**: Users can input a bird's name.
- **Search Button**: Initiates the search and generates results.
- **Results Display**: Displays detailed information about the queried bird, including scientific name, habitat, diet, lifespan, and more.

### Key Elements of the UI:
- **Prompt Template**: The chatbot is guided by a prompt template that ensures it delivers the necessary bird information in a structured format.
- **Streamlit Layout**: A sleek, dark-themed layout for easy navigation.
- **Search Functionality**: A text input and button for users to enter bird names and retrieve information.

This streamlined version integrates the UI functionality, making it easier for users to query bird information and view results in a user-friendly interface.
## Example Usage:

<img src="Screenshot (182).png">
<img src="Screenshot (184).png">

## License

MIT License - see the [LICENSE](LICENSE) file for details.

## Note

- Generate your Gemini API Key from <https://aistudio.google.com/apikey> and add it to `.env` file.
- 2 PDF sources in `\Data` were too large and hence couldn't be uploaded to GitHub, you can search them on Google with the terms Illustrated Encyclopedia of Birds - DK and Encyclopedia of birds - International Masters Publishing 2007 and add them to `\Data` path.
--
