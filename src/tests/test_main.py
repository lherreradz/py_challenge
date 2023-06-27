import pytest

from src.main import get_pairs

@pytest.mark.parametrize(
        "list, expected_sum, expected_result",
        [
            ([0,1,2,3,4,5,6], 5, [[2, 3],[1, 4],[0, 5]]),
            ([0,0,1,2,3,4,5,6], 5, [[2, 3],[1, 4],[0, 5]]),
            ([-1,1,2,3,4,5,6], 5, [[2, 3],[1, 4],[-1, 6]]),
            ([-1,1], 5, [])
        ]
)
def test_get_pairs_params(list, expected_sum, expected_result):
    assert get_pairs(list, expected_sum) == expected_result
