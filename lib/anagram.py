class Anagram: 
    def __init__(self, word):

        self.word = word 

    def match(self, match_list):
        main_list = sorted([letter for letter in self.word])
        return_list = []
        for word in match_list: 
            match_list = sorted([letter for letter in word])
            if main_list == match_list: 
                return_list.append(word)
        return return_list