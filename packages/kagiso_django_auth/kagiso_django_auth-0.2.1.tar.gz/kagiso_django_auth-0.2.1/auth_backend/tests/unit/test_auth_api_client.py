import json

from django.test import TestCase
import pytest
import requests
import responses

from ... import auth_api_client


class TestApiClient(TestCase):

    @responses.activate
    def test_get(self):
        sample_data = {'some': 'data'}
        responses.add(
            responses.GET,
            'https://auth.kagiso.io/api/v1/test_endpoint/.json',
            body=json.dumps(sample_data),
            status=200,
        )

        status, data = auth_api_client.call('test_endpoint')

        assert len(responses.calls) == 1
        assert responses.calls[
            0].request.url == 'https://auth.kagiso.io/api/v1/test_endpoint/.json'  # noqa
        assert status == 200
        assert data == sample_data

    @responses.activate
    def test_post(self):
        sample_data = {'some': 'data'}
        responses.add(
            responses.POST,
            'https://auth.kagiso.io/api/v1/test_endpoint/.json',
            body=json.dumps(sample_data),
            status=201,
        )

        status, data = auth_api_client.call(
            'test_endpoint', 'POST', payload=sample_data)

        assert len(responses.calls) == 1
        assert responses.calls[
            0].request.url == 'https://auth.kagiso.io/api/v1/test_endpoint/.json'  # noqa
        assert status == 201
        assert data == sample_data

    @responses.activate
    def test_put(self):
        sample_data = {'some': 'data'}
        responses.add(
            responses.PUT,
            'https://auth.kagiso.io/api/v1/test_endpoint/1/.json',
            body=json.dumps(sample_data),
            status=200,
        )

        status, data = auth_api_client.call(
            'test_endpoint/1',
            'PUT',
            sample_data
        )

        assert len(responses.calls) == 1
        assert responses.calls[
            0].request.url == 'https://auth.kagiso.io/api/v1/test_endpoint/1/.json'  # noqa
        assert status == 200
        assert data == sample_data

    @responses.activate
    def test_delete(self):
        responses.add(
            responses.DELETE,
            'https://auth.kagiso.io/api/v1/test_endpoint/1/.json',
            body=json.dumps({}),
            status=204,
        )

        status, data = auth_api_client.call('test_endpoint/1', method='DELETE')

        assert len(responses.calls) == 1
        assert responses.calls[
            0].request.url == 'https://auth.kagiso.io/api/v1/test_endpoint/1/.json'  # noqa
        assert data == {}
        assert status == 204

    @responses.activate
    def test_4xx_raises_if_not_404(self):
        responses.add(
            responses.GET,
            'https://auth.kagiso.io/api/v1/test_endpoint/1/.json',
            body=json.dumps({}),
            status=403,
        )

        with pytest.raises(requests.exceptions.HTTPError):
            auth_api_client.call('test_endpoint/1', method='GET')

    @responses.activate
    def test_404_does_not_raise(self):
        responses.add(
            responses.GET,
            'https://auth.kagiso.io/api/v1/test_endpoint/1/.json',
            body=json.dumps({}),
            status=404,
        )

        auth_api_client.call('test_endpoint/1', method='GET')

    @responses.activate
    def test_5xx_raises(self):
        responses.add(
            responses.GET,
            'https://auth.kagiso.io/api/v1/test_endpoint/1/.json',
            body=json.dumps({}),
            status=500,
        )

        with pytest.raises(requests.exceptions.HTTPError):
            auth_api_client.call('test_endpoint/1', method='GET')
