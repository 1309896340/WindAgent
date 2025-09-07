tools = [
    {
        "type": "function",
        "function": {
            "name": "sendEmail",
            "description": "向指定的收件人列表发送电子邮件。",
            "parameters": {
                "type": "object",
                "properties": {
                    "receivers": {
                        "type": "array",
                        "description": "邮件收件人列表。",
                        "items": {
                            "type": "object",
                            "properties": {
                                "email": {
                                    "type": "string",
                                    "format": "email",
                                    "description": "收件人的电子邮件地址。",
                                },
                                "nickname": {
                                    "type": "string",
                                    "description": "收件人的昵称，只包含字母、数字和下划线。",
                                    "pattern": "^\\w+$",
                                },
                            },
                            "required": ["email", "nickname"],
                        },
                    },
                    "message": {"type": "string", "description": "邮件内容。"},
                },
                "required": ["receivers", "message"],
            },
        },
    }
]
