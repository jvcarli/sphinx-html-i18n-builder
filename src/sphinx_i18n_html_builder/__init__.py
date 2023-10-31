from sphinx_i18n_html_builder.builder import Standalonei18nHTMLBuilder


def setup(app):
    app.add_builder(Standalonei18nHTMLBuilder)
