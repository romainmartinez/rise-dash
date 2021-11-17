from dash import html

from . import icons


def progress_bar_component(label: str, value: int, change: str, color: str) -> html.Div:
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
                html.Div(
                    [
                        getattr(
                            icons, f'arrow_{"up" if change[0] == "+" else "down"}_icon'
                        )(className="self-center flex-shrink-0 w-4 h-4"),
                        change[1:],
                    ],
                    className=f"flex items-center h-full text-sm font-semibold {'text-green-600' if color == 'green' else 'text-red-600'}",
                ),
            ],
            className="flex items-center justify-between gap-2",
        )
    )
    return html.Div([label, data], className="text-gray-500")
