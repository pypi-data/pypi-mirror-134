import weakref
from typing import Dict, Mapping, Union

from ruamel.yaml.comments import CommentedMap

from souschef import mixins


class Section(
    mixins.SelectorMixin,
    mixins.GetSetItemMixin,
    mixins.InlineCommentMixin,
    mixins.AddSection,
):
    def __init__(
        self,
        name: Union[int, str],
        item: CommentedMap,
        parent: CommentedMap,
        config,
    ):
        self.__yaml = weakref.ref(item)
        self._parent = weakref.ref(parent)
        self._config = weakref.ref(config)
        self._name = name

    def __repr__(self) -> str:
        return f"<Section {self._name}>"

    @property
    def _yaml(self):
        return self.__yaml()

    def __str__(self) -> str:
        return self._name

    @property
    def value(self):
        return [v for v in self]

    @value.setter
    def value(self, items: Union[None, "Section", str, Dict]):
        if isinstance(items, dict):
            for key, value in items.items():
                self[key] = value
        else:
            self._parent()[self._name] = items

    def update(self, section: Mapping):
        self.value = section
