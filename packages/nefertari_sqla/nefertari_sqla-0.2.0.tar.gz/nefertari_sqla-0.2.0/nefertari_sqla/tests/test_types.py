import datetime

import pytest
from mock import patch, Mock
from sqlalchemy.dialects.postgresql import HSTORE

from .. import fields
from .. import types
from .fixtures import memory_db, db_session, simple_model


class DemoClass(object):
    def __init__(self, *args, **kwargs):
        pass


class TestProcessableMixin(object):

    class Processable(types.ProcessableMixin, DemoClass):
        pass

    def test_process_bind_param(self):
        processors = [
            lambda v: v.lower(),
            lambda v: v.strip(),
            lambda v: 'Processed ' + v,
        ]
        mixin = self.Processable(processors=processors)
        value = mixin.process_bind_param(' WeIrd ValUE   ', None)
        assert value == 'Processed weird value'

    def test_process_bind_param_no_processors(self):
        mixin = self.Processable()
        value = mixin.process_bind_param(' WeIrd ValUE   ', None)
        assert value == ' WeIrd ValUE   '


class TestLengthLimitedStringMixin(object):

    class Limited(types.LengthLimitedStringMixin, DemoClass):
        pass

    def test_none_value(self):
        mixin = self.Limited(min_length=5)
        try:
            mixin.process_bind_param(None, None)
        except ValueError:
            raise Exception('Unexpected exception')

    def test_min_length(self):
        mixin = self.Limited(min_length=5)
        with pytest.raises(ValueError) as ex:
            mixin.process_bind_param('q', None)
        assert str(ex.value) == 'Value length must be more than 5'
        try:
            mixin.process_bind_param('asdasdasd', None)
        except ValueError:
            raise Exception('Unexpected exception')

    def test_max_length(self):
        mixin = self.Limited(max_length=5)
        with pytest.raises(ValueError) as ex:
            mixin.process_bind_param('asdasdasdasdasd', None)
        assert str(ex.value) == 'Value length must be less than 5'
        try:
            mixin.process_bind_param('q', None)
        except ValueError:
            raise Exception('Unexpected exception')

    def test_min_and_max_length(self):
        mixin = self.Limited(max_length=5, min_length=2)
        with pytest.raises(ValueError) as ex:
            mixin.process_bind_param('a', None)
        assert str(ex.value) == 'Value length must be more than 2'
        with pytest.raises(ValueError) as ex:
            mixin.process_bind_param('a12313123123', None)
        assert str(ex.value) == 'Value length must be less than 5'
        try:
            mixin.process_bind_param('12q', None)
        except ValueError:
            raise Exception('Unexpected exception')


class TestSizeLimitedNumberMixin(object):

    class Limited(types.SizeLimitedNumberMixin, DemoClass):
        pass

    def test_none_value(self):
        mixin = self.Limited(min_value=5)
        try:
            mixin.process_bind_param(None, None)
        except ValueError:
            raise Exception('Unexpected exception')

    def test_min_value(self):
        mixin = self.Limited(min_value=5)
        with pytest.raises(ValueError) as ex:
            mixin.process_bind_param(1, None)
        assert str(ex.value) == 'Value must be bigger than 5'
        try:
            mixin.process_bind_param(10, None)
        except ValueError:
            raise Exception('Unexpected exception')

    def test_max_value(self):
        mixin = self.Limited(max_value=5)
        with pytest.raises(ValueError) as ex:
            mixin.process_bind_param(10, None)
        assert str(ex.value) == 'Value must be less than 5'
        try:
            mixin.process_bind_param(1, None)
        except ValueError:
            raise Exception('Unexpected exception')

    def test_min_and_max_value(self):
        mixin = self.Limited(max_value=5, min_value=2)
        with pytest.raises(ValueError) as ex:
            mixin.process_bind_param(1, None)
        assert str(ex.value) == 'Value must be bigger than 2'
        with pytest.raises(ValueError) as ex:
            mixin.process_bind_param(10, None)
        assert str(ex.value) == 'Value must be less than 5'
        try:
            mixin.process_bind_param(3, None)
        except ValueError:
            raise Exception('Unexpected exception')


class TestProcessableChoice(object):

    def test_no_choices(self):
        field = types.ProcessableChoice()
        with pytest.raises(ValueError) as ex:
            field.process_bind_param('foo', None)
        assert str(ex.value) == \
            'Got an invalid choice `foo`. Valid choices: ()'

    def test_none_value(self):
        field = types.ProcessableChoice()
        try:
            field.process_bind_param(None, None)
        except ValueError:
            raise Exception('Unexpected error')

    def test_value_not_in_choices(self):
        field = types.ProcessableChoice(choices=['foo'])
        with pytest.raises(ValueError) as ex:
            field.process_bind_param('bar', None)
        assert str(ex.value) == \
            'Got an invalid choice `bar`. Valid choices: (foo)'

    def test_value_in_choices(self):
        field = types.ProcessableChoice(choices=['foo'])
        try:
            field.process_bind_param('foo', None)
        except ValueError:
            raise Exception('Unexpected error')

    def test_processed_value_in_choices(self):
        field = types.ProcessableChoice(
            choices=['foo'],
            processors=[lambda v: v.lower()])
        try:
            field.process_bind_param('FoO', None)
        except ValueError:
            raise Exception('Unexpected error')

    def test_choices_not_sequence(self):
        field = types.ProcessableChoice(choices='foo')
        try:
            field.process_bind_param('foo', None)
        except ValueError:
            raise Exception('Unexpected error')


