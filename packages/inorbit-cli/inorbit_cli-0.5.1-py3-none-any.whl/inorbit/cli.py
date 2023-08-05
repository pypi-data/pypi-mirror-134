# Copyright (c) 2021, InOrbit, Inc.
# All rights reserved.
import json
import logging
import sys
from datetime import datetime

import click
import inorbit.exceptions
from inorbit import client
from tabulate import tabulate

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))


def get_id_to_name_mapping(resource_name):
    """Returns a dictionary mapping resource id to resource name

    Args:
        resource_name (string): name of the resource to generate the mapping

    Returns:
        dict: dictionary mapping resource id to resource name
    """

    endpoint_raw_response = client.http_get(f"/{resource_name}").json()
    resource_id_to_name_mapping = {res["id"]: res["name"] for res in endpoint_raw_response}
    return resource_id_to_name_mapping


# This is the CLI entrypoint. It's hooked by `setup.py` (see `entry_points` parameter).
@click.group()
@click.option("--verbose", default=True, is_flag=True)  # TODO: set verbose default value to False
def cli(verbose):
    """InOrbit Command Line Interface tool

    The InOrbit CLI tool enable roboteers to interact
    with the InOrbit Cloud platform in order to manage
    robot configuration as code.
    """
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.ERROR)


@cli.group()
def get():
    pass


@cli.group()
def describe():
    pass


@cli.group()
def config():
    pass


@click.command(name="tags")
def get_tags():
    """Get all tags and relevant tag data."""
    response = client.http_get("/tags").json()
    response = [
        {
            "name": r["name"],
            "id": r["id"],
            "description": r.get("description", ""),
        }
        for r in response
    ]
    click.echo(tabulate(response, headers="keys"))


get.add_command(get_tags)


@click.command(name="collections")
def get_collections():
    """
    Get all collections and relevant collection data.

    Instead of showing all tags associated to a particular collection,
    it only shows the number of tags under each collection. To get more
    detailed data about collections use `describe_collections`.
    """

    response = client.http_get("/collections").json()
    response = [
        {
            "name": r["name"],
            "id": r["id"],
            "tags count": len(r["tags"]),
        }
        for r in response
    ]
    click.echo(tabulate(response, headers="keys"))


get.add_command(get_collections)


@click.command(name="robots")
def get_robots():
    """Get all robots and relevant robot data."""
    response = client.http_get("/robots").json()
    response = [
        {
            "name": r["name"],
            "id": r["id"],
            "agent version": r.get("agentVersion", ""),
        }
        for r in response
    ]
    click.echo(tabulate(response, headers="keys"))


get.add_command(get_robots)


@click.command(name="tags")
def describe_tags():
    """
    Describe all tags and detailed tag data.

    It also gathers the collection names so the collection id a tag is
    associated to it not shown alone.
    """

    # generate a `collection id` to `collection name` mapping to show
    # the collection name the tag is associated to.
    collection_id_to_name_mapping = get_id_to_name_mapping("collections")

    tags_raw_response = client.http_get("/tags").json()
    response = [
        {
            "name": r["name"],
            "description": r.get("description", ""),
            "collection id": r["collectionId"],
            "collection name": collection_id_to_name_mapping[r["collectionId"]],
        }
        for r in tags_raw_response
    ]

    click.echo(tabulate(response, headers="keys"))


describe.add_command(describe_tags)


@click.command(name="collections")
def describe_collections():
    """Describe all collections and detailed collection data."""
    collections_raw_response = client.http_get("/collections").json()
    for collection in collections_raw_response:
        click.echo(f"Collection '{collection['name']}' has {len(collection['tags'])} tags")
        collection_tags = [
            {"tag name": collection_tag["name"], "tag id": collection_tag["id"]}
            for collection_tag in collection["tags"]
        ]
        # Here `rst` table format has better appeareance and helps to understand
        # the data better. Consider using the same format for all `tabulate` calls.
        click.echo(tabulate(collection_tags, headers="keys", tablefmt="rst"))
        click.echo()


describe.add_command(describe_collections)


@click.command(name="robots")
def describe_robots():
    """Describe all robots and detailed robot data."""
    response = client.http_get("/robots").json()
    response = [
        {
            "name": r["name"],
            "id": r["id"],
            "agent version": r.get("agentVersion", ""),
            "online": r["agentOnline"],
            # TODO: decide which is the best date format and refactor to allow
            # changing it for all outputs or as a command parameter
            "last seen": datetime.fromtimestamp(r["updatedTs"] / 1000).isoformat(),
        }
        for r in response
    ]
    click.echo(tabulate(response, headers="keys"))


describe.add_command(describe_robots)


@click.command(name="apply")
@click.argument("filename", type=click.Path(exists=True, resolve_path=True))
def apply_config(filename):
    logger.debug(f"Reading file '{click.format_filename(filename)}'")

    # TODO: Add support for multidocument YAML files
    with open(file=filename, mode="r") as fd:
        inorbit_config = json.loads(fd.read())

    logger.debug(inorbit_config)

    try:
        logger.info("Applying configuration")
        response = client.http_post("/configuration/apply", post_data=inorbit_config)
    except inorbit.exceptions.InOrbitError as ex:
        raise click.ClickException(ex)

    click.echo(response.text)


# TODO: consider moving apply_config to CLI `config` group
# to unify UX e.g. `inorbit config apply`, `inorbit config list`
cli.add_command(apply_config)


@click.command(name="list")
def list_config():
    """List all configurations."""

    # TODO: define UX for CLI parameterization and parameterize `query_data` e.g.
    # $ inorbit config list incidents
    # $ inorbit config list foo
    response = client.http_get(
        path="/configuration/list", query_data={"kind": "IncidentDefinition"}
    ).json()

    logger.debug(response)

    response = [
        {
            "id": r["id"],
            "kind": r["kind"],
            "label": r["label"],
            "scope": r["scope"],
            "suppressed": r.get("suppresed", False),
        }
        for r in response
    ]
    click.echo(tabulate(response, headers="keys"))


config.add_command(list_config)
