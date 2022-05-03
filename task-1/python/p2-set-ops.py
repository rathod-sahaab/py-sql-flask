from dataclasses import dataclass
from typing import List

@dataclass
class AnalyticsResult:
    all_sports: List[int]
    no_hockey_cricket_football: List[int]
    exactly_2_sports: List[int]
    no_sport: List[int]

def analytics(cricket: List[int], football: List[int], hockey: List[int]) -> AnalyticsResult:
    """
    Returns the analytics of the three lists.
    1. Students who play all 3 sports
    2. Students who play cricket and football but not hockey.
    3. Students who play exactly 2 sports.
    4. Students who don't play any of 3 sports
    """
    # given all students are 1-20
    all_student_set = set(range(1, 20 + 1))
    cricket_set, football_set, hockey_set = set(cricket), set(football), set(hockey)

    # 1. Students who play all 3 sports
    all_sport_set = cricket_set & football_set & hockey_set

    # 2. Students who play cricket and football but not hockey.
    no_hockey_cricket_football_set = cricket_set & football_set - hockey_set

    no_cricket_football_hockey_set = football_set & hockey_set - cricket_set
    no_football_cricket_hockey_set = cricket_set & hockey_set - football_set

    # 3. Students who play exactly 2 sports.
    exactly_2_sports_set = no_hockey_cricket_football_set | no_cricket_football_hockey_set | no_football_cricket_hockey_set

    # 4. Students who don't play any of 3 sports
    no_sport_set = all_student_set - (cricket_set | football_set | hockey_set)

    return AnalyticsResult(
        sorted(all_sport_set),
        sorted(no_hockey_cricket_football_set),
        sorted(exactly_2_sports_set),
        sorted(no_sport_set)
    )


if __name__ == '__main__':
    # [int(x) for x in input().split()] to get a list from cli
    cricket = [2, 5, 9, 12, 13, 15, 16, 17, 18, 19]
    football = [2, 4, 5, 6, 7, 9, 13, 16]
    hockey = [1, 2, 5, 9, 10, 11, 12, 13, 15]

    result = analytics(cricket, football, hockey)

    print(result.all_sports)
    print(result.no_hockey_cricket_football)
    print(result.exactly_2_sports)
    print(result.no_sport)