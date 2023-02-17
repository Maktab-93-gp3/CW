class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self, age):
        if int(age) > 0:
            self._age = age
        else:
            raise ValueError ('age must be grater than zero')

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
    def set_salary(self, salary):
        if float(salary) > 0:
            self.__salary = salary
        else:
            raise ValueError ('salary must be positive')

    @property
    def age(self):
        return self._age
    @age.setter
    def set_age(self, age):
        if int(age) >= 15 and int(age) < 30:
            self._age = age
        else:
            raise ValueError ('you are not qualified to play')

    @property
    def score(self):
        return self._score
    
    @score.setter
    def set_score(self, score):
        if score > 0 and score < 100:
            self._score = score
        else: 
            raise ValueError ('invalid score')


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
    def set_age(self, age):
        if int(age) >= 30 and int(age) < 65:
            self._age = age
        else:
            raise ValueError ('you are not qualified to coach')
    
class team:
    def __init__(self, balance):
        self.list_of_players = []
        self.score = 0
        self.coach = None
        self.balance = balance

    @property
    def score(self):
        return self._score

    @score.setter
    def set_score(self, score):
        if score >= 0:
            self._score = score
        else: 
            raise ValueError ('invalid score')
    
    def check_number_of_player(self):
        if len(self.list_of_players) == 11:
            pass
        else:
            raise ValueError ('not valid')
    def add_player(self, player: Soccerplayer):
        if isinstance(player, Soccerplayer):
            self.list_of_players.append(player)
        else: 
            raise ValueError ('player is not recognized')
    
    def set_coach(self, ch: Coach):
        if not isinstance(ch, Coach):
            raise TypeError ('you should enter a coach')
        elif ch.is_assigned:
            raise ValueError ('coach already have a team')
        else:
            self.coach = ch
            ch.is_assigned = True
    
    def buy_player(self, pl: Soccerplayer, cost: int):
        if not isinstance(pl, Soccerplayer):
            raise TypeError ('doesnt exict')
        elif cost <= self.balance:
            self.balance -= cost
            self.add_player(pl)