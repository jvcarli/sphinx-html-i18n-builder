from sphinx_i18n_html_builder.html_i18n_builder import Standalonei18nHTMLBuilder


def setup(app):
    app.add_builder(Standalonei18nHTMLBuilder)
