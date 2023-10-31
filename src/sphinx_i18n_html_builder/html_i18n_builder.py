from sphinx.builders.html import StandaloneHTMLBuilder


class Standalonei18nHTMLBuilder(StandaloneHTMLBuilder):
    # Needed for calling `$ sphinx-build -b i18n_html <input-dir> <output-dir>`
    name = "i18n_html"
