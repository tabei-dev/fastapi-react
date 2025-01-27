from app.domain.value_objects.message import Message
from app.helpers.yaml import get_yaml_data
# from app.models.message import Message

__yaml_data = get_yaml_data('messages.yaml')
__messages = {message['number']: Message(**message) for message in __yaml_data['messages']}

def get_message(number: str) -> str:
    '''
    メッセージ番号に該当するメッセージを取得します
    :param number: str: メッセージ番号
    :return: str: メッセージ
    :raise ValueError: メッセージが見つからない場合
    '''
    message = __messages.get(number)
    if message:
        return message.message

    # assert False, f"メッセージ番号({number})に該当するメッセージが見つかりませんでした"
    raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませませんでした")