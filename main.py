import logging
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from pydantic import BaseModel
import inngest
import inngest.fast_api
import uuid
import datetime



load_dotenv()


inngest_client = inngest.Inngest(
    app_id="rag",
    logger=logging.getLogger("uvicorn"),
    is_production=False,
    # serialize=inngest.PydanticSerializer(),
)

@inngest_client.create_function(
    fn_id='rag/ask',
    trigger=inngest.TriggerEvent(event='rag/ask')


)

async def ask_rag(event: inngest.Event):
    # question = event.data['question']
    # # Here you would add the logic to process the question using RAG
    # answer = f"This is a placeholder answer for the question: {question}"
    return {"answer": {"response": "This is a placeholder answer for the question."}}




app = FastAPI()


inngest.fast_api.serve(app, inngest_client, functions=[ask_rag])

