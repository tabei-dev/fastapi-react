from app.models.message import Message
from app.managers.message_manager import create_messages, get_message
from app.utils.yaml_access import get_yaml_data

class MessageService:
    '''
    メッセージ情報サービス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''
        self.__messages = create_messages()

    def get_message(self, number: str) -> str:
        '''
        メッセージ番号に該当するメッセージを取得します
        :param number: str: メッセージ番号
        :return: str: メッセージ
        :raise ValueError: メッセージが見つからない場合
        '''
        message = get_message(self.__messages, number)
        if message:
            return message

        assert False, f"メッセージ番号({number})に該当するメッセージが見つかりませんでした"
        # raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませませんでした")

message_service = MessageService()