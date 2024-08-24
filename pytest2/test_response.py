from main import AnonymousSurvey

#Testing:
def test_1_response():
    """Testing AnonymousSurvey Class"""
    question = "Best Game?"
    survey = AnonymousSurvey(question)

    survey.store_response('Elden Ring')
    
    assert 'Elden Ring' in survey.responses

def test_4_response():
    """Testing 4 this time babyy!!"""
    question = "Best game?"
    survey = AnonymousSurvey(question)
    responses = ['Elden Ring', 'Minecraft', 'Hollow Knight']
    
    for response in responses:
        survey.store_response(response)

    for response in responses:
        assert response in survey.responses
