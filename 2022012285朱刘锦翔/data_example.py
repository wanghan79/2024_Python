test_data = {
    "datatype": "tuple",
    "subs": {
        "sub1": {
            "datatype": "list",
            "subs": {
                "sub1": {
                    "datatype": "int",
                    "datarange": (0, 100)
                },
                "sub2": {
                    "datatype": "str",
                    "datarange": "this is a string"
                }
            }
        },
        "sub2": {
            "datatype": "tuple",
            "subs": {
                "sub1": {
                    "datatype": "float",
                    "datarange": (0.0, 100.0)
                },
                "sub2": {
                    "datatype": "bool",
                    "datarange": (True, False)
                }
            }
        }
    }
}