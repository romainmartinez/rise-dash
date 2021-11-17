from dash import html

from . import icons


def card_component(children=None, additional_classes: str = "") -> html.Div:
    return html.Div(
        children,
        className=f"px-4 py-5 overflow-hidden bg-white rounded-lg shadow sm:p-6 {additional_classes}",
    )


def stat_card_component(
    name: str,
    icon: str,
    stat: str,
    change: str,
    description: str,
    color: str,
    is_last_cycle: bool,
) -> html.Div:
    header = html.Div(
        [
            getattr(icons, icon)("w-7 h-7"),
            html.Dt(name, className="text-sm font-medium truncate"),
        ],
        className="flex items-center gap-4 text-gray-500",
    )
    body = html.Div(
        [
            html.Div(
                [
                    html.P(stat, className="text-4xl font-semibold text-gray-600"),
                    html.P(description, className="text-sm font-medium text-gray-500"),
                ]
            ),
            html.Div(
                [
                    html.Div(
                        [
                            getattr(
                                icons,
                                f"arrow_{'up' if change[0] == '+' else 'down'}_icon",
                            )("self-center flex-shrink-0 w-5 h-5"),
                            change[1:],
                        ],
                        className="flex items-center text-lg font-semibold "
                        + ("text-green-600" if color == "green" else "text-red-600"),
                    ),
                ]
            ),
        ],
        className="flex justify-between gap-4 mt-3",
    )
    footer = (
        html.Div(
            [icons.delta_icon("-ml-0.5 mr-1.5 h-2 w-2 text-gray-400"), "Last Cycle"],
            className="absolute right-4 bottom-4 inline-flex items-center px-2.5 py-0.5 rounded-md text-sm font-medium text-gray-500 bg-gray-50",
        )
        if is_last_cycle
        else None
    )
    return card_component(
        [header, body, footer],
        additional_classes=f"relative border-l-8 pb-8 "
        + ("border-green-500" if color == "green" else "border-red-500"),
    )
