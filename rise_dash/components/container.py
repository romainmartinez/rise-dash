from dash import html


def main_container_component(
    content: html.Div, title: str, last_update: str
) -> html.Div:
    header = html.Div(
        [
            html.H1(title, className="text-3xl font-semibold"),
            html.Span(
                f"As of {last_update}",
                className="inline-flex items-center px-2.5 py-0.5 rounded-md text-sm font-medium bg-gray-100 text-gray-700",
            ),
        ],
        className="flex items-center justify-between",
    )
    return html.Div(
        [header, content], className="px-8 py-4 mx-auto mt-4 space-y-4 max-w-7xl"
    )
