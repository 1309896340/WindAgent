from zai import ZhipuAiClient
from typing import Generator
import os

from AiAgent import ToolSchema, ToolCall

class Client: 
    def __init__(self) -> None:
        self.client = ZhipuAiClient(api_key=os.environ['ZHIPU_API_KEY'])
        self.model = 'glm-4.5'
        

    def request_tool(self, question: str) -> Generator[str, None, None]:
        messages = [
            {
                'role': 'system',
                'content': '你是一个ai助手。'
            },
            {
                'role': 'user',
                'content': [
                    {
                        'type': 'text',
                        'text': question
                    }
                ]
            }
        ]
        try:
            # # 1. 普通调用
            # resp = self.client.chat.completions.create(
            #     model=self.model,
            #     messages=messages
            # )
            # result = resp.choices[0].message.content # type: ignore
            
            # 2. 流式调用
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=True,
                tools=ToolSchema.tools,
                tool_choice='auto'
            )
            for chunk in stream:
                chunk_result = chunk.choices[0].delta.content # type: ignore
                chunk_tool_call = chunk.choices[0].delta.tool_calls # type: ignore
                if chunk_result is not None:
                    yield chunk_result
                if chunk_tool_call is not None:
                    func = chunk_tool_call[0].function
                    if func is not None and hasattr(func, 'name') and hasattr(func, 'arguments'):
                        if isinstance(func.name, str) and isinstance(func.arguments, str):
                            ToolCall.function_caller(func.name, func.arguments)
        except Exception as e:
            print(f"请求大模型出错: \n{str(e)}")
        return
    
    # def request(self, question: str) -> Generator[str, None, None]:
    #     messages = [
    #         {
    #             'role': 'system',
    #             'content': '你是一个ai助手。'
    #         },
    #         {
    #             'role': 'user',
    #             'content': [
    #                 {
    #                     'type': 'text',
    #                     'text': question
    #                 }
    #             ]
    #         }
    #     ]
    #     try:
    #         # # 1. 普通调用
    #         # resp = self.client.chat.completions.create(
    #         #     model=self.model,
    #         #     messages=messages
    #         # )
    #         # result = resp.choices[0].message.content # type: ignore
            
    #         # 2. 流式调用
    #         stream = self.client.chat.completions.create(
    #             model=self.model,
    #             messages=messages,
    #             stream=True
    #         )
    #         for chunk in stream:
    #             chunk_result = chunk.choices[0].delta.content # type: ignore
    #             if chunk_result is not None:
    #                 yield chunk_result
    #     except Exception as e:
    #         print(f"请求大模型出错: \n{str(e)}")
    #     return
    
    
    