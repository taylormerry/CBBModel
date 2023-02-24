import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

def fill_nulls(row):

    game_id = row['game_id']

    if game_id == 400816789:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2031
        row['home_score'] = 81
        row['away_id'] = 2026
        row['away_score'] = 55
        row['status_type_detail'] = 'Final'
    elif game_id == 400816829:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 526
        row['home_score'] = 82
        row['away_id'] = 2885
        row['away_score'] = 78
        row['status_type_detail'] = 'Final/OT'
    elif game_id == 400816848:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2653
        row['home_score'] = 63
        row['away_id'] = 250
        row['away_score'] = 90
        row['status_type_detail'] = 'Final'
    elif game_id == 400816878:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 6
        row['home_score'] = 67
        row['away_id'] = 326
        row['away_score'] = 78
        row['status_type_detail'] = 'Final'
    elif game_id == 400816910:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 290
        row['home_score'] = 65
        row['away_id'] = 309
        row['away_score'] = 74
        row['status_type_detail'] = 'Final'
    elif game_id == 400816921:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2247
        row['home_score'] = 65
        row['away_id'] = 2433
        row['away_score'] = 51
        row['status_type_detail'] = 'Final'
    elif game_id == 400817003:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2458
        row['home_score'] = 66
        row['away_id'] = 149
        row['away_score'] = 73
        row['status_type_detail'] = 'Final'
    elif game_id == 400817488:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 16
        row['home_score'] = 82
        row['away_id'] = 304
        row['away_score'] = 71
        row['status_type_detail'] = 'Final'
    elif game_id == 400820694:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 155
        row['home_score'] = 85
        row['away_id'] = 147
        row['away_score'] = 68
        row['status_type_detail'] = 'Final'
    elif game_id == 400824541:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 236
        row['home_score'] = 77
        row['away_id'] = 2717
        row['away_score'] = 58
        row['status_type_detail'] = 'Final'
    elif game_id == 400827836:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 70
        row['home_score'] = 83
        row['away_id'] = 2464
        row['away_score'] = 76
        row['status_type_detail'] = 'Final'
    elif game_id == 400830143:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2351
        row['home_score'] = 83
        row['away_id'] = 2539
        row['away_score'] = 87
        row['status_type_detail'] = 'Final'
    elif game_id == 400830168:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2250
        row['home_score'] = 68
        row['away_id'] = 252
        row['away_score'] = 69
        row['status_type_detail'] = 'Final'
    elif game_id == 400830191:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2541
        row['home_score'] = 62
        row['away_id'] = 2492
        row['away_score'] = 60
        row['status_type_detail'] = 'Final'
    elif game_id == 400830510:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 294
        row['home_score'] = 83
        row['away_id'] = 338
        row['away_score'] = 70
        row['status_type_detail'] = 'Final'
    elif game_id == 400830534:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2454
        row['home_score'] = 95
        row['away_id'] = 288
        row['away_score'] = 83
        row['status_type_detail'] = 'Final'
    elif game_id == 400830563:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 331
        row['home_score'] = 106
        row['away_id'] = 253
        row['away_score'] = 80
        row['status_type_detail'] = 'Final'
    elif game_id == 400830597:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2502
        row['home_score'] = 58
        row['away_id'] = 2692
        row['away_score'] = 73
        row['status_type_detail'] = 'Final'
    elif game_id == 400830817:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 242
        row['home_score'] = 83
        row['away_id'] = 98
        row['away_score'] = 73
        row['status_type_detail'] = 'Final'
    elif game_id == 400833117:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 48
        row['home_score'] = 77
        row['away_id'] = 119
        row['away_score'] = 79
        row['status_type_detail'] = 'Final'
    elif game_id == 400833264:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2275
        row['home_score'] = 69
        row['away_id'] = 2182
        row['away_score'] = 61
        row['status_type_detail'] = 'Final'
    elif game_id == 400833360:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 111
        row['home_score'] = 63
        row['away_id'] = 256
        row['away_score'] = 75
        row['status_type_detail'] = 'Final'
    elif game_id == 400833393:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2127
        row['home_score'] = 64
        row['away_id'] = 2335
        row['away_score'] = 63
        row['status_type_detail'] = 'Final'
    elif game_id == 400835229:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 202
        row['home_score'] = 60
        row['away_id'] = 41
        row['away_score'] = 51
        row['status_type_detail'] = 'Final'
    elif game_id == 400835599:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2097
        row['home_score'] = 57
        row['away_id'] = 2344
        row['away_score'] = 74
        row['status_type_detail'] = 'Final'
    elif game_id == 400835618:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 13
        row['home_score'] = 73
        row['away_id'] = 2540
        row['away_score'] = 76
        row['status_type_detail'] = 'Final'
    elif game_id == 400839134:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2515
        row['home_score'] = 91
        row['away_id'] = 2427
        row['away_score'] = 86
        row['status_type_detail'] = 'Final/OT'
    elif game_id == 400839219:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 97
        row['home_score'] = 59
        row['away_id'] = 221
        row['away_score'] = 41
        row['status_type_detail'] = 'Final'
    elif game_id == 400839303:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 127
        row['home_score'] = 59
        row['away_id'] = 2294
        row['away_score'] = 76
        row['status_type_detail'] = 'Final'
    elif game_id == 400839829:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2750
        row['home_score'] = 70
        row['away_id'] = 325
        row['away_score'] = 53
        row['status_type_detail'] = 'Final'
    elif game_id == 400840010:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 166
        row['home_score'] = 65
        row['away_id'] = 140
        row['away_score'] = 64
        row['status_type_detail'] = 'Final'
    elif game_id == 400840113:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2501
        row['home_score'] = 71
        row['away_id'] = 301
        row['away_score'] = 82
        row['status_type_detail'] = 'Final'
    elif game_id == 400840797:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2057
        row['home_score'] = 81
        row['away_id'] = 93
        row['away_score'] = 73
        row['status_type_detail'] = 'Final'
    elif game_id == 400840818:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2737
        row['home_score'] = 86
        row['away_id'] = 2272
        row['away_score'] = 66
        row['status_type_detail'] = 'Final'
    elif game_id == 400841180:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2210
        row['home_score'] = 82
        row['away_id'] = 350
        row['away_score'] = 91
        row['status_type_detail'] = 'Final'
    elif game_id == 400841222:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 56
        row['home_score'] = 89
        row['away_id'] = 2908
        row['away_score'] = 86
        row['status_type_detail'] = 'Final/OT'
    elif game_id == 400841232:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2429
        row['home_score'] = 72
        row['away_id'] = 2393
        row['away_score'] = 73
        row['status_type_detail'] = 'Final'
    elif game_id == 400841254:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2226
        row['home_score'] = 58
        row['away_id'] = 2572
        row['away_score'] = 51
        row['status_type_detail'] = 'Final'
    elif game_id == 400841275:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2229
        row['home_score'] = 88
        row['away_id'] = 2348
        row['away_score'] = 74
        row['status_type_detail'] = 'Final'
    elif game_id == 400841291:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 12
        row['home_score'] = 99
        row['away_id'] = 264
        row['away_score'] = 67
        row['status_type_detail'] = 'Final'
    elif game_id == 400841317:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 24
        row['home_score'] = 77
        row['away_id'] = 25
        row['away_score'] = 71
        row['status_type_detail'] = 'Final'
    elif game_id == 400841549:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 302
        row['home_score'] = 63
        row['away_id'] = 2463
        row['away_score'] = 62
        row['status_type_detail'] = 'Final'
    elif game_id == 400841703:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 249
        row['home_score'] = 78
        row['away_id'] = 276
        row['away_score'] = 97
        row['status_type_detail'] = 'Final'
    elif game_id == 400841717:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 295
        row['home_score'] = 71
        row['away_id'] = 5
        row['away_score'] = 72
        row['status_type_detail'] = 'Final/OT'
    elif game_id == 400841994:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2710
        row['home_score'] = 69
        row['away_id'] = 2172
        row['away_score'] = 76
        row['status_type_detail'] = 'Final'
    elif game_id == 400842045:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2520
        row['home_score'] = 102
        row['away_id'] = 2368
        row['away_score'] = 100
        row['status_type_detail'] = 'Final/2OT'
    elif game_id == 400843526:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 82
        row['home_score'] = 76
        row['away_id'] = 2739
        row['away_score'] = 78
        row['status_type_detail'] = 'Final'
    elif game_id == 400843559:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 94
        row['home_score'] = 84
        row['away_id'] = 2754
        row['away_score'] = 64
        row['status_type_detail'] = 'Final'
    elif game_id == 400844030:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2608
        row['home_score'] = 78
        row['away_id'] = 279
        row['away_score'] = 62
        row['status_type_detail'] = 'Final'
    elif game_id == 400844054:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 9
        row['home_score'] = 84
        row['away_id'] = 265
        row['away_score'] = 73
        row['status_type_detail'] = 'Final'
    elif game_id == 400844055:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 254
        row['home_score'] = 59
        row['away_id'] = 2483
        row['away_score'] = 77
        row['status_type_detail'] = 'Final'
    elif game_id == 400844291:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2803
        row['home_score'] = 61
        row['away_id'] = 2597
        row['away_score'] = 59
        row['status_type_detail'] = 'Final'
    elif game_id == 400844315:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2523
        row['home_score'] = 52
        row['away_id'] = 116
        row['away_score'] = 76
        row['status_type_detail'] = 'Final'
    elif game_id == 400844337:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 324
        row['home_score'] = 87
        row['away_id'] = 2506
        row['away_score'] = 58
        row['status_type_detail'] = 'Final'
    elif game_id == 400844891:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2115
        row['home_score'] = 78
        row['away_id'] = 2529
        row['away_score'] = 80
        row['status_type_detail'] = 'Final/OT'
    elif game_id == 400844921:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2643
        row['home_score'] = 83
        row['away_id'] = 2747
        row['away_score'] = 86
        row['status_type_detail'] = 'Final'
    elif game_id == 400844944:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2535
        row['home_score'] = 77
        row['away_id'] = 2193
        row['away_score'] = 81
        row['status_type_detail'] = 'Final'
    elif game_id == 400844961:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2382
        row['home_score'] = 69
        row['away_id'] = 231
        row['away_score'] = 65
        row['status_type_detail'] = 'Final'
    elif game_id == 400845072:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2598
        row['home_score'] = 59
        row['away_id'] = 161
        row['away_score'] = 71
        row['status_type_detail'] = 'Final'
    elif game_id == 400845086:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2681
        row['home_score'] = 70
        row['away_id'] = 112358
        row['away_score'] = 71
        row['status_type_detail'] = 'Final'
    elif game_id == 400845479:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2634
        row['home_score'] = 66
        row['away_id'] = 2046
        row['away_score'] = 52
        row['status_type_detail'] = 'Final'
    elif game_id == 400845518:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2197
        row['home_score'] = 97
        row['away_id'] = 2198
        row['away_score'] = 85
        row['status_type_detail'] = 'Final'
    elif game_id == 400845563:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2565
        row['home_score'] = 67
        row['away_id'] = 2413
        row['away_score'] = 70
        row['status_type_detail'] = 'Final/OT'
    elif game_id == 400846777:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 292
        row['home_score'] = 82
        row['away_id'] = 2130
        row['away_score'] = 72
        row['status_type_detail'] = 'Final'
    elif game_id == 400847124:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2571
        row['home_score'] = 92
        row['away_id'] = 2870
        row['away_score'] = 76
        row['status_type_detail'] = 'Final'
    elif game_id == 400847203:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 2674
        row['home_score'] = 68
        row['away_id'] = 270
        row['away_score'] = 56
        row['status_type_detail'] = 'Final'
    elif game_id == 400847272:
        row['date'] = '2016-01-14'
        row['season'] = 2016
        row['neutral_site'] = False
        row['home_id'] = 85
        row['home_score'] = 71
        row['away_id'] = 198
        row['away_score'] = 80
        row['status_type_detail'] = 'Final'
    
    return row



# read in hoopR CSVs (which came from R)
games = pd.read_csv('games.csv', encoding='latin-1')
box = pd.read_csv('box.csv', encoding='latin-1')
pbp = pd.read_csv('pbp.csv', encoding='latin-1')

