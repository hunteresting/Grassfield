from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note, Rest

import random

def get_random_notes(n, pitches, durations, rests=True):
    if rests:
        pitches.append('r')

    result = NoteSeq()

    for i in range(n):
        pitch = random.choice(pitches)
        duration = random.choice(durations)

        if pitch == 'r':
            result.append(Rest(dur=duration))
        else:
            result.append(Note(pitch, octave=4, dur=duration))

    return result

durations = [1/2, 1/4, 1/8, 1/16]

A_major = [9, 11, 1, 2, 4, 6, 8]
G_major = [7, 9, 11, 0, 2, 4, 6]
D_major = [2, 4, 6, 7, 9, 11, 1]

notes1 = get_random_notes(20, pitches=A_major, durations=[1/8, 1/16])
midi = Midi(number_tracks=1, tempo=120)
midi.seq_notes(notes1, track=0)
midi.write('examples/A_major.mid')

hithat = NoteSeq('F#15, R16"') * 16
kick_snare = NoteSeq('C16, R16 R16 C16 D16 C16 R16 R16') * 4

midi = Midi(number_tracks=1, tempo=120)
midi.seq_notes(hithat, track=0)
midi.seq_notes(kick_snare, track=0)
midi.write('examples/drum.mid')

piano = NoteSeq('A4, R4') * 4

midi = Midi(number_tracks=3, tempo=120)
midi.seq_notes(hithat,track=0)
midi.seq_notes(kick_snare, track=0)
midi.seq_notes(notes1, track=1)
midi.seq_notes(piano, track=2)
midi.write('examples/Amajor_drum_piano.mid')
