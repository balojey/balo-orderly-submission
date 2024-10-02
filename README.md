# balo-orderly-submission

## EMA Cross Strategy Overview
![alt Strategy plot](assets/bokeh_plot.png "EMA Cross Strategy over DOGE")

### 1. **Focus**
The **EMA Cross Strategy** aims to leverage the crossover between two Exponential Moving Averages (EMAs) to capture short- to medium-term trends in the market. By tracking price momentum using EMAs, this strategy seeks to identify buying and selling opportunities when trend reversals or continuations are likely. The strategy primarily focuses on maximizing gains through an aggressive approach to capturing market momentum.

### 2. **Market Focus**
This strategy is tailored for trading in **cryptocurrency markets**, particularly the **Perpetual Asset Type DOGE (Dogecoin)**. The strategy can be adapted for other liquid assets but is optimized for volatile and high-volume markets where rapid price movements and trends are common.

### 3. **Time Horizon**
The strategy is designed for **short-term trading** with a maximum run time of **14 days**, focusing on **five-minute intervals**. It is ideal for traders who want to capitalize on fast-moving markets and take advantage of short-lived price movements. The short-term focus makes it suitable for day traders and those looking to profit from rapid market trends.

### 4. **Indicators**
The core indicators of the strategy are:
- **12-Day EMA**: A short-term EMA that reacts quickly to recent price movements.
- **26-Day EMA**: A longer-term EMA that smooths out price action over a more extended period.
- **Crossover**: The strategy triggers buy signals when the 12-day EMA crosses above the 26-day EMA (Golden Cross) and sell signals when the 12-day EMA crosses below the 26-day EMA (Death Cross).

### 5. **Execution**
The strategy operates as follows:
- **Buy Signal**: When the 12-day EMA crosses above the 26-day EMA, indicating upward momentum (Golden Cross), the strategy buys the asset.
- **Sell Signal**: When the 12-day EMA crosses below the 26-day EMA, signaling downward momentum (Death Cross), the strategy sells the asset or initiates a short position.
- **Position Management**: The strategy closes any open positions before opening a new one to avoid overlapping trades, and trades are executed using an **order size of 99.9%** of available capital.

### 6. **Why It Works**
The **EMA Cross Strategy** works well because:
- **Momentum Detection**: EMAs provide a smoothed representation of price trends, allowing the strategy to enter positions in the direction of the dominant trend.
- **Quick Reactions**: The use of a shorter EMA (12-day) ensures the strategy reacts quickly to changing market conditions, while the longer EMA (26-day) prevents it from reacting to insignificant price fluctuations.
- **Strong Market Movements**: Cryptocurrency markets like Dogecoin exhibit high volatility, which makes them ideal for capturing quick, substantial price movements. By focusing on crossover points, the strategy avoids low-momentum periods and capitalizes on significant trends.

This approach allows for systematic and disciplined trading, reducing emotional bias and ensuring timely entry and exit points during trending markets.

## Set Up

1. Install [poetry](https://python-poetry.org/)

2. Clone repo: 
```bash
git clone https://github.com/balojey/balo-orderly-submission
```

3. Change directory:
```bash
cd balo-orderly-submission
```

4. Install dependencies:
```bash
poetry install
```

5. Run strategy:
```bash
poetry run python ema_cross.py
```