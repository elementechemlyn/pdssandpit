import pytest
from .data.scenarios import relatedPerson, retrieve, search, update
from .utils import helpers


@pytest.mark.retrieve_scenarios
class TestPDSSandboxRetrieveSuite:
    """Sandbox PDS Retrieve Scenarios. Checks performed: canned Response_Bodies, Status_Codes and Headers"""

    def test_sandbox_retrieve_patient(self, additional_headers):
        response = helpers.retrieve_patient(retrieve[0]["patient"], additional_headers)
        helpers.check_retrieve_response_body(response, retrieve[0]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, additional_headers)

    def test_patient_does_not_exist(self, additional_headers):
        response = helpers.retrieve_patient(retrieve[1]["patient"], additional_headers)
        helpers.check_retrieve_response_body(response, retrieve[1]["response"])
        helpers.check_response_status_code(response, 404)
        helpers.check_response_headers(response, additional_headers)

    def test_sensetive_patient_exists(self, additional_headers):
        response = helpers.retrieve_patient(retrieve[2]["patient"], additional_headers)
        helpers.check_retrieve_response_body(response, retrieve[2]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, additional_headers)

    def test_invalid_nhs_number(self, additional_headers):
        response = helpers.retrieve_patient(retrieve[3]["patient"], additional_headers)
        helpers.check_retrieve_response_body(response, retrieve[3]["response"])
        helpers.check_response_status_code(response, 400)
        helpers.check_response_headers(response, additional_headers)

    def test_invalid_x_request_id(self):
        response = helpers.retrieve_patient(
            retrieve[4]["patient"], {"x-request-id": "1234"}
        )
        helpers.check_retrieve_response_body(response, retrieve[4]["response"])
        helpers.check_response_status_code(response, 400)
        helpers.check_response_headers(response, {"X-Request-ID": "1234"})


@pytest.mark.search_scenarios
class TestPDSSandboxSearchSuite:
    """Sandbox PDS Search Scenarios. Checks performed: canned Response_Bodies, Status_Codes and Headers"""

    def test_sandbox_simple_search(self, additional_headers):
        response = helpers.search_patient(search[0]["query_params"], additional_headers)
        helpers.check_search_response_body(response, search[0]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, additional_headers)

    def test_wildcard_search(self, additional_headers):
        response = helpers.search_patient(search[1]["query_params"], additional_headers)
        helpers.check_search_response_body(response, search[1]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, additional_headers)

    def test_limited_results_search(self, additional_headers):
        response = helpers.search_patient(search[2]["query_params"], additional_headers)
        helpers.check_search_response_body(response, search[2]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, additional_headers)

    def test_sandbox_date_range_search(self, additional_headers):
        response = helpers.search_patient(
            "family=Smith&gender=female&birthdate=ge2010-10-21&birthdate=le2010-10-23",
            additional_headers,
        )
        helpers.check_search_response_body(response, search[3]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, additional_headers)

    def test_fuzzy_search(self, additional_headers):
        response = helpers.search_patient(search[4]["query_params"], additional_headers)
        helpers.check_search_response_body(response, search[4]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, additional_headers)

    def test_restricted_patient_search(self, additional_headers):
        response = helpers.search_patient(search[5]["query_params"], additional_headers)
        helpers.check_search_response_body(response, search[5]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, additional_headers)

    def test_unsuccessful_search(self, additional_headers):
        response = helpers.search_patient(search[6]["query_params"], additional_headers)
        helpers.check_search_response_body(response, search[6]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, additional_headers)

    def test_invalid_date_format_search(self, additional_headers):
        response = helpers.search_patient(search[7]["query_params"], additional_headers)
        helpers.check_search_response_body(response, search[7]["response"])
        helpers.check_response_status_code(response, 400)
        helpers.check_response_headers(response, additional_headers)

    def test_too_few_parameters_search(self, additional_headers):
        response = helpers.search_patient("", additional_headers)
        helpers.check_search_response_body(response, search[8]["response"])
        helpers.check_response_status_code(response, 400)
        helpers.check_response_headers(response, additional_headers)


