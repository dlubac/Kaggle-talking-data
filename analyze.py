import csv
import random

class Player:
    """
    Class to represent a player
    """

    def __init__(self, name, role, cost, points):
        self.name = name
        self.role = role
        self.cost = float(cost)
        self.points = float(points)


class Pro_Player:
    """
    Class to represent a pro player
    """

    def __init__(self):


class Fantasy_Team:
    """
    Class to represent team
    """

    def __init__(self, pos1, pos2, pos3, pos4, pos5):
        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3
        self.pos4 = pos4
        self.pos5 = pos5

    def get_total_points(self):
        """
        Gets the total cost for a team
        :return: total
        """
        total = self.pos1.points + self.pos2.points + self.pos3.points + self.pos4.points + self.pos5.points

        return total

    def get_total_cost(self):
        """
        Gets the total points for a team
        :return: total
        """
        total = self.pos1.cost + self.pos2.cost + self.pos3.cost + self.pos4.cost + self.pos5.cost

        return total


def get_random_player(player_list):
    """
    Picks a random player from a list of players

    :param player_list: list of player objects
    :return: random_player, random player object
    """

    sys_random = random.SystemRandom()
    random_player = sys_random.choice(player_list)
    return random_player


def parse_players_by_role(player_list):
    """
    Parses a list of players into a dictionary of lists by role
    :param player_list: list of player objects
    :return: dictionary of lists
    """

    position_1_list = []
    position_2_list = []
    position_3_list = []
    position_4_list = []
    position_5_list = []

    for player in player_list:
        if player.role == '1':
            position_1_list.append(player)
        elif player.role == '2':
            position_2_list.append(player)
        elif player.role == '3':
            position_3_list.append(player)
        elif player.role == '4':
            position_4_list.append(player)
        elif player.role == '5':
            position_5_list.append(player)

    return {'pos_1_players': position_1_list, 'pos_2_players': position_2_list, 'pos_3_players': position_3_list,
            'pos_4_players': position_4_list, 'pos_5_players': position_5_list}


def get_random_team(player_list):
    """
    Creates a team of random players
    :param player_list: list of players
    :return:
    """

    players_by_role = parse_players_by_role(player_list)

    pos_1_player = get_random_player(players_by_role['pos_1_players'])
    pos_2_player = get_random_player(players_by_role['pos_2_players'])
    pos_3_player = get_random_player(players_by_role['pos_3_players'])
    pos_4_player = get_random_player(players_by_role['pos_4_players'])
    pos_5_player = get_random_player(players_by_role['pos_5_players'])

    return Fantasy_Team(pos_1_player, pos_2_player, pos_3_player, pos_4_player, pos_5_player)


if __name__ == '__main__':

    # Read data
    players = []
    with open('players.csv') as f:
        for row in csv.DictReader(f):
            player_dict = dict(row)
            new_player = Player(player_dict['name'], player_dict['role'], player_dict['cost'], player_dict['points'])
            players.append(new_player)

    team = get_random_team(players)
    print(team.get_total_cost())