box['team_poss'] = box['field_goals_made_field_goals_attempted'].str.split('-').str[1].astype(int) \
                    + box['turnovers'] \
                    + 0.47 * box['free_throws_made_free_throws_attempted'].str.split('-').str[1].astype(int) \
                    - box['offensive_rebounds']
box = box[['game_id', 'team_id', 'opponent_id', 'team_poss', 'team_short_display_name', 'opponent_name']]

box_self = pd.merge(box, box.rename(columns = {'team_poss': 'opp_poss'}), how = 'inner', 
                    left_on = ['game_id', 'team_id', 'opponent_id'], right_on = ['game_id', 'opponent_id', 'team_id'])
box_self = box_self[['game_id', 'team_id_x', 'team_short_display_name_x', 'opponent_id_x', 'opponent_name_x', 'team_poss', 'opp_poss']]

merge = pd.merge(box_self, games, how = 'outer', on = 'game_id')

merge = merge.apply(fill_nulls, axis = 1)

merge = merge[(merge['date'] == merge['date']) & (merge['team_id_x'] == merge['team_id_x'])]

confs = merge[merge['home_conference_id'] == merge['home_conference_id']][['home_id', 'home_conference_id', 'season']].drop_duplicates()

teams = merge[merge['team_short_display_name_x'] == merge['team_short_display_name_x']]\
            .groupby(['team_id_x'])['team_short_display_name_x']\
            .max()\
            .reset_index()

merge = pd.merge(merge, confs, how = 'left', on = ['home_id', 'season'])
merge = pd.merge(merge, confs.rename(columns = {'home_id': 'away_id', 'home_conference_id': 'away_conference_id'}), how = 'left', on = ['away_id', 'season'])


merge['away_conference_id'] = merge['away_conference_id_y'].combine_first(merge['away_conference_id_x'])
merge['home_conference_id'] = merge['home_conference_id_y'].combine_first(merge['home_conference_id_x'])

merge = pd.merge(merge, teams, how = 'left', on = ['team_id_x'])
merge = pd.merge(merge, teams.rename(columns = {'team_id_x': 'opponent_id_x', 'team_short_display_name_x': 'opponent_name_x'}), how = 'left', on = ['opponent_id_x'])

merge['team_name'] = merge['team_short_display_name_x_y'].combine_first(merge['team_short_display_name_x_x'])
merge['opp_name'] = merge['opponent_name_x_y'].combine_first(merge['opponent_name_x_x'])

def get_location(row):
    if row['neutral_site']:
        return 'N'
    elif row['team_id_x'] == row['home_id']:
        return 'H'
    elif row['team_id_x'] == row['away_id']:
        return 'A'
    else:
        return np.nan
merge['location'] = merge.apply(get_location, axis = 1)

merge['team_score'] = merge['home_score']
merge['opp_score'] = merge['away_score']
merge.loc[merge['team_id_x'] == merge['away_id'], 'team_score'] = merge.loc[merge['team_id_x'] == merge['away_id'], 'away_score']
merge.loc[merge['team_id_x'] == merge['away_id'], 'opp_score'] = merge.loc[merge['team_id_x'] == merge['away_id'], 'home_score']


merge['date'] = merge['date'].str[:10]

selection_sundays = pd.DataFrame({
    'season': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'selection_sunday': ['2014-03-16',
                            '2015-03-15',
                            '2016-03-13',
                            '2017-03-12',
                            '2018-03-11',
                            '2019-03-17',
                            '2020-03-15',
                            '2021-03-14',
                            '2022-03-13']
})
merge = pd.merge(merge, selection_sundays, how = 'left', on = ['season'])

def get_postseason(row):
    if row['date'] > row['selection_sunday']:
        return 1
    else:
        return 0
merge['postseason'] = merge.apply(get_postseason, axis = 1)

def get_noncon(row):
    if row['away_conference_id'] == row['home_conference_id']:
        return 0
    else:
        return 1
merge['noncon'] = merge.apply(get_noncon, axis = 1)

def get_min(row):
    detail = row['status_type_detail']
    if detail == 'Final':
        return 40
    elif detail == 'Final/OT':
        return 45
    else:
        num_ots = int(''.join(c for c in detail if c.isdigit()))
        return 40 + 5 * num_ots
merge['minutes'] = merge.apply(get_min, axis = 1)

merge.rename(
    columns = {
        'team_id_x': 'team_id',
        'opponent_id_x': 'opp_id'
    }
)[['game_id', 'date', 'season', 'location', 'venue_full_name', 'venue_id', 'noncon', 'postseason', 'minutes', \
    'team_id', 'opp_id', 'team_name', 'opp_name', 'home_conference_id', 'home_id',\
    'team_poss', 'opp_poss', 'team_score', 'opp_score']].to_csv('games_clean.csv', index = False)

pbp['clock'] = 1200 - (pbp['clock_minutes'] * 60 + pbp['clock_seconds'])
pbp['index'] = pbp.reset_index(drop = True).index
pbp = pbp.sort_values(['game_id', 'period', 'clock', 'index']).reset_index(drop = True)

# adds a unique ID column
pbp['temp'] = 1
pbp['temp_cumsum'] = pbp.groupby('game_id')['temp'].cumsum()
pbp['temp_cumsum_str'] = pbp['temp_cumsum'].astype('str')
pbp.loc[pbp['temp_cumsum'] < 1000, 'temp_cumsum_str'] = '0' + pbp.loc[pbp['temp_cumsum'] < 1000, 'temp_cumsum_str']
pbp.loc[pbp['temp_cumsum'] < 100, 'temp_cumsum_str'] = '0' + pbp.loc[pbp['temp_cumsum'] < 100, 'temp_cumsum_str']
pbp.loc[pbp['temp_cumsum'] < 10, 'temp_cumsum_str'] = '0' + pbp.loc[pbp['temp_cumsum'] < 10, 'temp_cumsum_str']
pbp['id'] = (pbp['game_id'].astype(str) + pbp['temp_cumsum_str']).astype(float)

# removes games that are missing info from one team
num_teams = pbp.groupby('game_id')['team_id'].nunique().reset_index().rename(columns = {'team_id': 'num_teams'})
pbp = pd.merge(num_teams[num_teams['num_teams'] == 2], pbp, how = 'inner', on = 'game_id')

pbp['home_previous_score'] = pbp.groupby('game_id')['home_score'].shift(1)
pbp['away_previous_score'] = pbp.groupby('game_id')['away_score'].shift(1)
pbp['score'] = pbp['home_score']
pbp['previous_score'] = pbp['home_previous_score']
pbp.loc[pbp['team_id'] == pbp['away_team_id'], 'score'] = pbp.loc[pbp['team_id'] == pbp['away_team_id'], 'away_score']
pbp.loc[pbp['team_id'] == pbp['away_team_id'], 'previous_score'] = pbp.loc[pbp['team_id'] == pbp['away_team_id'], 'away_previous_score']

# removes duplicated plays by takign the min ID
group_cols = ['text', 'game_id', 'team_id', 'clock_minutes', 'clock_seconds', 'period']
keep_cols = ['id', 'text', 'participants_0_athlete_id', 'home_score', 'away_score', 'score', 'previous_score', 'game_id', 'home_team_id',
                'away_team_id', 'team_id', 'clock_minutes', 'clock_seconds', 'period', 
                'participants_1_athlete_id', 'coordinate_x', 'coordinate_y']
pbp_ids = pbp.groupby(group_cols, dropna=False)['id'].min().reset_index()
pbp_ids['keep'] = True
pbp = pd.merge(pbp[keep_cols], pbp_ids[['id', 'keep']], how = 'left', on = ['id'])
pbp.loc[pbp['keep'] != pbp['keep'], 'keep'] = False
# keep free throws, because those could actually be duplicated
# but only keep two of the missed free throws and one of the made free throws (makes could still be duplicated with different scores)
pbp['occurrence'] = 1
pbp['num_of_occurrence'] = pbp.groupby(group_cols + ['score'])['occurrence'].cumsum()
pbp = pbp[(pbp['keep']) | (((pbp['num_of_occurrence'] <= 2) & (pbp['text'].astype(str).str.contains('missed Free Throw'))) | ((pbp['text'].astype(str).str.contains('made Free Throw')) & (pbp['num_of_occurrence'] == 1)))]

# ID potential made free throw duplicates
pbp['duplicate'] = pbp[group_cols].duplicated(keep = False)
pbp['potential_duplicate'] = False 
pbp.loc[(pbp['duplicate']) \
        & (pbp['text'].astype(str).str.contains('made Free Throw'))  \
        & (((pbp['team_id'] == pbp['away_team_id']) & ((pbp['away_score'] != pbp['away_score'].shift(1) + 1) | (pbp['home_score'] != pbp['home_score'].shift(1)))) \
            | ((pbp['team_id'] == pbp['home_team_id']) & ((pbp['home_score'] != pbp['home_score'].shift(1) + 1) | (pbp['away_score'] != pbp['away_score'].shift(1))))), 'potential_duplicate'] = True
pbp.loc[(pbp['duplicate']) \
        & (pbp['text'].astype(str).str.contains('made Free Throw'))  \
        & (((pbp['team_id'] == pbp['away_team_id']) & (pbp['away_score'] == pbp['away_score'].shift(-1) + 1)) \
            | ((pbp['team_id'] == pbp['home_team_id']) & (pbp['home_score'] == pbp['home_score'].shift(-1) + 1))), 'potential_duplicate'] = True

# removes games with less than 100 play entries in one half or with > 65% of entries to one team in one half
team_counts = pbp[pbp['period'] < 3].groupby(['game_id', 'team_id', 'period'])['id'].count().reset_index().rename(columns = {'id': 'team_count'})
game_counts = pbp[pbp['period'] < 3].groupby(['game_id', 'period'])['id'].count().reset_index().rename(columns = {'id': 'game_count'})
merge_counts = pd.merge(game_counts, team_counts, how = 'inner', on = ['game_id', 'period'])
merge_counts['team_pct'] = merge_counts['team_count'].div(merge_counts['game_count'])
remove_due_to_count = merge_counts[(merge_counts['team_pct'] > 0.65) | (merge_counts['game_count'] < 100)][['game_id']].drop_duplicates()
remove_due_to_count['remove'] = 1
pbp = pd.merge(pbp, remove_due_to_count, how = 'left', on = 'game_id')
pbp = pbp[pbp['remove'] != pbp['remove']]


# remakes the IDs now that we've removed some duplicates to reduce the size of the float
pbp['temp'] = 1
pbp['temp_cumsum'] = pbp.groupby('game_id')['temp'].cumsum()
pbp['temp_cumsum_str'] = pbp['temp_cumsum'].astype('str')
pbp.loc[pbp['temp_cumsum'] < 100, 'temp_cumsum_str'] = '0' + pbp.loc[pbp['temp_cumsum'] < 100, 'temp_cumsum_str']
pbp.loc[pbp['temp_cumsum'] < 10, 'temp_cumsum_str'] = '0' + pbp.loc[pbp['temp_cumsum'] < 10, 'temp_cumsum_str']
pbp['id'] = (pbp['game_id'].astype(str) + pbp['temp_cumsum_str']).astype(float)

# Not sure why this possession text was so weird
pbp.loc[pbp['text'] == 'BILLY CLARK GETS BUCKETS', 'text'] = 'Bill Clark made Three Point Jumper.'

# Not sure why these entries clocks were wrong
pbp.loc[(pbp['clock_minutes'] == 29) & (pbp['clock_seconds'] == 46), 'clock_minutes'] = 19
pbp = pbp[pbp['clock_minutes'] <= 20]

pbp['event_team'] = np.nan
pbp.loc[pbp['team_id'] == pbp['home_team_id'], 'event_team'] = 'Home'
pbp.loc[pbp['team_id'] == pbp['away_team_id'], 'event_team'] = 'Away'
pbp['event_team'] = pbp['event_team'].fillna(pbp['event_team'].shift(1)).fillna(pbp['event_team'].shift(2)).fillna(pbp['event_team'].shift(3))

