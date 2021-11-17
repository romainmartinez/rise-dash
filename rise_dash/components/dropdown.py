from dash import html, dcc


def dropdown_component(label: str, options: list, id: str, value: str) -> html.Div:
    return html.Div(
        [
            html.P(label, className="ml-1 text-sm font-medium text-gray-500 truncate"),
            dcc.Dropdown(
                id=id,
                options=options,
                value=value,
                className="mt-1",
            ),
        ],
        className="w-full",
    )
