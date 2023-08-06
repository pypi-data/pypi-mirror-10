from netlib.h2.frame import *
import tutils

from nose.tools import assert_equal

# TODO test stream association if valid or not


def test_invalid_flags():
    tutils.raises(
        ValueError,
        DataFrame,
        ContinuationFrame.FLAG_END_HEADERS,
        0x1234567,
        'foobar')


def test_frame_equality():
    a = DataFrame(6, Frame.FLAG_END_STREAM, 0x1234567, 'foobar')
    b = DataFrame(6, Frame.FLAG_END_STREAM, 0x1234567, 'foobar')
    assert_equal(a, b)


def test_too_large_frames():
    DataFrame(6, Frame.FLAG_END_STREAM, 0x1234567)


def test_data_frame_to_bytes():
    f = DataFrame(6, Frame.FLAG_END_STREAM, 0x1234567, 'foobar')
    assert_equal(f.to_bytes().encode('hex'), '000006000101234567666f6f626172')

    f = DataFrame(
        11,
        Frame.FLAG_END_STREAM | Frame.FLAG_PADDED,
        0x1234567,
        'foobar',
        pad_length=3)
    assert_equal(
        f.to_bytes().encode('hex'),
        '00000a00090123456703666f6f626172000000')

    f = DataFrame(6, Frame.FLAG_NO_FLAGS, 0x0, 'foobar')
    tutils.raises(ValueError, f.to_bytes)


def test_data_frame_from_bytes():
    f = Frame.from_bytes('000006000101234567666f6f626172'.decode('hex'))
    assert isinstance(f, DataFrame)
    assert_equal(f.length, 6)
    assert_equal(f.TYPE, DataFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_END_STREAM)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.payload, 'foobar')

    f = Frame.from_bytes('00000a00090123456703666f6f626172000000'.decode('hex'))
    assert isinstance(f, DataFrame)
    assert_equal(f.length, 10)
    assert_equal(f.TYPE, DataFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_END_STREAM | Frame.FLAG_PADDED)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.payload, 'foobar')


def test_data_frame_human_readable():
    f = DataFrame(
        11,
        Frame.FLAG_END_STREAM | Frame.FLAG_PADDED,
        0x1234567,
        'foobar',
        pad_length=3)
    assert f.human_readable()


def test_headers_frame_to_bytes():
    f = HeadersFrame(
        6,
        Frame.FLAG_NO_FLAGS,
        0x1234567,
        headers=[('host', 'foo.bar')])
    assert_equal(f.to_bytes().encode('hex'), '000007010001234567668594e75e31d9')

    f = HeadersFrame(
        10,
        HeadersFrame.FLAG_PADDED,
        0x1234567,
        headers=[('host', 'foo.bar')],
        pad_length=3)
    assert_equal(
        f.to_bytes().encode('hex'),
        '00000b01080123456703668594e75e31d9000000')

    f = HeadersFrame(
        10,
        HeadersFrame.FLAG_PRIORITY,
        0x1234567,
        headers=[('host', 'foo.bar')],
        exclusive=True,
        stream_dependency=0x7654321,
        weight=42)
    assert_equal(
        f.to_bytes().encode('hex'),
        '00000c012001234567876543212a668594e75e31d9')

    f = HeadersFrame(
        14,
        HeadersFrame.FLAG_PADDED | HeadersFrame.FLAG_PRIORITY,
        0x1234567,
        headers=[('host', 'foo.bar')],
        pad_length=3,
        exclusive=True,
        stream_dependency=0x7654321,
        weight=42)
    assert_equal(
        f.to_bytes().encode('hex'),
        '00001001280123456703876543212a668594e75e31d9000000')

    f = HeadersFrame(
        14,
        HeadersFrame.FLAG_PADDED | HeadersFrame.FLAG_PRIORITY,
        0x1234567,
        headers=[('host', 'foo.bar')],
        pad_length=3,
        exclusive=False,
        stream_dependency=0x7654321,
        weight=42)
    assert_equal(
        f.to_bytes().encode('hex'),
        '00001001280123456703076543212a668594e75e31d9000000')

    f = HeadersFrame(6, Frame.FLAG_NO_FLAGS, 0x0, 'foobar')
    tutils.raises(ValueError, f.to_bytes)