text = pbp['text'].astype(str)

# these seem like they're missing because ESPN classified it as an end of half
pbp.loc[text == 'Christian James made Three Point Jumper. Assisted by Aaron Calixte. End of 1st half', 'participants_0_athlete_id'] = 3924876.0
pbp.loc[text == 'Christian James made Three Point Jumper. Assisted by Aaron Calixte. End of 1st half', 'team_id'] = 2306

pbp['event_type'] = 'Unknown'

pbp.loc[(text.str.endswith(' Turnover.') | text.str.contains(' Turnover')), 'event_type'] = 'TO'
pbp.loc[(text.str.startswith('Jump Ball')), 'event_type'] = 'Jump'
pbp.loc[(text.str.endswith('Steal.')), 'event_type'] = 'STL'
pbp.loc[(text.str.endswith('Block.') & (~text.str.contains('Assisted'))), 'event_type'] = 'BLK'
pbp.loc[(text.str.startswith('Foul on ')), 'event_type'] = 'Foul'
pbp.loc[((text.str.contains('Technical Foul')) | (text.str.contains('Technical foul')) | (text.str.contains('technical foul'))), 'event_type'] = 'Tech'
pbp.loc[(text.str.contains('Flagrant') | text.str.contains('Flagrent') | text.str.contains('flagrant') | text.str.contains('Flagratn')), 'event_type'] = 'Flagrant'
pbp.loc[(text.str.contains('Intentional')), 'event_type'] = 'Intentional'
pbp.loc[(text.str.contains('Timeout')), 'event_type'] = 'Timeout'
pbp.loc[(text.str.contains('DELAY')), 'event_type'] = 'Delay'
pbp.loc[(text.str.startswith('End of ')), 'event_type'] = 'Half'
pbp.loc[(((text.str.startswith('Alternating possession ')) | text.str.contains('alternating possession'))), 'event_type'] = 'Poss'
pbp.loc[(text.str.contains('Ejected') | text.str.contains('ejected')), 'event_type'] = 'Ejection'
pbp.loc[(text.str.contains('Offensive Rebound')), 'event_type'] = 'OREB'
pbp.loc[(text.str.contains('Defensive Rebound')), 'event_type'] = 'DREB'
pbp.loc[(text.str.contains(' Deadball Team Rebound')), 'event_type'] = 'Deadball Rebound'
pbp.loc[(text.str.contains(' own basket')), 'event_type'] = 'Own'
pbp.loc[((text.str.contains(' missed ')) | (text.str.startswith('missed ')) | (text.str.endswith(' missed'))), 'event_type'] = 'Missed Shot'
pbp.loc[(text.str.contains(' made ')) | (text.str.startswith('made')), 'event_type'] = 'Made Shot'

pbp['shooting_player_id'] = np.nan
pbp.loc[(pbp['event_type'] == 'Made Shot') | (pbp['event_type'] == 'Missed Shot'), 'shooting_player_id'] = pbp.loc[(pbp['event_type'] == 'Made Shot') | (pbp['event_type'] == 'Missed Shot'), 'participants_0_athlete_id']

pbp['shooting_text'] = np.nan
pbp.loc[text.str.contains(' made '), 'shooting_text'] = pbp.loc[text.str.contains(' made '), 'text'].astype(str).str.split(' made ').str[1].str.split('.').str[0]
pbp.loc[text.str.startswith('made'), 'shooting_text'] = pbp.loc[text.str.startswith('made'), 'text'].astype(str).str.split('made ').str[1].str.split('.').str[0]
pbp.loc[text.str.contains(' missed '), 'shooting_text'] = pbp.loc[text.str.contains(' missed '), 'text'].astype(str).str.split(' missed ').str[1].str.split('.').str[0]
pbp.loc[text.str.startswith('missed'), 'shooting_text'] = pbp.loc[text.str.startswith('missed'), 'text'].astype(str).str.split('missed ').str[1].str.split('.').str[0]

pbp['shot_type'] = np.nan
pbp.loc[(pbp['event_type'] == 'Made Shot') | (pbp['event_type'] == 'Missed Shot'), 'shot_type'] = 'Unknown'
pbp.loc[pbp['shooting_text'].isin(['Three Point Jumper', 'three point jumper', '62-foot Three Point Jumper', 'Three Point Jumper (Petty leaves game with injury - Alabama has 3 available players)']), 'shot_type'] = 'Three'
pbp.loc[pbp['shooting_text'].isin(['Jumper', 'jumper', 'Two Point Jumper']), 'shot_type'] = 'Long Two'
pbp.loc[pbp['shooting_text'].isin(['Layup', 'Two Point Tip Shot', 'layup', 'putback', 'Tip-in']), 'shot_type'] = 'Layup'
pbp.loc[pbp['shooting_text'].isin(['Dunk', 'Two Point Dunk']), 'shot_type'] = 'Dunk'
pbp.loc[pbp['shooting_text'].isin(['Free Throw', 'free throw', 'two Free Throws', '2 Free Throws']), 'shot_type'] = 'Free Throw'

# whether or not the shot was made
pbp['made'] = np.nan
pbp.loc[pbp['event_type'] == 'Missed Shot', 'made'] = 0
pbp.loc[pbp['event_type'] == 'Made Shot', 'made'] = 1

pbp['previous_home_score'] = pbp.groupby('game_id')['home_score'].shift(1)
pbp['previous_away_score'] = pbp.groupby('game_id')['away_score'].shift(1)

pbp['result_points'] = 0
pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] == 'Free Throw'), 'result_points'] = 1
pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'].isin(['Long Two', 'Dunk', 'Layup'])), 'result_points'] = 2
pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] == 'Three'), 'result_points'] = 3
pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] == 'Unknown') & (pbp['team_id'] == pbp['home_team_id']), 'result_points'] = pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] == 'Unknown') & (pbp['team_id'] == pbp['home_team_id']), 'home_score'] - pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] == 'Unknown') & (pbp['team_id'] == pbp['home_team_id']), 'previous_home_score']
pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] == 'Unknown') & (pbp['team_id'] == pbp['away_team_id']), 'result_points'] = pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] == 'Unknown') & (pbp['team_id'] == pbp['away_team_id']), 'away_score'] - pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] == 'Unknown') & (pbp['team_id'] == pbp['away_team_id']), 'previous_away_score']

pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] == 'Unknown') & (pbp['result_points'] == 1), 'shot_type'] = 'Free Throw'
pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] == 'Unknown') & (pbp['result_points'] == 2), 'shot_type'] = 'Layup'
pbp.loc[(pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] == 'Unknown') & (pbp['result_points'] == 3), 'shot_type'] = 'Three'

pbp['home_result_points'] = 0
pbp.loc[pbp['team_id'] == pbp['home_team_id'], 'home_result_points'] = pbp.loc[pbp['team_id'] == pbp['home_team_id'], 'result_points']
pbp['away_result_points'] = 0
pbp.loc[pbp['team_id'] == pbp['away_team_id'], 'away_result_points'] = pbp.loc[pbp['team_id'] == pbp['away_team_id'], 'result_points']

pbp['home_result_score'] = pbp.groupby('game_id')['home_result_points'].cumsum()
pbp['away_result_score'] = pbp.groupby('game_id')['away_result_points'].cumsum()

pbp['score_differential'] = pbp['home_result_score'] - pbp['away_result_score']
pbp.loc[(pbp['team_id'] == pbp['away_team_id']), 'score_differential'] = -1 * pbp.loc[(pbp['team_id'] == pbp['away_team_id']), 'score_differential']

pbp.loc[(pbp['text'].astype(str).str.lower().str.contains('two free throws')) | (pbp['text'].astype(str).str.lower().str.contains('2 free throws')), 'result_points'] = 2 * pbp.loc[(pbp['text'].astype(str).str.lower().str.contains('two free throws')) | (pbp['text'].astype(str).str.lower().str.contains('2 free throws')), 'result_points']

pbp['seconds_remaining_game_clock'] = pbp['clock_minutes'] * 60 + pbp['clock_seconds']

# assign deadball rebounds labelled as offensive rebounds
pbp.loc[(pbp['event_type'] == 'OREB') & \
            (pbp['team_id'] == pbp['team_id'].shift(1)) & \
            (pbp['team_id'] == pbp['team_id'].shift(-1)) & \
            (pbp['shot_type'].shift(1) == 'Free Throw') & \
            (pbp['shot_type'].shift(-1) == 'Free Throw'), 'event_type'] = 'Deadball Rebound'

# reorder defensive rebounds, fouls that come before the missed shot
pbp['index'] = pbp.reset_index(drop = True).index
pbp['original_index'] = pbp.reset_index(drop = True).index
i = 0
while len(pbp[(pbp['game_id'] == pbp['game_id'].shift(-1)) \
                        & (pbp['period'] == pbp['period'].shift(-1)) \
                        & (pbp['team_id'] != pbp['team_id'].shift(-1)) \
                        & (((pbp['event_type'] == 'DREB') \
                                & (abs(pbp['seconds_remaining_game_clock'] - pbp['seconds_remaining_game_clock'].shift(-1)) <= 2) \
                                & (pbp['event_type'].shift(-1) == 'Missed Shot')
                                & (~pbp['event_type'].shift(-2).isin(['DREB', 'BLK', 'OREB']))
                                & (pbp['event_type'].shift(1) != 'Missed Shot')
                                )
                            | (((pbp['shot_type'] == 'Free Throw') | (pbp['event_type'] == 'Deadball Rebound')) \
                                & (abs(pbp['seconds_remaining_game_clock'] - pbp['seconds_remaining_game_clock'].shift(-1)) == 0) \
                                & ((pbp['event_type'].shift(-1).isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])))
                                & ((~pbp['event_type'].shift(-2).isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])) & (~pbp['event_type'].shift(-3).isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])) & (~pbp['event_type'].shift(-4).isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])))))]) > 0 \
    and i < 50:
    increase_index = (pbp['game_id'] == pbp['game_id'].shift(-1)) \
                        & (pbp['period'] == pbp['period'].shift(-1)) \
                        & (pbp['team_id'] != pbp['team_id'].shift(-1)) \
                        & (((pbp['event_type'] == 'DREB') \
                                & (abs(pbp['seconds_remaining_game_clock'] - pbp['seconds_remaining_game_clock'].shift(-1)) <= 2) \
                                & (pbp['event_type'].shift(-1) == 'Missed Shot')
                                & (~pbp['event_type'].shift(-2).isin(['DREB', 'BLK', 'OREB']))
                                & (pbp['event_type'].shift(1) != 'Missed Shot')
                                )
                            | (((pbp['shot_type'] == 'Free Throw') | (pbp['event_type'] == 'Deadball Rebound')) \
                                & (abs(pbp['seconds_remaining_game_clock'] - pbp['seconds_remaining_game_clock'].shift(-1)) == 0) \
                                & ((pbp['event_type'].shift(-1).isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])))
                                & ((~pbp['event_type'].shift(-2).isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])) & (~pbp['event_type'].shift(-3).isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])) & (~pbp['event_type'].shift(-4).isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])))))
    decrease_index = (pbp['game_id'] == pbp['game_id'].shift(1)) \
                        & (pbp['period'] == pbp['period'].shift(1)) \
                        & (pbp['team_id'] != pbp['team_id'].shift(1)) \
                        & (((pbp['event_type'] == 'Missed Shot') \
                                & (abs(pbp['seconds_remaining_game_clock'] - pbp['seconds_remaining_game_clock'].shift(1)) <= 2) \
                                & (pbp['event_type'].shift(1) == 'DREB')
                                & (pbp['event_type'].shift(2) != 'Missed Shot')
                                & (~pbp['event_type'].shift(-1).isin(['DREB', 'BLK', 'OREB']))
                                )
                            | ((pbp['event_type'].isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])) \
                                & (abs(pbp['seconds_remaining_game_clock'] - pbp['seconds_remaining_game_clock'].shift(1)) == 0) \
                                & ((pbp['shot_type'].shift(1) == 'Free Throw') | (pbp['event_type'].shift(1) == 'Deadball Rebound')) \
                                & ((~pbp['event_type'].shift(2).isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])) & (~pbp['event_type'].shift(3).isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])) & (~pbp['event_type'].shift(4).isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])))))
    pbp.loc[increase_index, 'index'] = pbp.loc[increase_index, 'index'] + 1
    pbp.loc[decrease_index, 'index'] = pbp.loc[decrease_index, 'index'] - 1
    pbp = pbp.sort_values(by = ['index', 'seconds_remaining_game_clock', 'original_index'], ascending = [True, False, True]).reset_index(drop = True)
    i = i + 1
    if (i == 50) and len(pbp[(pbp['game_id'] == pbp['game_id'].shift(-1)) \
                        & (pbp['period'] == pbp['period'].shift(-1)) \
                        & (pbp['team_id'] != pbp['team_id'].shift(-1)) \
                        & (((pbp['event_type'] == 'DREB') \
                                & (abs(pbp['seconds_remaining_game_clock'] - pbp['seconds_remaining_game_clock'].shift(-1)) <= 2) \
                                & (pbp['event_type'].shift(-1) == 'Missed Shot'))
                            | ((pbp['shot_type'] == 'Free Throw') \
                                & (abs(pbp['seconds_remaining_game_clock'] - pbp['seconds_remaining_game_clock'].shift(-1)) == 0) \
                                & (pbp['event_type'].shift(-1) == 'Foul')))]) > 0:
        print('Could not finish rearrangement while loop')

