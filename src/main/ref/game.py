from src.main.ref.player import Player

results_dict = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty"
}


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def get_score(self) -> str:
        p1 = self.player1.get_points()
        p2 = self.player2.get_points()

        if p1 == p2:
            if p1 == 0:
                return "Love-All"
            elif p1 == 1:
                return "Fifteen-All"
            elif p1 == 2:
                return "Thirty-All"
            else:
                return "Deuce"
        elif p1 < 4 and p2 < 4:
            return results_dict[p1] + "-" + results_dict[p2]
        else:
            diff = p1 - p2

            if diff >= 2:
                return "Win for player1"
            elif diff > 0:
                return "Advantage player1"
            elif diff <= -2:
                return "Win for player2"
            else:
                return "Advantage player2"

    def won_point(self, player: Player) -> None:
        if player == self.player1:
            self.player1.add_point()
        else:
            self.player2.add_point()