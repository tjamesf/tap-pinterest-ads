"""pinterest tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_pinterest_ads.streams import (
    AdAccountStream,
    CampaignStream,
    AdGroupStream,
    AdStream,
    AdAnalyticsStream,
    AccountAnalyticsStream,
)
STREAM_TYPES = [
    AdAccountStream,
    CampaignStream,
    AdGroupStream,
    AdStream,
    AdAnalyticsStream,
    AccountAnalyticsStream,
]


class TapPinterestAds(Tap):
    """pinterest tap class."""
    name = "tap-pinterest-ads"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            description="App ID"
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=True,
            description="App secret key"
        ),
        th.Property(
            "refresh_token",
            th.StringType,
            required=True,
            description="Refresh token obtained from the OAuth user flow"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            default="2019-10-17T00:00:00Z",
            description="Date to start collection analytics from"
        ),
        th.Property(
            "is_backfilled",
            th.BooleanType,
            default=False,
            description="Set to True once backfilled in order to reduce API calls per day"
        ),
        th.Property(
            "click_window_days",
            th.IntegerType,
            required=False,
            default=30,
            description="Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics."
        ),
        th.Property(
            "engagement_window_days",
            th.IntegerType,
            required=False,
            default=30,
            description="Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes."
        ),
        th.Property(
            "view_window_days",
            th.IntegerType,
            required=False,
            default=1,
            description="Number of days to use as the conversion attribution window for a view action."
        ),
        th.Property(
            "conversion_report_time",
            th.StringType,
            required=False,
            default="TIME_OF_AD_ACTION",
            description="The date by which the conversion metrics will be reported. Can be either TIME_OF_AD_ACTION or TIME_OF_CONVERSION."
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
