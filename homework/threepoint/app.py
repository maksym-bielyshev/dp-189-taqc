"""Module uses provided information for project estimation."""

import math


class Project:
    def __init__(self, estimated_tasks, standard_deviation_tasks):
        self.estimated_tasks = estimated_tasks
        self.standard_deviation_tasks = standard_deviation_tasks
        self.expected_value_project = None
        self.standard_error_project = None

    def calculate_expected_value_project(self):
        if self.expected_value_project is None:
            self.expected_value_project = sum(self.estimated_tasks)
        return self.expected_value_project

    def calculate_standard_error_project(self):
        squared_list = []
        for i in self.standard_deviation_tasks:
            squared_list.append(pow(i, 2))
        self.standard_error_project = math.sqrt(sum(squared_list))
        return self.standard_error_project

    def calculate_confidence_interval(self):
        min_confidence_interval = \
            self.expected_value_project - 2 * self.standard_error_project

        max_confidence_interval = \
            self.expected_value_project + 2 * self.standard_error_project

        return min_confidence_interval, max_confidence_interval


class Task:
    def __init__(self, best_case_estimate, most_likely_estimate,
                 worst_case_estimate):
        self.best_case_estimate = best_case_estimate
        self.most_likely_estimate = most_likely_estimate
        self.worst_case_estimate = worst_case_estimate
        self.estimation = None
        self.standard_deviation = None

    def calculate_task_estimation(self):
        if self.estimation is None:
            self.estimation = (self.best_case_estimate
                               + self.most_likely_estimate * 4
                               + self.worst_case_estimate) / 6
        return self.estimation

    def calculate_task_standard_deviation(self):
        if self.standard_deviation is None:
            self.standard_deviation = \
                (self.worst_case_estimate - self.best_case_estimate) / 6
        return self.standard_deviation


def main_app():
    estimated_tasks_values = []
    standard_deviation_tasks_values = []

    while True:
        def user_estimation():
            best_case_estimate = int(input("Best-case estimate: "))
            most_likely_estimate = int(input("Most-likely estimate: "))
            worst_case_estimate = int(input("Worst-case estimate: "))
            return \
                best_case_estimate, most_likely_estimate, worst_case_estimate

        task = Task(*user_estimation())

        estimated_tasks_values.append(task.calculate_task_estimation())

        standard_deviation_tasks_values.append(
            task.calculate_task_standard_deviation())

        adding_another_task_decision = \
            input("Do you want to add another task? y/n: ").lower()

        if adding_another_task_decision != "y":
            project = Project(estimated_tasks_values,
                              standard_deviation_tasks_values)

            expected_value_project = project.calculate_expected_value_project()
            print(f"Expected value for project: "
                  f"{expected_value_project}")

            standard_error_project = project.calculate_standard_error_project()
            print(f"Standard error for project: "
                  f"{standard_error_project}")

            min_confidence_interval, max_confidence_interval = \
                project.calculate_confidence_interval()

            print(f"95 % confidence interval for project: "
                  f"{min_confidence_interval} ... "
                  f"{max_confidence_interval} points")

            break


if __name__ == "__main__":
    main_app()
