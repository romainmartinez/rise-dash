from dash import html

from ..components.box import box_component
from ..components.progress_bar import progress_bar_component

title = html.Div(html.H1("Sandbox"), className="text-2xl font-bold text-center")

sanbox_component = html.Div(
    [
        progress_bar_component(
            label="Take-Off with Engine Failure",
            value=i * 10 + 10,
            change="+2%",
            color="red",
        )
        for i in range(6)
    ],
    className="space-y-4",
)

box = box_component(sanbox_component)


sanbox_page_layout = html.Div(
    [title, box],
    className="flex flex-col justify-center min-h-screen gap-5 px-8 py-12",
)