def test_headers_frame_from_bytes():
    f = Frame.from_bytes('000007010001234567668594e75e31d9'.decode('hex'))
    assert isinstance(f, HeadersFrame)
    assert_equal(f.length, 7)
    assert_equal(f.TYPE, HeadersFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_NO_FLAGS)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.headers, [('host', 'foo.bar')])

    f = Frame.from_bytes(
        '00000b01080123456703668594e75e31d9000000'.decode('hex'))
    assert isinstance(f, HeadersFrame)
    assert_equal(f.length, 11)
    assert_equal(f.TYPE, HeadersFrame.TYPE)
    assert_equal(f.flags, HeadersFrame.FLAG_PADDED)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.headers, [('host', 'foo.bar')])

    f = Frame.from_bytes(
        '00000c012001234567876543212a668594e75e31d9'.decode('hex'))
    assert isinstance(f, HeadersFrame)
    assert_equal(f.length, 12)
    assert_equal(f.TYPE, HeadersFrame.TYPE)
    assert_equal(f.flags, HeadersFrame.FLAG_PRIORITY)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.headers, [('host', 'foo.bar')])
    assert_equal(f.exclusive, True)
    assert_equal(f.stream_dependency, 0x7654321)
    assert_equal(f.weight, 42)

    f = Frame.from_bytes(
        '00001001280123456703876543212a668594e75e31d9000000'.decode('hex'))
    assert isinstance(f, HeadersFrame)
    assert_equal(f.length, 16)
    assert_equal(f.TYPE, HeadersFrame.TYPE)
    assert_equal(f.flags, HeadersFrame.FLAG_PADDED | HeadersFrame.FLAG_PRIORITY)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.headers, [('host', 'foo.bar')])
    assert_equal(f.exclusive, True)
    assert_equal(f.stream_dependency, 0x7654321)
    assert_equal(f.weight, 42)

    f = Frame.from_bytes(
        '00001001280123456703076543212a668594e75e31d9000000'.decode('hex'))
    assert isinstance(f, HeadersFrame)
    assert_equal(f.length, 16)
    assert_equal(f.TYPE, HeadersFrame.TYPE)
    assert_equal(f.flags, HeadersFrame.FLAG_PADDED | HeadersFrame.FLAG_PRIORITY)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.headers, [('host', 'foo.bar')])
    assert_equal(f.exclusive, False)
    assert_equal(f.stream_dependency, 0x7654321)
    assert_equal(f.weight, 42)


def test_headers_frame_human_readable():
    f = HeadersFrame(
        7,
        HeadersFrame.FLAG_PADDED | HeadersFrame.FLAG_PRIORITY,
        0x1234567,
        headers=[],
        pad_length=3,
        exclusive=False,
        stream_dependency=0x7654321,
        weight=42)
    assert f.human_readable()

    f = HeadersFrame(
        14,
        HeadersFrame.FLAG_PADDED | HeadersFrame.FLAG_PRIORITY,
        0x1234567,
        headers=[('host', 'foo.bar')],
        pad_length=3,
        exclusive=False,
        stream_dependency=0x7654321,
        weight=42)
    assert f.human_readable()


def test_priority_frame_to_bytes():
    f = PriorityFrame(
        5,
        Frame.FLAG_NO_FLAGS,
        0x1234567,
        exclusive=True,
        stream_dependency=0x7654321,
        weight=42)
    assert_equal(f.to_bytes().encode('hex'), '000005020001234567876543212a')

    f = PriorityFrame(
        5,
        Frame.FLAG_NO_FLAGS,
        0x1234567,
        exclusive=False,
        stream_dependency=0x7654321,
        weight=21)
    assert_equal(f.to_bytes().encode('hex'), '0000050200012345670765432115')

    f = PriorityFrame(5, Frame.FLAG_NO_FLAGS, 0x0, stream_dependency=0x1234567)
    tutils.raises(ValueError, f.to_bytes)

    f = PriorityFrame(5, Frame.FLAG_NO_FLAGS, 0x1234567, stream_dependency=0x0)
    tutils.raises(ValueError, f.to_bytes)


def test_priority_frame_from_bytes():
    f = Frame.from_bytes('000005020001234567876543212a'.decode('hex'))
    assert isinstance(f, PriorityFrame)
    assert_equal(f.length, 5)
    assert_equal(f.TYPE, PriorityFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_NO_FLAGS)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.exclusive, True)
    assert_equal(f.stream_dependency, 0x7654321)
    assert_equal(f.weight, 42)

    f = Frame.from_bytes('0000050200012345670765432115'.decode('hex'))
    assert isinstance(f, PriorityFrame)
    assert_equal(f.length, 5)
    assert_equal(f.TYPE, PriorityFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_NO_FLAGS)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.exclusive, False)
    assert_equal(f.stream_dependency, 0x7654321)
    assert_equal(f.weight, 21)


