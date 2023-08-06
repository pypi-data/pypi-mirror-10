#!/usr/bin/env python
# encoding: utf-8

"""Derived class to parse Moodle course items, it parses
   Moodle and therefor extends off of Parser
"""

from moodlefuse.moodle.parser import Parser
from moodlefuse.moodle import assignments
from moodlefuse.moodle import attributes


class AssignmentParser(Parser):

    def __init__(self):
        super(AssignmentParser, self).__init__()

    def get_all_submission_file_names(self, assignment_content):
        submission_file_names = []
        files = self.get_all_submission_names(assignment_content)
        emails = self.get_all_student_emails(assignment_content)
        for email, submission_name in zip(emails, files):
            file_name = email + assignments.SUBMISSION_LISTING_DELIMINATOR + submission_name
            submission_file_names.append(file_name)

        return submission_file_names

    def get_assignment_submission_path(self, assignment_content, submission):
        return self.scraper.get_link_from_linktext(assignment_content, submission)

    def get_all_student_names(self, assignment_content):
        return self.get_items_from_table(
            assignment_content, attributes.THIRD_CELL
        )

    def get_all_submission_names(self, assignment_content):
        return [item.strip('\t\r\n ') for item in self.get_items_from_table(
            assignment_content, attributes.EIGHT_CELL
        )]

    def get_all_student_emails(self, assignment_content):
        return self.get_items_from_table(
            assignment_content, attributes.THIRD_CELL_EMAIL
        )

    def get_all_student_grades(self, assignment_content):
        return self.get_items_from_table(
            assignment_content, attributes.FIFTH_CELL, self.remove_special_chars
        )

    def get_items_from_table(self, html, tdclass, convert_function=None):
        items = []
        item_list = self.scraper.get_html_items_with_tdclass(html, tdclass)
        for html_item in item_list:
            item = html_item.get_text()
            if item != '':
                if convert_function is not None:
                    item = convert_function(item)
                items.append(item)

        return self.remove_unicode(items)
