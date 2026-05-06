import Lab2_2610p.bmi as bmi

def test_bmi_normal_weight():
    expected = 0
    result = bmi.calculate_bmi(1.73, 70)
    assert(result == expected)



def test_bmi_over_weight():
    expected = 1
    result = bmi.calculate_bmi(1.73, 90)
    assert(result == expected)


def test_bmi_under_weight():
    expected = -1
    result = bmi.calculate_bmi(1.73, 50)
    assert(result == expected)
