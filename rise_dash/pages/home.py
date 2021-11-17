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
        id="customer-dropdown",
        options=options["customers"],
        value=options["customers"][0]["value"],
    )
    training_program = dropdown_component(
        "Training Program",
        id="training-program-dropdown",
        options=options["training_programs"],
        value=options["training_programs"][0]["value"],
        searchable=False,
    )
    training_cycle = dropdown_component(
        "Training Cycle",
        id="training-cycle-dropdown",
        options=options["training_cycles"],
        value=options["training_cycles"][0]["value"],
    )
    platform = dropdown_component(
        "Platform",
        id="platform-dropdown",
        options=options["platforms"],
        value=options["platforms"][0]["value"],
    )
    grading_approach = dropdown_component(
        "Grading Approach",
        options=options["grading_approaches"],
        id="grading-approach-dropdown",
        value=options["grading_approaches"][0]["value"],
        searchable=False,
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
