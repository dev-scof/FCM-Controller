from firebase_admin import (initialize_app, 
                            messaging, 
                            delete_app, 
                            credentials)
from .configs.config import Config
from .messages import SimpleMsg

class FirebaseAdmin():
    def __init__(
            self,
            cred_path=Config.FCM_CRED_PATH, 
            options=None
        ):
        cred = credentials.Certificate(cred_path)
        self.app = initialize_app(cred, options)
        self.message={}

    def send_single(self, token: str, msg:SimpleMsg):
        """
        특정 기기에 메시지 전송
        :param token: 특정 기기 토큰
        :param msg: 메시지 내용
        :return: 결과
        """
        message = messaging.Message(
            data=msg.dict(exclude_none=True),
            token=token
        )
        result = messaging.send(message)
        return result

    def send_multi(self, tokens: list, msg:SimpleMsg):
        """
        여러 기기에 메시지 전송
        :param tokens: 특정 기기 토큰 리스트
        :param msg: 메시지 내용
        :return: 결과
        """
        message = messaging.MulticastMessage(
            data=msg.dict(exclude_none=True),
            tokens=tokens,
        )
        result = messaging.send_multicast(message)
        return result

    def __del__(self):
        delete_app(self.app)


if __name__ == '__main__':
    fcm = FirebaseAdmin()
    msg = SimpleMsg(title="hello world",
                     body="test bodydkd")
    fcm.send_single(
        "token",
        msg.dict(exclude_none=True)
    )
    tokens=[
        "token1",
        "token2",
        "token3"
        ]
    fcm.send_multi(
        tokens=tokens,
        msg=msg.dict(exclude_none=True)
    )