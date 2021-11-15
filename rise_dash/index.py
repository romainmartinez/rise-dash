from dash import Input, Output, dcc, html

from .app import app
from .pages.home import home_page_layout
from .pages.sandbox import sanbox_page_layout

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")],
    className="bg-gray-200",
)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page(pathname):
    if pathname == "/":
        return home_page_layout
    elif pathname == "/sandbox":
        return sanbox_page_layout
    else:
        return "404"


def launch_server(debug: bool = True):
    if debug:
        app.run_server(debug=True, dev_tools_ui=False)
    else:
        app.run_server(debug=False)
