from langchain_community.tools import wikipedia, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from datetime import datetime

def save_to_txt(data, filename="research_output.txt"):
   timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   formatted_text= f"---Research Output---\nTimestamp: {timestamp}\n\n{data}\n\n"

   with open(filename, "a",encoding="utf-8") as file:
       file.write(formatted_text)

   return f"Data saved to {filename}"

save_tool = Tool(
    name="Save_to_Text_File",
    func=save_to_txt,
    description="Search the web for information and save the output to a text file."
)    

search= DuckDuckGoSearchRun()
search_tool = Tool(
    name="Search",
    func=search.run,
    description="Search the web for information.",
)

wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=100)
wiki = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

wiki_tool = Tool(
    name="Wikipedia",
    func=wiki.run,
    description="Use this tool to get summaries from Wikipedia."
)