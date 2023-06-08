#  This file is part of OctoBot (https://github.com/Drakkar-Software/OctoBot)
#  Copyright (c) 2023 Drakkar-Software, All rights reserved.
#
#  OctoBot is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  OctoBot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with OctoBot. If not, see <https://www.gnu.org/licenses/>.
import pytest

from additional_tests.exchanges_tests import abstract_authenticated_future_exchange_tester

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


class TestBybitFuturesAuthenticatedExchange(
    abstract_authenticated_future_exchange_tester.AbstractAuthenticatedFutureExchangeTester
):
    # enter exchange name as a class variable here
    EXCHANGE_NAME = "bybit"
    ORDER_CURRENCY = "BTC"
    SETTLEMENT_CURRENCY = "USDT"
    SYMBOL = f"{ORDER_CURRENCY}/{SETTLEMENT_CURRENCY}:{SETTLEMENT_CURRENCY}"
    INVERSE_SYMBOL = f"{ORDER_CURRENCY}/USD:{ORDER_CURRENCY}"
    ORDER_SIZE = 10  # % of portfolio to include in test orders
    OPEN_TIMEOUT = 25    # larger for bybit testnet
    CANCEL_TIMEOUT = 25  # larger for bybit testnet
    EDIT_TIMEOUT = 25    # larger for bybit testnet
    OPEN_ORDERS_IN_CLOSED_ORDERS = True
    SUPPORTS_GET_LEVERAGE = False

    async def test_get_portfolio(self):
        await super().test_get_portfolio()

    async def test_get_empty_linear_and_inverse_positions(self):
        await super().test_get_empty_linear_and_inverse_positions()

    async def test_get_and_set_margin_type(self):
        await super().test_get_and_set_margin_type()

    async def test_get_and_set_leverage(self):
        await super().test_get_and_set_leverage()

    async def test_create_and_cancel_limit_orders(self):
        await super().test_create_and_cancel_limit_orders()

    async def test_create_and_fill_market_orders(self):
        await super().test_create_and_fill_market_orders()

    async def test_get_my_recent_trades(self):
        await super().test_get_my_recent_trades()

    async def test_get_closed_orders(self):
        await super().test_get_closed_orders()

    async def test_create_and_cancel_stop_orders(self):
        # pass if not implemented
        await super().test_create_and_cancel_stop_orders()

    async def test_edit_limit_order(self):
        # pass if not implemented
        await super().test_edit_limit_order()

    async def test_edit_stop_order(self):
        # pass if not implemented
        await super().test_edit_stop_order()

    async def test_create_single_bundled_orders(self):
        await super().test_create_single_bundled_orders()

    async def test_create_double_bundled_orders(self):
        await super().test_create_double_bundled_orders()
