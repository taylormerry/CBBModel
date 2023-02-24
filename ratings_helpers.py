import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from plotnine import *

# TODO: param to apply the final score shrinkage to game predictions
def generate_parameters(backtest = False):
    """
    Generates random paramters if backtesting, otherwise returns the default parameters
    """

    if backtest:

        # list of possible params
        nonconf_multipliers = [1.0]
        pace_formats = ['Seconds', 'Poss']
        date_functions = [
            {'min': 0.9, 'inflexion': 0},
            {'min': 0.9, 'inflexion': 5},
            {'min': 0.9, 'inflexion': 7},
            {'min': 0.9, 'inflexion': 10},
            {'min': 0.9, 'inflexion': 14},
            {'min': 0.9, 'inflexion': 21},
            {'min': 0.9, 'inflexion': 30},
            {'min': 0.9, 'inflexion': 45},
            {'min': 0.9, 'inflexion': 60},
            {'min': 0.7, 'inflexion': 0},
            {'min': 0.7, 'inflexion': 5},
            {'min': 0.7, 'inflexion': 7},
            {'min': 0.7, 'inflexion': 10},
            {'min': 0.7, 'inflexion': 14},
            {'min': 0.7, 'inflexion': 21},
            {'min': 0.7, 'inflexion': 30},
            {'min': 0.7, 'inflexion': 45},
            {'min': 0.7, 'inflexion': 60},
            {'min': 0.5, 'inflexion': 0},
            {'min': 0.5, 'inflexion': 5},
            {'min': 0.5, 'inflexion': 7},
            {'min': 0.5, 'inflexion': 10},
            {'min': 0.5, 'inflexion': 14},
            {'min': 0.5, 'inflexion': 21},
            {'min': 0.5, 'inflexion': 30},
            {'min': 0.5, 'inflexion': 45},
            {'min': 0.5, 'inflexion': 60},
            {'min': 0.3, 'inflexion': 0},
            {'min': 0.3, 'inflexion': 5},
            {'min': 0.3, 'inflexion': 7},
            {'min': 0.3, 'inflexion': 10},
            {'min': 0.3, 'inflexion': 14},
            {'min': 0.3, 'inflexion': 21},
            {'min': 0.3, 'inflexion': 30},
            {'min': 0.3, 'inflexion': 45},
            {'min': 0.3, 'inflexion': 60}
        ]
        expected_points_weights = [0.8, 0.9, 0.95, 1.0]
        final_score_decays = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7, 0.8, 0.9, 1.0] # 0.0 is none, otherwise, lower is stronger decay
        score_differential_shrinkages = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.0]
        prior_weights = [0.0] # TODO: realistic prior weights (after end of season backtest)

        # randomly choose params for hierarchal sampling
        date_function = random.choice(date_functions)
        expected_points_weight_parent = random.choice(expected_points_weights)
        score_differential_shrinkage_parent = random.choice(score_differential_shrinkages)
        prior_weight_parent = random.choice(prior_weights)

        # use the randomly chosen "parent" to generate possible "children" (correlated with "parent")
        expected_points_weight_children = np.clip(
            [expected_points_weight_parent + x for x in [-0.1, -0.05, -0.05, 0, 0, 0, 0, 0.05, 0.05, 0.1]], 
            a_min = 0.0, a_max = 1.0
        )

        score_differential_shrinkage_children = np.clip(
            [score_differential_shrinkage_parent + x for x in [-0.3, -0.2, -0.1, 0, 0, 0, 0.1, 0.2, 0.3]], 
            a_min = 0.0, a_max = 1.0
        )

        prior_weight_children = np.clip(
            [prior_weight_parent + x for x in [0]], # TODO: realistic prior weights (after end of season backtest)
            a_min = 0.0, a_max = None
        )

        # assign the parameters to random choices
        nonconf_multiplier = random.choice(nonconf_multipliers)
        pace_format = random.choice(pace_formats)
        date_function_min = date_function['min']
        date_function_inflexion = date_function['inflexion']
        expected_points_weight_dunk = round(random.choice(expected_points_weight_children), 2)
        expected_points_weight_layup = round(random.choice(expected_points_weight_children), 2)
        expected_points_weight_ft = round(random.choice(expected_points_weight_children), 2)
        expected_points_weight_long_two = round(random.choice(expected_points_weight_children), 2)
        expected_points_weight_three = round(random.choice(expected_points_weight_children), 2)
        final_score_decay = random.choice(final_score_decays)
        score_differential_shrinkage_ppp_3 = round(random.choice(score_differential_shrinkage_children), 2)
        score_differential_shrinkage_ppp_close_2 = round(random.choice(score_differential_shrinkage_children), 2)
        score_differential_shrinkage_ppp_long_2 = round(random.choice(score_differential_shrinkage_children), 2)
        score_differential_shrinkage_ppp_transition = round(random.choice(score_differential_shrinkage_children), 2)
        score_differential_shrinkage_pct_3 = round(random.choice(score_differential_shrinkage_children), 2)
        score_differential_shrinkage_pct_close_2 = round(random.choice(score_differential_shrinkage_children), 2)
        score_differential_shrinkage_pct_long_2 = round(random.choice(score_differential_shrinkage_children), 2)
        score_differential_shrinkage_pct_to = round(random.choice(score_differential_shrinkage_children), 2)
        off_transition_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        off_turnover_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        off_close_2_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        off_long_2_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        off_3_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        off_other_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        def_transition_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        def_turnover_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        def_close_2_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        def_long_2_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        def_3_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        def_other_probability_prior_weight = round(random.choice(prior_weight_children), 2)
        off_transition_efficiency_prior_weight = round(random.choice(prior_weight_children), 2)
        off_close_2_efficiency_prior_weight = round(random.choice(prior_weight_children), 2)
        off_long_2_efficiency_prior_weight = round(random.choice(prior_weight_children), 2)
        off_3_efficiency_prior_weight = round(random.choice(prior_weight_children), 2)
        off_other_efficiency_prior_weight = round(random.choice(prior_weight_children), 2)
        def_transition_efficiency_prior_weight = round(random.choice(prior_weight_children), 2)
        def_close_2_efficiency_prior_weight = round(random.choice(prior_weight_children), 2)
        def_long_2_efficiency_prior_weight = round(random.choice(prior_weight_children), 2)
        def_3_efficiency_prior_weight = round(random.choice(prior_weight_children), 2)
        def_other_efficiency_prior_weight = round(random.choice(prior_weight_children), 2)
        pace_prior_weight = round(random.choice(prior_weight_children), 2)
    else:

        # default params
        nonconf_multiplier = 1.0
        pace_format = 'Poss'
        date_function_min = 0.6
        date_function_inflexion = 10.0
        expected_points_weight_dunk = 1.0
        expected_points_weight_layup = 1.0
        expected_points_weight_ft = 1.0
        expected_points_weight_long_two = 1.0
        expected_points_weight_three = 1.0
        final_score_decay = 0.0
        score_differential_shrinkage_ppp_3 = 1.0
        score_differential_shrinkage_ppp_close_2 = 1.0
        score_differential_shrinkage_ppp_long_2 = 1.0
        score_differential_shrinkage_ppp_transition = 1.0
        score_differential_shrinkage_pct_3 = 1.0
        score_differential_shrinkage_pct_close_2 = 1.0
        score_differential_shrinkage_pct_long_2 = 1.0
        score_differential_shrinkage_pct_to = 1.0
        off_transition_probability_prior_weight = 0.0
        off_turnover_probability_prior_weight = 0.0
        off_close_2_probability_prior_weight = 0.0
        off_long_2_probability_prior_weight = 0.0
        off_3_probability_prior_weight = 0.0
        off_other_probability_prior_weight = 0.0
        def_transition_probability_prior_weight = 0.0
        def_turnover_probability_prior_weight = 0.0
        def_close_2_probability_prior_weight = 0.0
        def_long_2_probability_prior_weight = 0.0
        def_3_probability_prior_weight = 0.0
        def_other_probability_prior_weight = 0.0
        off_transition_efficiency_prior_weight = 0.0
        off_close_2_efficiency_prior_weight = 0.0
        off_long_2_efficiency_prior_weight = 0.0
        off_3_efficiency_prior_weight = 0.0
        off_other_efficiency_prior_weight = 0.0
        def_transition_efficiency_prior_weight = 0.0
        def_close_2_efficiency_prior_weight = 0.0
        def_long_2_efficiency_prior_weight = 0.0
        def_3_efficiency_prior_weight = 0.0
        def_other_efficiency_prior_weight = 0.0
        pace_prior_weight = 0.0

    return {
        'nonconf_multiplier': nonconf_multiplier,
        'pace_format': pace_format,
        'date_function_min': date_function_min,
        'date_function_inflexion': date_function_inflexion,
        'expected_points_weight_dunk': expected_points_weight_dunk,
        'expected_points_weight_layup': expected_points_weight_layup,
        'expected_points_weight_ft': expected_points_weight_ft,
        'expected_points_weight_long_two': expected_points_weight_long_two,
        'expected_points_weight_three': expected_points_weight_three,
        'final_score_decay': final_score_decay,
        'score_differential_shrinkage_ppp_3': score_differential_shrinkage_ppp_3,
        'score_differential_shrinkage_ppp_close_2': score_differential_shrinkage_ppp_close_2,
        'score_differential_shrinkage_ppp_long_2': score_differential_shrinkage_ppp_long_2,
        'score_differential_shrinkage_ppp_transition': score_differential_shrinkage_ppp_transition,
        'score_differential_shrinkage_pct_3': score_differential_shrinkage_pct_3,
        'score_differential_shrinkage_pct_close_2': score_differential_shrinkage_pct_close_2,
        'score_differential_shrinkage_pct_long_2': score_differential_shrinkage_pct_long_2,
        'score_differential_shrinkage_pct_to': score_differential_shrinkage_pct_to,
        'off_transition_probability_prior_weight': off_transition_probability_prior_weight,
        'off_turnover_probability_prior_weight': off_turnover_probability_prior_weight,
        'off_close_2_probability_prior_weight': off_close_2_probability_prior_weight,
        'off_long_2_probability_prior_weight': off_long_2_probability_prior_weight,
        'off_3_probability_prior_weight': off_3_probability_prior_weight,
        'off_other_probability_prior_weight': off_other_probability_prior_weight,
        'def_transition_probability_prior_weight': def_transition_probability_prior_weight,
        'def_turnover_probability_prior_weight': def_turnover_probability_prior_weight,
        'def_close_2_probability_prior_weight': def_close_2_probability_prior_weight,
        'def_long_2_probability_prior_weight': def_long_2_probability_prior_weight,
        'def_3_probability_prior_weight': def_3_probability_prior_weight,
        'def_other_probability_prior_weight': def_other_probability_prior_weight,
        'off_transition_efficiency_prior_weight': off_transition_efficiency_prior_weight,
        'off_close_2_efficiency_prior_weight': off_close_2_efficiency_prior_weight,
        'off_long_2_efficiency_prior_weight': off_long_2_efficiency_prior_weight,
        'off_3_efficiency_prior_weight': off_3_efficiency_prior_weight,
        'off_other_efficiency_prior_weight': off_other_efficiency_prior_weight,
        'def_transition_efficiency_prior_weight': def_transition_efficiency_prior_weight,
        'def_close_2_efficiency_prior_weight': def_close_2_efficiency_prior_weight,
        'def_long_2_efficiency_prior_weight': def_long_2_efficiency_prior_weight,
        'def_3_efficiency_prior_weight': def_3_efficiency_prior_weight,
        'def_other_efficiency_prior_weight': def_other_efficiency_prior_weight,
        'pace_prior_weight': pace_prior_weight
    }

