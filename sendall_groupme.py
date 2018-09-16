#!/usr/bin/env python3

# Integration test to send each function to the GroupMe

from ff_bot import ff_bot

print('Starting GroupMe Function test...')
ff_bot.bot_main('get_matchups')
ff_bot.bot_main('get_scoreboard')
ff_bot.bot_main('get_scoreboard_short')
ff_bot.bot_main('get_close_scores')
ff_bot.bot_main('get_power_rankings')
ff_bot.bot_main('get_trophies')
ff_bot.bot_main('get_final')
print('GroupMe Function Test complete')