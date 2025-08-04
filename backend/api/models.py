from pydantic import BaseModel, Field

# Ingest Request
class IngestRequest(BaseModel):
    source: str = Field(..., description="The source of the data to ingest")
    payload: dict = Field(..., description="The payload to ingest")

# User request
class UserRequest(BaseModel):
    query: str = Field(..., description="The query to send to the API")

# Chat Response
class ChatResponse(BaseModel):
    response: str = Field(..., description="The response from the API")