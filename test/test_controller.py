import sys
import os

# 상위 디렉토리의 경로를 모듈 탐색 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fcm_controller.controller import FirebaseAdmin
from fcm_controller.messages import SimpleMsg

if __name__ == '__main__':
    controller = FirebaseAdmin()
    token = "token"

    msg = SimpleMsg(
        title="this is sample title",
        body="this is sample body")

    result = controller.send_single(
        token=token,
        msg=msg
    )
    print(f"결과 : {result}")