# find the players that played before 10 minutes were left
players = pbp[((pbp['period'] == 1) | (pbp['seconds_remaining_game_clock'] > 600)) \
                & (pbp['event_type'].isin(['Missed Shot', 'Made Shot', 'STL', 'TO', 'Foul', 'BLK', 'DREB', 'OREB', 'Flagrant', 'Intentional']))][['game_id', 'participants_0_athlete_id']].drop_duplicates()
players = players[players['participants_0_athlete_id'] == players['participants_0_athlete_id']]
players['garbage_time_player'] = 0

# count the amount of players that played before 10 minutes were left
player_counts = players.groupby('game_id').size().reset_index()
player_counts.columns = ['game_id', 'num_players']

# add player counts and an indicator of if the player played before 10 minutes were left to pbp data
pbp = pd.merge(pbp, player_counts, how = 'left', on = 'game_id')
pbp = pd.merge(pbp, players, how = 'left', on = ['game_id', 'participants_0_athlete_id'])

# find the first event the player appeared
player_first_occurrences = pbp.groupby(['game_id', 'participants_0_athlete_id'])[['game_id', 'participants_0_athlete_id', 'id']].head(1)
player_first_occurrences = player_first_occurrences[player_first_occurrences['participants_0_athlete_id'] == player_first_occurrences['participants_0_athlete_id']]
player_first_occurrences['player_first_occurrence'] = True

# designate the event that the player first appeared
pbp = pd.merge(pbp, player_first_occurrences, how = 'left', on = ['game_id', 'participants_0_athlete_id', 'id'])
pbp.loc[pbp['player_first_occurrence'] != pbp['player_first_occurrence'], 'player_first_occurrence'] = False

# assign garbage time player to those that did not play in first 30 minutes, where 12 players participated (only assign it to their first event)
pbp.loc[(pbp['garbage_time_player'] != 0) &\
        (pbp['participants_0_athlete_id'] == pbp['participants_0_athlete_id']) &\
        (pbp['num_players'] > 12) &\
        (pbp['player_first_occurrence']), 'garbage_time_player'] = 1
pbp.loc[(pbp['garbage_time_player'] != pbp['garbage_time_player']), 'garbage_time_player'] = 0

# sum the amount of garbage time players that have entered the game
pbp['garbage_time_player_cumsum'] = pbp.groupby('game_id')['garbage_time_player'].cumsum()

# determine when garbage time starts
pbp['garbage_time_indicator'] = 0
pbp.loc[(pbp['garbage_time_player_cumsum'] >= 2)\
        & (abs(pbp['score_differential']) >= 10) \
        & (pbp['period'] == 2) \
        & (pbp['seconds_remaining_game_clock'] < 600), 'garbage_time_indicator'] = 1
pbp.loc[(abs(pbp['score_differential']) >= 10)\
        & (pbp['period'] == 2) \
        & (pbp['seconds_remaining_game_clock'] < 60), 'garbage_time_indicator'] = 1
pbp.loc[(abs(pbp['score_differential']) >= 4)\
        & (pbp['period'] == 2) \
        & (pbp['seconds_remaining_game_clock'] < 30), 'garbage_time_indicator'] = 1

# filter to columns needed
cols_needed = ['id', 'game_id', 'team_id', 'period', 'event_type', 'event_team', 'garbage_time_indicator', 'made',
            'shooting_player_id', 'shot_type', 'result_points', 'home_team_id', 'away_team_id',
            'score_differential', 'seconds_remaining_game_clock', 'coordinate_x', 'coordinate_y', 'potential_duplicate']
pbp = pbp[cols_needed]


# remove these events, as they are not needed
pbp = pbp[~pbp['event_type'].isin(['Unknown', 'Deadball Rebound', 'Timeout', 'Ejection', 'Delay'])].reset_index(drop = True)

# calculate the number of fouls in each period
pbp['home_foul'] = 0
pbp['away_foul'] = 0
pbp.loc[((pbp['event_type'] == 'Foul') |\
            (pbp['event_type'] == 'Technical') |\
            (pbp['event_type'] == 'Flagrant') |\
            (pbp['event_type'] == 'Intentional')) \
            & (pbp['event_team'] == 'Home'), 'home_foul'] = 1
pbp.loc[((pbp['event_type'] == 'Foul') |\
            (pbp['event_type'] == 'Technical') |\
            (pbp['event_type'] == 'Flagrant') |\
            (pbp['event_type'] == 'Intentional')) \
            & (pbp['event_team'] == 'Away'), 'away_foul'] = 1
pbp['period_temp'] = pbp['period'].clip(upper = 2)
pbp['home_fouls'] = pbp.groupby(['game_id', 'period_temp'])['home_foul'].cumsum()
pbp['away_fouls'] = pbp.groupby(['game_id', 'period_temp'])['away_foul'].cumsum()

# determine who had possession during each event
pbp['poss_id'] = np.nan
pbp.loc[(pbp['event_type'].isin(['Jump', 'DREB', 'OREB', 'Missed Shot', 'Made Shot', 'TO', 'Poss'])), 'poss_id'] = pbp.loc[(pbp['event_type'].isin(['Jump', 'DREB', 'OREB', 'Missed Shot', 'Made Shot', 'TO', 'Poss'])), 'team_id']
pbp.loc[(pbp['event_type'].isin(['STL', 'BLK', 'Own'])) & (pbp['team_id'] == pbp['home_team_id']), 'poss_id'] = pbp.loc[(pbp['event_type'].isin(['STL', 'BLK', 'Own'])) & (pbp['team_id'] == pbp['home_team_id']), 'away_team_id']
pbp.loc[(pbp['event_type'].isin(['STL', 'BLK', 'Own'])) & (pbp['team_id'] == pbp['away_team_id']), 'poss_id'] = pbp.loc[(pbp['event_type'].isin(['STL', 'BLK', 'Own'])) & (pbp['team_id'] == pbp['away_team_id']), 'home_team_id']

# calculate a bunch of shifts that help with following calculations
pbp['previous_event_type'] = pbp.groupby(['game_id'])['event_type'].shift(1)
pbp['previous_event_team'] = pbp.groupby(['game_id'])['event_team'].shift(1)
pbp['previous_event_team_id'] = pbp.groupby(['game_id'])['team_id'].shift(1)
pbp['next_event_type'] = pbp.groupby(['game_id'])['event_type'].shift(-1)
pbp['next_event_team'] = pbp.groupby(['game_id'])['event_team'].shift(-1)
pbp['previous_poss_id'] = pbp.groupby(['game_id'])['poss_id'].shift(1).fillna(pbp.groupby(['game_id'])['poss_id'].shift(2)).fillna(pbp.groupby(['game_id'])['poss_id'].shift(3))
pbp['next_poss_id'] = pbp.groupby(['game_id'])['poss_id'].shift(-1).fillna(pbp.groupby(['game_id'])['poss_id'].shift(-2)).fillna(pbp.groupby(['game_id'])['poss_id'].shift(-3))
pbp['event_team_same'] = pbp['event_team'] == pbp['previous_event_team']

# poss id of the these events should be same as previous
pbp.loc[(pbp['event_type'].isin(['Foul', 'Tech', 'Flagrant', 'Intentional'])) & (pbp['previous_poss_id'] == pbp['next_poss_id']), 'poss_id'] = pbp.loc[(pbp['event_type'].isin(['Foul', 'Technical', 'Flagrant', 'Intentional'])) & (pbp['previous_poss_id'] == pbp['next_poss_id']), 'previous_poss_id']

# calculate previous and next poss id again
pbp['previous_poss_id'] = pbp.groupby(['game_id'])['poss_id'].shift(1)
pbp['next_poss_id'] = pbp.groupby(['game_id'])['poss_id'].shift(-1)

# charges
pbp.loc[
    (pbp['event_type'] == 'Foul') & (pbp['next_event_type'] == 'TO') & (pbp['event_team'] == pbp['next_event_team']), 'poss_id'
] = pbp.loc[
    (pbp['event_type'] == 'Foul') & (pbp['next_event_type'] == 'TO') & (pbp['event_team'] == pbp['next_event_team']), 'team_id'
]

