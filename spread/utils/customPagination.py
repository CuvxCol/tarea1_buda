from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from typing import OrderedDict

class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        next_page = self.page.number + 1 if self.page.has_next() else None
        previous_page = self.page.number - 1 if self.page.has_previous() else None
        return Response(
            OrderedDict([
                ('count', self.page.paginator.count),
                ('previous_link', self.get_previous_link()),
                ('next_link', self.get_next_link()),
                ('previous', previous_page),
                ('next', next_page),
                ('pages', self.page.paginator.num_pages),
                ('page_size', int(self.page_size)),
                ('current', self.page.number),
                ('results', data)
        ]))