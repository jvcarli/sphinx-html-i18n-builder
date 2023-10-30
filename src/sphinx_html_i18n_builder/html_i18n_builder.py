from sphinx.builders.html import StandaloneHTMLBuilder


class StandaloneHTMLi18nBuilder(StandaloneHTMLBuilder):
    # Needed for calling `$ sphinx-build -b html_i18n <input-dir> <output-dir>`
    name = "html_i18n"
