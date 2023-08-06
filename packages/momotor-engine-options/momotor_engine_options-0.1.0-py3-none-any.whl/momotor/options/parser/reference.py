import collections
import typing
from dataclasses import dataclass

from momotor.bundles import RecipeBundle, ConfigBundle, ProductBundle, ResultsBundle
from momotor.bundles.elements.files import FilesMixin, File
from momotor.bundles.elements.options import OptionsMixin, Option
from momotor.bundles.elements.properties import PropertiesMixin, Property
from momotor.bundles.elements.result import Outcome, Result
from momotor.bundles.elements.steps import Step
from momotor.bundles.utils.text import smart_split
from momotor.options.parser.consts import VALUE_ATTR, REFERENCE_RE, PROVIDER_RE, REF_RE
from momotor.options.parser.modifier import parse_mod, apply_combiner_modifier
from momotor.options.providers import Providers
from momotor.options.task_id import StepTaskId, apply_task_number


ProviderElement = typing.Union[RecipeBundle, ConfigBundle, ProductBundle, Step, Result]
ValueElement = typing.Union[Property, File, Option, Result]


@dataclass(frozen=True)
class Reference:
    """ A reference
    """

    #: The ``id`` of the reference
    id: typing.Optional[str]

    #: The ``name`` of the reference, including the class or domain parts
    name: typing.Optional[str]

    #: The original string from which this reference was parsed (used in exceptions)
    _source: str


@dataclass(frozen=True)
class ReferenceMatch:
    """ A reference match
    """

    #: The provider containing the elements referenced
    provider: ProviderElement

    #: A tuple with the referenced elements
    values: typing.Tuple[ValueElement]


def _split_reference(reference: str) -> typing.Tuple[typing.Optional[str], typing.Optional[str], str]:
    """ Split a :ref:`reference` into its string parts.

    :param reference: the reference to parse
    :return: a 3-tuple containing
             the :token:`~reference:type`,
             a string with the options between ``[]``, and
             a string with the rest of the string remaining after parsing.

    >>> _split_reference("type")
    ('type', None, '')

    >>> _split_reference("type rest")
    ('type', None, ' rest')

    >>> _split_reference("type[]")
    ('type', '', '')

    >>> _split_reference("type []")
    ('type', '', '')

    >>> _split_reference("type[ ]")
    ('type', '', '')

    >>> _split_reference("type[] rest")
    ('type', '', ' rest')

    >>> _split_reference("type[option]")
    ('type', 'option', '')

    >>> _split_reference("type [option]")
    ('type', 'option', '')

    >>> _split_reference("type [ option ]")
    ('type', 'option', '')

    >>> _split_reference("type[option] ")
    ('type', 'option', ' ')

    :param reference:
    :return:
    """
    m_ref = REFERENCE_RE.match(reference)
    if m_ref is None:
        return None, None, reference

    type_ = m_ref.group('type')
    ref_option = m_ref.group('opt')
    if ref_option:
        ref_option = ref_option[1:-1].strip()

    remainder = reference[m_ref.end(m_ref.lastindex):]

    return type_, ref_option, remainder


