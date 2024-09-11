from LLM_Input import LLM_Model

def test_LLM_Model():
    Response = LLM_Model('sad').Initiate_Response()
    Mood_List = ['Cold', 'Warm', 'Sunny', 'Gloomy', 'Neutral']
    assert Response in Mood_List

def test_LLM_Model_str():
    Response = LLM_Model('sad').Initiate_Response()
    assert type(Response) == str