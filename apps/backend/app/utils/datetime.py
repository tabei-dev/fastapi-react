from datetime import datetime
from zoneinfo import ZoneInfo

JST = ZoneInfo("Asia/Tokyo")

class DateTimeUtil:
    '''
    日時ユーティリティ
    '''

    @staticmethod
    def now() -> datetime:
        '''
        現在日時を取得する
        :return: datetime: 現在日時
        '''
        return datetime.now(JST)

    @staticmethod
    def now_str() -> str:
        '''
        現在日時を文字列で取得する
        :return: str: 現在日時
        '''
        return DateTimeUtil.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def from_str(date_str: str) -> datetime:
        '''
        文字列から日時を取得する
        :param date_str: str: 日時文字列
        :return: datetime: 日時
        '''
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def to_str(date: datetime) -> str:
        '''
        日時を文字列に変換する
        :param date: datetime: 日時
        :return: str: 日時文字列
        '''
        return date.strftime("%Y-%m-%d %H:%M:%S")