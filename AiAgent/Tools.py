import smtplib
from email.mime.text import MIMEText
from email.header import Header

from pydantic import BaseModel, EmailStr, Field, field_validator
import os, dotenv

dotenv.load_dotenv(".env")


class EmailUser(BaseModel):
    email: EmailStr
    nickname: str = Field(pattern=r"^\w+$")

def sendEmail(receivers: list[EmailUser], message: str):
    me = os.environ["EMAIL_USERNAME"]
    # 1. 登录连接
    obj = smtplib.SMTP_SSL("smtp.qq.com", 465)
    obj.login(user=me, password=os.environ["EMAIL_PASSWORD"])

    # 2. 构造消息体
    _from = f"Windwhisper <{me}>"
    _to = ", ".join([f"{user.nickname} <{user.email}>" for user in receivers])

    email = MIMEText(message, "plain", "utf-8")
    email["From"] = _from
    email["To"] = _to
    email["Subject"] = Header(f'来自"{me}"的邮件', "utf-8")  # type: ignore

    # 3. 发送邮件
    _receivers = [user.email for user in receivers]
    obj.sendmail(me, _receivers, email.as_string())


if __name__ == "__main__":
    # sendEmail([
    #     EmailUser(email='1309896340@qq.com', nickname='zsy')
    # ],
    #     message="一次简单的消息测试"
    # )

    # sendEmail(
    #     [{"email": "1309896340@qq.com", "nickname": "ZZSSYY"}],  # type: ignore
    #     message="测试以Dict作为list[EmailUser]的参数传递",
    # )
    
    print(EmailUser.model_json_schema())
