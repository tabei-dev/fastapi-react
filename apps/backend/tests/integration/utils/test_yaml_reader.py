from app.utils.yaml_reader import get_yaml_data

def test_get_messages_yaml_data_success():
    yaml_data = get_yaml_data('messages.yaml')
    assert yaml_data

def test_get_classifications_yaml_data_success():
    yaml_data = get_yaml_data('classifications.yaml')
    assert yaml_data