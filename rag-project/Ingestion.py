from dotenv import load_dotenv
import os
from pinecone import Pinecone, ServerlessSpec  # Updated Pinecone import
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import

# Load environment variables
load_dotenv()

if __name__ == "__main__":

    # 1. Loading Documents
    print("Loading Documents...")
    loader = TextLoader("./information.txt", encoding="utf-8")
    document = loader.load()  # loads the documents with metadata
    print(f"Loaded {len(document)} documents")

    # 2. Splitting Documents
    print("Splitting Documents...")
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_documents = splitter.split_documents(document)
    print(f"Split {len(document)} documents into {len(split_documents)} chunks")

    # 3. Initializing Pinecone
    print("Initializing Pinecone...")
    pinecone_client = Pinecone(
        api_key=os.getenv("PINECONE_API_KEY")
    )

    # Check if the index exists or create one
    if "test" not in pinecone_client.list_indexes().names():
        pinecone_client.create_index(
            name="test",
            dimension=1536,  # Adjust to match your embedding dimension
            metric="cosine",  # Metric can be 'cosine', 'dotproduct', or 'euclidean'
            spec=ServerlessSpec(
                cloud="aws",
                region=os.getenv("PINECONE_ENV")
            )
        )

    # 4. Embedding Documents
    print("Started Embedding Documents...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 5. Inserting Documents into VectorDB
    print("Inserting Documents into VectorDB...")
    vector_db = PineconeVectorStore.from_documents(
        split_documents, embeddings, index_name="test"
    )
    print(f"Inserted {len(split_documents)} documents into VectorDB")
