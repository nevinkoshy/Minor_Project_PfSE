from handcalcs.decorator import handcalc
def calc_Pr_list(t_list: list, l: int, h_u: float, k: float, phi_c: float, f_c: float):
    """
    Calculates Pr of a concrete bearing wall as per CSA A23.3-14
    """
    alpha_1 = max(0.67, 0.85-0.0015*f_c)
    P_r_list = []
    for t_value in t_list:        
        A_g = t_value * l
        P_r_value = round(0.001*(2/3) * alpha_1 * phi_c * f_c * A_g * (1 - (k * h_u/(32*t_value))**2),0)  #in kilonewtons
        P_r_list.append(P_r_value)
    return P_r_list

@handcalc()
def calc_Pr(t: int, l: int, h_u: float, k: float, phi_c: float, f_c: float):
    """
    Calculates Pr of a concrete bearing wall as per CSA A23.3-14
    """
    alpha_1 = max(0.67, 0.85-0.0015*f_c)
    A_g = t * l
    P_r = (2/3) * alpha_1 * phi_c * f_c * A_g * (1 - (k * h_u/(32*t))**2)
    return P_r