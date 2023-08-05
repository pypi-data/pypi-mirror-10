
#
# This module contains classes implementing the Xigt data model.
# Common members and methods may be found in the xigt.mixins module,
# so take note of the class inheritance below.
#

import logging
import warnings
from itertools import chain

from xigt.consts import (
    CONTENT,
    SEGMENTATION,
    FULL,
    INCREMENTAL,
    TRANSIENT
)

from xigt.mixins import (
    XigtContainerMixin,  # XigtCorpus, Igt, Tier, Metadata
    XigtAttributeMixin,  # XigtCorpus, Igt, Tier, Item, Metadata, Meta
    XigtReferenceAttributeMixin,  # Tier, Item
)

from xigt.metadata import (
    XigtMetadataMixin  # XigtCorpus, Igt, Tier
)

from xigt import ref

from xigt.errors import (
    XigtError,
    XigtStructureError,
    XigtAttributeError,
    XigtWarning
)


class XigtCorpus(XigtContainerMixin, XigtAttributeMixin, XigtMetadataMixin):
    """
    A container of Igt objects, as well as corpus-level attributes and
    metadata. In serialization formats (e.g. XigtXML), XigtCorpus
    becomes the root element.

    Args:
        id: corpus identifier
        attributes: corpus-level attributes
        metadata: corpus-level |Metadata|
        igts: iterator of |Igt|
        mode: how to instantiate the corpus (default: `full`).
            Possible values include:

            =========== ================================================
               Value        Description
            =========== ================================================
            full        Preload all |Igt| and store them in memory
                        during initialization
            incremental Load each |Igt| sequentially as needed, and keep
                        them in memory
            transient   Load each |Igt| sequentially as needed, but
                        don't keep them in memory; useful for piped
                        input processing
            =========== ================================================
    """

    def __init__(self, id=None, type=None, attributes=None, metadata=None,
                 igts=None, mode=FULL, namespace=None, nsmap=None):
        XigtContainerMixin.__init__(self, contained_type=Igt)
        XigtAttributeMixin.__init__(
            self, id=id, type=type, attributes=attributes,
            namespace=namespace, nsmap=nsmap
        )
        XigtMetadataMixin.__init__(self, metadata)
        self.mode = mode
        if mode == FULL:
            self.extend(igts or [])
        else:
            self._generator = igts

    def __repr__(self):
        return '<XigtCorpus object (id: {}) with {} Igts at {}>'.format(
            str(self.id or '--'), len(self), str(id(self))
        )

    def __iter__(self):
        if self.mode == FULL:
            for igt in XigtContainerMixin.__iter__(self):
                yield igt
        else:
            for igt in self._generator:
                if self.mode == INCREMENTAL:
                    self.add(igt)
                yield igt
            self.mode = FULL

    @property
    def igts(self):
        return self._list
    @igts.setter
    def igts(self, value):
        self.clear()
        self.extend(value or [])


class Igt(XigtContainerMixin, XigtAttributeMixin, XigtMetadataMixin):
    """
    An IGT (Interlinear Glossed Text) instance.
    """
    def __init__(self, id=None, type=None, attributes=None, metadata=None,
                 tiers=None, corpus=None, namespace=None, nsmap=None):
        XigtContainerMixin.__init__(self, contained_type=Tier)
        XigtAttributeMixin.__init__(
            self, id=id, type=type, attributes=attributes,
            namespace=namespace, nsmap=nsmap
        )
        XigtMetadataMixin.__init__(self, metadata)

        self._referent_cache = {}
        self._referrer_cache = {}
        self._parent = corpus
        self._itemdict = {}

        self.extend(tiers or [])
        self.refresh_indices()

    def __repr__(self):
        return '<Igt object (id: {}) with {} Tiers at {}>'.format(
            str(self.id or '--'), len(self), str(id(self))
        )

    def refresh_indices(self, tiers=False, items=True,
                        referents=True, referrers=True):
        if tiers:
            self.refresh_index()  # from XigtContainerMxin

        if items is True:
            items = [i for t in self.tiers for i in t.items]
        up = self._update_item_index
        for item in items:
            up(item)

        if referents is True:
            referents = self.tiers + [i for t in self.tiers for i in t.items]
        up = self._update_referent_index
        for r in referents:
            up(r)

        if referrers is True:
            referrers = self.tiers + [i for t in self.tiers for i in t.items]
        up = self._update_referrer_index
        for r in referrers:
            up(r)

    def _update_item_index(self, item):
        idict = self._itemdict
        i_id = item.id
        if i_id in idict and idict[i_id] != item:
            warnings.warn(
                'Item "{}" already exists in Igt.'.format(i_id),
                XigtWarning
            )
        idict[i_id] = item

    def _update_referent_index(self, obj):
        if obj.id is None:
            warnings.warn(
                'Cannot cache referents for an object with no id.',
                XigtWarning
            )
            return
        rdict = self._referent_cache.setdefault(obj.id, {})
        for refattr in obj.allowed_reference_attributes():
            rdict[refattr] = ref.ids(obj.attributes.get(refattr, ''))

    def _update_referrer_index(self, obj):
        o_id = obj.id
        if o_id is None:
            warnings.warn(
                'Cannot cache referrers for an object with no id.',
                XigtWarning
            )
            return
        rdict = self._referrer_cache
        attrget = obj.attributes.get  # just loop optimization
        for refattr in obj.allowed_reference_attributes():
            ids = ref.ids(attrget(refattr, ''))
            for id in ids:
                rdict.setdefault(id, {}).setdefault(refattr, []).append(o_id)

    @property
    def corpus(self):
        return self._parent

    @property
    def tiers(self):
        return self._list
    @tiers.setter
    def tiers(self, value):
        self.clear()
        self.extend(value or [])

    def get_item(self, item_id, default=None):
        return self._itemdict.get(item_id, default)

    def get_any(self, _id, default=None):
        return self.get(_id, self._itemdict.get(_id, default))

    def referents(self, id, refattrs=None):
        if refattrs is None:
            return self._referent_cache.get(id, {})
        else:
            return ref.referents(self, id, refattrs=refattrs)

    def referrers(self, id, refattrs=None):
        if refattrs is None:
            return self._referrer_cache.get(id, {})
        else:
            return ref.referrers(self, id, refattrs=refattrs)


