from app.models.message import Message
from app.utils.yaml import get_yaml_data

class MessageManager:
    '''
    メッセージ情報マネージャ
    '''
    def __init__(self):
        '''
        コンストラクタ
        '''
        self.__messages = self.__create_messages()

    def __create_messages(self) -> dict[str, Message]:
        '''
        メッセージ情報を生成します
        :return: dict[str, Message]: メッセージ辞書
        '''
        yaml_data = get_yaml_data('messages.yaml')
        messages = {message['number']: Message(**message) for message in yaml_data['messages']}
        return messages

    def get_message(self, number: str) -> str:
        '''
        メッセージ番号に該当するメッセージを取得します
        :param messages: dict[str, Message]: メッセージ辞書
        :param number: str: メッセージ番号
        :return: str: メッセージ
        '''
        message = self.__messages.get(number)
        if message:
            return message.message
        else:
            return ""

__message_manager = MessageManager()

def get_message(number: str) -> str:
    '''
    メッセージ番号に該当するメッセージを取得します
    :param number: str: メッセージ番号
    :return: str: メッセージ
    :raise ValueError: メッセージが見つからない場合
    '''
    message = __message_manager.get_message(number)
    if message:
        return message

    # assert False, f"メッセージ番号({number})に該当するメッセージが見つかりませんでした"
    raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませませんでした")
