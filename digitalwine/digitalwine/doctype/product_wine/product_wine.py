# Copyright (c) 2022, Aurélien Cibrario and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

# This is added when making doctype "has web view" with annoying bug that remove mandatory line above
# from frappe.website.website_generator import WebsiteGenerator


def get_list_context(context):
    """
    This gives context to the list view
    """
    context.parents = [{"name": "Home", "route": "/"}]
    context.title = "Products"
    context.products = frappe.get_all(
        "Product Wine",
        fields=["name", "price", "millesime", "route"],
        filters={"published": True},
    )

    # FOR DEBUG
    contextCopy = dict(context)
    context["all"] = contextCopy


class ProductWine(WebsiteGenerator):

    website = frappe._dict(
        # Default seems decent here,
        # template="templates/product_wine.html",
        # This guy is mandatory, otherwise, everybody is shown
        # and unpublished items are routed with /None, which is a bug in my opinion..
        condition_field="published",
        page_title_field="name",
    )

    def get_context(self, context):
        """
        This gives context (available in jinja2) for the page view
        """
        pass
        # This adds breadcrumbs, probably an {% if ... %} below
        # Don't totally get how it works, though
        # context.parents = [{"name": "name", "title": "A title"}]

    def autoname(self):
        cuvee = frappe.get_doc("Cuvee", self.cuvee)
        self.name = f"{cuvee.cepage} - {cuvee.millesime} - {self.bottle_capacity}"

    def before_save(self):
        # TODO : this should be achieved with fetch_from
        cuvee = frappe.get_doc("Cuvee", self.cuvee)
        self.millesime = cuvee.millesime
        self.cepage = cuvee.cepage


attrs_of_Document_obj = [
    "__class__",
    "__delattr__",
    "__dict__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__getstate__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__last_sync_on",
    "__le__",
    "__lt__",
    "__module__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "__unsaved",
    "__weakref__",
    "_action",
    "_cancel",
    "_doc_before_save",
    "_extract_images_from_text_editor",
    "_fix_numeric_types",
    "_get_missing_mandatory_fields",
    "_init_child",
    "_meta",
    "_original_modified",
    "_sanitize_content",
    "_save",
    "_save_passwords",
    "_set_defaults",
    "_submit",
    "_sync_autoname_field",
    "_validate",
    "_validate_code_fields",
    "_validate_constants",
    "_validate_data_fields",
    "_validate_length",
    "_validate_links",
    "_validate_mandatory",
    "_validate_non_negative",
    "_validate_selects",
    "_validate_update_after_submit",
    "add_comment",
    "add_seen",
    "add_tag",
    "add_viewed",
    "append",
    "apply_fieldlevel_read_permissions",
    "as_dict",
    "as_json",
    "autoname",
    "bottle_size",
    "cancel",
    "cast",
    "check_docstatus_transition",
    "check_if_latest",
    "check_no_back_links_exist",
    "check_permission",
    "clear_cache",
    "copy_attachments_from_amended_from",
    "creation",
    "db_get",
    "db_insert",
    "db_set",
    "db_update",
    "db_update_all",
    "delete",
    "delete_key",
    "docstatus",
    "doctype",
    "dont_update_if_missing",
    "extend",
    "flags",
    "get",
    "get_all_children",
    "get_assigned_users",
    "get_db_value",
    "get_doc_before_save",
    "get_field_name_by_key_name",
    "get_formatted",
    "get_invalid_links",
    "get_label_from_fieldname",
    "get_latest",
    "get_liked_by",
    "get_onload",
    "get_parentfield_of_doctype",
    "get_password",
    "get_permissions",
    "get_permlevel_access",
    "get_signature",
    "get_table_field_doctype",
    "get_tags",
    "get_title",
    "get_url",
    "get_valid_columns",
    "get_valid_dict",
    "get_value",
    "getone",
    "has_permission",
    "has_permlevel_access_to",
    "has_value_changed",
    "hook",
    "idx",
    "ignore_in_setter",
    "in_format_data",
    "init_valid_columns",
    "insert",
    "is_child_table_same",
    "is_dummy_password",
    "is_new",
    "is_print_hide",
    "is_whitelisted",
    "load_doc_before_save",
    "load_from_db",
    "lock",
    "meta",
    "modified",
    "modified_by",
    "name",
    "notify_update",
    "on_change",
    "owner",
    "precision",
    "price",
    "queue_action",
    "raise_no_permission_to",
    "reload",
    "remove",
    "reset_seen",
    "reset_values_if_no_permlevel_access",
    "round_floats_in",
    "run_before_save_methods",
    "run_method",
    "run_notifications",
    "run_post_save_methods",
    "run_trigger",
    "save",
    "save_version",
    "set",
    "set_docstatus",
    "set_fetch_from_value",
    "set_name_in_children",
    "set_new_name",
    "set_onload",
    "set_parent_in_children",
    "set_title_field",
    "set_user_and_timestamp",
    "show_unique_validation_message",
    "submit",
    "throw_length_exceeded_error",
    "unlock",
    "update",
    "update_child_table",
    "update_children",
    "update_if_missing",
    "update_modified",
    "update_single",
    "validate_from_to_dates",
    "validate_higher_perm_levels",
    "validate_set_only_once",
    "validate_table_has_rows",
    "validate_update_after_submit",
    "validate_value",
    "validate_workflow",
    "whitelist",
]
