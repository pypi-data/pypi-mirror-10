class Translated:
    """
    The Translated object, which contains Google Translator's result.

    :param src: source langauge (default: auto)
    :param dest: destination language (default: en)
    :param origin: original text
    :param text: translated text
    :param pronunciation: the pronunciation provided by Google Translator
    """
    def __init__(self, src, dest, origin, text, pronunciation):
        self.src = src
        self.dest = dest
        self.origin = origin
        self.text = text
        self.pronunciation = pronunciation

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '<Translated src={src} dest={dest} text={text} pronunciation={pronunciation}>'.format(
            src=self.src, dest=self.dest, text=self.text, pronunciation=self.pronunciation)