def test_priority_frame_human_readable():
    f = PriorityFrame(
        5,
        Frame.FLAG_NO_FLAGS,
        0x1234567,
        exclusive=False,
        stream_dependency=0x7654321,
        weight=21)
    assert f.human_readable()


def test_rst_stream_frame_to_bytes():
    f = RstStreamFrame(4, Frame.FLAG_NO_FLAGS, 0x1234567, error_code=0x7654321)
    assert_equal(f.to_bytes().encode('hex'), '00000403000123456707654321')

    f = RstStreamFrame(4, Frame.FLAG_NO_FLAGS, 0x0)
    tutils.raises(ValueError, f.to_bytes)


def test_rst_stream_frame_from_bytes():
    f = Frame.from_bytes('00000403000123456707654321'.decode('hex'))
    assert isinstance(f, RstStreamFrame)
    assert_equal(f.length, 4)
    assert_equal(f.TYPE, RstStreamFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_NO_FLAGS)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.error_code, 0x07654321)


def test_rst_stream_frame_human_readable():
    f = RstStreamFrame(4, Frame.FLAG_NO_FLAGS, 0x1234567, error_code=0x7654321)
    assert f.human_readable()


def test_settings_frame_to_bytes():
    f = SettingsFrame(0, Frame.FLAG_NO_FLAGS, 0x0)
    assert_equal(f.to_bytes().encode('hex'), '000000040000000000')

    f = SettingsFrame(0, SettingsFrame.FLAG_ACK, 0x0)
    assert_equal(f.to_bytes().encode('hex'), '000000040100000000')

    f = SettingsFrame(
        6,
        SettingsFrame.FLAG_ACK, 0x0,
        settings={
            SettingsFrame.SETTINGS.SETTINGS_ENABLE_PUSH: 1})
    assert_equal(f.to_bytes().encode('hex'), '000006040100000000000200000001')

    f = SettingsFrame(
        12,
        Frame.FLAG_NO_FLAGS,
        0x0,
        settings={
            SettingsFrame.SETTINGS.SETTINGS_ENABLE_PUSH: 1,
            SettingsFrame.SETTINGS.SETTINGS_MAX_CONCURRENT_STREAMS: 0x12345678})
    assert_equal(
        f.to_bytes().encode('hex'),
        '00000c040000000000000200000001000312345678')

    f = SettingsFrame(0, Frame.FLAG_NO_FLAGS, 0x1234567)
    tutils.raises(ValueError, f.to_bytes)


def test_settings_frame_from_bytes():
    f = Frame.from_bytes('000000040000000000'.decode('hex'))
    assert isinstance(f, SettingsFrame)
    assert_equal(f.length, 0)
    assert_equal(f.TYPE, SettingsFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_NO_FLAGS)
    assert_equal(f.stream_id, 0x0)

    f = Frame.from_bytes('000000040100000000'.decode('hex'))
    assert isinstance(f, SettingsFrame)
    assert_equal(f.length, 0)
    assert_equal(f.TYPE, SettingsFrame.TYPE)
    assert_equal(f.flags, SettingsFrame.FLAG_ACK)
    assert_equal(f.stream_id, 0x0)

    f = Frame.from_bytes('000006040100000000000200000001'.decode('hex'))
    assert isinstance(f, SettingsFrame)
    assert_equal(f.length, 6)
    assert_equal(f.TYPE, SettingsFrame.TYPE)
    assert_equal(f.flags, SettingsFrame.FLAG_ACK, 0x0)
    assert_equal(f.stream_id, 0x0)
    assert_equal(len(f.settings), 1)
    assert_equal(f.settings[SettingsFrame.SETTINGS.SETTINGS_ENABLE_PUSH], 1)

    f = Frame.from_bytes(
        '00000c040000000000000200000001000312345678'.decode('hex'))
    assert isinstance(f, SettingsFrame)
    assert_equal(f.length, 12)
    assert_equal(f.TYPE, SettingsFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_NO_FLAGS)
    assert_equal(f.stream_id, 0x0)
    assert_equal(len(f.settings), 2)
    assert_equal(f.settings[SettingsFrame.SETTINGS.SETTINGS_ENABLE_PUSH], 1)
    assert_equal(
        f.settings[
            SettingsFrame.SETTINGS.SETTINGS_MAX_CONCURRENT_STREAMS],
        0x12345678)


