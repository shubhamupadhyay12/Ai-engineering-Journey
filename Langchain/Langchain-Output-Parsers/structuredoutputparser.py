from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate  #core is small library frew used tools
from langchain_classic.output_parsers import StructuredOutputParser , ResponseSchema

load_dotenv()


#define the model 
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct"
)

model = ChatHuggingFace(llm=llm)


schemas = [
    ResponseSchema(name = 'fact_1', description="fact 1 about the topic"),
    ResponseSchema(name = 'fact_2', description="fact 2 about the topic"),
    ResponseSchema(name = 'fact_3', description="fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schemas)

template = PromptTemplate(
    template = 'give 3 facts about the {topic} \n {format_instruction}',
    input_variables= ['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
chain = template | model | parser
result = chain.invoke({'topic':'black holle'})

# prompt = template.invoke({'topic':'black hole'})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
print(result)