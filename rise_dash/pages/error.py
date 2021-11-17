from dash import html


def error_page_layout(error_msg: str) -> html.Div:
    return html.Div(
        html.P(error_msg, className="text-2xl font-light tracking-wider text-gray-500"),
        className="flex items-center justify-center min-h-screen",
    )