def test_settings_frame_human_readable():
    f = SettingsFrame(12, Frame.FLAG_NO_FLAGS, 0x0, settings={})
    assert f.human_readable()

    f = SettingsFrame(
        12,
        Frame.FLAG_NO_FLAGS,
        0x0,
        settings={
            SettingsFrame.SETTINGS.SETTINGS_ENABLE_PUSH: 1,
            SettingsFrame.SETTINGS.SETTINGS_MAX_CONCURRENT_STREAMS: 0x12345678})
    assert f.human_readable()


def test_push_promise_frame_to_bytes():
    f = PushPromiseFrame(
        10,
        Frame.FLAG_NO_FLAGS,
        0x1234567,
        0x7654321,
        'foobar')
    assert_equal(
        f.to_bytes().encode('hex'),
        '00000a05000123456707654321666f6f626172')

    f = PushPromiseFrame(
        14,
        HeadersFrame.FLAG_PADDED,
        0x1234567,
        0x7654321,
        'foobar',
        pad_length=3)
    assert_equal(
        f.to_bytes().encode('hex'),
        '00000e0508012345670307654321666f6f626172000000')

    f = PushPromiseFrame(4, Frame.FLAG_NO_FLAGS, 0x0, 0x1234567)
    tutils.raises(ValueError, f.to_bytes)

    f = PushPromiseFrame(4, Frame.FLAG_NO_FLAGS, 0x1234567, 0x0)
    tutils.raises(ValueError, f.to_bytes)


def test_push_promise_frame_from_bytes():
    f = Frame.from_bytes('00000a05000123456707654321666f6f626172'.decode('hex'))
    assert isinstance(f, PushPromiseFrame)
    assert_equal(f.length, 10)
    assert_equal(f.TYPE, PushPromiseFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_NO_FLAGS)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.header_block_fragment, 'foobar')

    f = Frame.from_bytes(
        '00000e0508012345670307654321666f6f626172000000'.decode('hex'))
    assert isinstance(f, PushPromiseFrame)
    assert_equal(f.length, 14)
    assert_equal(f.TYPE, PushPromiseFrame.TYPE)
    assert_equal(f.flags, PushPromiseFrame.FLAG_PADDED)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.header_block_fragment, 'foobar')


def test_push_promise_frame_human_readable():
    f = PushPromiseFrame(
        14,
        HeadersFrame.FLAG_PADDED,
        0x1234567,
        0x7654321,
        'foobar',
        pad_length=3)
    assert f.human_readable()


def test_ping_frame_to_bytes():
    f = PingFrame(8, PingFrame.FLAG_ACK, 0x0, payload=b'foobar')
    assert_equal(
        f.to_bytes().encode('hex'),
        '000008060100000000666f6f6261720000')

    f = PingFrame(8, Frame.FLAG_NO_FLAGS, 0x0, payload=b'foobardeadbeef')
    assert_equal(
        f.to_bytes().encode('hex'),
        '000008060000000000666f6f6261726465')

    f = PingFrame(8, Frame.FLAG_NO_FLAGS, 0x1234567)
    tutils.raises(ValueError, f.to_bytes)


def test_ping_frame_from_bytes():
    f = Frame.from_bytes('000008060100000000666f6f6261720000'.decode('hex'))
    assert isinstance(f, PingFrame)
    assert_equal(f.length, 8)
    assert_equal(f.TYPE, PingFrame.TYPE)
    assert_equal(f.flags, PingFrame.FLAG_ACK)
    assert_equal(f.stream_id, 0x0)
    assert_equal(f.payload, b'foobar\0\0')

    f = Frame.from_bytes('000008060000000000666f6f6261726465'.decode('hex'))
    assert isinstance(f, PingFrame)
    assert_equal(f.length, 8)
    assert_equal(f.TYPE, PingFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_NO_FLAGS)
    assert_equal(f.stream_id, 0x0)
    assert_equal(f.payload, b'foobarde')


def test_ping_frame_human_readable():
    f = PingFrame(8, PingFrame.FLAG_ACK, 0x0, payload=b'foobar')
    assert f.human_readable()


