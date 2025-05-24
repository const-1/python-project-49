# script to run brain-prime
#
#
from brain_games.engine import run_engine
from brain_games.games.prime import DESCRIPTION, generate_round


def main():
    run_engine(DESCRIPTION, generate_round)


if __name__ == "__main__":
    main()
