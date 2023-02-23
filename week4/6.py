import random
import datetime


def random_date(start, end):

    delta = end - start
    int_delta = delta.days
    random_days = random.randrange(int_delta)
    return start + datetime.timedelta(days=random_days)

# print(random_date(datetime.datetime(2022,2,13),datetime.datetime.today()))


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if int(age) > 0:
            self._age = age
        else:
            raise ValueError('age must be grater than zero')


class Soccerplayer(Human):
    def __init__(self, name, age: int, salary: float, pos, score: float):
        super().__init__(name, age)
        self.pos = pos
        self.salary = salary
        self.score = score

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if float(salary) > 0:
            self.__salary = salary
        else:
            raise ValueError('salary must be positive')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if int(age) >= 15 and int(age) < 30:
            self._age = age
        else:
            raise ValueError('you are not qualified to play')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score > 0 and score < 100:
            self._score = score
        else:
            raise ValueError('invalid score')

    def __str__(self) -> str:
        return self.name
class Coach(Human):
    def __init__(self, name, age, salary, start_date, end_date):
        super().__init__(name, age)
        self.salary = salary
        self.start_date = start_date
        self.end_date = end_date
        self.is_assigned = False

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if int(age) >= 30 and int(age) < 65:
            self._age = age
        else:
            raise ValueError('you are not qualified to coach')

    def __str__ (self):
        return self.name


class Team:
    def __init__(self, name, balance):
        self.list_of_players = []
        self._score = 0
        self.coach = None
        self.balance = balance
        self.name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score >= 0:
            self._score += score
        else:
            raise ValueError('invalid score')

    def __str__(self):

        return '-'*15 + '\n' + f"{self.name} has scored {self.score} \
with {self.coach} coaching.This team has ${self.balance}$." + '\n' + '-'*15

    def check_number_of_player(self):
        if len(self.list_of_players) == 11:
            pass
        else:
            raise ValueError('not valid')

    def add_player(self, player: Soccerplayer):
        if isinstance(player, Soccerplayer):
            self.list_of_players.append(player)
        else:
            raise ValueError('player is not recognized')

    def set_coach(self, ch: Coach):
        if not isinstance(ch, Coach):
            raise TypeError('you should enter a coach')
        elif ch.is_assigned:
            raise ValueError('coach already have a team')
        else:
            self.coach = ch
            ch.is_assigned = True

    def get_random_player(self):
        return random.choice(self.list_of_players)

    def buy_player(self, pl: Soccerplayer, cost: int):
        if cost <= self.balance:
            self.balance -= cost
            self.add_player(pl)
            print(f"You bought {pl}!")
        else:
            print('You are broke bro!')

    def sell_player(self, pl: Soccerplayer, cost: int):
        if pl not in self.list_of_players:
            raise KeyError('Where is your player asshole?')
        self.balance += cost
        print(f'{pl} was successfuly bye bye.')
        return self.list_of_players.pop(self.list_of_players.index(pl))

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __eq__(self, other):
        return self.score == other.score


class League:
    def __init__(self, list_of_teams):
        self.list_of_teams = list_of_teams

    def matchmaking(self):
        while True:
            t1 = random.randrange(0, 5)
            t2 = random.randrange(0, 5)
            if t2 != t1:
                break

        result = ['win t1', 'win t2', 'draw'][random.randint(0, 2)]
        self.update_scores(
            result, self.list_of_teams[t1], self.list_of_teams[t2])

    def display_league_table(self):
        for team in sorted(self.list_of_teams, key=lambda x: x.score):
            print(team)

    def update_scores(self, result, t1, t2):
        if result == 'win t1':
            t1.score += 3
        elif result == 'win t2':
            t2.score += 3
        else:
            t1.score += 1
            t2.score += 1


list_of_pos = ['RW', 'LW', 'CF', 'CM', 'CD', 'LB', 'RB', 'GK']
list_of_players = []
for i in range(1, 56):
    list_of_players.append(Soccerplayer(f'Neymar{i}', random.randrange(18, 30), random.randrange(
        10000, 50000, 10000), random.choice(list_of_pos), random.randrange(60, 90, 5)))
list_of_coach = []
for i in range(1, 6):
    list_of_coach.append(Coach(f'Pep{i}', random.randrange(36, 60, 2), random.randrange(10000, 500000, 10000), random_date(datetime.datetime(2010, 2, 13), datetime.datetime(2017, 2, 13)),
                               random_date(datetime.datetime(2018, 2, 13), datetime.datetime.today())))
list_of_teams_name = ['Real Madrid', 'Barca',
                      'PSG', 'Arsenal', 'Chelsea', 'Man U', 'Man C']
list_of_teams = [Team(list_of_teams_name.pop(), random.randrange(
    1000000, 10000000, 1000000)) for _ in range(5)]

for i, team in enumerate(list_of_teams):
    temp = random.choice(list_of_coach)
    team.set_coach(temp)
    list_of_coach.remove(temp)
    for pl in range(11):
        temp = random.choice(list_of_players)
        team.add_player(temp)
        list_of_players.remove(temp)

sold = list_of_teams[0].sell_player(list_of_teams[0].get_random_player(), 100000)
list_of_teams[1].buy_player(sold, 90000)

Champions_league = League(list_of_teams)
Champions_league.matchmaking()
Champions_league.display_league_table()