# other fouls
pbp.loc[
    (pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'].isin(['Foul', 'Flagrant', 'Intentional'])) & (pbp['team_id'] == pbp['home_team_id']), 'poss_id'
] = pbp.loc[
    (pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'].isin(['Foul', 'Technical', 'Flagrant', 'Intentional'])) & (pbp['team_id'] == pbp['home_team_id']), 'away_team_id'
]
pbp.loc[
    (pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'].isin(['Foul', 'Flagrant', 'Intentional'])) & (pbp['team_id'] == pbp['away_team_id']), 'poss_id'
] = pbp.loc[
    (pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'].isin(['Foul', 'Technical', 'Flagrant', 'Intentional'])) & (pbp['team_id'] == pbp['away_team_id']), 'home_team_id'
]

# techs
pbp.loc[(pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'] == 'Tech') & (pbp['previous_event_type'].isin(['DREB', 'Jump', 'OREB', 'STL', 'Missed Shot'])), 'poss_id'] = pbp.loc[(pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'] == 'Tech') & (pbp['previous_event_type'].isin(['DREB', 'Jump', 'OREB', 'STL'])), 'previous_poss_id']
pbp.loc[(pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'] == 'Tech') & (pbp['previous_event_type'].isin(['BLK', 'Made Shot', 'TO'])) & (pbp['previous_event_team_id'] == pbp['away_team_id']), 'poss_id'] = pbp.loc[(pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'] == 'Tech') & (pbp['previous_event_type'].isin(['BLK', 'Made Shot', 'TO']) & (pbp['previous_event_team_id'] == pbp['away_team_id'])), 'home_team_id']
pbp.loc[(pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'] == 'Tech') & (pbp['previous_event_type'].isin(['BLK', 'Made Shot', 'TO'])) & (pbp['previous_event_team_id'] == pbp['home_team_id']), 'poss_id'] = pbp.loc[(pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'] == 'Tech') & (pbp['previous_event_type'].isin(['BLK', 'Made Shot', 'TO']) & (pbp['previous_event_team_id'] == pbp['home_team_id'])), 'away_team_id']

# use previous possession id to determine who had possession during techs
i = 0
while (len(pbp[(pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'] == 'Tech') & (pbp['previous_poss_id'] == pbp['previous_poss_id'])]) > 0) and i < 15:
    pbp['previous_poss_id'] = pbp.groupby(['game_id'])['poss_id'].shift(1)
    pbp.loc[(pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'] == 'Tech'), 'poss_id'] = pbp.loc[(pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'] == 'Tech'), 'previous_poss_id']

    i = i + 1
    if (i == 15) and (len(pbp[(pbp['poss_id'] != pbp['poss_id']) & (pbp['event_type'] == 'Tech') & (pbp['previous_poss_id'] == pbp['previous_poss_id'])]) > 0):
        print('Could not finish technical foul while loop')

# Add charge info
pbp.loc[
    (pbp['event_type'] == 'Foul') & (pbp['next_event_type'] == 'TO') & (pbp['event_team'] == pbp['next_event_team']), 'event_type'
] = 'Charge Foul'
pbp.loc[
    (pbp['event_type'] == 'TO') & (pbp['event_type'].shift(1) == 'Charge Foul') & (pbp['event_team'] == pbp['event_team'].shift(1)), 'event_type'
] = 'Charge TO'

# Add steal info
pbp.loc[
    (pbp['event_type'] == 'TO') & (pbp['next_event_type'] == 'STL'), 'event_type'
] = 'Steal TO'

# add date and season and location info to pbp
pbp = pd.merge(pbp, games[['game_id', 'season', 'date', 'neutral_site']], how = 'inner', on = 'game_id')

# add location to pbp
pbp['location'] = 'H'
pbp.loc[pbp['event_team'] == 'Away', 'location'] = 'A'
pbp.loc[pbp['neutral_site'], 'location'] = 'N'

# calculate the seconds elapsed between the events by using the game clock difference
pbp['seconds_elapsed'] = pbp.groupby(['game_id', 'period'])['seconds_remaining_game_clock'].shift(1).fillna(pbp['seconds_remaining_game_clock']) - pbp['seconds_remaining_game_clock']

# reset the shot clock fully on these events, 35 seconds before 2016 and 30 seconds after
pbp['after_event_seconds_remaining_shot_clock'] = np.nan 
pbp.loc[(pbp['season'] < 2016) \
        & ((pbp['event_type'].isin(['DREB', 'OREB', 'TO', 'Charge TO', 'Steal TO', 'Own', 'Foul', 'Flagrant', 'Intentional', 'STL', 'Half', 'Jump', 'Poss'])) \
                | (((pbp['event_type'].isin(['Made Shot', 'Missed Shot'])) & (pbp['shot_type'] != 'Free Throw')))), 'after_event_seconds_remaining_shot_clock'] = 35
pbp.loc[(pbp['season'] < 2019) \
        & (pbp['season'] >= 2016) \
        & ((pbp['event_type'].isin(['DREB', 'OREB', 'TO', 'Charge TO', 'Steal TO', 'Own', 'Foul', 'Flagrant', 'Intentional', 'STL', 'Half', 'Jump', 'Poss'])) \
                | ((pbp['event_type'].isin(['Made Shot', 'Missed Shot'])) \
                        & (pbp['shot_type'] != 'Free Throw'))), 'after_event_seconds_remaining_shot_clock'] = 30
pbp.loc[(pbp['season'] >= 2019) \
        & ((pbp['event_type'].isin(['DREB', 'TO', 'Charge TO', 'Steal TO', 'Own', 'STL', 'Half', 'Jump', 'Poss'])) \
                | ((pbp['event_type'] == 'Made Shot') & (pbp['shot_type'] != 'Free Throw'))), 'after_event_seconds_remaining_shot_clock'] = 30

# reset the shot clock fully on these events, 35 seconds before 2016 and 30 seconds after
pbp.loc[(pbp['season'] < 2016) \
        & (pbp['shot_type'] == 'Free Throw') \
        & (pbp['event_type'] == 'Made Shot') \
        & ((~pbp['next_event_type'].isin(['Made Shot', 'Missed Shot'])) | (pbp['poss_id'] != pbp['next_poss_id'])), 'after_event_seconds_remaining_shot_clock'] = 35
pbp.loc[(pbp['season'] >= 2016) \
        & (pbp['shot_type'] == 'Free Throw') \
        & (pbp['event_type'] == 'Made Shot') \
        & ((~pbp['next_event_type'].isin(['Made Shot', 'Missed Shot'])) | (pbp['poss_id'] != pbp['next_poss_id'])), 'after_event_seconds_remaining_shot_clock'] = 30

# before event shot clock is th elast even't after event shot clock minus seconds elapsed
pbp['before_event_seconds_remaining_shot_clock'] = pbp.groupby('game_id')['after_event_seconds_remaining_shot_clock'].shift(1) - pbp['seconds_elapsed']

# these events do not reset the shot clock and do not take any time
pbp.loc[pbp['event_type'].isin(['Half', 'Jump', 'Poss', 'Charge Foul']), 'before_event_seconds_remaining_shot_clock'] = pbp.loc[pbp['event_type'].isin(['Half', 'Jump', 'Poss', 'Charge Foul']), 'after_event_seconds_remaining_shot_clock']

# set the shot clock for the first event of the game
first_events = pbp.groupby('game_id')[['game_id', 'id']].head(1)
first_events['first_event'] = 1
pbp = pbp.merge(first_events, on = ['game_id', 'id'], how = 'left')
pbp.loc[(pbp['first_event'] == 1) & (pbp['before_event_seconds_remaining_shot_clock'] != pbp['before_event_seconds_remaining_shot_clock']) & (pbp['season'] < 2016), 'before_event_seconds_remaining_shot_clock'] = 35 - (1200 - pbp.loc[(pbp['first_event'] == 1) & (pbp['before_event_seconds_remaining_shot_clock'] != pbp['before_event_seconds_remaining_shot_clock']) & (pbp['season'] < 2016), 'seconds_remaining_game_clock'])
pbp.loc[(pbp['first_event'] == 1) & (pbp['before_event_seconds_remaining_shot_clock'] != pbp['before_event_seconds_remaining_shot_clock']) & (pbp['season'] >= 2016), 'before_event_seconds_remaining_shot_clock'] = 30 - (1200 - pbp.loc[(pbp['first_event'] == 1) & (pbp['before_event_seconds_remaining_shot_clock'] != pbp['before_event_seconds_remaining_shot_clock']) & (pbp['season'] >= 2016), 'seconds_remaining_game_clock'])

# while loop to fill in null shot clock entries
i = 0
while (len(pbp[(pbp['after_event_seconds_remaining_shot_clock'] != pbp['after_event_seconds_remaining_shot_clock']) | (pbp['before_event_seconds_remaining_shot_clock'] != pbp['before_event_seconds_remaining_shot_clock'])]) > 0) and (i < 50):
    
    # after event shot clock on these events should be same as before event
    pbp.loc[(pbp['after_event_seconds_remaining_shot_clock'] != pbp['after_event_seconds_remaining_shot_clock']) & (pbp['event_type'].isin(['BLK', 'Tech', 'Made Shot', 'Missed Shot', 'Charge Foul'])), 'after_event_seconds_remaining_shot_clock'] = pbp.loc[(pbp['after_event_seconds_remaining_shot_clock'] != pbp['after_event_seconds_remaining_shot_clock']) & (pbp['event_type'].isin(['BLK', 'Tech', 'Made Shot', 'Missed Shot', 'Charge Foul'])), 'before_event_seconds_remaining_shot_clock']
    
    # reset shot clock on these events, after event shot clock should be 30 or 20 (20 in cases where before event shot clock was less than 20)
    pbp.loc[(pbp['season'] >= 2019) & (pbp['before_event_seconds_remaining_shot_clock'] >= 20) & (pbp['after_event_seconds_remaining_shot_clock'] != pbp['after_event_seconds_remaining_shot_clock']), 'after_event_seconds_remaining_shot_clock'] = pbp.loc[(pbp['season'] >= 2019) & (pbp['before_event_seconds_remaining_shot_clock'] >= 20) & (pbp['after_event_seconds_remaining_shot_clock'] != pbp['after_event_seconds_remaining_shot_clock']), 'before_event_seconds_remaining_shot_clock']
    pbp.loc[(pbp['season'] >= 2019) & (pbp['before_event_seconds_remaining_shot_clock'] < 20) & (pbp['after_event_seconds_remaining_shot_clock'] != pbp['after_event_seconds_remaining_shot_clock']), 'after_event_seconds_remaining_shot_clock'] = 20

    # fill in before event shot clock with seconds elapsed from previous events after event shot clock
    pbp['temp_shot_clock'] = pbp.groupby('game_id')['after_event_seconds_remaining_shot_clock'].shift(1)
    pbp.loc[pbp['before_event_seconds_remaining_shot_clock'] != pbp['before_event_seconds_remaining_shot_clock'], 'before_event_seconds_remaining_shot_clock'] = pbp.loc[pbp['before_event_seconds_remaining_shot_clock'] != pbp['before_event_seconds_remaining_shot_clock'], 'temp_shot_clock'] - pbp.loc[pbp['before_event_seconds_remaining_shot_clock'] != pbp['before_event_seconds_remaining_shot_clock'], 'seconds_elapsed']

    i = i + 1

    if i == 50 and (len(pbp[(pbp['after_event_seconds_remaining_shot_clock'] != pbp['after_event_seconds_remaining_shot_clock']) | (pbp['before_event_seconds_remaining_shot_clock'] != pbp['before_event_seconds_remaining_shot_clock'])]) > 0):
        print('Could not finish shot clock while loop')

# when game clock is less than shot clock, turn shot clock to game clock
pbp.loc[(pbp['before_event_seconds_remaining_shot_clock'] > (pbp['seconds_remaining_game_clock'])), 'before_event_seconds_remaining_shot_clock'] = pbp.loc[(pbp['before_event_seconds_remaining_shot_clock'] > (pbp['seconds_remaining_game_clock'])), 'seconds_remaining_game_clock']

# define a foul stage of the game, when the losing team is fouling early in shot clock at the end of the game to extend the game
pbp['foul_stage'] = 0
pbp['home_quick_foul'] = 0
pbp['away_quick_foul'] = 0
pbp.loc[(pbp['period'] >= 2) \
        & (pbp['seconds_remaining_game_clock'] <= 120) \
        & (pbp['event_type'] == 'Foul') \
        & (pbp['team_id'] == pbp['home_team_id']) \
        & (pbp['poss_id'] == pbp['away_team_id']) \
        & (pbp['before_event_seconds_remaining_shot_clock'] > pbp['after_event_seconds_remaining_shot_clock'] - 10) \
        & (pbp['before_event_seconds_remaining_shot_clock'] > 20) \
        & (pbp['score_differential'] < -3) \
        & (pbp['shot_type'].shift(-1) == 'Free Throw'), 'home_quick_foul'] = 1
pbp.loc[(pbp['period'] >= 2) \
        & (pbp['seconds_remaining_game_clock'] <= 120) \
        & (pbp['event_type'] == 'Foul') \
        & (pbp['team_id'] == pbp['away_team_id']) \
        & (pbp['poss_id'] == pbp['home_team_id']) \
        & (pbp['before_event_seconds_remaining_shot_clock'] > pbp['after_event_seconds_remaining_shot_clock'] - 10) \
        & (pbp['before_event_seconds_remaining_shot_clock'] > 20) \
        & (pbp['score_differential'] > 3) \
        & (pbp['shot_type'].shift(-1) == 'Free Throw'), 'away_quick_foul'] = 1
pbp['home_quick_fouls'] = pbp.groupby(['game_id', 'period'])['home_quick_foul'].cumsum()
pbp['away_quick_fouls'] = pbp.groupby(['game_id', 'period'])['away_quick_foul'].cumsum()
pbp.loc[(pbp['home_quick_fouls'] >= 2) | (pbp['away_quick_fouls'] >= 2), 'foul_stage'] = 1

# whether or not the event represents the start of a new possession
pbp['new_poss'] = 0
# first event of the game
pbp.loc[(pbp['first_event'] == 1), 'new_poss'] = 1
# possession switch in same game on events other than Half and Tech that were not preceded by a Tech
pbp.loc[(pbp['poss_id'] != pbp['previous_poss_id']) & (pbp['game_id'] == pbp.groupby('game_id')['game_id'].shift(1)) & ~(pbp['event_type'].isin(['Half', 'Tech'])) & ~(pbp['previous_event_type'].isin(['Tech'])), 'new_poss'] = 1
# whenever an event take 40 seconds or more (usually signals missing data)
pbp.loc[(pbp['seconds_elapsed'] >= 40), 'new_poss'] = 1
# if the same team still has possession but the previous event should signal a change in possession (also usually signals missing data)
pbp.loc[(((pbp['previous_event_type'].isin(['TO', 'Charge TO', 'Steal TO'])) & (pbp['event_type'] != 'STL')) | ((pbp['previous_event_type'] == 'Made Shot') & (pbp['shot_type'] != 'Free Throw'))) & (pbp['poss_id'] == pbp['previous_poss_id']), 'new_poss'] = 1

# the number of possessions in the game, to eventually be used for IDing possessions
pbp['poss_num'] = pbp.groupby('game_id')['new_poss'].cumsum()

# find foul before the free throws
pbp['free_throw_source'] = np.nan 
pbp['free_throw_source_shot_clock'] = np.nan 
pbp.loc[(pbp['shot_type'] == 'Free Throw'), 'free_throw_source'] = 'Unknown'
for i in range(1, 21):
    event_lag = pbp.groupby(['game_id', 'period'])['event_type'].shift(i)
    team_lag = pbp.groupby(['game_id', 'period'])['team_id'].shift(i)
    game_clock_lag = pbp.groupby(['game_id', 'period'])['seconds_remaining_game_clock'].shift(i)
    shot_clock_lag = pbp.groupby(['game_id', 'period'])['before_event_seconds_remaining_shot_clock'].shift(i)
    poss_lag = pbp.groupby(['game_id', 'period'])['poss_num'].shift(i)
    pbp.loc[(pbp['free_throw_source'] == 'Unknown') \
                & (event_lag.isin(['Tech', 'Foul', 'Flagrant', 'Intentional'])) \
                & (team_lag != pbp['team_id']) \
                & ((game_clock_lag == pbp['seconds_remaining_game_clock']) \
                    | ((poss_lag == pbp['poss_num']) \
                        & ((abs(game_clock_lag - pbp['seconds_remaining_game_clock']) < 5) \
                            | ((i <= 2) \
                                & (abs(game_clock_lag - pbp['seconds_remaining_game_clock']) < 15))))), 'free_throw_source_shot_clock'] = shot_clock_lag
    pbp.loc[(pbp['free_throw_source'] == 'Unknown') \
            & (event_lag.isin(['Tech', 'Foul', 'Flagrant', 'Intentional'])) \
            & (team_lag != pbp['team_id']) \
            & ((game_clock_lag == pbp['seconds_remaining_game_clock']) \
                | ((poss_lag == pbp['poss_num']) \
                    & ((abs(game_clock_lag - pbp['seconds_remaining_game_clock']) < 5) \
                        | ((i <= 2) \
                            & (abs(game_clock_lag - pbp['seconds_remaining_game_clock']) < 15))))), 'free_throw_source'] = event_lag

# look also for a regular foul at the same time as the technical and vice-versa
for i in range(1, 21):
    event_lag = pbp.groupby(['game_id', 'period'])['event_type'].shift(i)
    team_lag = pbp.groupby(['game_id', 'period'])['team_id'].shift(i)
    game_clock_lag = pbp.groupby(['game_id', 'period'])['seconds_remaining_game_clock'].shift(i)
    poss_lag = pbp.groupby(['game_id', 'period'])['poss_num'].shift(i)
    pbp.loc[(pbp['free_throw_source'] == 'Tech') \
            & (event_lag.isin(['Foul', 'Flagrant', 'Intentional'])) \
            & (team_lag != pbp['team_id']) \
            & ((game_clock_lag == pbp['seconds_remaining_game_clock']) \
                | ((poss_lag == pbp['poss_num']) \
                    & ((abs(game_clock_lag - pbp['seconds_remaining_game_clock']) < 5) \
                        | ((i <= 2) \
                            & (abs(game_clock_lag - pbp['seconds_remaining_game_clock']) < 15))))), 'free_throw_source'] = 'Tech and Foul'
    pbp.loc[(pbp['free_throw_source'].isin(['Foul', 'Flagrant', 'Intentional'])) \
            & (event_lag == 'Tech') \
            & (team_lag != pbp['team_id']) \
            & ((game_clock_lag == pbp['seconds_remaining_game_clock']) \
                | ((poss_lag == pbp['poss_num']) \
                    & ((abs(game_clock_lag - pbp['seconds_remaining_game_clock']) < 5) \
                        | ((i <= 2) \
                            & (abs(game_clock_lag - pbp['seconds_remaining_game_clock']) < 15))))), 'free_throw_source'] = 'Tech and Foul'
    
# find the number of consecutive free throws, to determine the foul that led to them as well as the number/place of the free throw event relative to the other free throws
pbp['num_free_throws'] = np.nan
pbp['place_free_throws'] = np.nan
pbp['place_made_free_throws'] = np.nan
pbp['place_missed_free_throws'] = np.nan
pbp['interrupt_lag'] = False
pbp['interrupt_lead'] = False
pbp.loc[pbp['shot_type'] == 'Free Throw', 'num_free_throws'] = 1
pbp.loc[pbp['shot_type'] == 'Free Throw', 'place_free_throws'] = 1
pbp.loc[(pbp['shot_type'] == 'Free Throw') & (pbp['event_type'] == 'Made Shot'), 'place_made_free_throws'] = 1
pbp.loc[(pbp['shot_type'] == 'Free Throw') & (pbp['event_type'] == 'Missed Shot'), 'place_missed_free_throws'] = 1
i = 1
while len(pbp[(pbp['shot_type'] == 'Free Throw') & (~(pbp['interrupt_lag']) | ~(pbp['interrupt_lead']))]) > 0 and i < 15:
    event_lag = pbp.groupby(['game_id', 'period', 'poss_num'])['event_type'].shift(i)
    shot_lag = pbp.groupby(['game_id', 'period', 'poss_num'])['shot_type'].shift(i)
    team_lag = pbp.groupby(['game_id', 'period', 'poss_num'])['team_id'].shift(i)
    dup_lag = pbp.groupby(['game_id', 'period', 'poss_num'])['potential_duplicate'].shift(i)
    shot_lead = pbp.groupby(['game_id', 'period', 'poss_num'])['shot_type'].shift(-1 * i)
    team_lead = pbp.groupby(['game_id', 'period', 'poss_num'])['team_id'].shift(-1 * i)
    dup_lead = pbp.groupby(['game_id', 'period', 'poss_num'])['potential_duplicate'].shift(-1 * i)
    pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']) & (event_lag == 'Made Shot'), 'place_made_free_throws'] = pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']) & (event_lag == 'Made Shot'), 'place_made_free_throws'] + 1
    pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']) & (event_lag == 'Missed Shot'), 'place_missed_free_throws'] = pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']) & (event_lag == 'Missed Shot'), 'place_missed_free_throws'] + 1
    pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']), 'place_free_throws'] = pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']), 'place_free_throws'] + 1
    pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']), 'num_free_throws'] = pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']), 'num_free_throws'] + 1
    pbp.loc[(~pbp['interrupt_lead']) & (pbp['shot_type'] == 'Free Throw') & (shot_lead == 'Free Throw') & (team_lead == pbp['team_id']), 'num_free_throws'] = pbp.loc[(~pbp['interrupt_lead']) & (pbp['shot_type'] == 'Free Throw') & (shot_lead == 'Free Throw') & (team_lead == pbp['team_id']), 'num_free_throws'] + 1
    pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']) & (dup_lag), 'potential_duplicate'] = True
    pbp.loc[(~pbp['interrupt_lead']) & (pbp['shot_type'] == 'Free Throw')  & (shot_lead == 'Free Throw') & (team_lead == pbp['team_id']) & (dup_lead), 'potential_duplicate'] = True
    pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (~((shot_lag == 'Free Throw') & (team_lag == pbp['team_id']))), 'interrupt_lag'] = True
    pbp.loc[(~pbp['interrupt_lead']) & (pbp['shot_type'] == 'Free Throw') & (~((shot_lead == 'Free Throw') & (team_lead == pbp['team_id']))), 'interrupt_lead'] = True
    i = i + 1
    if i == 15 and len(pbp[(pbp['shot_type'] == 'Free Throw') & (~(pbp['interrupt_lag']) | ~(pbp['interrupt_lead']))]) > 0:
        print('Could not finish free throw source while loop')

