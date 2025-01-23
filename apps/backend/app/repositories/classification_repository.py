from app.models.classification import ClassificationEnum, Classification, ClassificationDetail

def get_classification_details(
        classifications: dict,
        classification_enum: ClassificationEnum
    ) -> dict[str, ClassificationDetail]:
    '''
    指定の区分列挙型の区分明細情報一覧を取得する
    :param classifications: dict: 区分情報辞書
    :param classification_enum: Enum: 区分列挙型
    :return: dict[ClassificationEnum, ClassificationDetail]: 区分明細情報辞書
    '''
    classification = classifications.get(classification_enum.value)
    if classification:
        return classification.details

    assert False, f"区分列挙型({classification_enum.value})に該当する区分明細情報が見つかりませんでした"
    # raise ValueError(f"区分列挙型({classification_enum.value})に該当する区分明細情報が見つかりませんでした")

def get_classification_detail(
        classifications: dict,
        classification_enum: ClassificationEnum, detail_number: str
    ) -> ClassificationDetail:
    '''
    指定の区分列挙型と明細番号の区分明細情報を取得する
    :param classifications: dict: 区分情報辞書
    :param classification_enum: Enum: 区分列挙型
    :param detail_number: str: 明細番号
    :return: ClassificationDetail: 区分明細情報
    '''
    classification_details = get_classification_details(classifications, classification_enum)
    classification_detail = classification_details.get(detail_number)
    if classification_detail:
        return classification_detail

    assert False, f"区分列挙型({classification_enum.value})の区分明細情報({detail_number})が見つかりませんでした"
    # raise ValueError(f"区分列挙型({classification_enum.value})の区分明細情報({detail_number})が見つかりませんでした")
