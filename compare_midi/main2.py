import pretty_midi
import numpy as np
import mir_eval

def midi_to_note_array(midi_file):
    midi_data = pretty_midi.PrettyMIDI(midi_file)
    print(f'Midi data: {midi_data}')
    print(f'Number of instruments: {len(midi_data.instruments)}')
    notes = []
    for instrument in midi_data.instruments:
        if not instrument.is_drum:
            for note in instrument.notes:
                notes.append([note.start, note.end, note.pitch])
    return np.array(notes)

ground_truth_file = 'compare_midi/seq1.mid'
predicted_file = 'compare_midi/seq1_diff_note.mid'

ground_truth_notes = midi_to_note_array(ground_truth_file)
predicted_notes = midi_to_note_array(predicted_file)
# Extract onset, offset, and pitch information

ref_onsets = ground_truth_notes[:, :2]
ref_pitches = ground_truth_notes[:, 2]

est_onsets = predicted_notes[:, :2]
est_pitches = predicted_notes[:, 2]
# Evaluate the transcription
onset_tolerance = 0.05  # 50ms tolerance for onset matching
offset_ratio = 0.2      # Offset ratio tolerance

try:
    mir_eval.transcription.validate(ref_onsets, ref_pitches, est_onsets, est_pitches)
    print('Inputs have been validated')
except Exception as e:
    print(f'Exception: {e}')

eval_results = mir_eval.transcription.evaluate(
    ref_onsets, ref_pitches,
    est_onsets, est_pitches,
    onset_tolerance=onset_tolerance, offset_ratio=offset_ratio
)

# Print the results
for metric, value in eval_results.items():
    print(f'{metric}: {value:.4f}')
