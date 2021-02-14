import sys

import pytest

from base.npm_page import NPMPage


@pytest.mark.npm
@pytest.mark.parametrize('search', ['react', 'vue'
])
@pytest.mark.parametrize('page', [NPMPage], indirect=['page', ])
class TestNPMPage:
    # @pytest.mark.skip
    def test_search_positive(self, page, search):
        page.fill_search_input(search[0])
        page.click_search_button()
        assert page.get_result_list(search[0]), \
            f'search for "{search[0]}" not gave any results'

    # @pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
    # def test_search_negative(self, page, search):
    #     page.fill_search_input(search[0])
    #     page.click_search_button()
    #     assert not page.get_result_list('angular'), \
    #         f'search for "{search[0]}" not gave any results'
