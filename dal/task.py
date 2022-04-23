"""
This code was generated by a tool. Don't modify it manually.
http://sqldalmaker.sourceforge.net
"""

from .data_store import *


class Task(Base):
    __tablename__ = 'tasks'

    t_id = Column('t_id', Integer, primary_key=True, autoincrement=True)
    g_id = Column('g_id', Integer, ForeignKey('groups.g_id'))
    t_priority = Column('t_priority', Integer)
    t_date = Column('t_date', String)
    t_subject = Column('t_subject', String)
    t_comments = Column('t_comments', String)
