from agilicus.agilicus_api import (
    AuditDestination,
    AuditDestinationSpec,
    AuditDestinationFilter,
)

from . import context
from .input_helpers import build_updated_model
from .input_helpers import update_org_from_input_or_ctx
from .input_helpers import strip_none
from .output.table import (
    column,
    spec_column,
    format_table,
    metadata_column,
    subtable,
)

DESTINATION_TYPES = ["file"]
FILTER_TYPES = ["subsystem", "audit_agent_type", "audit_agent_id", "hostname"]


def list_audit_destinations(ctx, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    update_org_from_input_or_ctx(kwargs, ctx, **kwargs)
    params = strip_none(kwargs)
    query_results = apiclient.audits_api.list_audit_destinations(**params)
    return query_results.audit_destinations


def add_audit_destination(ctx, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    update_org_from_input_or_ctx(kwargs, ctx, **kwargs)
    spec = AuditDestinationSpec(filters=[], **strip_none(kwargs))
    model = AuditDestination(spec=spec)
    return apiclient.audits_api.create_audit_destination(model).to_dict()


def _get_audit_destination(ctx, apiclient, destination_id, **kwargs):
    update_org_from_input_or_ctx(kwargs, ctx, **kwargs)
    return apiclient.audits_api.get_audit_destination(destination_id, **kwargs)


def show_audit_destination(ctx, destination_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    return _get_audit_destination(ctx, apiclient, destination_id, **kwargs).to_dict()


def delete_audit_destination(ctx, destination_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    update_org_from_input_or_ctx(kwargs, ctx, **kwargs)
    return apiclient.audits_api.delete_audit_destination(destination_id, **kwargs)


def update_audit_destination(ctx, destination_id, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    get_args = {}
    update_org_from_input_or_ctx(get_args, ctx, **kwargs)
    mapping = _get_audit_destination(ctx, apiclient, destination_id, **get_args)

    mapping.spec = build_updated_model(AuditDestinationSpec, mapping.spec, kwargs)
    return apiclient.audits_api.replace_audit_destination(
        destination_id, audit_destination=mapping
    ).to_dict()


def add_audit_destination_filter(ctx, destination_id, filter_type, value, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    get_args = {}
    update_org_from_input_or_ctx(get_args, ctx, **kwargs)
    mapping = _get_audit_destination(ctx, apiclient, destination_id, **get_args)
    filter = AuditDestinationFilter(filter_type, value)

    mapping.spec.filters.append(filter)
    return apiclient.audits_api.replace_audit_destination(
        destination_id, audit_destination=mapping
    ).to_dict()


def delete_audit_destination_filter(ctx, destination_id, filter_type, value, **kwargs):
    apiclient = context.get_apiclient_from_ctx(ctx)
    get_args = {}
    update_org_from_input_or_ctx(get_args, ctx, **kwargs)
    mapping = _get_audit_destination(ctx, apiclient, destination_id, **get_args)
    remaining = []
    total = 0
    for filter in mapping.spec.filters:
        if filter.filter_type != filter_type:
            remaining.append(filter)
            continue
        if value is not None and filter.value != value:
            remaining.append(filter)
            continue
        total += 1
    mapping.spec.filters = remaining

    return apiclient.audits_api.replace_audit_destination(
        destination_id, audit_destination=mapping
    ).to_dict()


def format_audit_destinations_as_text(ctx, resources):
    filter_columns = [
        column("filter_type"),
        column("value"),
    ]
    columns = [
        metadata_column("id"),
        spec_column("org_id"),
        spec_column("name"),
        spec_column("destination_type"),
        spec_column("location"),
        spec_column("comment"),
        spec_column("enabled"),
        subtable(ctx, "filters", filter_columns, subobject_name="spec"),
    ]

    return format_table(ctx, resources, columns)
