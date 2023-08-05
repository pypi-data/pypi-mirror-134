"""Utility functions for gitlabclient
"""
import sys
from typing import Optional

import click
from gitlab.endpoints import GitLabEndpoint
from gitlab.resources import Releases
from gitlab.utils import ppjson
from packaging import version


@click.command()
@click.argument("tag_name")
@click.option("--endpoint-url", type=str, envvar="CI_API_V4_URL")
@click.option("--project-id", type=int, envvar="CI_PROJECT_ID")
@click.option(
    "--ref-name",
    "-r",
    default=None,
    help="git-ref for the tag. Required if tag_name does not exist yet",
)
@click.option("--auth-token", "-t", default=None, envvar="API_AUTH_TOKEN")
def publish_release(
    tag_name: str,
    endpoint_url: str,
    project_id: int,
    ref_name: Optional[str] = None,
    auth_token: Optional[str] = None,
):
    """Create a new Release against the project

    Arguments:
      - endpoint_url (str): the endpoint url, e.g. https://gitlab.com/api/v4. GitLabCI publishes it as $CI_API_V4_URL
      - project_id (int): the project id against which the release should be created, GitLabCI publishes it as
          $CI_PROJECT_ID
      - tag_name (str): the tag (in the project repository) against which the release should be created. If it exists,
          it will be used. Otherwise it will be created and ref_name is required.
      - ref_name (str): Required if tag_name does not exist. The git-ref against which to create the tag. GitLabCI
          publishes it as $CI_COMMIT_SHA
      - token (str): the authorization token to be used. It is usually required. It is set as optional for certain
          circumstance where authorization is token-less
    """
    endpoint = GitLabEndpoint(endpoint_url, token=auth_token)

    new_release_params = {
        # coerced to int since it can come from commandline
        "id": project_id,
        "tag_name": tag_name,
    }

    if ref_name is not None:
        new_release_params["ref"] = ref_name

    rels = Releases(endpoint, project_id).create(new_release_params)

    ppjson(rels)


# pylint: disable=too-many-locals
@click.command()
@click.argument("filename")
@click.option("--endpoint-url", type=str, envvar="CI_API_V4_URL")
@click.option("--project-id", type=int, envvar="CI_PROJECT_ID")
@click.option(
    "--fail-if-no-version",
    type=bool,
    default=False,
    help="""By default if no previous version is present 0.0.1 will be used. If this is True, instead a non-zero
        exist status will be returned and no filename will be written.""",
)
@click.option(
    "--forced-version",
    default=None,
    help="Set the starting version instead of asking via GitLab API for "
    "the most recent one",
)
@click.option("--auth-token", "-t", default=None, envvar="API_AUTH_TOKEN")
def get_package_version(
    filename: str,
    endpoint_url: str,
    project_id: int,
    fail_if_no_version: bool,
    forced_version: Optional[str] = None,
    auth_token: Optional[str] = None,
):
    """print the Bumped patch version value, based on the most recent gitlab release

    If the most recent version is not semver, it will try to cast it to a X.Y.Z syntax, or fail parsint it raising
    packaging.version.InvalidVersion

    This command does not create any new release, it just computes a value and prints it to stdout.
    """
    print(f"Endpoint: {endpoint_url} / Project id: {project_id}", file=sys.stderr)

    if forced_version is None:
        endpoint = GitLabEndpoint(endpoint_url, auth_token)

        try:
            most_recent_release = Releases(endpoint, project_id).read()[0]
        except IndexError:
            print("No previous version present", file=sys.stderr)

            if fail_if_no_version:
                sys.exit(1)

            most_recent_version = "0.0.0"
            print(
                f"Using {most_recent_version} as most recent version and bumping version from this",
                file=sys.stderr,
            )
        else:
            most_recent_version = most_recent_release["tag_name"]

            if most_recent_version.startswith("v"):
                most_recent_version = most_recent_version[1:]

    else:
        most_recent_version = forced_version

    ver = version.Version(most_recent_version)

    major = ver.major
    minor = ver.minor
    micro = ver.micro + 1
    pre = f"{ver.pre[0]}{ver.pre[1]}" if ver.pre is not None else ""
    local = f"+{ver.local}" if ver.local is not None else ""

    bumped_version = version.Version(f"{major}.{minor}.{micro}{pre}{local}")
    print(f"Bumping from {most_recent_version} to {bumped_version}", file=sys.stderr)
    with open(filename, "w", encoding="utf8") as output_file:
        output_file.write(str(bumped_version))


# pylint: disable=too-many-locals
@click.command()
@click.argument("filename")
@click.option("--endpoint-url", type=str, envvar="CI_API_V4_URL")
@click.option("--project-id", type=int, envvar="CI_PROJECT_ID")
@click.option(
    "--fail-if-no-version",
    type=bool,
    default=False,
    help="""By default if no previous version is present 0.0.1 will be used. If this is True, instead a non-zero
        exist status will be returned and no filename will be written.""",
)
@click.option(
    "--forced-version",
    type=str,
    default=None,
    help="Set the starting version instead of asking via GitLab API for the most recent one",
)
@click.option("--auth-token", "-t", default=None, envvar="API_AUTH_TOKEN")
def get_latest_release_version(
    filename: str,
    endpoint_url: str,
    project_id: int,
    fail_if_no_version: bool,
    forced_version: Optional[str] = None,
    auth_token: Optional[str] = None,
):
    """print the Bumped patch version value, based on the most recent gitlab release

    If the most recent version is not semver, it will try to cast it to a X.Y.Z syntax, or fail parsint it raising
    packaging.version.InvalidVersion

    If there is no most recenve version, it will use 0.0.1 as initial version.

    This command does not create any new release, it just computes a value and prints it to stdout.
    """
    print(f"Endpoint: {endpoint_url} / Project id: {project_id}")

    if forced_version is None:
        endpoint = GitLabEndpoint(endpoint_url, auth_token)

        try:
            most_recent_release = Releases(endpoint, project_id).read()[0]
        except IndexError:
            print("No previous version present", file=sys.stderr)

            if fail_if_no_version:
                sys.exit(1)

            most_recent_version = "0.0.0"
            print(
                f"Using {most_recent_version} as most recent version",
                file=sys.stderr,
            )

        else:
            most_recent_version = most_recent_release["tag_name"]

            if most_recent_version.startswith("v"):
                most_recent_version = most_recent_version[1:]

    else:
        most_recent_version = forced_version

    print(f"Version found: {most_recent_version}")
    with open(filename, "w", encoding="utf=8") as output_file:
        output_file.write(most_recent_version)
