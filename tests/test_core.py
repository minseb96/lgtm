from unittest import TestCase, skip


class LgtmTest(TestCase):
    @skip
    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm('./python.jpeg', 'LGTM'))