def _split_options(ref_option: str, task_id: typing.Optional[StepTaskId]) \
        -> typing.Tuple[typing.Optional[str], typing.Tuple[Reference], str]:
    """ Split the options of a reference (the part between ``[]``)

    :param ref_option: the reference options to parse
    :param task_id: a :py:class:`~momotor.options.task_id.StepTaskId` to use to expand task references in the ``id``.
    :return: a 3-tuple containing
             the :token:`~reference:provider`,
             a tuple of :py:class:`Reference` objects, and
             a string with the rest of the string remaining after parsing.

    Examples: (not all of these variants make sense, but the syntax is legal)

    >>> _split_options('@provider', None)
    ('provider', (), '')

    >>> _split_options('@provider#id', None)
    ('provider', (Reference(id='id', name=None, _source='#id'),), '')

    >>> _split_options('@provider:class#name', None)
    ('provider', (Reference(id=None, name='class#name', _source=':class#name'),), '')

    >>> _split_options('@provider:name', None)
    ('provider', (Reference(id=None, name='name', _source=':name'),), '')

    >>> _split_options('@provider#id:class#name', None)
    ('provider', (Reference(id='id', name='class#name', _source='#id:class#name'),), '')

    >>> _split_options('@provider#id:name', None)
    ('provider', (Reference(id='id', name='name', _source='#id:name'),), '')

    >>> _split_options('@provider #id, id2 : class#name', None)
    ('provider', (Reference(id='id', name='class#name', _source='#id, id2 : class#name'), Reference(id='id2', name='class#name', _source='#id, id2 : class#name')), '')

    >>> _split_options('#id', None)
    (None, (Reference(id='id', name=None, _source='#id'),), '')

    >>> _split_options('#id:name', None)
    (None, (Reference(id='id', name='name', _source='#id:name'),), '')

    >>> _split_options('#id:class#name', None)
    (None, (Reference(id='id', name='class#name', _source='#id:class#name'),), '')

    >>> _split_options(':name', None)
    (None, (Reference(id=None, name='name', _source=':name'),), '')

    >>> _split_options(':class#name', None)
    (None, (Reference(id=None, name='class#name', _source=':class#name'),), '')

    >>> _split_options('#id, id2', None)
    (None, (Reference(id='id', name=None, _source='#id, id2'), Reference(id='id2', name=None, _source='#id, id2')), '')

    >>> _split_options('#id.$0:class#name', StepTaskId('test', (11,)))
    (None, (Reference(id='id.11', name='class#name', _source='#id.$0:class#name'),), '')

    >>> _split_options('#id.$1:class#name', StepTaskId('test', (11, 12)))
    (None, (Reference(id='id.12', name='class#name', _source='#id.$1:class#name'),), '')

    >>> _split_options('#id.$@:class#name', StepTaskId('test', (11, 12)))
    (None, (Reference(id='id.11.12', name='class#name', _source='#id.$@:class#name'),), '')

    >>> _split_options('#id.$0-1:class#name', StepTaskId('test', (11, 12)))
    (None, (Reference(id='id.10', name='class#name', _source='#id.$0-1:class#name'),), '')

    >>> _split_options('#id.$1+1:class#name', StepTaskId('test', (11, 12)))
    (None, (Reference(id='id.13', name='class#name', _source='#id.$1+1:class#name'),), '')

    >>> _split_options('#id.$1/2:class#name', StepTaskId('test', (11, 12)))
    (None, (Reference(id='id.6', name='class#name', _source='#id.$1/2:class#name'),), '')

    >>> _split_options('#id.$1*2:class#name', StepTaskId('test', (11, 12)))
    (None, (Reference(id='id.24', name='class#name', _source='#id.$1*2:class#name'),), '')

    >>> _split_options('#id.$1%10:class#name', StepTaskId('test', (11, 12)))
    (None, (Reference(id='id.2', name='class#name', _source='#id.$1%10:class#name'),), '')

    >>> _split_options('#id.$0-1:class#name', StepTaskId('test', (0,)))
    (None, (), '')

    :param ref_option:
    :return:
    """
    m_provider = PROVIDER_RE.match(ref_option)

    provider = m_provider.group('provider')
    if provider:
        remaining = ref_option[m_provider.end(m_provider.lastindex):]
    else:
        remaining = ref_option

    refs: typing.MutableSequence[Reference] = collections.deque()
    if remaining.strip():
        m_ref = REF_RE.match(remaining)
        if m_ref:
            ids_str = m_ref.group('ids')
            name = m_ref.group('name') or None
        else:
            ids_str, name = None, None

        if ids_str or name:
            end_pos = m_ref.end(m_ref.lastindex)
            source, remaining = remaining[:end_pos].strip(), remaining[end_pos:]

            ids: typing.List[typing.Optional[str]]
            if not ids_str:
                ids = [None]
            else:
                ids = [id_.strip() for id_ in ids_str.split(',')]

            for id_ in ids:
                if id_ or name:
                    if id_ and task_id:
                        id_ = apply_task_number(id_, task_id)
                        if '#' in id_:
                            continue

                    refs.append(
                        Reference(id_, name, source)
                    )

    return provider, tuple(refs), remaining