pbp['missed_free_throws'] = 0
pbp.loc[(pbp['event_type'] == 'Missed Shot') & (pbp['shot_type'] == 'Free Throw'), 'missed_free_throws'] = 1
missed_free_throws = pbp.groupby(['game_id', 'period', 'poss_num', 'num_free_throws', 'seconds_remaining_game_clock', 'free_throw_source'])['missed_free_throws'].sum().reset_index()
pbp = pd.merge(pbp.drop(columns = ['missed_free_throws']), missed_free_throws, how = 'left', on = ['game_id', 'period', 'poss_num', 'num_free_throws', 'seconds_remaining_game_clock', 'free_throw_source'])

# remove the potential duplciates that are the 2nd+ made free throw in the sequence
pbp['remove'] = False 
pbp.loc[(pbp['potential_duplicate']) \
        & (pbp['free_throw_source'].isin(['Foul', 'Flagrant'])) \
        & (pbp['place_made_free_throws'] > 1), 'remove'] = True
# keep the second make when there aren't any misses
pbp.loc[(pbp['remove']) \
        & (pbp['place_made_free_throws'] == 2)
        & (pbp['missed_free_throws'] == 0), 'remove'] = False

# fix the duplicated missed free throws that are wrong, example game 400587106
pbp.loc[(pbp['num_free_throws'] > 2) \
        & (pbp['free_throw_source'].isin(['Foul', 'Flagrant'])) \
        & (pbp['event_type'] == 'Missed Shot')
        & (pbp['place_missed_free_throws'] > 1), 'remove'] = True
pbp = pbp[~pbp['remove']]

# repeat the above while loop now that we've removed duplicate makes
# find the number of consecutive free throws, to determine the foul that led to them as well as the number/place of the free throw event relative to the other free throws
pbp['num_free_throws'] = np.nan
pbp['place_free_throws'] = np.nan
pbp['interrupt_lag'] = False
pbp['interrupt_lead'] = False
pbp.loc[pbp['shot_type'] == 'Free Throw', 'num_free_throws'] = 1
pbp.loc[pbp['shot_type'] == 'Free Throw', 'place_free_throws'] = 1
i = 1
while len(pbp[(pbp['shot_type'] == 'Free Throw') & (~(pbp['interrupt_lag']) | ~(pbp['interrupt_lead']))]) > 0 and i < 15:
    shot_lag = pbp.groupby(['game_id', 'period', 'poss_num'])['shot_type'].shift(i)
    team_lag = pbp.groupby(['game_id', 'period', 'poss_num'])['team_id'].shift(i)
    shot_lead = pbp.groupby(['game_id', 'period', 'poss_num'])['shot_type'].shift(-1 * i)
    team_lead = pbp.groupby(['game_id', 'period', 'poss_num'])['team_id'].shift(-1 * i)
    pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']), 'place_free_throws'] = pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']), 'place_free_throws'] + 1
    pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']), 'num_free_throws'] = pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (shot_lag == 'Free Throw') & (team_lag == pbp['team_id']), 'num_free_throws'] + 1
    pbp.loc[(~pbp['interrupt_lead']) & (pbp['shot_type'] == 'Free Throw') & (shot_lead == 'Free Throw') & (team_lead == pbp['team_id']), 'num_free_throws'] = pbp.loc[(~pbp['interrupt_lead']) & (pbp['shot_type'] == 'Free Throw') & (shot_lead == 'Free Throw') & (team_lead == pbp['team_id']), 'num_free_throws'] + 1
    pbp.loc[(~pbp['interrupt_lag']) & (pbp['shot_type'] == 'Free Throw') & (~((shot_lag == 'Free Throw') & (team_lag == pbp['team_id']))), 'interrupt_lag'] = True
    pbp.loc[(~pbp['interrupt_lead']) & (pbp['shot_type'] == 'Free Throw') & (~((shot_lead == 'Free Throw') & (team_lead == pbp['team_id']))), 'interrupt_lead'] = True
    i = i + 1
    if i == 15 and len(pbp[(pbp['shot_type'] == 'Free Throw') & (~(pbp['interrupt_lag']) | ~(pbp['interrupt_lead']))]) > 0:
        print('Could not finish free throw source while loop2')

