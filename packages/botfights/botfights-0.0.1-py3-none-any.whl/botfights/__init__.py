import pathlib

import fire
import pkg_resources

from botfights.wordle.wordle import get_random, load_wordlist, play_bots


def _gen_implementations():
    for entry_point in pkg_resources.iter_entry_points("botfights.wordle.guesser"):
        factory_func = entry_point.load()
        yield entry_point.name, factory_func


def get_implementations():
    return dict(_gen_implementations())


def wordle(guesser: str, seed: str = "", num: int = 0):
    get_random().seed(seed)

    wordlist = load_wordlist(pathlib.Path(__file__).absolute().parent  /"wordle"/ "wordlist.txt")
    bot = get_implementations()[guesser](wordlist)

    return play_bots({guesser: bot}, wordlist, num)


def main():
    fire.Fire({func.__name__: func for func in [wordle]})
