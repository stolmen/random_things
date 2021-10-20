import pytest
from typing import Iterable
import itertools


@pytest.mark.parametrize(
    ("input_", "expected_output"),
    [
        ("", set()),
        ("a", {"a"}),
        ("ab", {"ab", "ba"}),
        ("abc", {"abc", "acb", "bac", "bca", "cab", "cba"}),
    ],
)
def test_anagrams__test_cases(input_, expected_output):
    output = get_all_permutations_str(input_)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_",
    [
        tuple(),
        ("a",),
        ("a", "b"),
        ("a", "b", "c"),
        ("a", "b", "c", "d"),
    ],
)
def test_against_permutations(input_: tuple):
    def permutations_blah(things):
        if not things:
            return set()
        if len(things) == 1:
            return set(things[0])
        return set(itertools.permutations(things, len(things)))

    assert get_all_permutations(input_) == permutations_blah(input_)


def get_all_permutations_str(word: str) -> set:
    return {"".join(i) for i in get_all_permutations(tuple([i for i in word]))}


def get_all_permutations(input_things: tuple) -> set:
    """Shitty recursive implementation of probably quadratic
    complexity of a function that calculates all permutations of the input."""
    if len(input_things) == 1:
        return set(input_things)

    if len(input_things) == 2:
        return {(input_things[0], input_things[1]), (input_things[1], input_things[0])}

    acc = set()
    for ele, subset in iterate_subsets(input_things):
        input_things = set((ele,) + subset for subset in get_all_permutations(subset))
        acc.update(input_things)

    return acc


def iterate_subsets(things_tuple: Iterable) -> Iterable[tuple]:
    """Generator that iterates through elements of an iterable and for each
    element, returns a two-tuple (x, y) where x is the element itself,
    and y is the subset of the input iterable with the element removed.
    """

    for idx, thing in enumerate(things_tuple):
        yield thing, things_tuple[:idx] + things_tuple[idx + 1 :]
