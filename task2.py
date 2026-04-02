
from workers.celery_app import celery

from backend.utils.llm import llm_stream

from backend.agents.research_tool import research_tool
from backend.agents.summarizer_tool import summarize_tool
from backend.agents.critic_tool import critic_tool
from backend.agents.writer_tool import writer_tool

import redis
r = redis.Redis(host="localhost", port=6379, db=0)

from workers.celery_app import celery
import redis

r = redis.Redis(host="localhost", port=6379, db=0)

@celery.task
def execute_convoy(task_id, convoy):
    channel = f"stream:{task_id}"
    data = {}

    print("Convoy received:", convoy)

    for bead in convoy:
        step = bead["type"]

        r.publish(channel, f"\n\n Running: {step.upper()}\n")

        if step == "research":
            result = research_tool(bead["input"])
            data["research"] = result

        elif step == "summarize":
            result = summarize_tool(data["research"])
            data["summary"] = result

        elif step == "critic":
            result = critic_tool(data["summary"])
            data["critic"] = result

        elif step == "write":
            result = writer_tool(data["critic"])
            data["final"] = result

        r.publish(channel, result)

    r.publish(channel, "[DONE]")

    return data["final"]



# @celery.task
# def execute_convoy(task_id, query):
#     channel = f"stream:{task_id}"

#     prompt = f"Write a detailed report on: {query}"

#     for chunk in llm_stream(prompt):
#         print("Streaming chunk:", chunk)
        
#         try:
#             data = json.loads(chunk)  
#             text = data.get("response", "")

#             if text:
#               r.publish(channel, text)   

#             if data.get("done"):
#               r.publish(channel, "[DONE]")

#         except Exception as e:
#          print("Parse error:", e)

#     r.publish(channel, "[DONE]")

