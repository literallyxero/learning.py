class AnonymousSurvey:
    """Collect disguised answers from a survey"""
    def __init__(self, question):
        """Stores question and response"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the actual question"""
        print(self.question)
    
    def store_response(self, new_response):
        """Store the response"""
        self.responses.append(new_response)

    def show_results(self):
        """Shows the results"""
        print("Survey Results:")
        for responses in self.responses:
            print(f"- {responses}")
