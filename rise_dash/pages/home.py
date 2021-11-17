from dash import html

from ..components.container import main_container_component
from ..components.box import box_component
from ..components.progress_bar import progress_bar_component


def home_page_layout() -> html.Div:
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

    header = []
    stats = []
    challenges = []

    return main_container_component(
        content=html.Div(
            [box],
        ),
        title="Overview",
        last_update="November 10",
    )
