"""
Generate audio program of spoken phrases, with optional background sound file mixed in

"""
import os
import re
import math
from queue import Queue
from threading import Thread

from io import StringIO, TextIOWrapper, BytesIO, BufferedReader
from typing import Union
from gtts import gTTS
from pydub import AudioSegment
from alive_progress import alive_bar, config_handler
from pathlib import Path
from single_source import get_version

from datetime import datetime


def parse_textfile(phrase_file_contents: str = "") -> list:
    """
    Clean up user-supplied phrase file to comform with expected format
    """

    def clean(dirty: str = "") -> str:
        cleaner = r"[^A-Za-z0-9\s;\v]"
        cleaned = re.compile(cleaner, flags=re.MULTILINE | re.UNICODE)
        return re.sub(cleaned, "", dirty)

    def capture(cleaned: str = "") -> list:
        capturer = r"^\s*([\w\s]+?)\s*;\s*(\d+)\s*$"
        captured = re.compile(capturer, flags=re.MULTILINE | re.UNICODE)
        return re.findall(captured, cleaned)

    return capture(clean(phrase_file_contents))


class AudioProgramGenerator:
    def __init__(
        self,
        phrase_file: Union[StringIO, TextIOWrapper],
        sound_file: BufferedReader = None,
        **kwargs,
    ):
        """
        Initialize class instance
        """
        if isinstance(phrase_file, (TextIOWrapper, StringIO)):
            self.phrases = phrase_file.read()
        else:
            raise (
                TypeError,
                f"phrase_file must be either StringIO or TextIOWrapper, not {type(phrase_file)}.",
            )

        self.__version__ = get_version(__name__, Path(__file__).parent.parent)
        self.sound_file = sound_file  # Fileobj to mix w/ generated speech
        self.slow = kwargs.get("slow", False)  # Half-speed speech if True
        self.attenuation = kwargs.get("attenuation", 10)  # Attenuation value, if mixing
        self.tld = kwargs.get("tld", "com")  # TLD for accents
        self.speech_file = None  # Generated speech/silence
        self.mix_file = None  # Mixed speeech/sound
        self.result = BytesIO(None)  # File-like object to store final result
        self.hide_progress_bar = kwargs.get("hide_progress_bar", False)
        self.book_mode = kwargs.get("book_mode", False)
        self.output_format = kwargs.get("output_format", "wav")
        self.q, self.p = Queue(), Queue()  # queues to manage threads, worker results

        config_handler.set_global(
            bar=None,
            stats=False,
            monitor=False,
            elapsed=False,
            disable=self.hide_progress_bar,
        )

    def _worker(self, phr, dur):
        while True:
            # print(f"phr, dur: {phr}, {dur}")
            thread = self.q.get()
            tmpfile = BytesIO(None)
            speech = gTTS(phr, slow=self.slow, tld=self.tld)
            speech.write_to_fp(tmpfile)
            tmpfile.seek(0)
            print(f"Putting item {tmpfile} onto results queue")
            self.p.put(tmpfile)
            # print(f"Queue sizes in worker: p: {self.p.qsize()}, q: {self.q.qsize()}")
            print(f"Thread done for p: {self.p.qsize()}, q: {self.q.qsize()}")
            self.q.task_done()

    def _gen_speech(self):
        """
        Generate a combined speech file, made up of gTTS-generated speech
        snippets from each line in the phrase_file + corresponding silence.
        """

        if self.book_mode:
            phrases = self.phrases.split(os.linesep)
            durations = [None for elem in range(len(phrases))]
            items = list(zip(phrases, durations))
        else:
            items = parse_textfile(self.phrases)

        combined = AudioSegment.empty()

        for phr, dur in items:
            if not phr.strip():
                continue
            print(f"Creating thread and pushing onto thread queue for {phr, dur}")
            thread = Thread(
                target=self._worker,
                args=(
                    phr,
                    dur,
                ),
                daemon=True,
            ).start()
            self.q.put(thread)
            # print(
            #     f"Queue sizes outside worker: p: {self.p.qsize()}, q: {self.q.qsize()}"
            # )

        self.q.join()
        print(f"Queue sizes: p: {self.p.qsize()}, q: {self.q.qsize()}")

        while not self.p.empty():
            # Add the current speech snippet + corresponding silence
            # to the combined file, building up for each new line.
            tmpfile = self.p.get()
            print(f"Pulling item {tmpfile} off the results queue")
            snippet = AudioSegment.from_file(tmpfile, format="mp3")
            combined += snippet
            if dur:
                combined += AudioSegment.silent(duration=1000 * int(dur))
            tmpfile.close()

        self.speech_file = combined

    def _mix(
        self,
        segment1: AudioSegment,
        segment2: AudioSegment,
        seg2_atten: int = 0,
        fadein: int = 3000,
        fadeout: int = 6000,
    ) -> AudioSegment:
        """
        Mixes two pydub AudioSegments, then fades the result in/out.
        Returns mixed AudioSegment.
        """
        duration1 = len(segment1)
        duration2 = len(segment2)

        if duration1 > duration2:
            times = math.ceil(duration1 / duration2)
            segment2_normalized = segment2 * times
            segment2_normalized = segment2_normalized[:duration1]
        else:
            segment2_normalized = segment2[:duration1]

        return (segment1).overlay(
            (segment2_normalized - float(seg2_atten)).fade_in(fadein).fade_out(fadeout)
        )

    def invoke(self) -> BytesIO:
        """
        Generate gTTS speech snippets for each phrase; optionally mix with
        background sound-file.
        Returns BytesIO object (encoded in format specified by 'output_format').
        """
        # assert self.filenames_valid
        with alive_bar(0):
            self._gen_speech()
            if self.sound_file:
                bkgnd = AudioSegment.from_file(self.sound_file, format="wav")
                self.mix_file = self._mix(self.speech_file, bkgnd, self.attenuation)
                self.mix_file.export(self.result, format=self.output_format)
            else:
                self.speech_file.export(self.result, format=self.output_format)
        return self.result
