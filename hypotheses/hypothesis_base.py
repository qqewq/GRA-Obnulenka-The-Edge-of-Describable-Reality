class GRAHypothesis:
    def __init__(self, name):
        self.name = name

    def build_potential(self):
        raise NotImplementedError

    def configure_sims(self):
        raise NotImplementedError

    def expected_signatures(self):
        raise NotImplementedError