def weight_function(min_w, slope, inflexion, value):
    """
    if inflexion is <= 0, then weight function returns exponential decay of slope and minimum 
    otherwise weight function returns 1 at 0, returns min_w at infinity, and returns approx MIDPOINT(1, min_w) at inflexion
    slope changes how quickly it moves from max to min

    if min_w = 1, then the variable is not changing the weight (ie it's not included in the ratings)

    returns the value of the weight function for the given min, slope, and value
    """

    if inflexion > 0:
        return ((((1 - min_w) * (1 + np.exp(-1 * slope * inflexion))) / (1 + np.exp(slope * (value - inflexion)))) + min_w)
    else:
        return np.exp(-1 * slope * value) * (1 - min_w) + min_w


# plots the given weight function values with the given x coordinates
def plot_weight_function(min_w, slope, inflexion, xs):
    """
    Returns a plot of the weight function using the given params
    """
    ys = []
    for x in xs:
        ys.append(weight_function(min_w, slope, inflexion, x))
    plot_df = pd.DataFrame({'x': xs, 'y': ys})
    return (ggplot(plot_df, aes(x = 'x', y = 'y')) + geom_line())

# function to return a realistic slope for the given minimum and inflexion
def get_slope(min_w, inflexion):
    """
    Returns an appropriate slope for the weight function using the given minimum weight and inflexion point
    """
    return 0.5


