class parses:
    @staticmethod
    def _clean_(x: str) -> str:
        return x.strip().lower().replace(',', '')

    @staticmethod
    def parse_int(x) -> int:
        try:
            return int(parses._clean_(x))
        except ValueError:
            return None

    @staticmethod
    def parse_float(x) -> float:
        try:
            return float(parses._clean_(x))
        except ValueError:
            return None
