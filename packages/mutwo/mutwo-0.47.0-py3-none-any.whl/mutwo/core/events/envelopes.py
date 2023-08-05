"""Envelope events"""

from __future__ import annotations

import typing

from mutwo.core import events
from mutwo.core.utilities import constants
from mutwo.core.utilities import tools


__all__ = ("Envelope", "RelativeEnvelope")

T = typing.TypeVar("T", bound=events.abc.Event)


class Envelope(events.basic.SequentialEvent, typing.Generic[T]):
    """Model continuous changing values (e.g. glissandi, crescendo).

    :param event_iterable_or_point_sequence: An iterable filled with events. Each event represents
        a point in a two dimensional graph where the y-axis presents time
        and the x-axis a changing value. Any event class can be used. It is
        more important that the used event classes fit with the functions
        passed in the following parameters.
    :type event_iterable_or_point_sequence: typing.Iterable[T]
    :param event_to_parameter: A function which receives an event and has to
        return a parameter object (any object). By default the function will
        ask the event for its `value` property. If the property can't be found
        it will return 0.
    :type event_to_parameter: typing.Callable[[events.abc.Event], constants.ParameterType]
    :param event_to_curve_shape: A function which receives an event and has
        to return a curve_shape. A curve_shape is either a float, an integer
        or a fraction. For a curve_shape = 0 a linear transition between two
        points is created. For a curve_shape > 0 the envelope changes slower
        at the beginning and faster at the end, for a curve_shape < 0 it is
        the inverse behaviour. The default function will ask the event for its
        `curve_shape` property. If the property can't be found
        it will return 0.
    :type event_to_curve_shape: typing.Callable[[events.abc.Event], CurveShape]
    :param parameter_to_value: Convert a parameter to a value. A value is any
        object which supports mathematical operations.
    :type parameter_to_value: typing.Callable[[Value], constants.ParameterType]
    :param value_to_parameter:
    :type value_to_parameter: typing.Callable[[Value], constants.ParameterType]
    :param apply_parameter_on_event:
    :type apply_parameter_on_event: typing.Callable[[events.abc.Event, constants.ParameterType], None]
    :param apply_curve_shape_on_event:
    :type apply_curve_shape_on_event: typing.Callable[[events.abc.Event, CurveShape], None]
    :param default_event_class:
    :type default_event_class: type[events.abc.Event]
    :param initialise_default_event_class:
    :type initialise_default_event_class: typing.Callable[[type[events.abc.Event], constants.DurationType], events.abc.Event]

    This class is inspired by Marc Evanstein `Envelope` class in his
    `expenvelope <https://git.sr.ht/~marcevanstein/expenvelope>`_
    python package and made to fit more into the `mutwo` ecosystem.
    """

    # Type definitions
    Value = constants.Real
    CurveShape = constants.Real
    IncompletePoint = tuple[constants.DurationType, constants.ParameterType]
    CompletePoint = tuple[
        constants.DurationType, constants.ParameterType, CurveShape  # type: ignore
    ]
    Point = typing.Union[CompletePoint, IncompletePoint]

    # class specific side attributes (keep consistent
    # when applying the "empty_copy" method)
    _class_specific_side_attribute_tuple = (
        "event_to_parameter",
        "event_to_curve_shape",
        "value_to_parameter",
        "parameter_to_value",
        "apply_parameter_on_event",
        "apply_curve_shape_on_event",
        "default_event_class",
        "initialise_default_event_class",
    )

    def __init__(
        self,
        event_iterable_or_point_sequence: typing.Union[
            typing.Iterable[T], typing.Sequence[Point]
        ],
        event_to_parameter: typing.Callable[
            [events.abc.Event], constants.ParameterType
        ] = lambda event: getattr(
            event, events.envelopes_constants.DEFAULT_PARAMETER_ATTRIBUTE_NAME
        )
        if hasattr(event, events.envelopes_constants.DEFAULT_PARAMETER_ATTRIBUTE_NAME)
        else 0,
        event_to_curve_shape: typing.Callable[
            [events.abc.Event], CurveShape
        ] = lambda event: getattr(
            event, events.envelopes_constants.DEFAULT_CURVE_SHAPE_ATTRIBUTE_NAME
        )
        if hasattr(event, events.envelopes_constants.DEFAULT_CURVE_SHAPE_ATTRIBUTE_NAME)
        else 0,
        parameter_to_value: typing.Callable[
            [Value], constants.ParameterType
        ] = lambda parameter: parameter,
        value_to_parameter: typing.Callable[
            [Value], constants.ParameterType
        ] = lambda value: value,
        apply_parameter_on_event: typing.Callable[
            [events.abc.Event, constants.ParameterType], None
        ] = lambda event, parameter: setattr(
            event,
            events.envelopes_constants.DEFAULT_PARAMETER_ATTRIBUTE_NAME,
            parameter,
        ),
        apply_curve_shape_on_event: typing.Callable[
            [events.abc.Event, CurveShape], None
        ] = lambda event, curve_shape: setattr(
            event,
            events.envelopes_constants.DEFAULT_CURVE_SHAPE_ATTRIBUTE_NAME,
            curve_shape,
        ),
        default_event_class: type[events.abc.Event] = events.basic.SimpleEvent,
        initialise_default_event_class: typing.Callable[
            [type[events.abc.Event], constants.DurationType], events.abc.Event
        ] = lambda simple_event, duration: simple_event(duration),
    ):
        self.event_to_parameter = event_to_parameter
        self.event_to_curve_shape = event_to_curve_shape
        self.value_to_parameter = value_to_parameter
        self.parameter_to_value = parameter_to_value
        self.apply_parameter_on_event = apply_parameter_on_event
        self.apply_curve_shape_on_event = apply_curve_shape_on_event
        self.default_event_class = default_event_class
        self.initialise_default_event_class = initialise_default_event_class

        item_type_list = [
            isinstance(event_or_point, events.abc.Event)
            for event_or_point in event_iterable_or_point_sequence
        ]
        if all(item_type_list):
            event_iterable = event_iterable_or_point_sequence
        elif any(item_type_list):
            raise TypeError(
                "Found inconsistent iterable with mixed types. "
                "Please only use events or only use points for "
                "'event_iterable_or_point_sequence'. First 200 "
                "characters of the problematic iterable: \n"
                f"{str(event_iterable_or_point_sequence)[:200]}"
            )
        else:
            event_iterable = self._point_sequence_to_event_list(
                event_iterable_or_point_sequence  # type: ignore
            )
        super().__init__(event_iterable)

    # ###################################################################### #
    #                      public class methods                              #
    # ###################################################################### #

    @classmethod
    def from_points(
        cls,
        *point: Point,
        **kwargs,
    ) -> Envelope:
        return cls(point, **kwargs)

    # ###################################################################### #
    #                    private static methods                              #
    # ###################################################################### #

    @staticmethod
    def _point_sequence_to_corrected_point_list(
        point_or_invalid_type_sequence: typing.Sequence[typing.Union[Point, typing.Any]]
    ) -> list[typing.Union[Envelope.CompletePoint, None]]:
        corrected_point_list: list[typing.Union[Envelope.CompletePoint, None]] = []
        for point in point_or_invalid_type_sequence:
            point_length = len(point)
            if point_length == 2:
                point += (0,)  # type: ignore
            elif point_length != 3:
                raise TypeError(
                    f"Found invalid point: '{point}' with {point_length} "
                    "items! Points should have two or three items."
                )
            corrected_point_list.append(point)  # type: ignore
        return corrected_point_list

    # ###################################################################### #
    #                         private methods                                #
    # ###################################################################### #

    def _point_sequence_to_event_list(
        self,
        point_or_invalid_type_sequence: typing.Sequence[
            typing.Union[Point, typing.Any]
        ],
    ) -> list[events.abc.Event]:
        corrected_point_list = Envelope._point_sequence_to_corrected_point_list(
            point_or_invalid_type_sequence
        )
        corrected_point_list.append(None)
        event_list = []
        for point0, point1 in zip(corrected_point_list, corrected_point_list[1:]):
            if point0 is not None:
                absolute_time0, value_or_parameter, curve_shape = point0
            else:
                raise TypeError("Found unexpected position of None in provided points.")
            if point1:
                absolute_time1 = point1[0]
                assert absolute_time1 >= absolute_time0
            else:
                absolute_time1 = absolute_time0
            duration = absolute_time1 - absolute_time0
            event = self.initialise_default_event_class(
                self.default_event_class, duration
            )
            self.apply_parameter_on_event(event, value_or_parameter)
            self.apply_curve_shape_on_event(event, curve_shape)
            event_list.append(event)
        return event_list

    def _event_to_value(self, event: events.abc.Event) -> Value:
        return self.parameter_to_value(self.event_to_parameter(event))

    # ###################################################################### #
    #                         public properties                              #
    # ###################################################################### #

    @property
    def value_tuple(self) -> tuple[Value, ...]:
        return tuple(map(self._event_to_value, self))

    @property
    def is_static(self) -> bool:
        """Return `True` if :class:`Envelope` only has one static value."""

        return len(set(self.value_tuple)) <= 1

    # ###################################################################### #
    #                          public methods                                #
    # ###################################################################### #

    def value_at(self, absolute_time: constants.DurationType) -> Value:
        absolute_time_tuple = self.absolute_time_tuple

        use_only_first_event = absolute_time <= absolute_time_tuple[0]
        use_only_last_event = absolute_time >= absolute_time_tuple[-1]
        if use_only_first_event or use_only_last_event:
            index = 0 if use_only_first_event else -1
            return self._event_to_value(self[index])

        event_0_index = self._get_index_at_from_absolute_time_tuple(
            absolute_time, absolute_time_tuple, self.duration
        )
        assert event_0_index is not None

        value0, value1 = (
            self._event_to_value(self[event_0_index + n]) for n in range(2)
        )
        curve_shape = self.event_to_curve_shape(self[event_0_index])

        return tools.scale(
            absolute_time,
            absolute_time_tuple[event_0_index],
            absolute_time_tuple[event_0_index + 1],
            value0,
            value1,
            curve_shape,
        )

    def parameter_at(
        self, absolute_time: constants.DurationType
    ) -> constants.ParameterType:
        return self.value_to_parameter(self.value_at(absolute_time))


