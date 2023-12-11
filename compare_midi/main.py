#!/usr/bin/env python3
import mido
from mido import MidiFile
import argparse

def read_midi(file_path):
    mid = MidiFile(file_path)
    notes, tempo_changes = [], []
    ticks_per_beat = mid.ticks_per_beat

    for i, track in enumerate(mid.tracks):
        for msg in track:
            if msg.type == 'note_on':
                notes.append((msg.note, msg.time))
            if msg.type == 'set_tempo':
                tempo_changes.append(msg.tempo)
    return notes, tempo_changes, ticks_per_beat

def compare_notes(notes1, notes2, ticks_per_beat):
    # Compare notes here and return a similarity score
    matched_notes = 0
    for n1 in notes1:
        for n2 in notes2:
            if n1[0] == n2[0]:  # same pitch and within time tolerance ## and abs(n1[1] - n2[1]) <= (ticks_per_beat / 2)
                matched_notes += 1
                break
    return matched_notes / max(len(notes1), len(notes2))

def compare_note_times(notes1, notes2, ticks_per_beat):
    matched_notes = 0
    for n1, n2 in zip(notes1, notes2):
        if n1[1] == n2[1]:  # same pitch and within time tolerance ## and abs(n1[1] - n2[1]) <= (ticks_per_beat / 2)
            matched_notes += 1
    return matched_notes / max(len(notes1), len(notes2))


def compare_avg_tempo(tempo1, tempo2, ticks_per_beat):
    avg_tempo1 = sum(tempo1) / len(tempo1) if tempo1 else 0
    avg_tempo2 = sum(tempo2) / len(tempo2) if tempo2 else 0
    return 1 - abs(avg_tempo1 - avg_tempo2) / max(avg_tempo1, avg_tempo2)

def main(args):
    # Read MIDI files
    notes_ref, tempo_ref, ticks_per_beat = read_midi(args.reference)
    notes_other, tempo_other, ticks_per_beat = read_midi(args.other)

    # Compare and get scores
    note_similarity = compare_notes(notes_ref, notes_other, ticks_per_beat)
    avg_tempo_similarity = compare_avg_tempo(tempo_ref, tempo_other, ticks_per_beat)
    exact_timestamp_similarity = compare_note_times(notes_ref, notes_other, ticks_per_beat)

    # Report
    print(f"Note similarity: {note_similarity}")
    print(f"Exact timestamp similarity: {exact_timestamp_similarity}")
    print(f"Avg tempo similarity: {avg_tempo_similarity}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two MIDI files in terms of notes and tempo.")
    parser.add_argument("reference", help="Path to the reference MIDI file")
    parser.add_argument("other", help="Path to the MIDI file to compare with the reference")

    args = parser.parse_args()
    main(args)