# foul types

# parse the free throws that are from Techs and fouls
# call first 2 free throws as foul, the rest as Techs
pbp.loc[(pbp['free_throw_source'] == 'Tech and Foul') & (pbp['place_free_throws'] <= 2), 'free_throw_source'] = 'Foul Before Tech'
pbp.loc[(pbp['free_throw_source'] == 'Tech and Foul'), 'free_throw_source'] = 'Tech'

# And ones
pbp.loc[(pbp['free_throw_source'].isin(['Foul', 'Unknown'])) \
            & (pbp['event_type'].shift(2) == 'Made Shot') \
            & (pbp['team_id'] == pbp['team_id'].shift(2)) \
            & (pbp['shot_type'].shift(2).isin(['Long Two', 'Dunk', 'Layup']) \
            & (pbp['num_free_throws'] == 1)), 'free_throw_source'] = 'Shooting 2'
pbp.loc[(pbp['free_throw_source'].isin(['Foul', 'Unknown'])) \
        & (pbp['event_type'].shift(2) == 'Made Shot') \
        & (pbp['team_id'] == pbp['team_id'].shift(2)) \
        & (pbp['shot_type'].shift(2).isin(['Three'])) \
        & (pbp['num_free_throws'] == 1), 'free_throw_source'] = 'Shooting 3'

# Threes
pbp.loc[(pbp['free_throw_source'].isin(['Foul', 'Unknown'])) \
        & (pbp['num_free_throws'] == 3), 'free_throw_source'] = 'Shooting 3'

# Twos
pbp.loc[(pbp['free_throw_source'].isin(['Foul', 'Unknown'])) \
        & (pbp['team_id'] == pbp['home_team_id']) \
        & (pbp['away_fouls'] < 7) \
        & (pbp['num_free_throws'] == 2), 'free_throw_source'] = 'Shooting 2'
pbp.loc[(pbp['free_throw_source'].isin(['Foul', 'Unknown'])) \
        & (pbp['team_id'] == pbp['away_team_id']) \
        & (pbp['home_fouls'] < 7) \
        & (pbp['num_free_throws'] == 2), 'free_throw_source'] = 'Shooting 2'

# Twos before Techs
pbp.loc[(pbp['free_throw_source'] == 'Foul Before Tech') \
        & (pbp['team_id'] == pbp['home_team_id']) \
        & (pbp['away_fouls'] < 7), 'free_throw_source'] = 'Shooting 2'
pbp.loc[(pbp['free_throw_source'] == 'Foul Before Tech') \
        & (pbp['team_id'] == pbp['away_team_id']) \
        & (pbp['home_fouls'] < 7), 'free_throw_source'] = 'Shooting 2'

# Missed front ends
pbp.loc[(pbp['free_throw_source'].isin(['Foul', 'Unknown']))\
        & (pbp['team_id'] == pbp['home_team_id']) \
        & (pbp['away_fouls'] >= 7) \
        & (pbp['away_fouls'] < 10) \
        & (pbp['event_type'] == 'Missed Shot') \
        & (pbp['num_free_throws'] == 1), 'free_throw_source'] = '1 and 1'
pbp.loc[(pbp['free_throw_source'].isin(['Foul', 'Unknown']))\
        & (pbp['team_id'] == pbp['away_team_id']) \
        & (pbp['home_fouls'] >= 7) \
        & (pbp['home_fouls'] < 10) \
        & (pbp['event_type'] == 'Missed Shot') \
        & (pbp['num_free_throws'] == 1), 'free_throw_source'] = '1 and 1'

# Unknown whether it's a shooting foul or bonus
pbp.loc[(pbp['free_throw_source'].isin(['Foul', 'Unknown']))\
        & (pbp['team_id'] == pbp['home_team_id']) \
        & (pbp['away_fouls'] >= 7) \
        & (pbp['num_free_throws'] == 2), 'free_throw_source'] = 'Bonus or Shooting 2'
pbp.loc[(pbp['free_throw_source'].isin(['Foul', 'Unknown']))\
        & (pbp['team_id'] == pbp['away_team_id']) \
        & (pbp['home_fouls'] >= 7) \
        & (pbp['num_free_throws'] == 2), 'free_throw_source'] = 'Bonus or Shooting 2'

# Beofre technical, Unknown whether it's a shooting foul or bonus
pbp.loc[(pbp['free_throw_source'] == 'Foul Before Tech')\
        & (pbp['team_id'] == pbp['home_team_id']) \
        & (pbp['away_fouls'] >= 7), 'free_throw_source'] = 'Bonus or Shooting 2'
pbp.loc[(pbp['free_throw_source'] == 'Foul Before Tech')\
        & (pbp['team_id'] == pbp['away_team_id']) \
        & (pbp['home_fouls'] >= 7), 'free_throw_source'] = 'Bonus or Shooting 2'

# Assign Bonus or Shooting 2 based on if foul occurs in first 10 seconds of shot clock
pbp.loc[(pbp['free_throw_source'] == 'Bonus or Shooting 2') & (pbp['free_throw_source_shot_clock'] > 20) & (pbp['season'] >= 2016), 'free_throw_source'] = 'Bonus'
pbp.loc[(pbp['free_throw_source'] == 'Bonus or Shooting 2') & (pbp['free_throw_source_shot_clock'] > 25), 'free_throw_source'] = 'Bonus'
pbp.loc[(pbp['free_throw_source'] == 'Bonus or Shooting 2'), 'free_throw_source'] = 'Shooting 2'

# Assign what type of bonus
pbp.loc[(pbp['free_throw_source'] == 'Bonus')\
        & (pbp['team_id'] == pbp['away_team_id']) \
        & (pbp['home_fouls'] >= 7) \
        & (pbp['home_fouls'] < 10), 'free_throw_source'] = '1 and 1'
pbp.loc[(pbp['free_throw_source'] == 'Bonus')\
        & (pbp['team_id'] == pbp['home_team_id']) \
        & (pbp['away_fouls'] >= 7) \
        & (pbp['away_fouls'] < 10), 'free_throw_source'] = '1 and 1'
pbp.loc[pbp['free_throw_source'] == 'Bonus', 'free_throw_source'] = 'Double Bonus'

# identify the last free throw in the sequence (only one that can be rebounded)
pbp['last_free_throw'] = np.nan
pbp.loc[pbp['shot_type'] == 'Free Throw', 'last_free_throw'] = False
pbp.loc[
    (pbp['shot_type'] == 'Free Throw') \
    & (pbp['next_event_type'] != 'Tech') \
    & (pbp['shot_type'].shift(-1) != 'Free Throw'), 'last_free_throw'
] = True

# how the previous possession ended
poss_enders = pbp[pbp['event_type'].isin(['TO', 'Missed Shot', 'Made Shot', 'Charge TO', 'Steal TO'])].groupby(['game_id', 'poss_num'])[['game_id', 'poss_num', 'event_type', 'score_differential']].tail(1)
poss_enders['poss_num'] = poss_enders['poss_num'] + 1
poss_enders['score_differential'] = poss_enders['score_differential'] * -1
poss_enders = poss_enders.rename(columns = {'event_type': 'previous_possession_end', 'score_differential': 'possession_score_differential'})
pbp = pd.merge(pbp, poss_enders, how = 'left', on = ['game_id', 'poss_num'])
pbp.loc[pbp['previous_possession_end'] != pbp['previous_possession_end'], 'previous_possession_end'] = 'Other'

# event type at beginning of possession for DREB and score differential at beginning of possession for later
poss_start = pbp.groupby(['game_id', 'poss_num'])[['game_id', 'poss_num', 'event_type', 'score_differential']].head(1).rename(columns = {
    'event_type': 'start_event',
    'score_differential': 'start_possession_score_differential'
})
pbp = pd.merge(pbp, poss_start, how = 'left', on = ['game_id', 'poss_num'])
pbp.loc[pbp['start_event'] == 'DREB', 'previous_possession_end'] = 'DREB'
pbp['possession_score_differential'] = pbp['possession_score_differential'].combine_first(pbp['start_possession_score_differential'])

# read player info data for position info
player_info_season = pd.read_csv('players.csv')
player_info_season = player_info_season[~player_info_season['athlete_position_name'].isin(['Athlete', 'Not Available'])]
player_info_season.loc[(player_info_season['athlete_position_name'].isin(['Forward/Center'])), 'athlete_position_name'] = 'Center'
player_info_season.loc[(player_info_season['athlete_position_name'].isin(['Small Forward', 'Power Forward', 'Guard/Forward'])), 'athlete_position_name'] = 'Forward'
player_info_season.loc[(player_info_season['athlete_position_name'].isin(['Point Guard', 'Shooting Guard'])), 'athlete_position_name'] = 'Guard'
player_info_season.loc[player_info_season['athlete_id'] == 4902435, 'athlete_position_name'] = 'Guard'
player_info_season = player_info_season.sort_values('athlete_position_name').groupby(['athlete_id', 'season']).head(1)
player_info = player_info_season.sort_values('athlete_position_name').groupby(['athlete_id'])[['athlete_id', 'athlete_position_name']].head(1)

# join back to pbp and coalesce season position and career position
pbp = pd.merge(pbp, player_info_season, how = 'left', left_on=['season', 'shooting_player_id'], right_on=['season', 'athlete_id'])
pbp = pd.merge(pbp, player_info, how = 'left', left_on=['shooting_player_id'], right_on=['athlete_id'])
pbp['position'] = pbp['athlete_position_name_x'].combine_first(pbp['athlete_position_name_y'])

# date in YYYY-MM-DD format
pbp['date'] = pbp['date'].str[:10]

# add oppponent ID
pbp['opp_id'] = pbp['home_team_id']
pbp.loc[pbp['home_team_id'] == pbp['team_id'], 'opp_id'] = pbp.loc[pbp['home_team_id'] == pbp['team_id'], 'away_team_id']

# whether or not the team was home, away
pbp['home'] = 0
pbp.loc[pbp['location'] == 'H', 'home'] = 1

# whether the shot is off a turnover or off a miss
pbp['off_stl'] = 0
pbp.loc[pbp['previous_possession_end'] == 'Steal TO', 'off_stl'] = 1

# get date for start of season 
season_start = pbp[['game_id', 'season', 'date']].drop_duplicates().groupby('season')['date'].min().reset_index().rename(columns={'date':'season_start'})
pbp = pd.merge(pbp, season_start, on = 'season')

# days since start of season
pbp['days_since_season_start'] = (pd.to_datetime(pbp['date']) - pd.to_datetime(pbp['season_start'])).dt.days


pbp['shot_blocked'] = np.nan
pbp.loc[pbp['event_type'].isin(['Made Shot', 'Missed Shot']), 'shot_blocked'] = 0
pbp.loc[(pbp['event_type'] == 'Missed Shot') & (pbp['event_type'].shift(-1) == 'BLK') & (pbp['team_id'] != pbp['team_id'].shift(-1)), 'shot_blocked'] = 1  


pbp['distance'] = (((pbp['coordinate_x'] - 25) ** 2 + pbp['coordinate_y'].clip(lower = -1) ** 2) ** 0.5).round()
pbp.loc[pbp['distance'] > 36, 'distance'] = np.nan
pbp = pd.merge(pbp, pbp[pbp['shot_type'] == 'Three'].groupby(['shot_type', 'season'])['distance'].agg(pd.Series.mode).reset_index(), how = 'left', on = ['shot_type', 'season'], suffixes = ('' , '_mode_3'))
pbp['distance_3'] = pbp['distance'].combine_first(pbp['distance_mode_3']).clip(lower = 20).fillna(24)
pbp = pd.merge(pbp, pbp[pbp['shot_type'] == 'Long Two'].groupby(['shot_type', 'season'])['distance'].agg(pd.Series.mode).reset_index(), how = 'left', on = ['shot_type', 'season'], suffixes = ('' , '_mode_2'))
pbp['distance_2'] = pbp['distance'].combine_first(pbp['distance_mode_2']).clip(upper = 21).fillna(6)
pbp.loc[pbp['shot_type'] == 'Three', 'distance'] = pbp.loc[pbp['shot_type'] == 'Three', 'distance_3']
pbp.loc[pbp['shot_type'] == 'Long Two', 'distance'] = pbp.loc[pbp['shot_type'] == 'Long Two', 'distance_2']

