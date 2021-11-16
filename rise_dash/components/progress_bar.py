from dash import html


def progress_bar_component(
    label: str = None, value: int = 0, change: str = None, color: str = None
) -> html.Div:
    label = html.Dt(label, className="text-sm font-medium truncate")  # type: ignore
    data = html.Dd(
        html.Div(
            [
                html.Div(
                    html.Div(
                        className="bg-gray-500",
                        style={"width": f"{value}%"},
                    ),
                    className="flex w-full h-2 overflow-hidden bg-gray-200 rounded-sm",
                ),
                html.P(
                    change,
                    className="flex items-center h-full text-sm font-semibold "
                    + "text-green-600"
                    if color == "green"
                    else "text-red-600",
                ),
            ],
            className="flex items-center justify-between gap-2",
        )
    )
    return html.Div([label, data], className="text-gray-500")
