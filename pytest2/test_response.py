import pytest
from main import AnonymousSurvey

@pytest.fixture
def survey():
    """Define survey for tests"""
    question = "Best game?"
    survey = AnonymousSurvey(question)
    return survey

#Testing:
def test_1_response(survey):
    """Testing AnonymousSurvey Class 1 time"""
    survey.store_response('Elden Ring')
    
    assert 'Elden Ring' in survey.responses

def test_4_response(survey):
    """Testing 4 this time babyy!!"""
    responses = ["Elden Ring", 'Minecraft', 'Hollow Knight']
    for response in responses:
        survey.store_response(response)

    for response in responses:
        assert response in survey.responses