def adjust_expected_points_for_oreb_prob(pbp_df, tol = 0.001):
    """
    Adjusts the expected points in the given pbp data so that the expected points is unbiased towards
    the result points (max difference is the given tolerance). 
    Only adjusts shots that were made (offensive team could have rebounded the ball).
    """

    # only adjusting made shots (for free throws, has to be the last one of non-deadball free throws)
    to_adj = (
        (
            (
                pbp_df['shot_type'] != 'Free Throw'
            ) | (
                (pbp_df['last_free_throw']) & (~pbp_df['free_throw_source'].isin(['Tech', 'Intentional', 'Flagrant']))
            )
        ) & (pbp_df['event_type'] == 'Made Shot')
    )

    # avg miss probability per season and shot
    avg_miss_prob = pbp_df[to_adj].groupby(['shot_type', 'season'])['miss_prob'].mean().reset_index()

    # calculate number of shots per shot and season
    totals = pbp_df.groupby(['shot_type', 'season']).size().reset_index()
    totals.columns = ['shot_type', 'season', 'total']

    # calculate the number of shots we should be adjusting
    num_adj = pbp_df[to_adj].groupby(['shot_type', 'season']).size().reset_index()
    num_adj.columns = ['shot_type', 'season', 'num_adj']

    # start the adjustment while loop
    need_to_adj = True
    while need_to_adj:

        # calculate average expected points and result points per season, shot
        avgs = pbp_df.groupby(['shot_type', 'season'])[['expected_points', 'result_points']].mean().reset_index()

        # merge each of the calclations
        agg = avgs.merge(
            totals, on = ['shot_type', 'season']
        ).merge(
            num_adj, on = ['shot_type', 'season']
        ).merge(
            avg_miss_prob, on = ['shot_type', 'season']
        )

        # calculate the adjustment as the difference we need to close multiplied by the total number of shots divided by the number we can actual adjust divided by the average miss probability
        agg['adj'] = (agg['result_points'] - agg['expected_points']).mul(agg['total'].div(agg['num_adj'])).div(agg['miss_prob'])

        # merge the adjustment with the play by play data
        pbp_df = pd.merge(pbp_df, agg[['season', 'shot_type', 'adj']], on = ['season', 'shot_type'], how = 'left')
        
        # make the adjustments of all rows we do not want to adjust 0
        pbp_df.loc[pbp_df['adj'] != pbp_df['adj'], 'adj'] = 0
        pbp_df.loc[~to_adj, 'adj'] = 0

        # adjust the expected points by adding the adjustment times the miss probability of the shot
        pbp_df['expected_points'] = pbp_df['expected_points'] + pbp_df['adj'].mul(pbp_df['miss_prob'])

        # drop the adj column so we can adjust again in the while loop
        pbp_df = pbp_df.drop(columns = ['adj'])

        # again, calculate average expected points and result points per season, shot
        avgs = pbp_df.groupby(['shot_type', 'season'])[['expected_points', 'result_points']].mean().reset_index()
        avgs['diff'] = abs(avgs['expected_points'] - avgs['result_points'])

        # stop adjusting if the max difference is less than the tolerance
        if max(avgs['diff']) < tol:
            need_to_adj = False

    return pbp_df

