from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field,EmailStr
import os

load_dotenv()


class Review(BaseModel):
    key_themes: list[str]=Field(desctiption="the main themes or topics discussed in the review")
    summary : str=Field(description="a brief summary of the review")
    sentiment : Literal['pos','neg']=Field(description="the sentiment of the review either positive,negative or neutral based on the review")
    rating : int=Field(desctiption="the rating of the product on a scale of 1 to 5")
    pros: Optional[list[str]]=Field(default=None,description="the positive aspect of the product mentioned in the review ,if any")
    cons: Optional[list[str]]=Field(default=None,description="the negative aspect of the product mentioned in the review,if any")
    name: Optional[str]=Field(default="raju joshi",description="the name of the reviewer present in the review ,if any")
    



model = ChatOpenAI(
    model=os.getenv("OPENROUTER_MODEL"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7,
)

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result)