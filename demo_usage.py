"""简单演示：如何调用一个可复用的交易信号函数。"""


def generate_signal(price_now: float, price_prev: float) -> str:
    """根据价格变化返回最基础的交易信号。"""
    if price_now > price_prev:
        return "BUY"
    if price_now < price_prev:
        return "SELL"
    return "HOLD"


def main() -> None:
    # 示例数据（可以替换成真实行情）
    yesterday_price = 100.0
    today_price = 103.5

    signal = generate_signal(today_price, yesterday_price)
    print(f"昨日价格: {yesterday_price}")
    print(f"今日价格: {today_price}")
    print(f"交易信号: {signal}")


if __name__ == "__main__":
    main()
