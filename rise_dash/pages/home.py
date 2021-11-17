from dash import html

from ..api.dropdown import get_dropdowns_options
from ..components import (
    box_component,
    dropdown_component,
    main_container_component,
    progress_bar_component,
)


def header_dropdowns() -> html.Div:
    options = get_dropdowns_options()
    customer = dropdown_component(
        "Customer",
        options=[
            {"label": "Air Asia", "value": "ASIA"},
        ],
        id="customer-dropdown",
        value="ASIA",
    )
    training_program = dropdown_component(
        "Training Program",
        options=[
            {"label": "New York City", "value": "NYC"},
        ],
        id="training-program-dropdown",
        value="NYC",
    )
    training_cycle = dropdown_component(
        "Training Cycle", options=[], id="training-cycle-dropdown", value=""
    )
    platform = dropdown_component(
        "Platform", options=[], id="platform-dropdown", value=""
    )
    grading_approach = dropdown_component(
        "Grading Approach", options=[], id="grading-approach-dropdown", value=""
    )
    return html.Div(
        [customer, training_program, training_cycle, platform, grading_approach],
        className="flex items-center justify-around gap-5",
    )


def challenge_column(title: str) -> html.Div:
    title = html.H3(title, className="text-lg font-medium leading-7")  # type:ignore
    bar_charts = html.Div(
        [
            progress_bar_component(
                label="Take-Off with Engine Failure",
                value=i * 10 + 10,
                change="-2%",
                color="green",
            )
            for i in range(6, 0, -1)
        ],
        className="mt-4 space-y-4",
    )
    return html.Div([title, bar_charts], className="px-4 py-5 sm:p-6")


def top_events_column(title: str) -> html.Div:
    title = html.H3(title, className="text-lg font-medium leading-7")  # type:ignore
    return box_component([title])


def home_page_layout() -> html.Div:
    header = header_dropdowns()
    stats = html.Div(
        "Stats",
        className="flex items-center justify-center h-40 text-blue-700 bg-blue-200 border border-blue-700 rounded-lg",
    )
    challenges = html.Div(
        [
            html.H2(
                "Challenges your Pilots are Experiencing",
                className="text-xl font-medium leading-7",
            ),
            html.Div(
                [
                    challenge_column("Based on Grades"),
                    challenge_column("Based on Telemetry"),
                    challenge_column("Your Watchlist"),
                    top_events_column("Top FOQA Events"),
                ],
                className="grid grid-cols-1 gap-5 mt-4 divide-x sm:grid-cols-2 lg:grid-cols-4",
            ),
        ],
    )
    return main_container_component(
        content=html.Div(
            [header, stats, challenges], className="space-y-6"  # type:ignore
        ),
        title="Overview",
        last_update="November 10",
    )
