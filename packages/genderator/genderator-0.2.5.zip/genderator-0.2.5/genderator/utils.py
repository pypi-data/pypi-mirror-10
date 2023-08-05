import unicodedata


class Normalizer:
    def normalize(text):
        """
        Normalize a given text applying all normalizations.

        Params:
            text: The text to be processed.

        Returns:
            The text normalized.
        """
        text = Normalizer.remove_extra_whitespaces(text)
        text = Normalizer.replace_hyphens(text)
        text = Normalizer.normalize_unicode(text)

        return text.lower()

    @staticmethod
    def normalize_unicode(text):
        """
        Remove accent marks and symbols from input text.

        This function has the same effect that remove_accent_marks and remove_symbols but use a single loop.

        Params:
            text: The text to be processed.

        Returns:
            The text without accent marks and symbols.
        """
        categories = ['Mn', 'Sc', 'Sk', 'Sm', 'So']
        good_accents = {
            u'\N{COMBINING TILDE}',
            u'\N{COMBINING CEDILLA}'
        }

        return ''.join(c for c in unicodedata.normalize('NFKC', text)
                       if unicodedata.category(c) not in categories or c in good_accents)

    @staticmethod
    def remove_accent_marks(text):
        """
        Remove accent marks from input text.

        Params:
            text: The text to be processed.

        Returns:
            The text without accent marks.
        """
        good_accents = {
            u'\N{COMBINING TILDE}',
            u'\N{COMBINING CEDILLA}'
        }

        return ''.join(c for c in unicodedata.normalize('NFKD', text)
                       if unicodedata.category(c) != 'Mn' or c in good_accents)

    @staticmethod
    def remove_extra_whitespaces(text):
        """
        Remove extra whitespaces from input text.

        This function removes whitespaces from the beginning and the end of
        the string, but also duplicated whitespaces between words.

        Params:
            text: The text to be processed.

        Returns:
            The text without extra whitespaces.
        """
        return ' '.join(text.strip().split());

    @staticmethod
    def replace_hyphens(text):
        """
        Remove hyphens from input text.

        Params:
            text: The text to be processed.

        Returns:
            The text without hyphens.
        """
        return text.replace('-', ' ')

    @staticmethod
    def remove_symbols(text):
        """
        Remove symbols from input text.

        Params:
            text: The text to be processed.

        Returns:
            The text without symbols.
        """

        good_accents = {
            u'\N{COMBINING TILDE}',
            u'\N{COMBINING CEDILLA}'
        }

        return ''.join(c for c in unicodedata.normalize('NFKD', text)
                       if unicodedata.category(c) != 'Mn' or c in good_accents)
