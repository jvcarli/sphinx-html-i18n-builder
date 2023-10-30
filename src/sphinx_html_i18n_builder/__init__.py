from sphinx_html_i18n_builder.html_i18n_builder import StandaloneHTMLi18nBuilder


def setup(app):
    app.add_builder(StandaloneHTMLi18nBuilder)
