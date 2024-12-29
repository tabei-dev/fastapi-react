from pydantic import BaseModel

class Message(BaseModel):
    '''
    メッセージ情報
    :param number: int: メッセージ番号
    :param message: str: メッセージ
    '''
    number: int
    message: str

class MessageManager:
    '''
    メッセージ情報管理クラス
    '''

    def __init__(self, messages: list[Message]):
        '''
        メッセージ情報リストを設定する
        :param messages: list[Message]: メッセージ情報リスト
        '''
        self.messages = messages

    def get_message(self, number: int) -> str:
        '''
        メッセージ番号に該当するメッセージを取得する
        :param number: int: 番号
        :return: str: メッセージ
        :raise ValueError: メッセージが見つからない場合
        '''
        for message in self.messages:
            if message.number == number:
                return message.message

        raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませんでした")
