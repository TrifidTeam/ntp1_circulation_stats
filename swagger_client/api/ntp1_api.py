# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class NTP1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def broadcast_tx(self, body, **kwargs):  # noqa: E501
        """Broadcasts a signed raw transaction to the network  # noqa: E501

        Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.broadcast_tx(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param BroadcastTxRequest body: Object representing a transaction to broadcast (required)
        :return: BroadcastTxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.broadcast_tx_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.broadcast_tx_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def broadcast_tx_with_http_info(self, body, **kwargs):  # noqa: E501
        """Broadcasts a signed raw transaction to the network  # noqa: E501

        Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.broadcast_tx_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param BroadcastTxRequest body: Object representing a transaction to broadcast (required)
        :return: BroadcastTxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method broadcast_tx" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `broadcast_tx`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ntp1/broadcast', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BroadcastTxResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def burn_token(self, body, **kwargs):  # noqa: E501
        """Builds a transaction that burns an NTP1 Token  # noqa: E501

        Builds an unsigned raw transaction that burns an NTP1 token on the Neblio blockchain.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.burn_token(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param BurnTokenRequest body: Object representing the token to be burned (required)
        :return: BurnTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.burn_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.burn_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def burn_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """Builds a transaction that burns an NTP1 Token  # noqa: E501

        Builds an unsigned raw transaction that burns an NTP1 token on the Neblio blockchain.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.burn_token_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param BurnTokenRequest body: Object representing the token to be burned (required)
        :return: BurnTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method burn_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `burn_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ntp1/burntoken', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BurnTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_address_info(self, address, **kwargs):  # noqa: E501
        """Information On a Neblio Address  # noqa: E501

        Returns both NEBL and NTP1 token UTXOs held at the given address.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_address_info(address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str address: Neblio Address to get information on. (required)
        :return: GetAddressInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_address_info_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_info_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def get_address_info_with_http_info(self, address, **kwargs):  # noqa: E501
        """Information On a Neblio Address  # noqa: E501

        Returns both NEBL and NTP1 token UTXOs held at the given address.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_address_info_with_http_info(address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str address: Neblio Address to get information on. (required)
        :return: GetAddressInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_address_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ntp1/addressinfo/{address}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAddressInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_token_holders(self, tokenid, **kwargs):  # noqa: E501
        """Get Addresses Holding a Token  # noqa: E501

        Returns the the the addresses holding a token and how many tokens are held   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_token_holders(tokenid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tokenid: TokenId to request metadata for (required)
        :return: GetTokenHoldersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_token_holders_with_http_info(tokenid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_token_holders_with_http_info(tokenid, **kwargs)  # noqa: E501
            return data

    def get_token_holders_with_http_info(self, tokenid, **kwargs):  # noqa: E501
        """Get Addresses Holding a Token  # noqa: E501

        Returns the the the addresses holding a token and how many tokens are held   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_token_holders_with_http_info(tokenid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tokenid: TokenId to request metadata for (required)
        :return: GetTokenHoldersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tokenid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token_holders" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tokenid' is set
        if ('tokenid' not in params or
                params['tokenid'] is None):
            raise ValueError("Missing the required parameter `tokenid` when calling `get_token_holders`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tokenid' in params:
            path_params['tokenid'] = params['tokenid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ntp1/stakeholders/{tokenid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetTokenHoldersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_token_id(self, tokensymbol, **kwargs):  # noqa: E501
        """Returns the tokenId representing a token  # noqa: E501

        Translates a token symbol to a tokenId if a token exists with that symbol on the network   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_token_id(tokensymbol, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tokensymbol: Token symbol (required)
        :return: GetTokenIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_token_id_with_http_info(tokensymbol, **kwargs)  # noqa: E501
        else:
            (data) = self.get_token_id_with_http_info(tokensymbol, **kwargs)  # noqa: E501
            return data

    def get_token_id_with_http_info(self, tokensymbol, **kwargs):  # noqa: E501
        """Returns the tokenId representing a token  # noqa: E501

        Translates a token symbol to a tokenId if a token exists with that symbol on the network   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_token_id_with_http_info(tokensymbol, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tokensymbol: Token symbol (required)
        :return: GetTokenIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tokensymbol']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tokensymbol' is set
        if ('tokensymbol' not in params or
                params['tokensymbol'] is None):
            raise ValueError("Missing the required parameter `tokensymbol` when calling `get_token_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tokensymbol' in params:
            path_params['tokensymbol'] = params['tokensymbol']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ntp1/tokenid/{tokensymbol}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetTokenIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_token_metadata_of_issuance(self, tokenid, **kwargs):  # noqa: E501
        """Get Issuance Metadata of Token  # noqa: E501

        Returns the metadata associated with a token at time of issuance.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_token_metadata_of_issuance(tokenid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tokenid: TokenId to request metadata for (required)
        :return: GetTokenMetadataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_token_metadata_of_issuance_with_http_info(tokenid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_token_metadata_of_issuance_with_http_info(tokenid, **kwargs)  # noqa: E501
            return data

    def get_token_metadata_of_issuance_with_http_info(self, tokenid, **kwargs):  # noqa: E501
        """Get Issuance Metadata of Token  # noqa: E501

        Returns the metadata associated with a token at time of issuance.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_token_metadata_of_issuance_with_http_info(tokenid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tokenid: TokenId to request metadata for (required)
        :return: GetTokenMetadataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tokenid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token_metadata_of_issuance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tokenid' is set
        if ('tokenid' not in params or
                params['tokenid'] is None):
            raise ValueError("Missing the required parameter `tokenid` when calling `get_token_metadata_of_issuance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tokenid' in params:
            path_params['tokenid'] = params['tokenid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ntp1/tokenmetadata/{tokenid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetTokenMetadataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_token_metadata_of_utxo(self, tokenid, utxo, **kwargs):  # noqa: E501
        """Get UTXO Metadata of Token  # noqa: E501

        Returns the metadata associated with a token for that specific utxo instead of the issuance transaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_token_metadata_of_utxo(tokenid, utxo, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tokenid: TokenId to request metadata for (required)
        :param str utxo: Specific UTXO to request metadata for (required)
        :return: GetTokenMetadataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_token_metadata_of_utxo_with_http_info(tokenid, utxo, **kwargs)  # noqa: E501
        else:
            (data) = self.get_token_metadata_of_utxo_with_http_info(tokenid, utxo, **kwargs)  # noqa: E501
            return data

    def get_token_metadata_of_utxo_with_http_info(self, tokenid, utxo, **kwargs):  # noqa: E501
        """Get UTXO Metadata of Token  # noqa: E501

        Returns the metadata associated with a token for that specific utxo instead of the issuance transaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_token_metadata_of_utxo_with_http_info(tokenid, utxo, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tokenid: TokenId to request metadata for (required)
        :param str utxo: Specific UTXO to request metadata for (required)
        :return: GetTokenMetadataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tokenid', 'utxo']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token_metadata_of_utxo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tokenid' is set
        if ('tokenid' not in params or
                params['tokenid'] is None):
            raise ValueError("Missing the required parameter `tokenid` when calling `get_token_metadata_of_utxo`")  # noqa: E501
        # verify the required parameter 'utxo' is set
        if ('utxo' not in params or
                params['utxo'] is None):
            raise ValueError("Missing the required parameter `utxo` when calling `get_token_metadata_of_utxo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tokenid' in params:
            path_params['tokenid'] = params['tokenid']  # noqa: E501
        if 'utxo' in params:
            path_params['utxo'] = params['utxo']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ntp1/tokenmetadata/{tokenid}/{utxo}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetTokenMetadataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def issue_token(self, body, **kwargs):  # noqa: E501
        """Builds a transaction that issues a new NTP1 Token  # noqa: E501

        Builds an unsigned raw transaction that issues a new NTP1 token on the Neblio blockchain.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.issue_token(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param IssueTokenRequest body: Object representing the token to be created (required)
        :return: IssueTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.issue_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.issue_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def issue_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """Builds a transaction that issues a new NTP1 Token  # noqa: E501

        Builds an unsigned raw transaction that issues a new NTP1 token on the Neblio blockchain.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.issue_token_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param IssueTokenRequest body: Object representing the token to be created (required)
        :return: IssueTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method issue_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `issue_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ntp1/issue', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IssueTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_token(self, body, **kwargs):  # noqa: E501
        """Builds a transaction that sends an NTP1 Token  # noqa: E501

        Builds an unsigned raw transaction that sends an NTP1 token on the Neblio blockchain.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_token(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param SendTokenRequest body: Object representing the token to be sent (required)
        :return: SendTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.send_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.send_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def send_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """Builds a transaction that sends an NTP1 Token  # noqa: E501

        Builds an unsigned raw transaction that sends an NTP1 token on the Neblio blockchain.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_token_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param SendTokenRequest body: Object representing the token to be sent (required)
        :return: SendTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `send_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ntp1/sendtoken', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SendTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)