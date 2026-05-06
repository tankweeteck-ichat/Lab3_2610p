import price_info


def test_total_cost():
    expected_result = 46.75
    result = price_info.total_cost_shopping()
    assert (result == expected_result)


def test_const_of_fruits():
    expected_result = 14.0   # 10 oranges = 10 x 1.40 = 14.0
    result = price_info.cost_of_fruits('orange', 10)
    assert (result == expected_result)

