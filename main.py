from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core.node_parser import SentenceSplitter
from llama_index.readers.file import PDFReader

# 1. Configure LLM and Embedding models with memoryyy limits
Settings.llm = Ollama(
    model="llama3.2",
    request_timeout=120.0,
    context_window=2048,
    additional_kwargs={"num_ctx": 2048}
)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

print("Loading and cleanly parsing the PDF...")
# 2. Use an explicit PDF reader to filter out structural junk (trailers, xref, metadata)
parser_dict = {".pdf": PDFReader()}
file_extractor = SimpleDirectoryReader("data", file_extractor=parser_dict)
documents = file_extractor.load_data()

print("Parsing text into memory-friendly chunks...")
parser = SentenceSplitter(chunk_size=256,
                          chunk_overlap=20)
nodes = parser.get_nodes_from_documents(documents)

print("Indexing chunks into a local vector store...")
index = VectorStoreIndex(nodes)

# 3. Create the querii engine
query_engine = index.as_query_engine(similarity_top_k=2)

print("\n--- RAG Ready ---")
question = ("What are the generic medicines used for diabetes?")
print(f"Question: {question}\n")

try:
    response = query_engine.query(question)
    print(f"Answer:\n{response}")
except Exception as e:
    print(f"\nAn error occurred: {e}")