def test_goaway_frame_to_bytes():
    f = GoAwayFrame(
        8,
        Frame.FLAG_NO_FLAGS,
        0x0,
        last_stream=0x1234567,
        error_code=0x87654321,
        data=b'')
    assert_equal(
        f.to_bytes().encode('hex'),
        '0000080700000000000123456787654321')

    f = GoAwayFrame(
        14,
        Frame.FLAG_NO_FLAGS,
        0x0,
        last_stream=0x1234567,
        error_code=0x87654321,
        data=b'foobar')
    assert_equal(
        f.to_bytes().encode('hex'),
        '00000e0700000000000123456787654321666f6f626172')

    f = GoAwayFrame(
        8,
        Frame.FLAG_NO_FLAGS,
        0x1234567,
        last_stream=0x1234567,
        error_code=0x87654321)
    tutils.raises(ValueError, f.to_bytes)


def test_goaway_frame_from_bytes():
    f = Frame.from_bytes('0000080700000000000123456787654321'.decode('hex'))
    assert isinstance(f, GoAwayFrame)
    assert_equal(f.length, 8)
    assert_equal(f.TYPE, GoAwayFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_NO_FLAGS)
    assert_equal(f.stream_id, 0x0)
    assert_equal(f.last_stream, 0x1234567)
    assert_equal(f.error_code, 0x87654321)
    assert_equal(f.data, b'')

    f = Frame.from_bytes(
        '00000e0700000000000123456787654321666f6f626172'.decode('hex'))
    assert isinstance(f, GoAwayFrame)
    assert_equal(f.length, 14)
    assert_equal(f.TYPE, GoAwayFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_NO_FLAGS)
    assert_equal(f.stream_id, 0x0)
    assert_equal(f.last_stream, 0x1234567)
    assert_equal(f.error_code, 0x87654321)
    assert_equal(f.data, b'foobar')


def test_go_away_frame_human_readable():
    f = GoAwayFrame(
        14,
        Frame.FLAG_NO_FLAGS,
        0x0,
        last_stream=0x1234567,
        error_code=0x87654321,
        data=b'foobar')
    assert f.human_readable()


def test_window_update_frame_to_bytes():
    f = WindowUpdateFrame(
        4,
        Frame.FLAG_NO_FLAGS,
        0x0,
        window_size_increment=0x1234567)
    assert_equal(f.to_bytes().encode('hex'), '00000408000000000001234567')

    f = WindowUpdateFrame(
        4,
        Frame.FLAG_NO_FLAGS,
        0x1234567,
        window_size_increment=0x7654321)
    assert_equal(f.to_bytes().encode('hex'), '00000408000123456707654321')

    f = WindowUpdateFrame(
        4,
        Frame.FLAG_NO_FLAGS,
        0x0,
        window_size_increment=0xdeadbeef)
    tutils.raises(ValueError, f.to_bytes)

    f = WindowUpdateFrame(4, Frame.FLAG_NO_FLAGS, 0x0, window_size_increment=0)
    tutils.raises(ValueError, f.to_bytes)


def test_window_update_frame_from_bytes():
    f = Frame.from_bytes('00000408000000000001234567'.decode('hex'))
    assert isinstance(f, WindowUpdateFrame)
    assert_equal(f.length, 4)
    assert_equal(f.TYPE, WindowUpdateFrame.TYPE)
    assert_equal(f.flags, Frame.FLAG_NO_FLAGS)
    assert_equal(f.stream_id, 0x0)
    assert_equal(f.window_size_increment, 0x1234567)


def test_window_update_frame_human_readable():
    f = WindowUpdateFrame(
        4,
        Frame.FLAG_NO_FLAGS,
        0x1234567,
        window_size_increment=0x7654321)
    assert f.human_readable()


def test_continuation_frame_to_bytes():
    f = ContinuationFrame(
        6,
        ContinuationFrame.FLAG_END_HEADERS,
        0x1234567,
        'foobar')
    assert_equal(f.to_bytes().encode('hex'), '000006090401234567666f6f626172')

    f = ContinuationFrame(6, ContinuationFrame.FLAG_END_HEADERS, 0x0, 'foobar')
    tutils.raises(ValueError, f.to_bytes)


def test_continuation_frame_from_bytes():
    f = Frame.from_bytes('000006090401234567666f6f626172'.decode('hex'))
    assert isinstance(f, ContinuationFrame)
    assert_equal(f.length, 6)
    assert_equal(f.TYPE, ContinuationFrame.TYPE)
    assert_equal(f.flags, ContinuationFrame.FLAG_END_HEADERS)
    assert_equal(f.stream_id, 0x1234567)
    assert_equal(f.header_block_fragment, 'foobar')


def test_continuation_frame_human_readable():
    f = ContinuationFrame(
        6,
        ContinuationFrame.FLAG_END_HEADERS,
        0x1234567,
        'foobar')
    assert f.human_readable()
