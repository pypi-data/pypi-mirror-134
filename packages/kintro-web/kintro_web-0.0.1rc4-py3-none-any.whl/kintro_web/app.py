import json
import os

from click.testing import CliRunner
from flask import Flask
from kintro import kintro


def get_env_or_abort(env: str):
    val = os.getenv(env, None)
    if val is None:
        raise ValueError(f"{env} must be set")
    return val


def create_app(cfg=None):
    plex_server_url = get_env_or_abort("KINTRO_PLEX_URL")
    plex_server_token = get_env_or_abort("KINTRO_PLEX_TOKEN")
    kintro_log_level = get_env_or_abort("KINTRO_LOG_LEVEL")
    tv_path = get_env_or_abort("KINTRO_TV_PATH")
    replace_path = get_env_or_abort("KINTRO_REPLACE_PATH")

    application = Flask(__name__)

    @application.route("/episode/<series>/<int:season>/<int:episode>", methods=["POST"])
    def episode(series: str, season: int, episode: int):
        runner = CliRunner()
        result = runner.invoke(
            kintro.cli,
            [
                "--log-level",
                kintro_log_level,
                "server",
                "--url",
                plex_server_url,
                "--token",
                plex_server_token,
                "sync",
                "--find-path",
                tv_path,
                "--replace-path",
                replace_path,
                "--libtype",
                "episode",
                "--filter-json",
                json.dumps(
                    {
                        "and": [
                            {
                                "show.title==": series,
                            },
                            {
                                "season.index=": season,
                            },
                            {
                                "episode.index=": episode,
                            },
                        ],
                    },
                ),
                "--max-workers",
                "1",
                "--worker-batch-size",
                "1",
            ],
            catch_exceptions=False,
        )
        return {
            "exit_code": result.exit_code,
            "output": result.output,
        }

    return application
