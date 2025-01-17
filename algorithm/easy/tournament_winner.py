# Tournament Winner
# There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible. Teams
# compete in a round robin, where each team faces off against all other teams. Only two teams compete against each other at a time, and for each competition, one
# team is designated the home team, while the other team is the away team. In each competition there's always one winner and one loser; there are no ties. A team
# receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team that receives the most amount of points.
# Given an array of pairs representing the teams that have competed against each other and an array containing the results of each competition, write a function that
# returns the winner of the tournament. The input arrays are named competitions and results, respectively. The competitions array has elements in the
# form of [home Team, awayTeam], where each team is a string of at most 30 characters representing the name of the team. The results array contains
# information about the winner of each corresponding competition in the competitions array. Specifically, results[i] denotes the winner of
# competitions[i], where a 1 in the results array means that the home team in the corresponding competition won and a
# won.
# means that the away team
# It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once. It's also guaranteed that the
# tournament will always have at least two teams.

# def tournamentWinner(competitions, results):
#     #
#     output = {}
#     for index, competition in enumerate(competitions):
#         winner = competition[int(not bool(results[index]))]
#         # print(winner, results[index])
#         if winner not in output:
#             output[winner] = 3
#         else:
#             output[winner] += 3

#     return max(output, key=output.get)

def tournamentWinner(competitions, results):
    """
        O(n) time
        O(k) space - number of unique teams + maybe the lenght of the keys in the dict but this is a constant
    """
    best_team = ""
    output = { best_team: 0 }

    for index, competition in enumerate(competitions):
        winner = competition[int(not bool(results[index]))]
        output[winner] = output.get(winner, 0) + 3

        if output[winner] > output[best_team]:
            best_team = winner


    return best_team
