class Selection:

    @staticmethod
    def result(number):
        number_dictionary = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty'
        }
        return number_dictionary.get(number)

    def problem(self, number):
        if number == 4:
            print("Four is cosmo")
        else:
            word = self.result(number)
            new_word = self.result(len(word))
            print(f'{self.result(number)} is {new_word}')
            self.problem(len(word))


run = Selection()
UserInput = int(input('Choose a number between 0 and 20! '))
run.problem(UserInput)