def parse_reference(reference: str, task_id: typing.Optional[StepTaskId]) \
        -> typing.Tuple[str, typing.Optional[str], typing.Tuple[Reference], str]:
    """ Parse a :ref:`reference <reference>` into its parts.

    :param reference: the reference to parse
    :param task_id: a :py:class:`~momotor.options.task_id.StepTaskId` to use to expand task references in the ``id``.
    :return: a 4-tuple containing
             the :token:`~reference:type`,
             the :token:`~reference:provider`,
             a tuple of :py:class:`Reference` objects, and
             a string with the rest of the `reference` string remaining after parsing.
    :raises ValueError: the reference cannot be parsed

    Examples:

    >>> parse_reference("type", None)
    ('type', None, (), '')

    >>> parse_reference("type rest", None)
    ('type', None, (), ' rest')

    >>> parse_reference("type[] rest", None)
    ('type', None, (), ' rest')

    >>> parse_reference("type[@provider] rest", None)
    ('type', 'provider', (), ' rest')

    >>> parse_reference("type[@provider#id:class#name] rest", None)
    ('type', 'provider', (Reference(id='id', name='class#name', _source='#id:class#name'),), ' rest')

    >>> parse_reference("type[@provider#id,id2:class#name] rest", None)
    ('type', 'provider', (Reference(id='id', name='class#name', _source='#id,id2:class#name'), Reference(id='id2', name='class#name', _source='#id,id2:class#name')), ' rest')

    >>> parse_reference("type[@provider#id.$0,id2.$1:class#name] rest", StepTaskId('test', (11, 12,)))
    ('type', 'provider', (Reference(id='id.11', name='class#name', _source='#id.$0,id2.$1:class#name'), Reference(id='id2.12', name='class#name', _source='#id.$0,id2.$1:class#name')), ' rest')

    >>> parse_reference("type[@provider#id.$0-1:class#name] rest", StepTaskId('test', (0,)))
    ('type', 'provider', (), ' rest')

    """
    type_, ref_option, remainder = _split_reference(reference)

    if ref_option:
        provider, refs, ref_remainder = _split_options(ref_option, task_id)
        if ref_remainder and ref_remainder.strip():
            raise ValueError(f"Invalid reference {reference.strip()}")

    else:
        provider, refs = None, tuple()

    return type_, provider, refs, remainder


def _resolve_id_references(objects: typing.Mapping, refs: typing.Sequence[Reference]) \
        -> typing.Generator[typing.Tuple[typing.Any, typing.Optional[Reference]], None, None]:

    if not refs:
        for obj in objects.values():
            yield obj, None

    for ref in refs:
        if ref.id:
            try:
                yield objects[ref.id], ref
            except KeyError:
                pass
        else:
            for result in objects.values():
                yield result, ref


def _duplicate_references(obj: typing.Any, refs: typing.Sequence[Reference]) \
        -> typing.Generator[typing.Tuple[typing.Any, typing.Optional[Reference]], None, None]:

    if not refs:
        yield obj, None

    for ref in refs:
        yield obj, ref


def _split_name_class(nc: str) -> typing.Tuple[typing.Optional[str], typing.Optional[str]]:
    """
    Split a name/class reference into its parts.

    >>> _split_name_class('class')
    ('class', None)

    >>> _split_name_class('#name')
    (None, 'name')

    >>> _split_name_class('class#name')
    ('class', 'name')

    >>> _split_name_class('class#"name"')
    ('class', '"name"')

    >>> _split_name_class('class#*.txt')
    ('class', '*.txt')

    >>> _split_name_class('class#"spaced name.txt"')
    ('class', '"spaced name.txt"')

    >>> _split_name_class('class#"name"123' + "'test'")
    ('class', '"name"123\\'test\\'')

    >>> _split_name_class('#"noclass#name"')
    (None, '"noclass#name"')

    >>> _split_name_class('#"spaced name.txt"')
    (None, '"spaced name.txt"')

    :param nc:
    :return:
    """
    parts = list(smart_split(nc))

    if parts and '#' in parts[0] and parts[0][0] not in {'"', "'"}:
        class_, rest = parts[0].split('#', 1)
        if rest:
            parts[0] = rest
        else:
            parts.pop(0)

        name = ''.join(parts)

    else:
        class_ = ''.join(parts)
        name = None

    if not class_:
        class_ = None

    return class_, name


def _split_name_domain(nd: str) -> typing.Tuple[str, typing.Optional[str]]:
    """ Split name/domain reference into its parts

    >>> _split_name_domain('name')
    ('name', None)

    >>> _split_name_domain('name@domain')
    ('name', 'domain')

    """

    if '@' in nd:
        name, domain = nd.split('@', 1)
    else:
        name, domain = nd, None

    return name, domain


def _match_result_reference(type_: str, objects: typing.Iterable[typing.Tuple[Result, Reference]]) \
        -> typing.Generator[ReferenceMatch, None, None]:
    """ A generator to generate :py:class:`ReferenceMatch` objects for result and outcome references

    :param type_: The :token:`~reference:type`
    :param objects:
    :raises ValueError: the reference is invalid
    """

    if type_ == 'result':
        _test = lambda obj: True

    elif type_.startswith('not-'):
        try:
            outcome = Outcome(type_[4:])
        except ValueError:
            raise ValueError(f"Invalid type {type_}")

        _test = lambda obj: obj.outcome_enum != outcome

    else:
        try:
            outcome = Outcome(type_)
        except ValueError:
            raise ValueError(f"Invalid type {type_}")

        _test = lambda obj: obj.outcome_enum == outcome

    for obj, ref in objects:
        if ref and ref.name:
            # noinspection PyProtectedMember
            raise ValueError(
                f"{ref._source!r} is not valid: name or class not allowed"
            )

        result = (obj,) if _test(obj) else tuple()
        yield ReferenceMatch(obj, result)