# TODO: filter out tech free throws
def get_poss_df(pbp_df, params, season = None):
    """
    Transforms the Play-By-Play data into possession data using the given params
    """

    # use all season if param isn't passed, otherwise use given season only
    # also adjusting expected points for offensive rebounds in this step
    if season is None:
        pbp_filter_df = adjust_expected_points_for_oreb_prob(pbp_df.copy())
    else:
        pbp_filter_df = adjust_expected_points_for_oreb_prob(pbp_df[pbp_df['season'] == season])

    # create a column for how much we want to weight each shot type's expected points
    pbp_filter_df['expected_weight'] = 0
    pbp_filter_df.loc[pbp_filter_df['shot_type'] == 'Dunk', 'expected_weight'] = params['expected_points_weight_dunk']
    pbp_filter_df.loc[pbp_filter_df['shot_type'] == 'Layup', 'expected_weight'] = params['expected_points_weight_layup']
    pbp_filter_df.loc[pbp_filter_df['shot_type'] == 'Free Throw', 'expected_weight'] = params['expected_points_weight_ft']
    pbp_filter_df.loc[pbp_filter_df['shot_type'] == 'Long Two', 'expected_weight'] = params['expected_points_weight_long_two']
    pbp_filter_df.loc[pbp_filter_df['shot_type'] == 'Three', 'expected_weight'] = params['expected_points_weight_three']

    # calculate a weighted average of the result points and expected points
    pbp_filter_df['final_points'] = (
        pbp_filter_df['result_points'].mul(1 - pbp_filter_df['expected_weight']) +\
            pbp_filter_df['expected_points'].mul(pbp_filter_df['expected_weight'])
    )

    # find first TO or shot of possession and designate the type of the first event
    first_events = pbp_filter_df[pbp_filter_df['event_type'].isin(['Missed Shot', 'Made Shot', 'TO', 'Charge TO'])].groupby('poss_id')[['poss_id', 'event_type', 'shot_type', 'free_throw_source']].head(1)
    first_events['first_event'] = first_events['event_type']
    first_events.loc[first_events['first_event'].isin(['Missed Shot', 'Made Shot']), 'first_event'] = first_events.loc[first_events['first_event'].isin(['Missed Shot', 'Made Shot']), 'shot_type']
    first_events.loc[first_events['first_event'] == 'Free Throw', 'first_event'] = first_events.loc[first_events['first_event'] == 'Free Throw', 'free_throw_source']
    first_events.loc[first_events['first_event'] == 'Shooting 3', 'first_event'] = 'Three'
    first_events.loc[first_events['first_event'] == 'Shooting 2', 'first_event'] = 'Layup'
    first_events.loc[first_events['first_event'] == 'Charge TO', 'first_event'] = 'TO'

    # find the time of the first event (need to include fouls this time)
    first_events_time = pbp_filter_df[pbp_filter_df['event_type'].isin(['Missed Shot', 'Made Shot', 'Charge TO', 'TO', 'Shooting Foul', 'Foul', 'Intentional', 'Flagrant'])].groupby('poss_id')[['poss_id', 'before_event_seconds_remaining_shot_clock', 'season', 'event_type']].head(1)
    first_events_time['seconds_elapsed_before_first_event'] = 35 - first_events_time['before_event_seconds_remaining_shot_clock']
    first_events_time.loc[first_events_time['season'] >= 2016, 'seconds_elapsed_before_first_event'] = first_events_time.loc[first_events_time['season'] >= 2016, 'seconds_elapsed_before_first_event'] - 5
    first_events_time = first_events_time.rename(columns = {'event_type': 'first_event_time'})

    # merge together
    first_events = pd.merge(first_events[['poss_id', 'first_event']], first_events_time[['poss_id', 'seconds_elapsed_before_first_event', 'first_event_time']], how = 'inner', on = 'poss_id')
    first_events.loc[first_events['first_event_time'] == 'Foul', 'seconds_elapsed_before_first_event'] = 30.5 # dummy so that these possessions do not get classified as transition
    
    # group data by possessions
    poss_df = pbp_filter_df.groupby(
        ['season', 'game_id', 'date', 'poss_id', 'team_id_with_poss', 'previous_possession_end', 'possession_score_differential']
    ).agg(
        final_points = ('final_points', sum),
        garbage_time = ('garbage_time_indicator', max),
        foul_stage = ('foul_stage', max),
        seconds_elapsed = ('seconds_elapsed', sum)
    ).reset_index()

    # join to the first event
    poss_df = pd.merge(poss_df, first_events.drop(columns = ['first_event_time']), how = 'inner', on = 'poss_id')

    # make sure possessions that start with turnovers have 0 points
    # if this is a data error, it will be corrected later in final score decay adjustment
    poss_df.loc[poss_df['first_event'] == 'TO', 'final_points'] = 0

    # get the opponent info
    game_teams = poss_df[['game_id', 'team_id_with_poss']].drop_duplicates()
    opponents = pd.merge(game_teams, game_teams.rename(columns = {'team_id_with_poss': 'opp_id'}), how = 'inner', on = 'game_id')
    opponents = opponents[opponents['team_id_with_poss'] != opponents['opp_id']]
    poss_df = pd.merge(poss_df, opponents, how = 'left', on = ['game_id', 'team_id_with_poss'])

    # separate the possessions by class
    poss_df['class'] = np.nan
    poss_df.loc[
        (poss_df['seconds_elapsed_before_first_event'] > 0.5) \
        & (poss_df['seconds_elapsed_before_first_event'] < 7.5) \
        & (poss_df['previous_possession_end'] == 'TO'), 'class'
    ] = 'transition'
    poss_df.loc[(poss_df['class'] != poss_df['class']) & (poss_df['first_event'] == 'TO'), 'class'] = 'to'
    poss_df.loc[(poss_df['class'] != poss_df['class']) & (poss_df['first_event'].isin(['Dunk', 'Layup'])), 'class'] = 'close 2'
    poss_df.loc[(poss_df['class'] != poss_df['class']) & (poss_df['first_event'] == 'Long Two'), 'class'] = 'long 2'
    poss_df.loc[(poss_df['class'] != poss_df['class']) & (poss_df['first_event'] == 'Three'), 'class'] = '3'
    poss_df.loc[(poss_df['class'] != poss_df['class']) | (poss_df['garbage_time'] == 1) | (poss_df['foul_stage'] == 1), 'class'] = 'other'

    return poss_df


