from plutus_backtest import backtest

# bt1 = backtest(asset = ["AAPL", "BTC-USD","GC=F"],
#                o_day = ["2021-08-01", "2021-07-15", "2021-08-20"],
#                c_day = ["2021-09-01", "2021-09-01","2021-09-15"])
# bt2 = backtest(asset = ["AMZN", "EURUSD=X", "AAPL"],
#                o_day = ["2021-06-01", "2021-06-15", "2021-11-15"],
#                c_day = ["2021-06-30", "2021-07-05", "2021-12-05"])
#
# p1 = bt1.multiple_executions()
# p2 = bt2.multiple_executions()
# q1 = bt1.final_portfolio
# q2 = bt2.final_portfolio
#
# dic ={}
# dic[0] = q1
# dic[1]= q2
#
# combined_frame = backtest.puzzle_assembly(dic)
#
#
# backtest.puzzle_plotting(combined_frame)



bt = backtest(asset = ["AAPL", "BTC-USD","GC=F"],
              o_day = ["2020-08-01", "2020-07-15", "2020-08-20"],
              c_day = ["2021-09-01", "2021-09-01","2021-09-15"],
              benchmark = "SPY")
bt.plotting()

