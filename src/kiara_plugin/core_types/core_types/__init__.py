# -*- coding: utf-8 -*-
from typing import Any, Mapping

from kiara.models.values.value import Value
from kiara.modules.included_core_modules.persistence import SaveInlineDataModule


class SaveInlineStringDataModule(SaveInlineDataModule):
    """Save some core data types inline."""

    _module_type_name = "core_data.save_inline"

    def data_type__boolean(self, value: Value, persistence_config: Mapping[str, Any]):

        load_config = self.create_inline_load_config(
            data=value.data, data_type=value.value_schema.type
        )
        return load_config, None

    def data_type__date(self, value: Value, persistence_config: Mapping[str, Any]):

        load_config = self.create_inline_load_config(
            data=value.data, data_type=value.value_schema.type
        )
        return load_config, None

    def data_type__integer(self, value: Value, persistence_config: Mapping[str, Any]):

        load_config = self.create_inline_load_config(
            data=value.data, data_type=value.value_schema.type
        )
        return load_config, None

    def data_type__float(self, value: Value, persistence_config: Mapping[str, Any]):

        load_config = self.create_inline_load_config(
            data=value.data, data_type=value.value_schema.type
        )
        return load_config, None
