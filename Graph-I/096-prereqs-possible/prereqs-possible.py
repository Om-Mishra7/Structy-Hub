def _course_requirements(prereqs):
    course_requirements = {}

    for i, j in prereqs:
        if i not in course_requirements:
            course_requirements[i] = set()
        course_requirements[i].add(j)

    return course_requirements


def prereqs_possible(num_courses, prereqs):
    course_requirements = _course_requirements(prereqs)

    visited_courses = set()
    visiting_courses = set()

    for course in course_requirements:
        if course not in visited_courses:
            if not traverse_course(course_requirements, course, visited_courses, visiting_courses):
                return False  # cycle found

    return True  # no cycles


def traverse_course(course_requirements, course, visited_courses, visiting_courses):
    # Cycle detected
    if course in visiting_courses:
        return False

    # Already processed
    if course in visited_courses:
        return True

    visiting_courses.add(course)

    for prereq in course_requirements.get(course, []):
        if not traverse_course(course_requirements, prereq, visited_courses, visiting_courses):
            return False

    visiting_courses.remove(course)
    visited_courses.add(course)

    return True
