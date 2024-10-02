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
    days_length_1: 12 days length for 
        calculating 12 days EMA.
    days_length_2: 26 days length for 
        calculating 26 days EMA.
    length: The number of days the Strategy is 
        intended to run for.
    """

    order_size: float = 0.999
    days_length_1: int = 12
    days_length_2: int = 26
    
    @classmethod
    def update_lags(cls, days_length_1, days_length_2):
        cls.days_length_1 = days_length_1
        cls.days_length_2 = days_length_2

    def init(self):
        close = self.data.close
        self.ema_days_1 = self.I(EMA, close, self.days_length_1)
        self.ema_days_2 = self.I(EMA, close, self.days_length_2)

    def next(self):
        if (
            crossover(self.ema_days_1, self.ema_days_2)
        ):
            self.position.close()
            self.buy(size=self.order_size)
        elif (
            crossover(self.ema_days_2, self.ema_days_1)
        ):
            self.position.close()
            self.sell(size=self.order_size)


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
        interval=Interval.five_minute,
        asset=PerpetualAssetType.DOGE,
    )

    # backtest
    tester.backtest()

    # plot
    tester.plot(show_price_data=False)
    plt.show()

asyncio.run(main())