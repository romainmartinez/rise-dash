from dash import dcc, html

from . import icons

nav_items = [
    {"name": "Overview", "href": "/", "icon": "home", "current": True},
    {
        "name": "Training Events",
        "href": "/training-events",
        "icon": "paper_airplane",
        "current": False,
    },
    {
        "name": "Deep Dive Analysis",
        "href": "#",
        "icon": "chart_bar",
        "current": False,
        "disabled": True,
    },
    {
        "name": "Instructor Grading Insights",
        "href": "#",
        "icon": "document_text",
        "current": False,
        "disabled": True,
    },
    {
        "name": "EBT",
        "href": "#",
        "icon": "chart_pie",
        "current": False,
        "disabled": True,
    },
]


def sidebar_component() -> html.Div:
    logo = html.Div(
        html.H2(
            [
                html.Span("CAE", className="font-extralight"),
                html.Span("Rise Analytics", className="font-semibold"),
            ],
            className="text-2xl leading-7 tracking-wide text-gray-600",
        ),
        className="flex items-center flex-shrink-0 px-4",
    )

    navigation = html.Div(
        html.Nav(
            [
                dcc.Link(
                    [
                        getattr(icons, f"{nav_item['icon']}_icon")(
                            className="flex-shrink-0 w-6 h-6 mr-3 pointer-events-none opacity-70"
                        ),
                        nav_item["name"],
                    ],
                    href=nav_item["href"],
                    id=nav_item["name"],
                    className=f"flex items-center px-3 py-2 text-sm font-medium border-l-4 "
                    + (
                        "bg-blue-50 border-blue-600 text-blue-600 hover:bg-blue-50 hover:text-blue-600"
                        if nav_item["current"]
                        else "border-transparent text-gray-600 hover:bg-gray-50 hover:text-gray-700 "
                        + (
                            "opacity-50 cursor-not-allowed"
                            if nav_item.get("disabled")
                            else ""
                        )
                    ),
                )
                for nav_item in nav_items
            ],
            className="flex-1 space-y-1",
        ),
        className="flex flex-col flex-grow mt-5",
    )

    sidebar = html.Div(
        [logo, navigation],
        className="fixed inset-y-0 flex flex-col flex-grow w-64 py-5 overflow-y-auto bg-white border-r border-gray-200",
    )

    footer = html.Footer(
        html.P(
            "© 2021 CAE, Inc. All rights reserved.",
            className="text-center text-gray-400",
        ),
        className="mx-auto overflow-hidden p-7",
    )

    content = html.Div(
        [
            html.Div(
                [html.Main(id="page-content"), footer],
                className="flex-1 space-y-12",
            )
        ],
        className="flex flex-col flex-1 pl-64",
    )

    return html.Div(
        [dcc.Location(id="url", refresh=False), sidebar, content],
        className="min-h-screen antialiased text-gray-800 bg-gray-50",
    )
