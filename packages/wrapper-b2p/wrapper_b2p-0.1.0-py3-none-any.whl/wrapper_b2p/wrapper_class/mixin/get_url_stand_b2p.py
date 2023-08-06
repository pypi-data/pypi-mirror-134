from ... import settings


class MixinGetURLStandB2P:
    is_prod_stand = False

    def _get_url_b2p(self) -> bool:
        if self.is_prod_stand:
            return settings.URL_PROD_STAND
        return settings.URL_TEST_STAND
