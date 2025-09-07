from AiAgent import Agent

client = Agent.Client()

cnt = 0

while True:
    print('>', end='')
    if cnt==0:
        _input = "帮我给邮箱为1309896340@qq.com的用户发送一条电子邮件，内容大致为打一声招呼，然后说明自己的身份和目的"
        print(_input)
    else:
        _input = str(input())
    response = client.request_tool(question=_input)
    for chunk in response:
        print(chunk, end="")
    print("")
    cnt += 1