# TODO: finish
def get_hca(season, pbp_df):
    """
    """

    prev_season = season - 1

    # Skip the COVID year without fans
    if prev_season == 2021:
        prev_season = 2020

    # We don't have 2013 data
    if prev_season == 2013:
        prev_season = 2014

    return prev_season


# TODO: finish
def get_averages(season, pbp_df):
    """
    """
    return season

class SeasonRatings:
    """
    """

    def __init__(self, season, params, games_df, pbp_df, min_games_for_predictions):
        """
        """
        self.season = season
        self.params = params
        self.games_df = games_df
        
        self.poss_df = get_poss_df(pbp_df, self.params, self.season)
        self.hca = get_hca(self.season, pbp_df)
        self.averages = get_averages(self.season, pbp_df)
        
        self.min_backtest_date = str(self.season) + '-02-01'
        self.min_games_for_predictions = min_games_for_predictions
    

    # TODO: finish
    def calculate_ratings(self, date = None, use_future_games = False):
        """
        Calculates the team ratings on the given date.
        Uses the maximum date in the games if not given a date
        Uses only past games by defualt
        """

        # use max date if no date is provided as cutoff (all games will be used)
        if date is None:
            cutoff_date = max(self.games_df['Date'])

        # use May 1st of that season as cutoff (all games will be used to calculate ratings no matter what)
        elif use_future_games:
            cutoff_date = str(self.season) + '-05-01'

        # otherwise, use the previous day relative to the date you are calculating the ratings for
        else:
            cutoff_date = datetime.strftime(datetime.strptime(date, '%Y-%m-%d') - timedelta(1), '%Y-%m-%d')

        return cutoff_date

    # TODO: finish
    def predict_games(self, date_games_df, ratings_df):
        """
        Uses the given ratings to predict the results of given date games data
        """
        return ratings_df

    def date_run(self, date):
        """
        On the given date, only calculate the ratings and the day's predictions if there are sufficient games
        """

        date_games_df = self.games_df[self.games_df['Date'] == date]

        # If there are more than the min games on that day (2 rows per game)
        if len(date_games_df) >= self.min_games_for_predictions * 2:
            ratings_df = self.calculate_ratings(date)

            return self.predict_games(date_games_df, ratings_df)

        else:
            return pd.DataFrame()

    
    def backtest(self):
        """
        Over each date in the data that's after the minimum backtest date, calculate the ratings and predict the day's games
        """

        # filter games for the games after the minimum backtest date
        backtest_games_df = self.games_df[self.games_df['Date'] >= self.min_backtest_date]
        
        predict_df = pd.DataFrame()

        # For each day in the dataset, do a run of the ratings on that date
        for date in backtest_games_df['Date'].unique():
            date_predict_df = self.date_run(date)

            predict_df = pd.concat([predict_df, date_predict_df])

        return predict_df

    def predict_future_games(self, future_df):
        """
        Use the current ratings to predict the given future games (as if they were played today)
        """
        return future_df

            


def get_backtest_predictions(season, params, games_df, pbp_df):
    """
    Runs a backtest of the given season's ratings using the given params and game data

    Returns a dataframe of game predictions
    """
    temp_season = SeasonRatings(season, params, games_df, pbp_df, 30)
    return temp_season.backtest()

def get_current_ratings(season, params, games_df, pbp_df):
    """
    Gets the current ratings
    """
    temp_season = SeasonRatings(season, params, games_df, pbp_df, 0)
    return temp_season.calculate_ratings()

def get_future_predictions(season, params, games_df, pbp_df, future_df):
    """
    Predicts the game results of the given future games data using the given params and game data
    """
    temp_season = SeasonRatings(season, params, games_df, pbp_df, 0)
    return temp_season.predict_future_games(future_df)

def compile_predictions(predictions):
    """
    Somehting to do with the Pooling
    """
    return pd.DataFrame()