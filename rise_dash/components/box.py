from dash import html


def box_component(children=None, additional_classes: str = "") -> html.Div:
    return html.Div(
        children,
        className=f"px-4 py-5 overflow-hidden bg-white rounded-lg shadow sm:p-6 {additional_classes}",
    )
