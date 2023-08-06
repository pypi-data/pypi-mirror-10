# codings: utf-8

from rels.relations import Column, Relation


class Enum(Relation):
    name = Column(primary=True)
    value = Column(external=True)


class EnumWithText(Relation):
    name = Column(primary=True)
    value = Column(external=True)
    text = Column()


class NullObject(object):

    def set_related_name(self, *argv, **kwargs):
        pass
