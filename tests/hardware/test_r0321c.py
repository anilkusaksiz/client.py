from __future__ import annotations

from deebot_client.commands import StationAction
from deebot_client.commands.json.charge_state import GetChargeState
from deebot_client.commands.json.clean import CleanAreaV2, CleanV2, GetCleanInfo
from deebot_client.commands.json.map import GetMapSet
from deebot_client.commands.json.work_state import GetWorkState
from deebot_client.hardware.r0321c import get_device_info


def test_r0321c_uses_v2_capabilities() -> None:
    capabilities = get_device_info().capabilities

    assert capabilities.clean.action.command is CleanV2
    assert capabilities.clean.action.area is CleanAreaV2

    assert capabilities.map is not None
    assert capabilities.map.info is None
    assert capabilities.map.set.execute is GetMapSet

    assert capabilities.state.get == [
        GetChargeState(),
        GetCleanInfo(),
]
    assert capabilities.station is not None
    assert capabilities.station.state.get == [GetWorkState()]
    assert capabilities.station.action.types == (
        StationAction.EMPTY_DUSTBIN,
        StationAction.DRY_MOP,
        StationAction.WASH_MOP,
    )
