from dash import Input, Output

from .app import app

from .components import sidebar_component

from .pages.home import home_page_layout
from .pages.error import error_page_layout

app.layout = sidebar_component()


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page(pathname):
    if pathname == "/":
        return home_page_layout()
    else:
        return error_page_layout(error_msg="404 | Page not found")


def launch_server(debug: bool = True):
    if debug:
        app.run_server(debug=True, dev_tools_ui=False)
    else:
        app.run_server(debug=False)
