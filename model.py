#!/usr/bin/python
# -*- coding: utf-8 -*-

# There's no header yet, give me some time :)
# TODO: find the right database to use (portable noSQL or json files)
# TODO: fill all classes with basic methods

################################################################################
# Investigation-related classes
################################################################################


class Case():
    '''
    Object that contains case metadata and one or more timemaps
    '''
    def __init__(self, parameters):  # FIXME: Force dictionary
        self.name = parameters["name"]
        self.date = parameters["date"]
        self.id = parameters["id"]
        self.description = parameters["description"]
        self.investigator = parameters["investigator"]
        if parameters["timemaps"] is not None:
            self.timemaps = parameters["timemaps"]
        else:
            self.timemaps = list()


class TimeMap():
    '''
    Object that contains one or more stories.
    '''
    def __init__(self, parameters):  # FIXME: Force dictionary
        self.name = parameters["name"]
        self.date = parameters["date"]
        self.id = parameters["id"]
        self.description = parameters["description"]
        if parameters["stories"] is not None:
            self.stories = parameters["stories"]
        else:
            self.stories = list()


class Story():
    '''
    Object that contains a series of events that tell a story
    '''
    def __init__(self, parameters):  # FIXME: Force dictionary
        self.name = parameters["name"]
        self.date = parameters["date"]
        self.id = parameters["id"]
        self.description = parameters["description"]
        if parameters["events"] is not None:
            self.events = parameters["events"]
        else:
            self.events = list()


class StoryEvent():
    '''
    Object that contains metadata (timestamp, device...),  notes and evidence
    linked to an event
    '''
    def __init__(self, parameters):  # FIXME: Force dictionary
        self.name = parameters["name"]
        self.date = parameters["date"]
        self.date = parameters["timezone"]
        self.id = parameters["id"]
        self.description = parameters["description"]
        if parameters["event_data"] is not None:
            self.event_data = parameters["event_data"]
        else:
            self.event_data = list()
    pass


class EventData():
    '''
    Abstract class
    Defines general methods and atributes of an object that can be linked to a
    StoryEvent object, such as Notes or Evidence objects.
    '''


class Evidence(EventData):
    '''
    Abstract class
    Inherits from EventData ################ FIXME ##################
    Defines general methods and atributes of an Evidence Object
    Object that can store a screenshot, hash, log, code...
    '''
    pass


class EvidenceFile(Evidence):
    '''
    Inherits from Evidence ################ FIXME ##################
    Object that stores a file, hashes and metadata
    '''
    pass


class EvidenceScreenshot(Evidence):
    '''
    Inherits from Evidence ################ FIXME ##################
    Object that stores a screenshot
    '''


class Note(EventData):
    '''
    Inherits from EventData ################ FIXME ##################
    Object thatcontais text, and can be associated to an event.
    '''
    pass

################################################################################
# Special classes
################################################################################


class Exporter():
    '''
    Contains methods that export one story, event or timemap to the desired format
    Evidence, notes, diagrams...
    '''
    pass


class DBI():
    '''
    Database Interface. Contains standarized calls to the Database
    '''
    pass


################################################################################
# Static functions
################################################################################

def create_case(case_data):  # FIXME: Force dictionary
    '''
    Creates case object and writes data to database through DBI
    Returns case object
    '''
    pass


def load_case(case_id):
    '''
    Creates case object and loads its data from database through DBI
    Returns status code
    '''
    pass


def save_case(case_object):
    '''
    Creates case object and loads its data from database through DBI
    Returns status code
    '''
    pass