@pytest.mark.update_scenarios
class TestPDSSandboxUpdateAsyncSuite:
    """Sandbox PDS Update Async Scenarios. Checks performed: canned Response_Bodies, Status_Codes and Headers"""
    def test_update_add_name(self, additional_headers):
        additional_headers["Prefer"] = "respond-async"
        # send update request
        update_response = helpers.update_patient(
            update[0]["patient"],
            update[0]["patient_record"],
            update[0]["patch"],
            additional_headers
        )
        assert update_response.text == ""
        helpers.check_response_status_code(update_response, 202)
        helpers.check_response_headers(update_response, additional_headers)
        # send message poll request
        poll_message_response = helpers.poll_message(
            update_response.headers["content-location"]
        )
        helpers.check_retrieve_response_body(
            poll_message_response, update[0]["response"]
        )
        helpers.check_response_status_code(poll_message_response, 200)

    def test_update_replace_given_name(self, additional_headers):
        additional_headers["Prefer"] = "respond-async"
        # send update request
        update_response = helpers.update_patient(
            update[1]["patient"],
            update[1]["patient_record"],
            update[1]["patch"],
            additional_headers,
        )
        assert update_response.text == ""
        helpers.check_response_status_code(update_response, 202)
        helpers.check_response_headers(update_response, additional_headers)
        # send message poll request
        poll_message_response = helpers.poll_message(
            update_response.headers["content-location"]
        )
        helpers.check_retrieve_response_body(
            poll_message_response, update[1]["response"]
        )
        helpers.check_response_status_code(poll_message_response, 200)

    def test_update_suffix_from_name(self, additional_headers):
        additional_headers["Prefer"] = "respond-async"
        # send update request
        update_response = helpers.update_patient(
            update[2]["patient"],
            update[2]["patient_record"],
            update[2]["patch"],
            additional_headers,
        )
        assert update_response.text == ""
        helpers.check_response_status_code(update_response, 202)
        helpers.check_response_headers(update_response, additional_headers)
        # send message poll request
        poll_message_response = helpers.poll_message(
            update_response.headers["content-location"]
        )
        helpers.check_retrieve_response_body(
            poll_message_response, update[2]["response"]
        )
        helpers.check_response_status_code(poll_message_response, 200)


@pytest.mark.update_scenarios
class TestPDSSandboxUpdateSyncWrapSuite:
    """Sandbox PDS Update Sync-Wrap Scenarios. Checks performed: canned Response_Bodies, Status_Codes and Headers"""
    def test_update_add_name(self, additional_headers):
        # send update request
        update_response = helpers.update_patient(
            update[0]["patient"],
            update[0]["patient_record"],
            update[0]["patch"],
            additional_headers
        )

        helpers.check_retrieve_response_body(
            update_response, update[0]["response"]
        )
        helpers.check_response_status_code(update_response, 200)
        helpers.check_response_headers(update_response, additional_headers)

    def test_update_replace_given_name(self, additional_headers):
        # send update request
        update_response = helpers.update_patient(
            update[1]["patient"],
            update[1]["patient_record"],
            update[1]["patch"],
            additional_headers,
        )

        # helpers.check_response_headers(update_response, additional_headers)
        helpers.check_retrieve_response_body(
            update_response, update[1]["response"]
        )
        helpers.check_response_status_code(update_response, 200)
        helpers.check_response_headers(update_response, additional_headers)

    def test_update_suffix_from_name(self, additional_headers):
        # send update request
        update_response = helpers.update_patient(
            update[2]["patient"],
            update[2]["patient_record"],
            update[2]["patch"],
            additional_headers,
        )

        helpers.check_retrieve_response_body(
            update_response, update[2]["response"]
        )
        helpers.check_response_status_code(update_response, 200)
        helpers.check_response_headers(update_response, additional_headers)


