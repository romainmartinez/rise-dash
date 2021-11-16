from dash import html


def box_component(children=None, additional_classes: str = "") -> html.Div:
    return html.Div(
        children,
        className="px-4 py-10 bg-white shadow rounded-lg " + additional_classes,
    )
