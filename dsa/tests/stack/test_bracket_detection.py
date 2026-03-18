from dsa.solutions.stack.bracket_detection import check_bracket


class TestBracketDetection:
    """
    Test for bracket detection

    LeetCode: https://leetcode.com/problems/valid-parentheses
    """

    def test_valid_sequences(self):
        valid_sequences = [None, "()", "hello",
                           "(world)", "()[]{}","{} [{}] ()",
                           "  [ ]","[({})]","[sometext]",
                           "[hello([{}])]","[hello(w[o{r}l]d)]","[([{}])]{}[]()"]
        assert_bracket_detections(valid_sequences, True)

    def test_invalid_sequences(self):
        invalid_sequences = [")", "{"," ({)}"]
        assert_bracket_detections(invalid_sequences, False)

def assert_bracket_detections(bracket_sequences, expected_result: bool):
    for bracket_sequence in bracket_sequences:
        assert_bracket_detection(bracket_sequence, expected_result)

def assert_bracket_detection(bracket_sequence, expected_result):
    assert check_bracket(bracket_sequence) == expected_result