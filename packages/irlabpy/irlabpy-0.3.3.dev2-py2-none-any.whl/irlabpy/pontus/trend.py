from typing import Dict


class Trend:
    def __init__(self,trend):
        self.trend = trend


    def get_tags(self):
        return self.trend.tags

    def get_metrics(self):
        return self.trend.trends

if __name__ == "__main__":
    print('a')
