# -*- encoding: utf-8 -*-
'''
@File    :  __init__.py
@Time    :  2021/12/23 15:49:33
@Version :  1.0
@Desc    :  参考: https://github.com/vn-crypto/vnpy_bybit
'''


from datetime import timedelta
from typing import Dict, Set

from abquant.trader.common import Direction, Interval, OrderType, Status
from abquant.trader.object import ContractData


# 实盘REST API地址
REST_HOST = "https://api.bybit.com"

# 实盘Websocket API地址
INVERSE_WEBSOCKET_HOST = "wss://stream.bybit.com/realtime"
PUBLIC_WEBSOCKET_HOST = "wss://stream.bybit.com/realtime_public"
PRIVATE_WEBSOCKET_HOST = "wss://stream.bybit.com/realtime_private"

# 模拟盘REST API地址
TESTNET_REST_HOST = "https://api-testnet.bybit.com"

# 模拟盘Websocket API地址
TESTNET_INVERSE_WEBSOCKET_HOST = "wss://stream-testnet.bybit.com/realtime"
TESTNET_PUBLIC_WEBSOCKET_HOST = "wss://stream-testnet.bybit.com/realtime_public"
TESTNET_PRIVATE_WEBSOCKET_HOST = "wss://stream-testnet.bybit.com/realtime_private"

# 委托状态映射
STATUS_BYBIT2AB: Dict[str, Status] = {
    "Created": Status.NOTTRADED,
    "New": Status.NOTTRADED,
    "PartiallyFilled": Status.PARTTRADED,
    "Filled": Status.ALLTRADED,
    "Cancelled": Status.CANCELLED,
    "Rejected": Status.REJECTED,
}

# 委托类型映射
ORDER_TYPE_AB2BYBIT: Dict[OrderType, str] = {
    OrderType.LIMIT: "Limit",
    OrderType.MARKET: "Market",
}
ORDER_TYPE_BYBIT2AB: Dict[str, OrderType] = {v: k for k, v in ORDER_TYPE_AB2BYBIT.items()}

# 买卖方向映射
DIRECTION_AB2BYBIT: Dict[Direction, str] = {Direction.LONG: "Buy", Direction.SHORT: "Sell"}
DIRECTION_BYBIT2AB: Dict[str, Direction] = {v: k for k, v in DIRECTION_AB2BYBIT.items()}

# 数据频率映射
INTERVAL_AB2BYBIT: Dict[Interval, str] = {
    Interval.MINUTE: "1",
    Interval.HOUR: "60",
    Interval.DAILY: "D",
    Interval.WEEKLY: "W",
}
TIMEDELTA_MAP: Dict[Interval, timedelta] = {
    Interval.MINUTE: timedelta(minutes=1),
    Interval.HOUR: timedelta(hours=1),
    Interval.DAILY: timedelta(days=1),
    Interval.WEEKLY: timedelta(days=7),
}

# 反向永续合约类型列表
swap_symbols: Set[str] = set()

# 反向交割合约类型列表
futures_symbols: Set[str] = set()

# USDT永续合约类型列表
usdt_symbols: Set[str] = set()

# 本地委托号缓存集合
local_orderids: Set[str] = set()

symbol_contract_map: Dict[str, ContractData] = {}
