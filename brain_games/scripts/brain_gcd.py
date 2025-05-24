# script to run brain-gcd
#
#
from brain_games.engine import run_engine
from brain_games.games.gcd import DESCRIPTION, generate_round


def main():
    run_engine(DESCRIPTION, generate_round)

if __name__ == "__main__":
    main()
