""" from https://github.com/keithito/tacotron """
from text import cleaners


def text_to_sequence(text, symbols, cleaner_names):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
      cleaner_names: names of the cleaner functions to run the text through
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  _symbol_to_id = {s: i for i, s in enumerate(symbols)}

  clean_text = _clean_text(text, cleaner_names)
  return [
      _symbol_to_id[symbol] for symbol in clean_text if symbol in _symbol_to_id
  ]


def _clean_text(text, cleaner_names):
  for name in cleaner_names:
    if cleaner := getattr(cleaners, name):
      text = cleaner(text)
    else:
      raise Exception(f'Unknown cleaner: {name}')
  return text
