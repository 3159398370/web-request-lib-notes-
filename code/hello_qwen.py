import os
from openai import OpenAI

try:
    client = OpenAI(
        # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
        api_key= "sk-d2bc26318f6747feb9357b95e016b682",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    # 初始化对话历史
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]

    print("欢迎使用AI助手！输入'退出'或'exit'结束对话。")

    while True:
        # 获取用户输入
        user_question = input("\n请输入您的问题: ")

        # 检查退出条件
        if user_question.lower() in ['退出', 'exit', 'quit']:
            print("感谢使用，再见！")
            break

        # 将用户问题添加到对话历史
        messages.append({'role': 'user', 'content': user_question})

        # 发送请求并获取回答
        completion = client.chat.completions.create(
            model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            messages=messages
        )

        # 获取AI回答
        ai_response = completion.choices[0].message.content
        print(f"\nAI回答: {ai_response}")

        # 将AI回答添加到对话历史
        messages.append({'role': 'assistant', 'content': ai_response})

except Exception as e:
    print(f"错误信息：{e}")
    print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")
