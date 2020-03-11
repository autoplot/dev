This shows where Autoplot's code to guess at names falls short.  Somehow it needs to identify 
the $Ym$m$d part of data/1991-080/mpa/20140101_1991-080_MPA_MOMENTS_1Cycle_json_v1.1.0.txt,
but currently it keeps seeing the 1991-080 (spacecraft id) as the date.

