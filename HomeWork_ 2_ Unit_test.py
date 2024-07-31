import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

# runer_1 = Runner('Ускейн', speed=10)
# runer_2 = Runner('Андрей', speed=9)
# runer_3 = Runner('Ник', speed=3)
#
# turnament_1 =Tournament(10, runer_1, runer_2, runer_3)
# a = turnament_1.start()
# print(a.values())


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}


    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_result.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def setUp(self):
        self.runer_1 = Runner('Ускейн', speed=10)
        self.runer_2 = Runner('Андрей', speed=9)
        self.runer_3 = Runner('Ник', speed=3)

    def test_turn1(self):

        turn_1 = Tournament(90, self.runer_1, self.runer_3)
        result = turn_1.start()
        # print(result[list(result.keys())[-1]] == 'Ник')
        self.assertTrue(result[list(result.keys())[-1]] == self.runer_3)
        self.all_result['№ 1'] = result

    def test_turn2(self):
        turn_2 = Tournament(90, self.runer_2, self.runer_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == self.runer_3)
        self.all_result['№ 2'] = result

    def test_turn3(self):
        turn_3 = Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == self.runer_3)
        self.all_result['№ 3'] = result


        
    def test_turn4(self):
        """
        Дополнительный тест, выявляющий ошибку функции start
        Ошибка заключается в том, что удаление объекта из списка participants может
        происходить до того, как будет обработан весь цикл и для каждого объекта будет
        запущен метод participant.run()
        Для решения этого недочета надо переписать функцию и вместо self.participants.remove(participant)
        использовать цикл сортировки но для прохождения использованного теста достаточно
        убрать знак равенства в этом вырожении participant.distance >= self.full_distance:
   
        """
        turn_4 = Tournament(5, self.runer_1, self.runer_2, self.runer_3)
        result = turn_4.start()
        self.assertTrue(result[list(result.keys())[-1]] == self.runer_3)
        self.all_result['test_turn4'] = result

if __name__ == '__main__':
    unittest.main()