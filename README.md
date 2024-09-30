# balo-orderly-submission

## Strategy
**EMA Momentum and Slope Breakout Strategy (EMSB)**

## Focus
**Profit from explosive breakout moves by combining momentum and price slope.**

## Market Focus
**BTC/USDC**

## Time Horizon
**Short-term (14-days)**

## Indicators

* Exponential Moving Average (EMA): 9-day and 14-day EMAs.
* Slope Indicator: Measures the slope of price action to confirm momentum.

## Execution

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

## Why It Works
* Innovation: Combining EMA crossovers with the Slope indicator amplifies the strategy’s ability to catch strong momentum-based breakouts, especially in short-term timeframes.

* Profitability: By focusing on periods of sharp price movement and using trailing stops, the strategy maximizes gains from explosive price moves.

## Set Up
1. Install [poetry](https://python-poetry.org/)
2. Clone repo: `git clone https://github.com/balojey/balo-orderly-submission`
3. Change directory: `cd balo-orderly-submission`
4. Install dependencies: `poetry install`
5. Create and populate `.env` file
```
touch .env
echo "PRIVATE_KEY=<enter your wallet private key here>" > .env
```
6. Open `emsb.ipynb`
7. Click "Select kernel" and select appropriate kernel
8. Click "Run all"