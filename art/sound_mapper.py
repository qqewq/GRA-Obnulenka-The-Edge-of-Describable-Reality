def map_to_sound(foam_history, stability_history):
    """
    Mapping internal sim states to MIDI-like sequences.
    Foam maps to pitch (dissonance), stability maps to duration.
    """
    midi_notes = []
    for f, s in zip(foam_history, stability_history):
        note = int(f * 10) % 128  # Pitch
        duration = max(0.1, 1.0 - s)  # Duration
        midi_notes.append({"note": note, "duration": duration})
    return midi_notes
