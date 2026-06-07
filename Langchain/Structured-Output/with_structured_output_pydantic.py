from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional  , Literal #litral for just to get desired output and optional is for just if optional
from pydantic import BaseModel , Field
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')


#schema in 
class review(BaseModel):
    key_themes : list[str] = Field(decription="write down all the key themes discussed in the review in a list")
    summary : str = Field(description="A brief summary of the review")
    sentiment : Literal['pos','neg']= Field(description="return sentiment")
    pros : Optional[list[str]] = Field(default=None,description="Tell the pros inside the list")
    cons: Optional[list[str]] = Field(default=None,description="Tell the cons inside the list")
    reviewer_name : Optional[str] = Field(default=None, description='Extract ONLY the human reviewer/person name. Do NOT write product name. If no reviewer name is mentioned, return None.')
    
    
    
structured_model = model.with_structured_output(review)

result= structured_model.invoke("""I recently upgraded to the Samsung Galaxy 524 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

reviewer name :  shubham upadhyay

""")


print(result.reviewer_name) 
