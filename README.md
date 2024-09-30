# balo-orderly-submission

_Strategy_: **EMA Momentum and Slope Breakout Strategy (EMSB)**

_Focus_: Profit from explosive breakout moves by combining momentum and price slope.

_Indicators_:

* Exponential Moving Average (EMA): 9-day and 14-day EMAs.
* Slope Indicator: Measures the slope of price action to confirm momentum.

_Execution_:

1. Identify Momentum with EMAs:
    * Use a 9-day EMA and a 14-day EMA to detect short-term momentum.
    * A bullish breakout occurs when the 9-day EMA crosses above the 14-day EMA, indicating upward momentum.
    * A bearish breakout occurs when the 9-day EMA crosses below the 14-day EMA, signaling downward momentum.

2. Confirm with Slope:
    * The Slope indicator (calculated as the angle of the price trend) must be positive for long trades and negative for short trades.
    * Use a Slope filter of at least 15° for bullish momentum and -15° for bearish momentum to ensure a strong price trend.

3. Buy Signal:
    * Enter a long position when:
        * The 9-day EMA crosses above the 14-day EMA.
        * The Slope indicator is greater than 15°.

4. Sell Signal:
    * Enter a short position when:
        * The 9-day EMA crosses below the 14-day EMA.
        * The Slope indicator is less than -15°.

5. Stop Loss:
    * Place a stop loss at the nearest price support or resistance level, adjusted to risk tolerance.

6. Take Profit:
    * Set a trailing stop to lock in profits as the trend continues.

_Why It Works_:
* Innovation: Combining EMA crossovers with the Slope indicator amplifies the strategy’s ability to catch strong momentum-based breakouts, especially in short-term timeframes.

* Profitability: By focusing on periods of sharp price movement and using trailing stops, the strategy maximizes gains from explosive price moves.