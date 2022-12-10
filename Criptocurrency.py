from datetime import datetime
class Criptocurrency:

    name: str
    symbol: str
    slug: str
    num_market_pairs: int
    total_supply: int
    max_supply: int
    eur_price: float
    market_cap: float
    last_updated: datetime

    def __init__(self, data: dict):
        self.name = data['name']
        self.symbol = data['symbol']
        self.slug = data['slug']
        self.num_market_pairs = data['num_market_pairs']
        self.total_supply = data['total_supply']
        self.max_supply = data['max_supply']
        self.eur_price = data['quote']['EUR']['price']
        self.market_cap = data['quote']['EUR']['market_cap']
        self.last_updated = datetime.strptime(data['last_updated'].split('T')[0], '%Y-%m-%d')


def get_marketcap(c: Criptocurrency) -> float:
    return c.market_cap
