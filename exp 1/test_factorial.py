from factorial import factorial 

def test_positive_number():
    assert factorial(5) == 120
def test_negative_number():
    assert factorial(-9) == 0