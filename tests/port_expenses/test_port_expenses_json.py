import pytest

from signal_ocean.port_expenses import PortExpenses, CanalExpenses
from signal_ocean.port_expenses import _port_expenses_json


@pytest.mark.parametrize('port_id, port_canal, towage, berth, port_dues, '
    'lighthouse, mooring, pilotage, quay, anchorage, agency_fees, other, '
    'suez_dues, total_cost, miscellaneous_dues, is_estimated, canal_dues, '
    'berth_dues, lighthouse_dues, mooring_unmooring, quay_dues, anchorage_dues, '
    'port_agents', [
    (3153, 0, 0, 0, 40196, 594, 0, 0, 0, 0, 1500, 2277, 0, 44568, 0, False, 0,
     0, 0, 0, 0, 0, [])
])
def test_parse_port_expenses(port_id, port_canal, towage, berth, port_dues,
    lighthouse, mooring, pilotage, quay, anchorage, agency_fees, other,
    suez_dues, total_cost, miscellaneous_dues, is_estimated, canal_dues,
    berth_dues, lighthouse_dues, mooring_unmooring, quay_dues, anchorage_dues,
    port_agents):
    port_expenses_json = {
        "portId": port_id,
        "portCanal": port_canal,
        "towage": towage,
        "berth": berth,
        "portDues": port_dues,
        "lighthouse": lighthouse,
        "mooring": mooring,
        "pilotage": pilotage,
        "quay": quay,
        "anchorage": anchorage,
        "agencyFees": agency_fees,
        "other": other,
        "suezDues": suez_dues,
        "totalCost": total_cost,
        "miscellaneousDues": miscellaneous_dues,
        "isEstimated": is_estimated,
        "canalDues": canal_dues,
        "berthDues": berth_dues,
        "lighthouseDues": lighthouse_dues,
        "mooringUnmooring": mooring_unmooring,
        "quayDues": quay_dues,
        "anchorageDues": anchorage_dues,
        "portAgents": port_agents
    }

    pe_object = _port_expenses_json.parse_port_expenses(port_expenses_json)

    assert type(pe_object) is PortExpenses
    assert pe_object.port_id == port_id
    assert pe_object.port_canal == port_canal
    assert pe_object.towage == towage
    assert pe_object.berth == berth
    assert pe_object.port_dues == port_dues
    assert pe_object.lighthouse == lighthouse
    assert pe_object.mooring == mooring
    assert pe_object.pilotage == pilotage
    assert pe_object.quay == quay
    assert pe_object.anchorage == anchorage
    assert pe_object.agency_fees == agency_fees
    assert pe_object.other == other
    assert pe_object.suez_dues == suez_dues
    assert pe_object.total_cost == total_cost
    assert pe_object.miscellaneous_dues == miscellaneous_dues
    assert pe_object.is_estimated == is_estimated
    assert pe_object.canal_dues == canal_dues
    assert pe_object.berth_dues == berth_dues
    assert pe_object.lighthouse_dues == lighthouse_dues
    assert pe_object.mooring_unmooring == mooring_unmooring
    assert pe_object.quay_dues == quay_dues
    assert pe_object.anchorage_dues == anchorage_dues
    assert pe_object.port_agents == port_agents


@pytest.mark.parametrize('total_cost', [
    (264324.5555392)    #Placeholder in case parameters increase
])
def test_parse_port_expenses(total_cost):
    canal_expenses_json = {
        "totalCost": total_cost,
    }

    ce_object = _port_expenses_json.parse_canal_expenses(canal_expenses_json)

    assert type(ce_object) is CanalExpenses
    assert ce_object.total_cost == total_cost
