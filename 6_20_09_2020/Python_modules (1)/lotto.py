"""Return the sum of x and y."""
from modules import tryagain as ta
from modules import hello as hi
from modules import numbers as nb
from modules import user as us
from modules import results as rs
from modules import reward as rd
from modules import thankyou as thx

def lotto() -> None:
    """
    Glowna funkcja lotto, zawiera w sobie cala logike
    :return:
    """
    playing = True
    hi.hello()

    while playing:
        number = us.retrieve_number_from_user()
        times = nb.generate_until_drawn(number, 1, 100)
        rs.inform_about_the_result(times)
        rd.get_reward(times)
        playing = ta.try_again()

    thx.thank_you()
