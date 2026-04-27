from langchain.tools import tool
from langchain_community.document_loaders import PyPDFLoader

from logger import log

@tool("read_pdf", description=(
    """
    Read a single pdf file which has a list variable that holds each page content
    """
))
def read_pdf(file_path: str):
    msg = f"Content is being read from '{file_path}'"
    log("System", msg)
    loader = PyPDFLoader(f"../{file_path}")
    docs = loader.load()
    pages = [page.page_content[:5780] for page in docs]
    return pages

@tool("create_pdf", description=(
    """
    Create a single pdf file
    """
))
def create_pdf(file_name: str, file_content):
    pass