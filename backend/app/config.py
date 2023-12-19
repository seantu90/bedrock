# Configure generation parameter for Claude chat response.
# Adjust the values according to your application.
# See: https://docs.anthropic.com/claude/reference/complete_post
GENERATION_CONFIG = {
    "max_tokens_to_sample": 2000,
    "temperature": 0.6,
    "top_k": 250,
    "top_p": 0.999,
    "stop_sequences": ["Human: ", "Assistant: "],
}

# Configure embedding parameter.
# This parameter will pass to `RecursiveCharacterTextSplitter` of `langchain`.
# See: https://api.python.langchain.com/en/latest/text_splitter/langchain.text_splitter.RecursiveCharacterTextSplitter.html
EMBEDDING_CONFIG = {
    # DO NOT change `model_id` (currently other models are not supported)
    "model_id": "cohere.embed-multilingual-v3",
    "chunk_size": 1000,
    "chunk_overlap": 100,
}

# Configure search parameter to fetch relevant documents from vector store.
SEARCH_CONFIG = {
    "max_results": 5,
}