def _match_prop_reference(objects: typing.Iterable[typing.Tuple[typing.Union[ProviderElement, PropertiesMixin], Reference]]) \
        -> typing.Generator[ReferenceMatch, None, None]:

    for obj, ref in objects:
        if ref is None:
            raise ValueError("a name is required")
        elif ref.name is None:
            # noinspection PyProtectedMember
            raise ValueError(
                f"{ref._source!r} is not valid: a name is required"
            )

        properties = obj.properties.filter(name=ref.name)
        yield ReferenceMatch(obj, properties)


def _match_file_reference(objects: typing.Iterable[typing.Tuple[typing.Union[ProviderElement, FilesMixin], Reference]]) \
        -> typing.Generator[ReferenceMatch, None, None]:

    for obj, ref in objects:
        files = obj.files
        if ref and ref.name:
            class_, name = _split_name_class(ref.name)

            filters = {}
            if name:
                filters['name__glob'] = name
            if class_:
                filters['class_'] = class_

            files = files.filter(**filters)

        yield ReferenceMatch(obj, files)


def _match_opt_reference(objects: typing.Iterable[typing.Tuple[typing.Union[ProviderElement, OptionsMixin], Reference]]) \
        -> typing.Generator[ReferenceMatch, None, None]:

    for obj, ref in objects:
        if ref is None:
            raise ValueError("a name is required")
        elif ref.name is None:
            # noinspection PyProtectedMember
            raise ValueError(
                f"{ref._source!r} is not valid: a name is required"
            )

        name, domain = _split_name_domain(ref.name)

        options = obj.options.filter(name=name, domain=domain or Option.DEFAULT_DOMAIN)
        yield ReferenceMatch(obj, options)


def _get_bundle_objects(provider: str, refs: typing.Sequence[Reference], bundles: Providers):
    if provider is None:
        raise ValueError(f"no provider")
    elif provider == 'recipe' and bundles.recipe:
        objects = _duplicate_references(bundles.recipe, refs)
    elif provider == 'config' and bundles.config:
        objects = _duplicate_references(bundles.config, refs)
    elif provider == 'product' and bundles.product:
        objects = _duplicate_references(bundles.product, refs)
    elif provider == 'step' and bundles.recipe and bundles.task_id:
        try:
            step = bundles.recipe.steps[bundles.task_id.step_id]
        except KeyError:
            raise ValueError(f"invalid provider {provider!r} for task {bundles.task_id!s}")

        objects = _duplicate_references(step, refs)
    elif provider == 'result' and bundles.results:
        objects = _resolve_id_references(bundles.results.results, refs)
    else:
        raise ValueError(f"invalid provider {provider!r}")

    return objects


def generate_reference(
    type_: str, provider: typing.Optional[str], refs: typing.Sequence[Reference], bundles: Providers
) -> typing.Generator[ReferenceMatch, None, None]:
    """ A generator producing reference matches.

    Each :py:class:`ReferenceMatch` object generated is a single reference resolved.

    :param type_: The reference :token:`~reference:type`
    :param provider: The reference :token:`~reference:provider`
    :param refs: A sequence ``id`` and ``name`` pairs
    :param bundles: The bundles to resolve the references too
    """
    if type_ in {'opt', 'file'}:
        objects = _get_bundle_objects(provider, refs, bundles)

    else:
        if (provider and provider != 'result') or not bundles.results:
            raise ValueError(f"invalid provider {provider!r}")

        objects = _resolve_id_references(bundles.results.results, refs)

    if type_ == 'prop':
        yield from _match_prop_reference(objects)

    elif type_ == 'file':
        yield from _match_file_reference(objects)

    elif type_ == 'opt':
        yield from _match_opt_reference(objects)

    else:
        yield from _match_result_reference(type_, objects)


