# coding: utf-8
# pylint: disable=R0912,E0102
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.template import Context, Template
import pytest

import django_tables2 as tables
from django_tables2.utils import build_request
from django_tables2 import A
from ..app.models import Person
from ..utils import attrs, warns


def test_unicode():
    """Test LinkColumn"""
    # test unicode values + headings
    class UnicodeTable(tables.Table):
        first_name = tables.LinkColumn('person', args=[A('pk')])
        last_name = tables.LinkColumn('person', args=[A('pk')], verbose_name='äÚ¨´ˆÁ˜¨ˆ˜˘Ú…Ò˚ˆπ∆ˆ´')

    dataset = [
        {'pk': 1, 'first_name': 'Brädley', 'last_name': '∆yers'},
        {'pk': 2, 'first_name': 'Chr…s', 'last_name': 'DÒble'},
        ]

    table = UnicodeTable(dataset)
    request = build_request('/some-url/')
    template = Template('{% load django_tables2 %}{% render_table table %}')
    html = template.render(Context({'request': request, 'table': table}))

    assert 'Brädley' in html
    assert '∆yers' in html
    assert 'Chr…s' in html
    assert 'DÒble' in html


@pytest.mark.django_db
def test_null_foreign_key():
    class PersonTable(tables.Table):
        first_name = tables.Column()
        last_name = tables.Column()
        occupation = tables.LinkColumn('occupation', args=[A('occupation.pk')])

    Person.objects.create(first_name='bradley', last_name='ayers')

    table = PersonTable(Person.objects.all())
    table.as_html()


def test_kwargs():
    class PersonTable(tables.Table):
        a = tables.LinkColumn('occupation', kwargs={"pk": A('a')})

    html = PersonTable([{"a": 0}, {"a": 1}]).as_html()
    assert reverse("occupation", kwargs={"pk": 0}) in html
    assert reverse("occupation", kwargs={"pk": 1}) in html


def test_html_escape_value():
    class PersonTable(tables.Table):
        name = tables.LinkColumn("escaping", kwargs={"pk": A("pk")})

    table = PersonTable([{"name": "<brad>", "pk": 1}])
    assert table.rows[0]["name"] == '<a href="/&amp;&#39;%22/1/">&lt;brad&gt;</a>'


def test_old_style_attrs_should_still_work():
    with warns(DeprecationWarning):
        class TestTable(tables.Table):
            col = tables.LinkColumn('occupation', kwargs={"pk": A('col')},
                                    attrs={"title": "Occupation Title"})

    table = TestTable([{"col": 0}])
    assert attrs(table.rows[0]["col"]) == {"href": reverse("occupation", kwargs={"pk": 0}),
                                           "title": "Occupation Title"}


def test_a_attrs_should_be_supported():
    class TestTable(tables.Table):
        col = tables.LinkColumn('occupation', kwargs={"pk": A('col')},
                                attrs={"a": {"title": "Occupation Title"}})

    table = TestTable([{"col": 0}])
    assert attrs(table.rows[0]["col"]) == {"href": reverse("occupation", kwargs={"pk": 0}),
                                           "title": "Occupation Title"}


def test_defaults():
    class Table(tables.Table):
        link = tables.LinkColumn('occupation', kwargs={"pk": 1}, default="xyz")

    table = Table([{}])
    assert table.rows[0]['link'] == 'xyz'
