import os
import unittest

from readability import Document


SAMPLES = os.path.join(os.path.dirname(__file__), 'samples')


def load_sample(filename):
    """Helper to get the content out of the sample files"""
    return open(os.path.join(SAMPLES, filename)).read()


class TestArticleOnly(unittest.TestCase):
    """The option to not get back a full html doc should work

    Given a full html document, the call can request just divs of processed
    content. In this way the developer can then wrap the article however they
    want in their own view or application.

    """

    def test_si_sample(self):
        """Using the si sample, load article with only opening body element"""
        sample = load_sample('si-game.sample.html')
        doc = Document(
            sample,
            url='http://sportsillustrated.cnn.com/baseball/mlb/gameflash/2012/04/16/40630_preview.html')
        res = doc.summary()
        self.assertEqual('<html><body><div><div class', res[0:27])

    def test_si_sample_html_partial(self):
        """Using the si sample, make sure we can get the article alone."""
        sample = load_sample('si-game.sample.html')
        doc = Document(sample, url='http://sportsillustrated.cnn.com/baseball/mlb/gameflash/2012/04/16/40630_preview.html')
        res = doc.summary(html_partial=True)
        self.assertEqual('<div><div class="', res[0:17])

    def test_too_many_images_sample_html_partial(self):
        """Using the too-many-images sample, make sure we still get the article."""
        sample = load_sample('too-many-images.sample.html')
        doc = Document(sample)
        res = doc.summary(html_partial=True)
        self.assertEqual('<div><div class="post-body', res[0:26])

    def test_wrong_link_issue_49(self):
        """We shouldn't break on bad HTML."""
        sample = load_sample('the-hurricane-rubin-carter-denzel-washington.html')
        doc = Document(sample)
        res = doc.summary(html_partial=True)
        self.assertEqual('<div><div class="content__article-body ', res[0:39])