class RelativeEnvelope(Envelope, typing.Generic[T]):
    __parent_doc_string = Envelope.__doc__.split("\n")[2:]  # type: ignore
    __after_parameter_text_index = __parent_doc_string.index("")
    __doc__ = "\n".join(
        ["Envelope with relative durations and values / parameters.\n"]
        + __parent_doc_string[:__after_parameter_text_index]
        + [
            "    :param base_parameter_and_relative_parameter_to_absolute_parameter: A function",
            "        which runs when the :func:`resolve` is called. It expects the base parameter",
            "        and the relative parameter (which is extracted from the envelope events)",
            "        and should return an absolute parameter.",
        ]
        + __parent_doc_string[__after_parameter_text_index:]
        + [
            "    The :class:`RelativeEnvelope` adds the :func:`resolve` method",
            "    to the base class :class:`Envelope`.",
        ]
    )

    def __init__(
        self,
        *args,
        base_parameter_and_relative_parameter_to_absolute_parameter: typing.Callable[
            [constants.ParameterType, constants.ParameterType], constants.ParameterType
        ],
        **kwargs,
    ):
        self.base_parameter_and_relative_parameter_to_absolute_parameter = (
            base_parameter_and_relative_parameter_to_absolute_parameter
        )
        super().__init__(*args, **kwargs)

    def resolve(
        self,
        duration: constants.DurationType,
        base_parameter: constants.ParameterType,
        resolve_envelope_class: type[Envelope] = Envelope,
    ) -> Envelope:
        point_list = []
        try:
            duration_factor = duration / self.duration
        except ZeroDivisionError:
            duration_factor = 0
        for absolute_time, event in zip(self.absolute_time_tuple, self):
            relative_parameter = self.event_to_parameter(event)
            new_parameter = (
                self.base_parameter_and_relative_parameter_to_absolute_parameter(
                    base_parameter, relative_parameter
                )
            )
            point = (
                absolute_time * duration_factor,
                new_parameter,
                self.event_to_curve_shape(event),
            )
            point_list.append(point)
        return resolve_envelope_class(point_list)
