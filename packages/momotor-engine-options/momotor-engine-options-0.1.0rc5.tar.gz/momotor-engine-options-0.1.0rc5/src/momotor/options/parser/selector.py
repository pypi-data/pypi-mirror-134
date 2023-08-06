import collections
import typing

from momotor.bundles.elements.base import Element
from momotor.options.parser.modifier import parse_mod
from momotor.options.parser.reference import parse_reference, generate_reference, Reference, ReferenceMatch
from momotor.options.parser.consts import VALUE_ATTR, OPERATIONS, OPERATIONS_WITHOUT_VALUE, CONDITION_RE
from momotor.options.providers import Providers
from momotor.options.task_id import StepTaskId


def parse_selector(selector: str, task_id: typing.Optional[StepTaskId]) \
        -> typing.Tuple[
            str,
            typing.Optional[str],
            typing.Tuple[Reference],
            typing.Optional[str],
            typing.Union[None, str, int, float],
            str
        ]:
    """ Parse a :ref:`selector <selector>` into its parts.

    :param selector: the :token:`~selector:selector` to parse
    :param task_id: a :py:class:`~momotor.options.task_id.StepTaskId` to use to expand task references in the ``id``.
    :return: a 6-tuple containing
             the :token:`~reference:type`,
             the :token:`~reference:provider`,
             a tuple of :py:class:`~momotor.options.parser.reference.Reference` objects,
             the `operator`,
             the `value`, and
             a string with the rest of the `selector` string remaining after parsing.
    :raises ValueError: the selector cannot be parsed

    Examples:

    >>> parse_selector('pass', None)
    ('pass', None, (), None, None, '')

    >>> parse_selector('prop[#test]!', None)
    ('prop', None, (Reference(id='test', name=None, _source='#test'),), '!', None, '')

    >>> parse_selector('prop[#test]?', None)
    ('prop', None, (Reference(id='test', name=None, _source='#test'),), '?', None, '')

    >>> parse_selector('prop[#test]?123', None)
    ('prop', None, (Reference(id='test', name=None, _source='#test'),), '?', None, '123')

    >>> parse_selector('prop[#test]>0', None)
    ('prop', None, (Reference(id='test', name=None, _source='#test'),), '>', 0, '')

    >>> parse_selector('prop[#test]>1_000', None)
    ('prop', None, (Reference(id='test', name=None, _source='#test'),), '>', 1000, '')

    >>> parse_selector('prop[#test]>1.5', None)
    ('prop', None, (Reference(id='test', name=None, _source='#test'),), '>', 1.5, '')

    >>> parse_selector('prop[#test]>-2', None)
    ('prop', None, (Reference(id='test', name=None, _source='#test'),), '>', -2, '')

    >>> parse_selector('prop[#test]>-2e2', None)
    ('prop', None, (Reference(id='test', name=None, _source='#test'),), '>', -200.0, '')

    >>> parse_selector('prop[#test]>2e-2', None)
    ('prop', None, (Reference(id='test', name=None, _source='#test'),), '>', 0.02, '')

    >>> parse_selector('prop[#test]=="test string"', None)
    ('prop', None, (Reference(id='test', name=None, _source='#test'),), '==', 'test string', '')

    >>> parse_selector('prop[#test]>0 123', None)
    ('prop', None, (Reference(id='test', name=None, _source='#test'),), '>', 0, ' 123')

    >>> parse_selector('prop[#test.$0]>0 123', StepTaskId('step', (1, 2, 3)))
    ('prop', None, (Reference(id='test.1', name=None, _source='#test.$0'),), '>', 0, ' 123')

    >>> parse_selector('prop[#test.$0-1]>0 123', StepTaskId('step', (1, 2, 3)))
    ('prop', None, (Reference(id='test.0', name=None, _source='#test.$0-1'),), '>', 0, ' 123')

    >>> parse_selector('prop[#test.$0-1.*]>0 123', StepTaskId('step', (1, 2, 3)))
    ('prop', None, (Reference(id='test.0.*', name=None, _source='#test.$0-1.*'),), '>', 0, ' 123')

    >>> parse_selector('prop[#test.$0-2.*]>0 123', StepTaskId('step', (1, 2, 3)))
    ('prop', None, (), '>', 0, ' 123')

    >>> parse_selector('prop[#test.$@]>0 123', StepTaskId('step', (1, 2, 3)))
    ('prop', None, (Reference(id='test.1.2.3', name=None, _source='#test.$@'),), '>', 0, ' 123')

    :return:
    """
    type_, provider, refs, remainder = parse_reference(selector, task_id)
    if not type_:
        # A selector without reference makes no sense
        raise ValueError(f"Invalid selector {selector!r}")

    m_oper_value = CONDITION_RE.match(remainder)

    if m_oper_value:
        oper = m_oper_value.group('oper')
        value = m_oper_value.group('value')
    else:
        oper, value = None, None

    if oper or value:
        remainder = remainder[m_oper_value.end(m_oper_value.lastindex):]

    if oper:
        assert oper in OPERATIONS.keys()
    else:
        oper = None

    if value == '' or value is None:
        if oper not in OPERATIONS_WITHOUT_VALUE:
            raise ValueError(f"Invalid selector {selector!r} (operator {oper!r} requires a value)")

        value = None

    elif oper not in OPERATIONS_WITHOUT_VALUE:
        if value.startswith("'"):
            assert value.endswith("'")
            value = value[1:-1]
        elif value.startswith('"'):
            assert value.endswith('"')
            value = value[1:-1]
        elif '.' in value or 'e' in value:
            value = float(value)
        else:
            value = int(value)

    elif value:
        # The operator does not expect a value, so it's part of the remainder
        remainder = value + remainder
        value = None

    return type_, provider, refs, oper, value, remainder


