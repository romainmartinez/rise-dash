def get_overview_stats() -> dict:
    return {
        "pilots_trained": {
            "name": "Pilots Trained",
            "icon": "users_icon",
            "stat": "29",
            "change": "+2",
            "description": "",
            "color": "green",
            "is_last_cycle": False,
        },
        "unsatisfactory_grade_training": {
            "name": "Unsatisfactory Grade Training",
            "icon": "shield_exclamation_icon",
            "stat": "5.94%",
            "change": "+1%",
            "description": "2 pilots",
            "color": "red",
            "is_last_cycle": True,
        },
        "failed_checking": {
            "name": "Failed Checking",
            "icon": "clipboard_check_icon",
            "stat": "0%",
            "change": "-1%",
            "description": "0 pilot",
            "color": "green",
            "is_last_cycle": True,
        },
        "additional_sessions_incurred": {
            "name": "Additional Sessions Incured",
            "icon": "view_grid_add_icon",
            "stat": "1",
            "change": "+1",
            "description": "",
            "color": "red",
            "is_last_cycle": True,
        },
    }


def get_challenges_based_on_grades() -> list:
    return [
        {
            "name": "Take-Off with Engine Failure",
            "value": 10,
            "change": "+1%",
            "color": "red",
            "href": "/grade-based",
        },
        {
            "name": "Landing with Engine Failure",
            "value": 5,
            "change": "-1%",
            "color": "green",
        },
        {"name": "Go-around", "value": 4, "change": "+1%", "color": "red"},
        {"name": "Reactive Windshear", "value": 3, "change": "-2%", "color": "green"},
        {"name": "Landing", "value": 2, "change": "-1%", "color": "green"},
        {"name": "Take-Off", "value": 2, "change": "+1%", "color": "red"},
    ]


def get_challenges_based_on_telemetry() -> list:
    return [
        {
            "name": "Take-Off with Engine Failure",
            "value": 12,
            "change": "+1%",
            "color": "red",
            "href": "/training-events",
        },
        {"name": "Go Around", "value": 5, "change": "+2%", "color": "red"},
        {
            "name": "Landing with Engine Failure",
            "value": 4,
            "change": "-2%",
            "color": "green",
        },
        {"name": "Reactive Windshear", "value": 3, "change": "-1%", "color": "green"},
        {"name": "CAT II/III approach", "value": 2, "change": "+1%", "color": "red"},
        {"name": "Take-Off", "value": 1, "change": "+1%", "color": "red"},
    ]


def get_top_foqa_events() -> list:
    return [
        {
            "name": "Unstable Landing",
            "values": [0, 10, 15, 12, 9, 23, 30, 45, 50, 52],
            "change": "+1%",
            "color": "red",
        },
        {
            "name": "Unstable Approach",
            "values": [40, 38, 33, 39, 43, 45, 42, 30, 32, 30],
            "change": "-2%",
            "color": "green",
        },
        {
            "name": "Flight Operations",
            "values": [70, 60, 55, 54, 53, 47, 43, 20, 12, 10],
            "change": "-2%",
            "color": "green",
        },
    ]
