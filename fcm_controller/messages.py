from pydantic import BaseModel
'''
필요한 메시지 양식을 작성
'''
class SimpleMsg(BaseModel):
    """
    간단한 메시지 양식
    - title: 메시지 제목
    - body: 메시지 내용
    """
    title: str
    body: str