from dash import html

from ..api.dropdown import get_dropdowns_options
from ..api.home import (
    get_overview_stats,
    get_challenges_based_on_grades,
    get_challenges_based_on_telemetry,
    get_top_foqa_events,
)

from ..components import (
    card_component,
    stat_card_component,
    dropdown_component,
    main_container_component,
    progress_bar_component,
    sparkline_component,
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


def overview_stats() -> html.Div:
    stats = get_overview_stats()
    return html.Div(
        [
            stat_card_component(
                stat["name"],
                stat["icon"],
                stat["stat"],
                stat["change"],
                stat["description"],
                stat["color"],
                stat["is_last_cycle"],
            )
            for stat in stats.values()
        ],
        className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4",
    )


def challenge_column(title: str, challenges: list) -> html.Div:
    title = html.H3(title, className="text-lg font-medium leading-7")  # type:ignore
    bar_charts = html.Div(
        [
            progress_bar_component(
                label=challenge["name"],
                value=challenge["value"],
                change=challenge["change"],
                color=challenge["color"],
            )
            for challenge in challenges
        ],
        className="mt-4 space-y-4",
    )
    return html.Div([title, bar_charts], className="px-4 py-5 sm:p-6")


def top_events_column(title: str) -> html.Div:
    title = html.H3(title, className="text-lg font-medium leading-7")  # type:ignore
    graphs = html.Div(
        [
            sparkline_component(
                event["name"], event["change"], event["color"], event["values"]
            )
            for event in get_top_foqa_events()
        ],
        className="mt-4 space-y-4",
    )
    return card_component([title, graphs])


def home_page_layout() -> html.Div:
    header = header_dropdowns()
    stats = overview_stats()
    challenges = html.Div(
        [
            html.H2(
                "Challenges your Pilots are Experiencing",
                className="text-xl font-medium leading-7",
            ),
            html.Div(
                [
                    challenge_column(
                        "Based on Grades", get_challenges_based_on_grades()
                    ),
                    challenge_column(
                        "Based on Telemetry", get_challenges_based_on_telemetry()
                    ),
                    challenge_column(
                        "Your Watchlist", get_challenges_based_on_telemetry()
                    ),
                    top_events_column("Top FOQA Events"),
                ],
                className="grid grid-cols-1 gap-5 mt-4 divide-x sm:grid-cols-2 lg:grid-cols-4",
            ),
        ],
    )
    return main_container_component(
        content=html.Div(
            [header, stats, challenges], className="space-y-10"  # type:ignore
        ),
        title="Overview",
        last_update="November 10",
    )
