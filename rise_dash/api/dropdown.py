def get_dropdowns_options() -> dict:
    return {
        "customers": [{"label": "Saudi Aramco", "value": "Saudi Aramco"}],
        "training_programs": [{"label": "Recurrent", "value": "Recurrent"}],
        "training_cycles": [
            {
                "label": "07/2021 -> 12/2021",
                "value": "07/2021 -> 12/2021",
            }
        ],
        "platforms": [{"label": "B737", "value": "B737"}],
        "grading_approaches": [
            {"label": "Task Based", "value": "Task Based"},
            {"label": "Competency Based", "value": "Competency Based"},
        ],
        "training_events": [
            {
                "label": "Take-offs with Engine Failure",
                "value": "Take-offs with Engine Failure",
            }
        ],
    }
