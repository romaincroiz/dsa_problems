from dsa.solutions.array.best_time_buy_sell_stock import max_profit

def assert_profit(prices, expected):
    assert max_profit(prices) == expected

class TestBestTimeToBuyAndSellStock:
    """
    Test for Best-time-to-buy-and-sell-stock problem

    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
    """

    def test_edge_one_element(self):
        assert_profit([7], 0)

    def test_case_profit(self):
        assert_profit([7,1,5,3,6,4], 5)

    def test_case_no_transaction(self):
        assert_profit([7, 6, 4, 3, 1], 0)

    def test_case_transaction_no_profit(self):
        assert_profit([7,7,7], 0)

    def test_case_transaction_profit(self):
        assert_profit([3, 2, 6, 1, 4, 7, 0, 5], 6)