class Tier(XigtContainerMixin, XigtAttributeMixin,
           XigtReferenceAttributeMixin, XigtMetadataMixin):
    """
    A tier of IGT data. A tier should contain homogenous Items of
    data, such as all words or all glosses.
    """
    def __init__(self, id=None, type=None,
                 alignment=None, content=None, segmentation=None,
                 attributes=None, metadata=None,
                 items=None, igt=None,
                 namespace=None, nsmap=None):
        XigtContainerMixin.__init__(self, contained_type=Item)
        XigtAttributeMixin.__init__(
            self, id=id, type=type, attributes=attributes,
            namespace=namespace, nsmap=nsmap
        )
        XigtReferenceAttributeMixin.__init__(
            self, alignment=alignment, content=content,
            segmentation=segmentation
        )
        XigtMetadataMixin.__init__(self, metadata)

        self._parent = igt
        self.extend(items or [])

    def __repr__(self):
        return '<Tier object (id: {}; type: {}) with {} Items at {}>'.format(
            str(self.id or '--'), self.type, len(self), str(id(self))
        )

    @property
    def igt(self):
        return self._parent

    @property
    def corpus(self):
        try:
            return self.igt.corpus
        except AttributeError:
            return None

    @property
    def items(self):
        return self._list
    @items.setter
    def items(self, value):
        self.clear()
        self.extend(value or [])


class Item(XigtAttributeMixin, XigtReferenceAttributeMixin):
    """
    A single datum on a Tier. Often these are tokens, such as words
    or glosses, but may be phrases, translations, or (via extensions)
    more complex data like syntax nodes or dependencies.
    """
    def __init__(self, id=None, type=None,
                 alignment=None, content=None, segmentation=None,
                 attributes=None, text=None, tier=None,
                 namespace=None, nsmap=None):
        XigtAttributeMixin.__init__(
            self, id=id, type=type, attributes=attributes,
            namespace=namespace, nsmap=nsmap
        )
        XigtReferenceAttributeMixin.__init__(
            self, alignment=alignment, content=content,
            segmentation=segmentation
        )

        self._parent = tier  # mainly used for alignment expressions
        self.text = text

    def __repr__(self):
        return '<Item object (id: {}) with value "{}" at {}>'.format(
            str(self.id or '--'), self.value(), str(id(self))
        )

    @property
    def tier(self):
        return self._parent

    @property
    def igt(self):
        try:
            return self.tier.igt
        except AttributeError:
            return None

    @property
    def corpus(self):
        try:
            return self.igt.corpus
        except AttributeError:
            return None

    def value(self, refattrs=(CONTENT, SEGMENTATION)):
        if self.text is not None:
            return self.text
        for refattr in (refattrs or []):
            if refattr in self.attributes:
                return self.resolve_ref(refattr)
        # all other cases
        return None

    def resolve_ref(self, refattr):
        algnexpr = self.attributes[refattr]
        if self.tier is None:
            raise XigtStructureError(
                'Cannot resolve item reference; item (id: {}) is not '
                'contained by a Tier.'
                .format(self.id)
            )
        reftier_id = self.tier.attributes[refattr]
        if self.igt is None:
            raise XigtStructureError(
                'Cannot resolve item reference; item\'s tier (id: {}) '
                'is not contained by an Igt.'
                .format(self.tier.id)
            )
        reftier = self.igt.get(reftier_id)
        if reftier is None:
            raise XigtStructureError(
                'Referred tier (id: {}) does not exist in the Igt.'
                .format(reftier_id)
            )
        value = ref.resolve(reftier, algnexpr)
        return value

    def span(self, start, end):
        c = self.value()
        if c is None:
            return None
        return c[start:end]

    # deprecated methods

    def get_content(self, resolve=True):
        warnings.warn(
            'Item.get_content() is deprecated; use Item.value() instead.',
            DeprecationWarning
        )
        return self.value(refattrs=(CONTENT, SEGMENTATION))
