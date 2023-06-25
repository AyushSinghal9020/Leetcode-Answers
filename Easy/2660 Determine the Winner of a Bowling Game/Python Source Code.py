class Solution:
    
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        
        player_1_s = []
        player_2_s = []

        for score in player1:
            
            if 10 not in player_1_s:player_1_s.append(score)
            else : player_1_s.append(score * 2)
            
        for score in player2:
            
            if 10 not in player_2_s:player_2_s.append(score)
            else:player_2_s.append(score * 2)
        
        score_1 = sum(player_1_s)
        score_2 = sum(player_2_s)

        if score_1 > score_2:return 1
        elif score_1 < score_2:return 2
        else : return 0
