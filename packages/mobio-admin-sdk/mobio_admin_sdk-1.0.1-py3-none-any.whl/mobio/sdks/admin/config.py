#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: AnhNT
    Company: MobioVN
    Date created: 26/02/2021

"""

import os


YEK_REWOP = os.environ.get("YEK_REWOP", "f38b67fa-22f3-4680-9d01-c36b23bd0cad")

class SystemConfigKeys:
    JWT_SECRET_KEY = "jwt_secret_key"
    JWT_ALGORITHM = "jwt_algorithm"
    X_MERCHANT_ID = "X-Merchant-ID"
    LICENSE_KEY = os.environ.get("LICENSE_KEY_SALT", "LICENSE_MOBIO_v1_")
    MOBIO_TOKEN = "Basic " + YEK_REWOP
    vm_type = os.environ.get("VM_TYPE")


class StoreCacheType:
    LOCAL = 1
    REDIS = 2


class Cache:
    PREFIX_KEY = "admin_sdk_"


class UrlConfig:
    ADMIN_CONFIG = "{host}/adm/{version}/merchants/{merchant_id}/configs"
    PARTNER_INFO = "{host}/adm/{version}/partners/{partner_id}/info"
    PARTNER_INFO_CIPHER_ENCRYPT = (
        "{host}/adm/{version}/partners/{partner_id}/info/encrypt"
    )
    MERCHANT_RELATED = "{host}/adm/{version}/merchants/{merchant_id}/related"
    STAFF_INFO = "{host}/adm/{version}/merchants/{merchant_id}/accounts/{account_id}"
    LIST_STAFF_INFO = "{host}/adm/{version}/merchants/{merchant_id}/accounts"
    MERCHANT_PARENT = "{host}/adm/{version}/merchants/{merchant_id}/parent"
    LIST_PROFILE_GROUP = "{host}/adm/{version}/profile-groups"
    LIST_SUBBRANDS_BY_MERCHANT = "{host}/adm/{version}/sub-brands"
    GET_INFO_SUBBRAND = "{host}/adm/{version}/merchants/sub-brands/{subbrand_id}"
    GET_INTERNAL_MERCHANT_CONFIG = "{host}/adm/{version}/merchants/{merchant_id}/internal-configs"
    GET_SERVER_FROM_MERCHANT = "{host}/adm/{version}/server-uri/merchant"
    GET_LIST_SERVER_FROM_MODULE = "{host}/adm/{version}/server-uri"
    GET_DETAIL_MERCHANT_CONFIG = "{host}/adm/{version}/merchants/{merchant_id}/config/detail"

class KafkaTopic:
    LogActionAccount = "admin-log-action-account"