def select_by_reference(reference: str, bundles: Providers) \
        -> typing.Tuple[typing.Optional[str], typing.Tuple[ReferenceMatch], str]:
    """ Parse a :ref:`reference <reference>` string and collect the referenced items

    :param reference: The :token:`~reference:reference` string to parse
    :param bundles: The providers providing the objects that are referenced
    :return: a 3-tuple containing
             the :token:`~reference:type`,
             a tuple of :py:class:`ReferenceMatch` objects, and
             a string with the rest of the `reference` string remaining after parsing.
    :raises ValueError: the reference cannot be parsed
    """

    type_, provider, refs, remainder = parse_reference(reference, bundles.task_id)
    try:
        if type_:
            items = tuple(generate_reference(type_, provider, refs, bundles))
        else:
            items = tuple()

    except ValueError as exc:
        raise ValueError(f"Invalid {type_!r} reference {reference!r}: {exc}")

    return type_, items, remainder


def select_by_prop_reference(reference: str, results: ResultsBundle = None, task_id: StepTaskId = None) \
        -> typing.Tuple[typing.Tuple[ReferenceMatch], str]:
    """ Parse a property :token:`~reference:reference` string and collect the referenced properties.

    This is similar to the ``prop[...]`` :ref:`reference syntax <reference>`,
    but does not require the ``prop`` nor the square brackets.

    :param reference: The reference to parse
    :param results: The results bundle containing the properties
    :param task_id: The task id to expand task references
    :return: a 2-tuple containing
             a tuple of :py:class:`ReferenceMatch` objects, and
             a string with the rest of the `reference` string remaining after parsing.
    """

    provider, refs, remainder = _split_options(reference, task_id)

    try:
        if (provider and provider != 'result') or not results:
            raise ValueError(f"invalid provider {provider!r}")

        objects = _resolve_id_references(results.results, refs)
    except ValueError as exc:
        raise ValueError(f"Invalid property reference {reference!r}: {exc}")

    return tuple(_match_prop_reference(objects)), remainder


def select_by_file_reference(reference: str, bundles: Providers) -> typing.Tuple[typing.Tuple[ReferenceMatch], str]:
    """ Parse a file :token:`~reference:reference` string and collect the referenced files.

    This is similar to the ``file[...]`` :ref:`reference syntax <reference>`,
    but does not require the ``file`` nor the square brackets.

    :param reference: The reference to parse
    :param bundles: The bundles to resolve the references too
    :return: a 2-tuple containing
             a tuple of :py:class:`ReferenceMatch` objects, and
             a string with the rest of the `reference` string remaining after parsing.
    """
    provider, refs, remainder = _split_options(reference, bundles.task_id)

    try:
        objects = _get_bundle_objects(provider, refs, bundles)
    except ValueError as exc:
        raise ValueError(f"Invalid file reference {reference!r}: {exc}")

    return tuple(_match_file_reference(objects)), remainder


def select_by_opt_reference(reference: str, bundles: Providers) -> typing.Tuple[typing.Tuple[ReferenceMatch], str]:
    """ Parse an option :token:`~reference:reference` string and collect the referenced options.

    This is similar to the ``opt[...]`` :ref:`reference syntax <reference>`,
    but does not require the ``opt`` nor the square brackets.

    :param reference:
    :param bundles: The bundles to resolve the references too
    :return: a 2-tuple containing
             a tuple of :py:class:`ReferenceMatch` objects, and
             a string with the rest of the `reference` string remaining after parsing.
    """
    provider, refs, remainder = _split_options(reference, bundles.task_id)

    try:
        objects = _get_bundle_objects(provider, refs, bundles)
    except ValueError as exc:
        raise ValueError(f"Invalid option reference {reference!r}: {exc}")

    return tuple(_match_opt_reference(objects)), remainder


def resolve_reference_value(
        value_reference: str, bundles: Providers, *,
        default_mod: str = 'join'
) -> typing.Tuple[typing.Union[str, int, float, bool, None], str]:
    """ Resolve a :ref:`reference value <reference value>` string into the value

    :param value_reference: The :token:`~reference_value:value_reference`
    :param bundles: The bundles to resolve the references too
    :param default_mod: The default :token:`~reference_value:mod`
    :return: The resolved value
    """

    mod, remaining = parse_mod(value_reference)
    type_, provider, refs, remaining = parse_reference(remaining, bundles.task_id)

    if not type_:
        return None, value_reference

    matches = tuple(
        generate_reference(type_, provider, refs, bundles)
    )

    attr = VALUE_ATTR.get(type_, VALUE_ATTR[None])

    values = collections.deque()
    for match in matches:
        if match.values:
            values.extend(getattr(value, attr, None) for value in match.values)
        else:
            values.append(None)

    return apply_combiner_modifier(mod or default_mod, values), remaining
