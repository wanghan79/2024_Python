data_range = {
    'name': ['John', 'Smith', 'Bob','Jane'],
    'age': (18, 22),
    'id': (100000, 200000),
    'major': ['Computer Science', 'Software Engineering', 'Electronics']
}

example_template = {
    "datatype": list,
    "subs": {
        "sub1":{
            "datatype": dict,
            "subs": {
                "name": {
                    "datatype": str,
                    "datarange": data_range['name']
                },
                "age": {
                    "datatype": int,
                    "datarange": data_range['age']
                },
                "id": {
                    "datatype": int,
                    "datarange": data_range['id']
                }
            }
        },

        "sub2": {
            "datatype": dict,
            "subs": {
                "major": {
                    "datatype": str,
                    "datarange":data_range['major']
                },

                "teacher": {
                    "datatype": str,
                    "datarange":data_range['name']
                }
            }
        }  
    }
}
