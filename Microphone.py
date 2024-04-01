from speech_recognition import Recognizer
from speech_recognition import AudioSource
from speech_recognition import AudioData
import keyboard
import io

def recordUntilKeyPressed(self, source, offset=None, stopKey=None, necessaryKey=None, extraRecordingTime=0):
    """
    Records up to ``duration`` seconds of audio from ``source`` (an ``AudioSource`` instance) starting at ``offset`` (or at the beginning if not specified) into an ``AudioData`` instance, which it returns.

    If ``duration`` is not specified, then it will record until there is no more audio input.
    """
    assert isinstance(source, AudioSource), "Source must be an audio source"
    assert source.stream is not None, "Audio source must be entered before recording, see documentation for ``AudioSource``; are you using ``source`` outside of a ``with`` statement?"

    frames = io.BytesIO()
    seconds_per_buffer = (source.CHUNK + 0.0) / source.SAMPLE_RATE
    elapsed_time = 0
    exit_time = 0
    offset_time = 0
    offset_reached = False
    while True:  # loop for the total number of chunks needed
        if offset and not offset_reached:
            offset_time += seconds_per_buffer
            if offset_time > offset:
                offset_reached = True

        buffer = source.stream.read(source.CHUNK)
        if len(buffer) == 0: break

        if offset_reached or not offset:
            elapsed_time += seconds_per_buffer
            if exit_time == 0 and stopKey != None and (keyboard.is_pressed(stopKey.lower()) or keyboard.is_pressed(stopKey.upper())):
                exit_time = elapsed_time
            if exit_time == 0 and necessaryKey != None and not keyboard.is_pressed(necessaryKey.lower()) and not keyboard.is_pressed(necessaryKey.upper()):
                exit_time = elapsed_time
            if exit_time > 0 and elapsed_time - exit_time >= extraRecordingTime:
                break

            frames.write(buffer)

    frame_data = frames.getvalue()
    frames.close()
    return AudioData(frame_data, source.SAMPLE_RATE, source.SAMPLE_WIDTH)

Recognizer.recordUntilKeyPressed = recordUntilKeyPressed