class TestProcessableInterval(object):

    def test_passing_seconds(self):
        field = types.ProcessableInterval()
        value = field.process_bind_param(36000, None)
        assert isinstance(value, datetime.timedelta)
        assert value.seconds == 36000

    def test_passing_timedelta(self):
        field = types.ProcessableInterval()
        value = field.process_bind_param(datetime.timedelta(seconds=60), None)
        assert isinstance(value, datetime.timedelta)


class TestProcessableDict(object):

    def test_load_dialect_impl_postgresql(self):
        field = types.ProcessableDict()
        dialect = Mock()
        dialect.name = 'postgresql'
        field.load_dialect_impl(dialect=dialect)
        assert field.is_postgresql
        dialect.type_descriptor.assert_called_once_with(HSTORE)

    def test_load_dialect_impl_not_postgresql(self):
        from sqlalchemy.types import UnicodeText
        field = types.ProcessableDict()
        dialect = Mock()
        dialect.name = 'some_other'
        field.load_dialect_impl(dialect=dialect)
        assert not field.is_postgresql
        dialect.type_descriptor.assert_called_once_with(UnicodeText)

    def test_process_bind_param_postgres(self):
        field = types.ProcessableDict()
        dialect = Mock()
        dialect.name = 'postgresql'
        assert {'q': 'f'} == field.process_bind_param({'q': 'f'}, dialect)

    def test_process_bind_param_not_postgres(self):
        field = types.ProcessableDict()
        dialect = Mock()
        dialect.name = 'some_other'
        assert '{"q": "f"}' == field.process_bind_param({'q': 'f'}, dialect)

    def test_process_result_value_postgres(self):
        field = types.ProcessableDict()
        dialect = Mock()
        dialect.name = 'postgresql'
        assert {'q': 'f'} == field.process_result_value({'q': 'f'}, dialect)

    def test_process_result_value_not_postgres(self):
        field = types.ProcessableDict()
        dialect = Mock()
        dialect.name = 'some_other'
        assert {'q': 'f'} == field.process_result_value('{"q": "f"}', dialect)


class TestProcessableChoiceArray(object):

    @patch.object(types, 'ARRAY')
    @patch.object(types.types, 'UnicodeText')
    def test_load_dialect_impl_postgresql(self, mock_unic, mock_array):
        field = types.ProcessableChoiceArray(item_type=fields.StringField)
        dialect = Mock()
        dialect.name = 'postgresql'
        field.load_dialect_impl(dialect=dialect)
        assert field.is_postgresql
        assert not mock_unic.called
        assert mock_array.called

    @patch.object(types, 'ARRAY')
    @patch.object(types.types, 'UnicodeText')
    def test_load_dialect_impl_not_postgresql(self, mock_unic, mock_array):
        field = types.ProcessableChoiceArray(item_type=fields.StringField)
        dialect = Mock()
        dialect.name = 'some_other'
        field.load_dialect_impl(dialect=dialect)
        assert not field.is_postgresql
        assert mock_unic.called
        assert not mock_array.called

    def test_choices_not_sequence(self):
        field = types.ProcessableChoiceArray(
            item_type=fields.StringField, choices='foo')
        assert field.choices == ['foo']

    def test_validate_choices_no_choices(self):
        field = types.ProcessableChoiceArray(item_type=fields.StringField)
        assert field.choices is None
        try:
            field._validate_choices(['foo'])
        except ValueError:
            raise Exception('Unexpected error')

    def test_validate_choices_no_value(self):
        field = types.ProcessableChoiceArray(
            item_type=fields.StringField, choices=['foo'])
        try:
            field._validate_choices(None)
        except ValueError:
            raise Exception('Unexpected error')

    def test_validate_choices_valid(self):
        field = types.ProcessableChoiceArray(
            item_type=fields.StringField,
            choices=['foo', 'bar'])
        try:
            field._validate_choices(['foo'])
        except ValueError:
            raise Exception('Unexpected error')

    def test_validate_choices_invalid(self):
        field = types.ProcessableChoiceArray(
            item_type=fields.StringField,
            choices=['foo', 'bar'])
        with pytest.raises(ValueError) as ex:
            field._validate_choices(['qoo', 'foo'])
        assert str(ex.value) == (
            'Got invalid choices: (qoo). Valid choices: (foo, bar)')

    def test_process_bind_param_postgres(self):
        field = types.ProcessableChoiceArray(item_type=fields.StringField)
        dialect = Mock()
        dialect.name = 'postgresql'
        assert ['q'] == field.process_bind_param(['q'], dialect)

    def test_process_bind_param_not_postgres(self):
        field = types.ProcessableChoiceArray(item_type=fields.StringField)
        dialect = Mock()
        dialect.name = 'some_other'
        assert '["q"]' == field.process_bind_param(['q'], dialect)

    def test_process_result_value_postgres(self):
        field = types.ProcessableChoiceArray(item_type=fields.StringField)
        dialect = Mock()
        dialect.name = 'postgresql'
        assert ['q'] == field.process_result_value(['q'], dialect)

    def test_process_result_value_not_postgres(self):
        field = types.ProcessableChoiceArray(item_type=fields.StringField)
        dialect = Mock()
        dialect.name = 'some_other'
        assert ['q'] == field.process_result_value('["q"]', dialect)
