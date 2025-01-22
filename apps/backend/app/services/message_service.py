from app.models.message import Message
from app.utils.yaml_access import get_yaml_data

class MessageService:
    '''
    メッセージ情報サービス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''
        yaml_data = get_yaml_data('messages.yaml')
        self.__messages = {message['number']: Message(**message) for message in yaml_data['messages']}

    def get_message(self, number: str) -> str:
        '''
        メッセージ番号に該当するメッセージを取得します
        :param number: str: メッセージ番号
        :return: str: メッセージ
        :raise ValueError: メッセージが見つからない場合
        '''
        # messages = __load_messages_yaml()
        message = self.__messages.get(number)
        if message:
            return message.message

        assert False, f"メッセージ番号({number})に該当するメッセージが見つかりませんでした"
        # raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませんでした")

message_service = MessageService()