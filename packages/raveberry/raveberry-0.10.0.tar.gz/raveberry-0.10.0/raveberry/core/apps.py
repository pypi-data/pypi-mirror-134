"""Contains the core app configuration."""
import sys
import logging
import os
import atexit
from distutils.util import strtobool

from django.apps import AppConfig
from django.conf import settings as conf


class CoreConfig(AppConfig):
    """This is the configuration for the core app."""

    name = "core"

    def ready(self) -> None:
        if "celery" in sys.argv and strtobool(os.environ.get("RUN_MAIN", "0")):
            # if the development celery process starts,
            # have it import all modules containing celery tasks
            # this way, its autoreload is notified on changes in these modules

            for module in conf.CELERY_IMPORTS:
                __import__(module)

            # these are used by the lights worker but imported locally.
            # in order to trigger autoreloads they need to imported here as well
            import core.lights.ring
            import core.lights.wled
            import core.lights.strip
            import core.lights.screen

            return

        # ready is called for every management command and for autoreload
        # only start raveberry when
        # in debug mode and the main application is run (not autoreload)
        # or in prod mode (run by daphne)
        start_raveberry = (
            "runserver" in sys.argv and strtobool(os.environ.get("RUN_MAIN", "0"))
        ) or (sys.argv[0].endswith("daphne"))

        if conf.TESTING:
            import core.musiq.controller as controller

            # when MopidyAPI instances are created too often,
            # mopidy runs into a "Set changed size during iteration" error.
            # Thus we initialize the interface once and not for every testcase
            controller.start()

        if start_raveberry:
            import core.celery as celery
            import core.redis as redis
            import core.musiq.musiq as musiq
            import core.musiq.playback as playback
            import core.settings.basic as basic
            import core.settings.platforms as platforms
            import core.lights.worker as worker

            logging.info("starting raveberry")

            redis.start()
            celery.start()

            worker.start()
            musiq.start()
            basic.start()
            platforms.start()

            def stop_workers() -> None:
                # wake up the playback thread and stop it
                redis.set("stop_playback_loop", True)
                playback.queue_changed.set()

                # wake the buzzer thread so it exits
                playback.buzzer_stopped.set()

                # wake up the listener thread with an instruction to stop the lights worker
                redis.publish("lights_settings_changed", "stop")

            atexit.register(stop_workers)