@pytest.mark.update_scenarios
class TestSandboxUpdateFailureSuite:
    """Sandbox PDS Update Sad Path Scenarios. Checks performed: canned Response_Bodies, Status_Codes and Headers"""

    @pytest.mark.parametrize("additional_headers", [
        dict(prefer=False),
        dict(prefer=True)],
        indirect=["additional_headers"]
    )
    def test_update_no_patch_sent(self, set_delay, additional_headers):
        # send update request
        update_response = helpers.update_patient(
            update[3]["patient"],
            update[3]["patient_record"],
            update[3]["patch"],
            additional_headers,
        )
        helpers.check_update_response_body(update_response, update[3]["response"])
        helpers.check_response_status_code(update_response, 400)
        helpers.check_response_headers(update_response, additional_headers)

    @pytest.mark.parametrize("additional_headers", [
        dict(prefer=False),
        dict(prefer=True)],
        indirect=["additional_headers"]
    )
    def test_update_incorrect_resource_version(self, set_delay, additional_headers):
        # send update request
        update_response = helpers.update_patient(
            update[4]["patient"],
            update[4]["patient_record"],
            update[4]["patch"],
            additional_headers,
        )
        helpers.check_update_response_body(update_response, update[4]["response"])
        helpers.check_response_status_code(update_response, 412)
        helpers.check_response_headers(update_response, additional_headers)

    @pytest.mark.parametrize('parameterized_headers', [
        {"x-request-id": "12345"},
        {"x-request-id": "12345", "Prefer": "respond-async"}
    ])
    def test_update_invalid_x_request_id(self, set_delay, parameterized_headers):
        # send update request
        update_response = helpers.update_patient(
            update[5]["patient"],
            update[5]["patient_record"],
            update[5]["patch"],
            parameterized_headers,
        )
        helpers.check_update_response_body(update_response, update[5]["response"])
        helpers.check_response_status_code(update_response, 400)
        helpers.check_response_headers(update_response, {"X-Request-ID": "12345"})

    @pytest.mark.parametrize('parameterized_headers', [
        {},
        {"Prefer": "respond-async"}
    ])
    def test_update_missing_x_request_id(self, set_delay, parameterized_headers):
        # send update request
        update_response = helpers.update_patient(
            update[5]["patient"],
            update[5]["patient_record"],
            update[5]["patch"],
            parameterized_headers
        )

        helpers.check_update_response_body(update_response, update[11]["response"])
        helpers.check_response_status_code(update_response, 412)

    @pytest.mark.parametrize('parameterized_headers', [
        {"Content-Type": "application/json-patch+json"},
        {"Content-Type": "application/json-patch+json", "Prefer": "respond-async"}
    ])
    def test_update_missing_if_match_header(self, set_delay, parameterized_headers):
        update_response = helpers.update_patient_invalid_headers(
            update[6]["patient"], update[6]["patch"], parameterized_headers
        )
        helpers.check_update_response_body(update_response, update[6]["response"])
        helpers.check_response_status_code(update_response, 412)
        helpers.check_response_headers(update_response)

    @pytest.mark.parametrize('parameterized_headers', [
        {"Content-Type": "text/xml", "If-Match": 'W/"2"'},
        {"Content-Type": "text/xml", "If-Match": 'W/"2"', "Prefer": "respond-async"}
    ])
    def test_update_incorrect_content_type(self, set_delay, parameterized_headers):
        update_response = helpers.update_patient_invalid_headers(
            update[7]["patient"], update[7]["patch"], parameterized_headers
        )
        helpers.check_update_response_body(update_response, update[7]["response"])
        helpers.check_response_status_code(update_response, 400)
        helpers.check_response_headers(update_response)

    @pytest.mark.parametrize("additional_headers", [
        dict(prefer=False),
        dict(prefer=True)],
        indirect=["additional_headers"]
    )
    def test_update_invalid_patch(self, set_delay, additional_headers):
        # send update request
        update_response = helpers.update_patient(
            update[8]["patient"],
            update[8]["patient_record"],
            update[8]["patch"],
            additional_headers,
        )
        helpers.check_update_response_body(update_response, update[8]["response"])
        helpers.check_response_status_code(update_response, 400)
        helpers.check_response_headers(update_response, additional_headers)

    @pytest.mark.parametrize("additional_headers", [
        dict(prefer=False),
        dict(prefer=True)],
        indirect=["additional_headers"]
    )
    def test_invalid_nhs_number(self, set_delay, additional_headers):
        # send update request
        update_response = helpers.update_patient(
            update[9]["patient"],
            update[9]["patient_record"],
            update[9]["patch"],
            additional_headers,
        )
        helpers.check_update_response_body(update_response, update[9]["response"])
        helpers.check_response_status_code(update_response, 400)
        helpers.check_response_headers(update_response, additional_headers)

    @pytest.mark.parametrize("additional_headers", [
        dict(prefer=False),
        dict(prefer=True)],
        indirect=["additional_headers"]
    )
    def test_patient_does_not_exist(self, set_delay, additional_headers):
        # send update request
        update_response = helpers.update_patient(
            update[10]["patient"],
            update[10]["patient_record"],
            update[10]["patch"],
            additional_headers,
        )
        helpers.check_update_response_body(update_response, update[10]["response"])
        helpers.check_response_status_code(update_response, 404)
        helpers.check_response_headers(update_response, additional_headers)


@pytest.mark.related_person_scenarios
class TestSandboxRelatedPersonSuite:
    """Sandbox PDS Related Person Scenarios. Checks performed: canned Response_Bodies, Status_Codes and Headers"""

    def test_related_person_exists(self, additional_headers):
        response = helpers.retrieve_related_person(
            relatedPerson[0]["patient"], additional_headers
        )
        helpers.check_search_response_body(response, relatedPerson[0]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, additional_headers)

    def test_related_person_patient_does_not_exist(self, additional_headers):
        response = helpers.retrieve_related_person(
            relatedPerson[1]["patient"], additional_headers
        )
        helpers.check_search_response_body(response, relatedPerson[1]["response"])
        helpers.check_response_status_code(response, 404)
        helpers.check_response_headers(response, additional_headers)

    def test_related_person_does_not_exist(self, additional_headers):
        response = helpers.retrieve_related_person(
            relatedPerson[2]["patient"], additional_headers
        )
        helpers.check_search_response_body(response, relatedPerson[2]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, additional_headers)
