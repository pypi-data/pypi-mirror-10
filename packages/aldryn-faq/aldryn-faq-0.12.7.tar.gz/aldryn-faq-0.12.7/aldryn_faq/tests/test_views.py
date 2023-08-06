# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.http import Http404
from django.test.client import RequestFactory
from django.utils.translation import override

from ..views import FaqByCategoryView, FaqAnswerView

from .test_base import AldrynFaqTest


class TestFaqByCategoryView(AldrynFaqTest):
    def test_as_view(self):
        """Tests that the FaqByCategoryView produces the correct context."""
        category1 = self.reload(self.category1, "en")
        question1 = self.reload(self.question1, "en")

        kwargs = {"category_slug": category1.slug}
        with override('en'):
            category1_url = reverse(
                '{0}:faq-category'.format(self.app_config.namespace),
                kwargs=kwargs
            )
        factory = RequestFactory()
        request = factory.get(category1_url)
        request.user = self.user
        # We're not going through the middleware, and apphooks_config needs
        # 'current_page' to be set on the request objects, so...
        request.current_page = self.page
        try:
            response = FaqByCategoryView.as_view()(request, **kwargs)
        except Http404:
            self.fail('Could not find category')
        self.assertEqualItems(
            response.context_data['object_list'],
            [question1, ],
        )


class TestFaqAnswerView(AldrynFaqTest):
    def test_as_view(self):
        """Tests that the FaqAnswerView produces the correct context."""
        category1 = self.reload(self.category1, "en")
        question1 = self.reload(self.question1, "en")

        kwargs = {"category_slug": category1.slug, "pk": question1.id}
        with override('en'):
            url = reverse(
                '{0}:faq-answer'.format(self.app_config.namespace),
                kwargs=kwargs
            )
        factory = RequestFactory()
        request = factory.get(url)
        request.user = self.user
        # We're not going through the middleware, and apphooks_config needs
        # 'current_page' to be set on the request objects, so...
        request.current_page = self.page
        response = FaqAnswerView.as_view()(request, **kwargs)
        self.assertEqual(
            response.context_data['object'],
            question1,
        )

        # Now, check that manipulating the url to get an answer from the wrong
        # category returns a 404. In this case, we have to do it in DE, since
        # question2 is only available in that language.
        category1 = self.reload(self.category1, "de")
        question2 = self.reload(self.question2, "de")
        kwargs = {"category_slug": category1.slug, "pk": question2.pk}
        with override('de'):
            url = reverse(
                '{0}:faq-answer'.format(self.app_config.namespace),
                kwargs=kwargs
            )
        request = factory.get(url)
        request.user = self.user
        request.current_page = self.page
        with self.assertRaises(Http404):
            response = FaqAnswerView.as_view()(request, **kwargs)

        # Now, do that again, this time mixing the languages.
        category1 = self.reload(self.category1, "en")  # NOTE THESE DO NOT MATCH
        question2 = self.reload(self.question2, "de")
        kwargs = {"category_slug": category1.slug, "pk": question2.pk}
        with override('de'):  # NOTE THIS IS DE
            url = reverse(
                '{0}:faq-answer'.format(self.app_config.namespace),
                kwargs=kwargs
            )
        request = factory.get(url)
        request.user = self.user
        request.current_page = self.page
        with self.assertRaises(Http404):
            response = FaqAnswerView.as_view()(request, **kwargs)

        # Now, now the opposite way, for good measure.
        category1 = self.reload(self.category1, "en")  # NOTE THESE DO NOT MATCH
        question2 = self.reload(self.question2, "de")
        kwargs = {"category_slug": category1.slug, "pk": question2.pk}
        with override('en'):  # NOTE: THIS IS NOW EN
            url = reverse(
                '{0}:faq-answer'.format(self.app_config.namespace),
                kwargs=kwargs
            )
        request = factory.get(url)
        request.user = self.user
        request.current_page = self.page
        with self.assertRaises(Http404):
            response = FaqAnswerView.as_view()(request, **kwargs)
