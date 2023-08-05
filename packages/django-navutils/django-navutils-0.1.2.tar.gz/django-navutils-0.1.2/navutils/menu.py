from django.core.urlresolvers import reverse

from persisting_theory import Registry


class Menus(Registry):
    """ Keep a reference to all menus"""
    look_into = 'menus'

    def prepare_name(self, data, name=None):
        return data.id

registry = Menus()
register = registry.register


class Menu(Registry):
    """A collection of nodes"""
    def __init__(self, id, *args, **kwargs):
        self.id = id
        self.template = kwargs.pop('template', 'navutils/menu.html')
        super(Menu, self).__init__(*args, **kwargs)

    def prepare_name(self, data, name=None):
        return data.id



class Node(object):

    parent = None

    def __init__(self, id, label, pattern_name=None, url=None, weight=0, title=None,
                 template='navutils/node.html', children=[], css_class=None,
                 reverse_kwargs=[], attrs={}, link_attrs={}, **kwargs):
        """
        :param str id: a unique identifier for further retrieval
        :param str label: a label for the node, that will be displayed in templates
        :param str pattern_name: the name of a django url, such as `myapp:index` to use
        as a link for the node. It will be automatically reversed.
        :param str url: a URL to use as a link for the node
        :param int weight: The importance of the node. Higher is more\
        important, default to ``0``.
        :param list reverse_kwargs: A list of strings that the pattern_name will\
        accept when reversing. Defaults to ``[]``
        :param list children: A list of children :py:class:`Node` instances\
        that will be considered as submenus of this instance.\ You can also pass\
        a callable that will return an iterable of menu nodes.
        Defaults to ``[]``.
        :param str css_class: a CSS class that will be applied to the node when
        rendering
        :param str template: the template that will be used to render the node.\
        defaults to `navutils/menu/node.html`
        :param dict node_attrs: a dictionnary of attributes to apply to the node
        html
        :param dict link_attrs: a dictionnary of attributes to apply to the node
        link html
        """
        if pattern_name and url:
            raise ValueError('MenuNode accepts either a url or a pattern_name arg, but not both')
        if not pattern_name and not url:
            raise ValueError('MenuNode needs either a url or a pattern_name arg')

        self._id = id
        self.pattern_name = pattern_name
        self.url = url
        self.label = label
        self.weight = weight
        self.template = template
        self.css_class = css_class
        self.reverse_kwargs = reverse_kwargs
        self.link_attrs = link_attrs
        self.attrs = attrs

        if 'class' in self.attrs:
            raise ValueError('CSS class is handled via  the css_class argument, don\'t use attrs for this purpose')

        self._children = children

        if not hasattr(self._children, '__call__'):
            self._children = []
            for node in children:
                self.add(node)

    @property
    def children(self):
        if hasattr(self._children, '__call__'):
            return self._children()
        return self._children

    def get_url(self, **kwargs):
        """
        :param kwargs: a dictionary of values that will be used for reversing,\
        if the corresponding key is present in :py:attr:`self.reverse_kwargs\
        <Node.reverse_kwargs>`
        :return: The target URL of the node, after reversing (if needed)
        """
        if self.pattern_name:
            expected_kwargs = {
                key: value for key, value in kwargs.items()
                if key in self.reverse_kwargs
            }
            return reverse(self.pattern_name, kwargs=expected_kwargs)
        return self.url

    def add(self, node):
        """
        Add a new node to the instance children and sort them by weight.

        :param node: A node instance
        """
        node.parent = self
        self._children.append(node)
        self._children = sorted(
            self._children,
            key=lambda i: i.weight,
            reverse=True
        )

    def is_viewable_by(self, user):
        return True

    @property
    def id(self):
        if self.parent:
            return '{0}:{1}'.format(self.parent.id, self._id)
        return self._id

    @property
    def depth(self):
        return 0 if not self.parent else self.parent.depth + 1

    def __repr__(self):
        return '<MenuNode {0}>'.format(self.label)

class AnonymousNode(Node):
    """Only viewable by anonymous users"""
    def is_viewable_by(self, user):
        return not user.is_authenticated()


class AuthenticatedNode(Node):
    """Only viewable by authenticated users"""
    def is_viewable_by(self, user):
        return user.is_authenticated()


class StaffNode(AuthenticatedNode):
    """Only viewable by staff members / admins"""

    def is_viewable_by(self, user):
        return user.is_staff or user.is_superuser
