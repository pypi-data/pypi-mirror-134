# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.essbasic.v20210526 import models


class EssbasicClient(AbstractClient):
    _apiVersion = '2021-05-26'
    _endpoint = 'essbasic.tencentcloudapi.com'
    _service = 'essbasic'


    def CreateConsoleLoginUrl(self, request):
        """此接口（CreateConsoleLoginUrl）用于创建电子签控制台登录链接。若企业未激活，调用同步企业信息、同步经办人信息

        :param request: Request instance for CreateConsoleLoginUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateConsoleLoginUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateConsoleLoginUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateConsoleLoginUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateConsoleLoginUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFlowsByTemplates(self, request):
        """接口（CreateFlowsByTemplates）用于使用多个模板批量创建流程

        :param request: Request instance for CreateFlowsByTemplates.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowsByTemplatesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowsByTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFlowsByTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFlowsByTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSignUrls(self, request):
        """根据流程Id批量创建签署参与者签署H5链接

        :param request: Request instance for CreateSignUrls.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateSignUrlsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateSignUrlsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSignUrls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSignUrlsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlowDetailInfo(self, request):
        """此接口（DescribeFlowDetailInfo）用于查询合同(流程)的详细信息。

        :param request: Request instance for DescribeFlowDetailInfo.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeFlowDetailInfoRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeFlowDetailInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlowDetailInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowDetailInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceUrlsByFlows(self, request):
        """根据流程信息批量获取资源下载链接

        :param request: Request instance for DescribeResourceUrlsByFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeResourceUrlsByFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeResourceUrlsByFlowsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceUrlsByFlows", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceUrlsByFlowsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTemplates(self, request):
        """通过此接口（DescribeTemplates）查询该企业在电子签渠道版中配置的有效模板列表

        :param request: Request instance for DescribeTemplates.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeTemplatesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUsage(self, request):
        """此接口（DescribeUsage）用于获取渠道所有合作企业流量消耗情况。
         注: 此接口每日限频2次，若要扩大限制次数,请提前与客服经理或邮件至e-contract@tencent.com进行联系。

        :param request: Request instance for DescribeUsage.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeUsageRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeUsageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUsage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDownloadFlowUrl(self, request):
        """此接口（GetDownloadFlowUrl）用于创建电子签批量下载确认页面链接，支持客户合同（流程）归类打包下载。

        :param request: Request instance for GetDownloadFlowUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.GetDownloadFlowUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.GetDownloadFlowUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDownloadFlowUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDownloadFlowUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OperateChannelTemplate(self, request):
        """此接口（OperateChannelTemplate）用于渠道侧将模板库中的模板对合作企业进行查询和设置, 其中包括可见性的修改以及对合作企业的指定.
        1、同步标识=select时：
        输入规则：“可见标识”、“指定合作企业列表”为空。
        处理规则：返回指定模版的可见标识、指定合作企业列表。
        2、同步标识=update时：
        输入规则：“可见标识”、“指定合作企业列表”非必填输入。
        处理规则：
        若“可见标识”=空，不做处理，返回当前的可见标识。
        若“可见标识”=所有合作企业，不取“指定合作企业列表”的值处理。
        若“可见标识”=指定合作企业，取“指定合作企业列表”的值进行更新/插入。
        3、同步标识=delete时：
        输入规则：“可见标识”、“指定合作企业列表”非必填输入。
        处理规则：
        仅取“指定合作企业列表”的值进行删除处理，为空时不做处。

        :param request: Request instance for OperateChannelTemplate.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.OperateChannelTemplateRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.OperateChannelTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OperateChannelTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OperateChannelTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PrepareFlows(self, request):
        """该接口 (PrepareFlows) 用于创建待发起文件

        :param request: Request instance for PrepareFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.PrepareFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.PrepareFlowsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PrepareFlows", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PrepareFlowsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SyncProxyOrganization(self, request):
        """此接口（SyncProxyOrganization）用于同步渠道侧企业信息

        :param request: Request instance for SyncProxyOrganization.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SyncProxyOrganization", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncProxyOrganizationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SyncProxyOrganizationOperators(self, request):
        """此接口（SyncProxyOrganizationOperators）用于同步渠道合作企业经办人列表

        :param request: Request instance for SyncProxyOrganizationOperators.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationOperatorsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationOperatorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SyncProxyOrganizationOperators", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncProxyOrganizationOperatorsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)