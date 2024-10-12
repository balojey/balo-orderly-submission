from typing import Union
import pandas_ta as ta
import pandas as pd
import asyncio
from dotenv import load_dotenv
import matplotlib.pyplot as plt

from eth_rpc import PrivateKeyWallet
from emp_orderly.utils import from_address
from emp_orderly import (
    Strategy, EmpOrderly,
    crossover, EMA,
    EmpyrealOrderlySDK,
)
from emp_orderly_types import PerpetualAssetType, Interval

load_dotenv()

wallet = PrivateKeyWallet.create_new()
orderly_id = from_address(wallet.address)

sdk = EmpyrealOrderlySDK(pvt_hex=wallet.private_key, account_id=orderly_id, is_testnet=True)

class EmaCross(Strategy):
    """Exponential Moving Average Death/Golden Cross Strategy.
    
    order_size: The amount of order that can be 
        made at a time.
    parameters: The parameters
    """

    # Define the strategy parameters
    parameters: dict[str, Union[int, float]] = {
        "fast_ema_period": 5,
        "slow_ema_period": 20,
        "rsi_period": 14,
        "rsi_overbought": 70,
        "rsi_oversold": 30,
        "risk_percentage": 0.02,  # 2% risk per trade
        "reward_risk_ratio": 2,   # Reward to risk ratio
    }

    order_size: float = 0.999
    
    def init(self):
        close = self.data.close
        self.fast_ema = self.I(EMA, close, self.parameters["fast_ema_period"])
        self.slow_ema = self.I(EMA, close, self.parameters["slow_ema_period"])
        self.current_price = self.data.df.close.iloc[-1]

    def next(self):
        rsi = ta.rsi(self.data.df.close, self.parameters["rsi_period"])
        current_rsi = rsi.iloc[-1]
        if (
            crossover(self.fast_ema, self.slow_ema)
            and
            self.parameters["rsi_oversold"] < current_rsi < self.parameters["rsi_overbought"]
        ):
            stop_loss_price = self.current_price * (1 - self.parameters["risk_percentage"])
            take_profit_price = self.current_price * (1 + self.parameters["risk_percentage"] * self.parameters["reward_risk_ratio"])
            limit_price = stop_loss_price + 0.001
            self.buy(size=self.order_size, sl=stop_loss_price, tp=take_profit_price, limit=limit_price)
        elif (
            crossover(self.slow_ema, self.fast_ema)
            and
            self.parameters["rsi_oversold"] < current_rsi < self.parameters["rsi_overbought"]
        ):
            stop_loss_price = self.current_price * (1 + self.parameters["risk_percentage"])
            take_profit_price = self.current_price * (1 - self.parameters["risk_percentage"] * self.parameters["reward_risk_ratio"])
            limit_price = stop_loss_price - 0.001
            self.sell(size=self.order_size, sl=stop_loss_price, tp=take_profit_price, limit=limit_price)


tester = EmpOrderly(
    cash=1000000,
    commission=.0000001,
    exclusive_orders=True,
    sdk=sdk,
)

# load strategy and data
tester.set_strategy(EmaCross)

async def main():
    await tester.load_data(
        lookback=14,
        interval=Interval.fifteen_minute,
        asset=PerpetualAssetType.SEI,
    )

    # backtest
    tester.backtest()

    # plot
    tester.plot(show_price_data=False)
    plt.show()

asyncio.run(main())