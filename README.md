# nfl-power-rankings

Data model to calculate weekly NFL power rankings

Breakdown of the latest data model iteration:

* win_value (50% of ranking) — team wins multiplied by strength of victory.

* point_differential_value (25% of ranking) — points per game plus/minus differential multiplied by strength of schedule.

* points_scored_value (10% of ranking) — points scored transformed to a scale of 0-10. *i.e. league best 30 points equals 10 on the transformation scale and 0 points equals 0.

* points_against_value (10% of ranking) — points scored against transformed to a scale of 0-10. *i.e. league best 10 points equals 10 on the transformation scale and 0 points equals 0.

* turnover_differential_value (5% of ranking) — a team’s plus/minus turnover differential transformed to a scale of -10-10. *i.e. league best +7 turnovers equals 10 on the transformation scale and -7 turnovers equals -7.
