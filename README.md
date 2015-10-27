# nfl-power-rankings

Data model to calculate weekly NFL power rankings

Breakdown of the latest data model iteration:

* win_value (50% of ranking) — team wins multiplied by strength of victory.

* point_differential_value (20% of ranking) — points per game plus/minus differential multiplied by strength of schedule.

* points_scored_value (10% of ranking) — points scored NFL ranking scaled to a baseline of 10. *i.e. number 1 / 32 team is equal to 32 / 1 points before scaling and 10 / 0.3125 after.

* points_against_value (10% of ranking) — points scored against NFL ranking scaled down to 10. *i.e. number 1 / 32 team is equal to 32 / 1 points before scaling and 10 / 0.3125 after.

* turnover_differential_value (10% of ranking) — a team’s plus/minus turnover differential ranking scaled to a baseline of 10. *i.e number 1 / 32 team is equal to 32 / 1 points before scaling and 10 / 0.3125 after.
