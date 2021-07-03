class SotaP:
    def __init__(self, nPlayers) -> None:
        if not isinstance(nPlayers, int) or nPlayers < 1:
            raise Exception("Number of players invalid")