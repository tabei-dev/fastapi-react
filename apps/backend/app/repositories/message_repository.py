from app.models.message import Message

def get_message(messages: dict[str, Message], number: str) -> str:
    '''
    メッセージ番号に該当するメッセージを取得します
    :param messages: dict[str, Message]: メッセージ辞書
    :param number: str: メッセージ番号
    :return: str: メッセージ
    :raise ValueError: メッセージが見つからない場合
    '''
    message = messages.get(number)
    if message:
        return message.message

    assert False, f"メッセージ番号({number})に該当するメッセージが見つかりませんでした"
    # raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませんでした")