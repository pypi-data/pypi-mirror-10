from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from ripozo import Relationship, ListRelationship
from ripozo.resources.constructor import ResourceMetaClass
from ripozo.resources.restmixins import CRUDL

from ripozo_sqlalchemy import AlchemyManager

from sqlalchemy.inspection import inspect
from sqlalchemy.orm import class_mapper, RelationshipProperty


def _get_fields_for_model(model):
    """
    Gets all of the fields on the model.

    :param DeclarativeModel model: A SQLAlchemy ORM Model
    :return: A tuple of the fields on the Model corresponding
        to the columns on the Model.
    :rtype: tuple
    """
    fields = []
    for name in model._sa_class_manager:
        prop = getattr(model, name)
        if isinstance(prop.property, RelationshipProperty):
            for pk in class_mapper(prop.class_).primary_key:
                fields.append('{0}.{1}'.format(name, pk.name))
        else:
            fields.append(name)
    return tuple(fields)


def _get_pks(model):
    """
    Gets a tuple of the primary keys
    on the model.

    :param DeclarativeMeta model: The SQLAlchemy ORM model.
    :return: tuple of unicode primary key column names
    :rtype: tuple
    """
    return tuple([key.name for key in inspect(model).primary_key])


def _get_relationships(model):
    """
    Gets the necessary relationships for the resource
    by inspecting the sqlalchemy model for relationships.

    :param DeclarativeMeta model: The SQLAlchemy ORM model.
    :return: A tuple of Relationship/ListRelationship instances
        corresponding to the relationships on the Model.
    :rtype: tuple
    """
    relationships = []
    for name in model._sa_class_manager:
        prop = getattr(model, name)
        if isinstance(prop.property, RelationshipProperty):
            class_ = inspect(model).relationships._data[name].mapper.class_
            if prop.property.uselist:
                rel = ListRelationship(name, relation=class_.__name__)
            else:
                rel = Relationship(name, relation=class_.__name__)
            relationships.append(rel)
    return tuple(relationships)


def create_resource(model, session_handler, resource_bases=(CRUDL,),
                    relationships=None, links=None, preprocessors=None,
                    postprocessors=None, fields=None, paginate_by=100,
                    auto_relationships=True, pks=None):
        """
        Creates a ResourceBase subclass by inspecting a SQLAlchemy
        Model. This is somewhat more restrictive than explicitly
        creating managers and resources.  However, if you only need
        any of the basic CRUD+L operations,

        :param sqlalchemy.Model model:  This is the model that
            will be inspected to create a Resource and Manager from.
            By default, all of it's fields will be exposed, although
            this can be overridden using the fields attribute.
        :param tuple resource_bases: A tuple of ResourceBase subclasses.
            Defaults to the restmixins.CRUDL class only.  However if you only
            wanted Update and Delete you could pass in
            ```(restmixins.Update,  restmixins.Delete)``` which
            would cause the resource to inherit from those two.
            Additionally, you could create your own mixins and pass them in
            as the resource_bases
        :param tuple relationships: extra relationships to pass
            into the ResourceBase constructor.  If auto_relationships
            is set to True, then they will be appended to these relationships.
        :param tuple links: Extra links to pass into the ResourceBase as
            the class _links attribute.  Defaults to an empty tuple.
        :param tuple preprocessors: Preprocessors for the resource class attribute.
        :param tuple postprocessors: Postprocessors for the resource class attribute.
        :param ripozo_sqlalchemy.SessionHandler session_handler: A session handler
            to use when instantiating an instance of the Manager class created
            from the model.  This is responsible for getting and handling
            sessions in both normal cases and exceptions.
        :param tuple fields: The fields to expose on the api.  Defaults to
            all of the fields on the model.
        :param bool auto_relationships: If True, then the SQLAlchemy Model
            will be inspected for relationships and they will be automatically
            appended to the relationships on the resource class attribute.
        :return: A ResourceBase subclass and AlchemyManager subclass
        :rtype: ResourceMetaClass
        """
        relationships = relationships or tuple()
        if auto_relationships:
            relationships += _get_relationships(model)
        links = links or tuple()
        preprocessors = preprocessors or tuple()
        postprocessors = postprocessors or tuple()
        pks = pks or _get_pks(model)
        fields = fields or _get_fields_for_model(model)

        manager_cls_attrs = dict(paginate_by=paginate_by, fields=fields, model=model)
        manager_class = type(str(model.__name__), (AlchemyManager,), manager_cls_attrs)
        manager = manager_class(session_handler)

        resource_cls_attrs = dict(preprocessors=preprocessors,
                                  postprocessors=postprocessors,
                                  _relationships=relationships, _links=links,
                                  pks=pks, manager=manager)
        res_class = ResourceMetaClass(str(model.__name__), resource_bases, resource_cls_attrs)
        return res_class
