from app_module import calc_Pr

def test_calc():
    assert calc_Pr(200, 2000, 3000, 1, 0.65, 40) == ["3.625 MN", "3.625 MN"]