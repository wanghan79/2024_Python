import random
import string

class RandomStudentGenerator:
    def __init__(self):
        self.subjects = ["Math", "Science", "History", "English"]
        self.data = {
            "Basic Info": {
                "datatype": dict,
                "subs": {
                    "Name": {
                        "datatype": str,
                        "datarange": string.ascii_uppercase,
                        "strlength": 3
                    },
                    "Gender": {
                        "datatype": str,
                        "datarange": ["Male", "Female"]
                    },
                    "Age": {
                        "datatype": int,
                        "datarange": (18, 22)
                    }
                }
            },
            "Enrollment Year": {
                "datatype": int,
                "datarange": (2010, 2024)
            },
            "Student ID": {
                "datatype": str,
                "datarange": string.digits,
                "strlength": 6
            },
            "Subject": {
                "datatype": str,
                "datarange": self.subjects
            },
            "Score": {
                "datatype": float,
                "datarange": (60, 100)
            },
            "Hometown": {
                "datatype": str,
                "datarange": ["Beijing", "Shanghai", "Guangzhou", "Chengdu", "Wuhan"]
            }
        }

    def generate_random_student(self):
        student_data = {
            "Basic Info": self._generate_data(self.data["Basic Info"]),
            "Enrollment Year": self._generate_data(self.data["Enrollment Year"]),
            "Student ID": self._generate_data(self.data["Student ID"]),
            "Subject": self._generate_data(self.data["Subject"]),
            "Score": self._generate_data(self.data["Score"]),
            "Hometown": self._generate_data(self.data["Hometown"])
        }
        return student_data

    def _generate_data(self, data):
        if data["datatype"] == int:
            return random.randint(data["datarange"][0], data["datarange"][1])
        elif data["datatype"] == float:
            return random.uniform(data["datarange"][0], data["datarange"][1])
        elif data["datatype"] == str:
            if isinstance(data["datarange"], str):
                return ''.join(random.choices(data["datarange"], k=data.get("strlength", 1)))
            else:
                return random.choice(data["datarange"])

    def generate_random_students(self, num_students):
        students = [self.generate_random_student() for _ in range(num_students)]
        return students

# 使用示例
generator = RandomStudentGenerator()
random_students = generator.generate_random_students(num_students=5)
for student in random_students:
    print(student)
