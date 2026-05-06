import employee_info
from employee_info import employee_data as EMPDATA


def test_calculate_average_salary():
    expected_result = 60166.67   # rounded to 2 decimal points
    result = employee_info.calculate_average_salary()
    assert (round(result,2) == expected_result)



def test_get_empolyees_by_age_range_29_39():
    indices = [0, 3, 4]
    expected_result = [EMPDATA[i] for i in indices]
    # Alternatively, can use the code below, which is less flexible.
    # expected_result = [EMPDATA[0], EMPDATA[3], EMPDATA[4]]  # 0, 3, 4
    result = []
    result = employee_info.get_employees_by_age_range(29, 39)
    assert (result == expected_result)


def test_get_empolyees_by_age_range_24_44():
    indices = [0, 1, 3, 4, 5]
    expected_result = [EMPDATA[i] for i in indices]
    result = []
    result = employee_info.get_employees_by_age_range(24, 44)
    assert (result == expected_result)


def test_get_empolyees_by_dept_Sales():
    indices = [0, 5]
    expected_result = [EMPDATA[i] for i in indices]
    # Alternatively, can use the code below, which is less flexible.
    # expected_result = [EMPDATA[0], EMPDATA[3], EMPDATA[4]]  # 0, 3, 4
    result = []
    result = employee_info.get_employees_by_dept("Sales")
    assert (result == expected_result)


def test_get_empolyees_by_dept_Marketing():
    indices = [1, 2]
    expected_result = [EMPDATA[i] for i in indices]
    # Alternatively, can use the code below, which is less flexible.
    # expected_result = [EMPDATA[0], EMPDATA[3], EMPDATA[4]]  # 0, 3, 4
    result = []
    result = employee_info.get_employees_by_dept("Marketing")
    assert (result == expected_result)


def test_get_empolyees_by_dept_Not_Found():
    expected_result = []
    # Alternatively, can use the code below, which is less flexible.
    # expected_result = [EMPDATA[0], EMPDATA[3], EMPDATA[4]]  # 0, 3, 4
    result = []
    result = employee_info.get_employees_by_dept("Research")
    assert (result == expected_result)
