import json
from AiAgent.Tools import EmailUser
from AiAgent.Tools import sendEmail

def function_caller(name: str, argument_json: str):
    argument = json.loads(argument_json)
    match name:
        case "sendEmail":
            _receivers = []
            for receiver in argument['receivers']:
                _receivers.append(EmailUser(**receiver))
            sendEmail(_receivers, argument['message'])