def resolve_selector(selector: str, bundles: Providers) \
        -> typing.Tuple[
            typing.Optional[str],
            str,
            typing.Iterable[ReferenceMatch],
            typing.Callable,
            typing.Union[None, str, int, float],
            str
        ]:
    """ Resolve all parts of a :ref:`selector <selector>`

    :param selector: the :token:`~selector:selector` to parse
    :param bundles: The bundles to resolve the references too
    :return: A 6-tuple containing
             the :token:`~reference:provider`,
             the attribute to get the reference value from (based on :token:`~reference:type`),
             an iterator for :py:class:`~momotor.options.parser.reference.ReferenceMatch` objects,
             the `operator`,
             the `value`, and
             a string with the rest of the `selector` string remaining after parsing.
    :raises ValueError: if the selector is not valid
    """

    type_, provider, refs, oper, value, remainder = parse_selector(selector, bundles.task_id)

    try:
        matches = generate_reference(type_, provider, refs, bundles)
    except ValueError as exc:
        raise ValueError(f"Invalid {type_!r} selector {selector!r}: {exc}")

    attr = VALUE_ATTR.get(type_, VALUE_ATTR[None])
    oper = OPERATIONS.get(oper)

    return provider, attr, matches, oper, value, remainder


def filter_by_selector(selector: str, bundles: Providers) \
        -> typing.Tuple[typing.Optional[str], typing.Tuple[Element], str]:
    """ Filter the elements selected by :ref:`selector <selector>` from the bundles

    :param selector: the :token:`~selector:selector` to parse
    :param bundles: The bundles to resolve the references too
    :return: a 3-tuple containing
             the :token:`~reference:provider`,
             a tuple with the selected elements, and
             a string with the rest of the `selector` string remaining after parsing.
    :raises ValueError: if the selector is not valid
    """
    provider, attr, matches, oper, value, remainder = resolve_selector(selector, bundles)

    results: typing.MutableSequence[Element] = collections.deque()
    for match in matches:
        obj_values = [getattr(mv, attr, None) for mv in match.values]
        for obj_value in obj_values:
            if oper(obj_value, value):
                results.append(match.provider)
                break

    return provider, tuple(results), remainder


def match_by_selector(selector: str, bundles: Providers) -> typing.Tuple[bool, str]:
    """ Match the elements selected by :ref:`match selector <match>` from the bundles

    :param selector: the :token:`~match:match` selector to parse
    :param bundles: The bundles to resolve the references too
    :return: a 2-tuple containing
             a boolean indicating if there was a match, and
             a string with the rest of the `selector` string remaining after parsing.
    :raises ValueError: if the selector is not valid
    """
    mod, selector = parse_mod(selector)
    if mod and mod not in {'any', 'all'}:
        raise ValueError(f"Invalid modifier {mod!r} for selector {selector!r}")

    provider, attr, matches, oper, value, remainder = resolve_selector(selector, bundles)

    matched_any = False
    for match in matches:
        obj_values = [getattr(mv, attr, None) for mv in match.values]
        if not obj_values and mod != 'any':
            return False, remainder

        matched_any = True
        for obj_value in obj_values:
            if mod == 'any':
                if oper(obj_value, value):
                    return True, remainder
            else:
                if not oper(obj_value, value):
                    return False, remainder

    return matched_any and mod != 'any', remainder
