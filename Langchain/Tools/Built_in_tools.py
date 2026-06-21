# DUCKDUCKGO SEARCH

from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()
results = search_tool.invoke('ipl news')

print(results)

#built in shell tool 

from langchain_community.tools import ShellTool

shell_tool = ShellTool()

result = shell_tool.invoke('whoami')

print(result)


#there is alot more toos u can check it on website