pbp['made'] = np.nan
pbp.loc[pbp['event_type'] == 'Made Shot', 'made'] = 1
pbp.loc[pbp['event_type'] == 'Missed Shot', 'made'] = 0

pbp.loc[pbp['seconds_remaining_game_clock'] < pbp['before_event_seconds_remaining_shot_clock'], 'before_event_seconds_remaining_shot_clock'] = pbp.loc[pbp['seconds_remaining_game_clock'] < pbp['before_event_seconds_remaining_shot_clock'], 'seconds_remaining_game_clock']

pbp['season_adjusted_shot_clock'] = pbp['before_event_seconds_remaining_shot_clock']

# any shot clock under -4 seconds is overwritten with NaN
pbp.loc[pbp['season_adjusted_shot_clock'] < -4, 'season_adjusted_shot_clock'] = np.nan

# reduce 16-19 seconds in 35 second shot clock to be 15
pbp.loc[(pbp['season'] <= 2015) & (pbp['before_event_seconds_remaining_shot_clock'] >= 16) & (pbp['before_event_seconds_remaining_shot_clock'] <= 19), 'season_adjusted_shot_clock'] = 15

# reduce 20-35 seconds in 35 second shot clock era to be 15-30 seconds
pbp.loc[(pbp['season'] <= 2015) & (pbp['before_event_seconds_remaining_shot_clock'] >= 20), 'season_adjusted_shot_clock'] = pbp.loc[(pbp['season'] <= 2015) & (pbp['before_event_seconds_remaining_shot_clock'] >= 20), 'before_event_seconds_remaining_shot_clock'] - 5

pbp = pd.merge(pbp, pbp[(pbp['shot_type'] != 'Unknown') & (pbp['shot_type'] == pbp['shot_type'])].groupby(['shot_type', 'season', 'off_stl'])['season_adjusted_shot_clock'].agg(pd.Series.mode).reset_index(), how = 'left', on = ['shot_type', 'season', 'off_stl'], suffixes = ('' , '_mode'))
pbp['season_adjusted_shot_clock'] = pbp['season_adjusted_shot_clock'].combine_first(pbp['season_adjusted_shot_clock_mode']).clip(upper = 30)

pbp_cols = [
    'id', 'game_id', 'season', 'date', 'period', 'poss_num', 'poss_id', 'team_id', 'opp_id',
    'seconds_remaining_game_clock', 'before_event_seconds_remaining_shot_clock', 'event_type',
    'shot_type', 'shooting_player_id', 'position', 'result_points', 'possession_score_differential',
    'seconds_elapsed', 'distance', 'foul_stage', 'garbage_time_indicator',
    'last_free_throw', 'free_throw_source', 'previous_event_type', 'previous_possession_end',
    'home', 'off_stl', 'days_since_season_start', 'shot_blocked', 'season_adjusted_shot_clock', 'made'
]


pbp[pbp_cols].to_csv('pbp_pre_shot.csv', index = False)


import pandas as pd
import numpy as np
import pickle
pbp = pd.read_csv('pbp_pre_shot.csv')

# TODO: edit this code to calculate player_shot_make_prob

# calculate season makes and attempts by shot type
season_stats_long = pbp[
    (pbp['event_type'].isin(['Made Shot', 'Missed Shot'])) & (pbp['shot_type'] != 'Unknown')
].groupby(
    ['shooting_player_id', 'shot_type', 'season']
).agg(
    makes = ('made', sum),
    attempts = ('id', len)
).reset_index()

season_stats = pd.DataFrame(
    season_stats_long.pivot_table(
        index = ['shooting_player_id', 'season'], 
        columns = 'shot_type', 
        values = ['makes', 'attempts'], 
        fill_value = 0
    ).to_records()
)

# create career stats by season
career_stats = pd.DataFrame()

for season in season_stats_long['season'].unique():

    # only look at stats before and during this season
    career_stats_temp = season_stats_long[
        season_stats_long['season'] <= season
    ].groupby(
        ['shooting_player_id', 'shot_type']
    ).agg(
        makes = ('makes', sum),
        attempts = ('attempts', sum)
    ).reset_index()

    career_stats_temp['season'] = season

    career_stats = pd.concat(
        [career_stats,
        pd.DataFrame(
            career_stats_temp.pivot_table(
                index = ['shooting_player_id', 'season'], 
                columns = 'shot_type', 
                values = ['makes', 'attempts'], 
                fill_value = 0
            ).to_records()
        )]
    )

career_stats = career_stats.reset_index(drop = True)

opp_stats_long = pbp[
    (pbp['event_type'].isin(['Made Shot', 'Missed Shot'])) & (pbp['shot_type'] != 'Unknown')
].groupby(
    ['opp_id', 'season', 'shot_type']
).agg(
    makes = ('made', sum),
    attempts = ('id', len)
).reset_index()

opp_stats = pd.DataFrame(
    opp_stats_long.pivot_table(
        index = ['opp_id', 'season'], 
        columns = 'shot_type', 
        values = ['makes', 'attempts'], 
        fill_value = 0
    ).to_records()
)

# rename columns
rename_map = {}
for col in season_stats.columns:
    if ', ' in col:
        col_list = col.replace('(', '').replace(')', '').replace('\'', '').split(', ')
        rename_map[col] = col_list[1].lower() + '_' + col_list[0]

career_stats = career_stats.rename(columns = rename_map)
season_stats = season_stats.rename(columns = rename_map)
opp_stats = opp_stats.rename(columns = rename_map)

# join back to pbp data
pbp = pd.merge(pbp, career_stats, how = 'left', on = ['shooting_player_id', 'season'], suffixes = (None, '_career'))
pbp = pd.merge(pbp, season_stats, how = 'left', on = ['shooting_player_id', 'season'], suffixes = (None, '_season'))
pbp = pd.merge(pbp, opp_stats, how = 'left', on = ['opp_id', 'season'], suffixes = (None, '_opp'))


# fill nulls for makes and attempts with zeros
for col in pbp.columns:
    if 'attempts' in col or 'makes' in col:
        pbp[col] = pbp[col].fillna(0)


# calculate percentages for each shot type
for col in pbp.columns:
    if 'makes' in col:
        col_split = col.split('_')
        if len(col_split) == 2:
            suffix = ''
        else:
            suffix = '_season'
        pbp[col_split[0] + '_pct' + suffix] = pbp[col_split[0] + '_makes' + suffix].div(pbp[col_split[0] + '_attempts' + suffix])

# calculate percentages for opponents
for col in pbp.columns:
    if 'makes' in col and 'opp' in col:
        col_split = col.split('_')
        suffix = '_opp'
        pbp[col_split[0] + '_pct' + suffix] = pbp[col_split[0] + '_makes' + suffix].div(pbp[col_split[0] + '_attempts' + suffix])

# features to use per shot type
features = {
    'Layup': ['season', 'before_event_seconds_remaining_shot_clock', 'days_since_season_start', 'off_steal', 'player_shot_make_prob'],
    'Dunk': ['season', 'before_event_seconds_remaining_shot_clock', 'days_since_season_start', 'off_steal', 'player_shot_make_prob'],
    'Free Throw': ['season', 'days_since_season_start', 'home', 'player_shot_make_prob'],
    'Long Two': ['season', 'before_event_seconds_remaining_shot_clock', 'days_since_season_start', 'off_steal', 'home', 'player_shot_make_prob'],
    'Three': ['season', 'before_event_seconds_remaining_shot_clock', 'days_since_season_start', 'off_steal', 'home', 'distance', 'player_shot_make_prob']
}

# for each shot, read model and make predictions
shot_preds = pd.DataFrame()
for shot in pbp['shot_type'].unique():
    if shot == shot and shot != 'Unknown':
        file_name = 'models/' + shot.lower().replace(' ', '_') + '.sav'
        shot_model = pickle.load(open(file_name, 'rb'))
        shots = pbp[pbp['shot_type'] == shot][['id'] + features[shot]].reset_index(drop = True)
        shots['make_prob'] = shot_model.predict_proba(shots[features[shot]])[:, 1]
        shot_preds = pd.concat([shot_preds, shots[['id', 'make_prob']]])

# join predictions back to pbp
pbp = pd.merge(pbp, shot_preds, how = 'left', on = 'id')

# fill NaN make probs for Unknown shot types with the result
pbp.loc[pbp['shot_type'] == 'Unknown', 'make_prob'] = pbp.loc[pbp['shot_type'] == 'Unknown', 'made']

# calculate the miss prob and set to 1 for all non-shooting events (useful for the cumulative product)
pbp['miss_prob'] = 1 - pbp['make_prob']
pbp.loc[pbp['miss_prob'] != pbp['miss_prob'], 'miss_prob'] = 1

# set miss prob to 1 for all non technical free throws that aren't the last attempted
pbp.loc[(pbp['last_free_throw'] == False) | (pbp['free_throw_source'].isin(['Tech', 'Intentional', 'Flagrant'])), 'miss_prob'] = 1

# calculate probability multiplier as the cumulative product of all earlier shots
pbp['prob_multiplier'] = pbp.groupby(['game_id', 'poss_num'])['miss_prob'].cumprod().mul(pbp['make_prob']).div(pbp['miss_prob'])

# calculate expected points
pbp['expected_points'] = 0
pbp.loc[pbp['shot_type'] == 'Unknown', 'expected_points'] = pbp.loc[pbp['shot_type'] == 'Unknown', 'result_points'] * pbp.loc[pbp['shot_type'] == 'Unknown', 'prob_multiplier']
pbp.loc[pbp['shot_type'] == 'Free Throw', 'expected_points'] = pbp.loc[pbp['shot_type'] == 'Free Throw', 'prob_multiplier']
pbp.loc[pbp['shot_type'].isin(['Dunk', 'Layup', 'Long Two']), 'expected_points'] = 2 * pbp.loc[pbp['shot_type'].isin(['Dunk', 'Layup', 'Long Two']), 'prob_multiplier']
pbp.loc[pbp['shot_type'] == 'Three', 'expected_points'] = 3 * pbp.loc[pbp['shot_type'] == 'Three', 'prob_multiplier']

# rename the team with poss column
pbp['team_id_with_poss'] = pbp['poss_id']

# make a possession id column
pbp['temp_poss_id'] = pbp['poss_num'].astype('str')
pbp.loc[pbp['poss_num'] < 100, 'temp_poss_id'] = '0' + pbp.loc[pbp['poss_num'] < 100, 'temp_poss_id']
pbp.loc[pbp['poss_num'] < 10, 'temp_poss_id'] = '0' + pbp.loc[pbp['poss_num'] < 10, 'temp_poss_id']
pbp['poss_id'] = (pbp['game_id'].astype(str) + pbp['temp_poss_id']).astype(float)

# add info on if the foul was a shooting foul
pbp.loc[(pbp['event_type'] == 'Foul') \
        & (
            (pbp['free_throw_source'].shift(-1).isin(['Shooting 2', 'Shooting 3'])) \
            | (
                (pbp['event_type'].shift(-1) == 'Tech') \
                & (pbp['free_throw_source'].shift(-2).isin(['Shooting 2', 'Shooting 3']))
            )
        ), 'event_type'] = 'Shooting Foul'

# output the pbp data
pbp[['id', 'game_id', 'season', 'date', 'poss_id', 'team_id_with_poss', 'period', 
    'seconds_remaining_game_clock', 'before_event_seconds_remaining_shot_clock', 
    'event_type', 'shot_type', 'shooting_player_id', 'seconds_elapsed',
    'result_points', 'possession_score_differential', 'coordinate_x', 'coordinate_y', 
    'foul_stage', 'garbage_time_indicator', 'last_free_throw', 'miss_prob', 'make_prob', 'made',
    'free_throw_source', 'previous_event_type', 'previous_possession_end', 'expected_points']].to_csv('pbp_clean.csv', index = False)
