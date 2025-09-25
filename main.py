import logging
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from pydantic import BaseModel
import inngest.fast_api 
import uuid
import datetime



load_dotenv()


inngest_client = inngest.fast_api.Client(
    app_id="rag",
    logging=logging.getLogger("uvicorn"),
    is_production=False,
    serialize=inngest.PydanticSerializer(),
)


