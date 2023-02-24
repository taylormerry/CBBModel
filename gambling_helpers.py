from datetime import datetime

# input: probability
# output: American gambling odds format
def prob_to_american(prob):
    if prob > 0.5:
        return str(round(100 * prob / (prob - 1)))
    else:
        return '+' + str(round((1 - prob) / prob * 100))

# input: American gambling odds format
# output: probability
def american_to_prob(am_odds):
    if am_odds > 0:
        return 100 / (100 + am_odds)
    else:
        return 1 - (100 / (100 - am_odds))

def american_to_decimal(am_odds):
    if am_odds > 0:
        return 1 + (am_odds / 100)
    else:
        return 1 - (100 / am_odds)


def kelly_criterion(win_prob, bet_odds, payout_date = None, yearly_roi_proj = None):
    
    if (not isinstance(win_prob, float)) and (not isinstance(win_prob, int)):
        raise TypeError(f"Argument win_prob must be of type float or int, not {type(win_prob)}")

    if (not isinstance(bet_odds, int)):
        raise TypeError(f"Argument bet_odds must be of type int, not {type(bet_odds)}")

    if payout_date and (not isinstance(payout_date, str)):
        raise TypeError(f"Argument payout_date must be of type string, not {type(payout_date)}")

    if yearly_roi_proj and (not isinstance(yearly_roi_proj, float)):
        raise TypeError(f"Argument yearly_roi_proj must be of type float, not {type(yearly_roi_proj)}")

    if win_prob < 0 or win_prob > 1:
        raise ValueError("win_prob must be greater than or equal to zero and less than or equal to one")

    if payout_date and len(payout_date) != 8:
        raise ValueError("payout_date must be 8 characters long in YYYYMMDD format")

    if payout_date and yearly_roi_proj:
        days_to_payout = (datetime.strptime(payout_date, '%Y%m%d') - datetime.now()).days + 1

        if days_to_payout < 0:
            raise ValueError("payout_date must be today or in the future")

        payout_date_roi_proj = days_to_payout * yearly_roi_proj / 365        

    elif not payout_date and not yearly_roi_proj:
        payout_date_roi_proj = 0
    else:
        raise ValueError("Must provide both or neither of payout_date and yearly_roi_proj")

    win_proportion = american_to_decimal(bet_odds) - 1 - payout_date_roi_proj

    if win_proportion * win_prob > 0.5:
        return (win_prob + ((win_prob - 1) / win_proportion))
    else:
        return 0