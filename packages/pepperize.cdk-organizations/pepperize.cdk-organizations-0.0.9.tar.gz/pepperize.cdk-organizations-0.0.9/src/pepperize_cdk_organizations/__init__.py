'''
[![GitHub](https://img.shields.io/github/license/pepperize/cdk-organizations?style=flat-square)](https://github.com/pepperize/cdk-organizations/blob/main/LICENSE)
[![npm (scoped)](https://img.shields.io/npm/v/@pepperize/cdk-organizations?style=flat-square)](https://www.npmjs.com/package/@pepperize/cdk-organizations)
[![PyPI](https://img.shields.io/pypi/v/pepperize.cdk-organizations?style=flat-square)](https://pypi.org/project/pepperize.cdk-organizations/)
[![Nuget](https://img.shields.io/nuget/v/Pepperize.CDK.Organizations?style=flat-square)](https://www.nuget.org/packages/Pepperize.CDK.Organizations/)
[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/pepperize/cdk-organizations/release/main?label=release&style=flat-square)](https://github.com/pepperize/cdk-organizations/actions/workflows/release.yml)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/pepperize/cdk-organizations?sort=semver&style=flat-square)](https://github.com/pepperize/cdk-organizations/releases)

# AWS Organizations

This project provides a CDK construct creating AWS organizations.

> Project status: WIP
>
> Currently there is no `@aws-cdk/organizations` available. See this [AWS CDK Issue](https://github.com/aws/aws-cdk/issues/2877).

* [AWS User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
* [AWS API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/Welcome.html)
* [AWS Bootstrapkit](https://github.com/awslabs/aws-bootstrap-kit)
* [AWS CDK Custom Resources](https://docs.aws.amazon.com/cdk/api/v1/docs/custom-resources-readme.html#custom-resources-for-aws-apis)

See [API.md](https://github.com/pepperize/cdk-organizations/blob/main/API.md)

## Install

### TypeScript

```shell
npm install @pepperize/cdk-organizations
```

or

```shell
yarn add @pepperize/cdk-organizations
```

### Python

```shell
pip install pepperize.cdk-organizations
```

### C# / .Net

```
dotnet add package Pepperize.CDK.Organizations
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


class Account(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@pepperize/cdk-organizations.Account",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        account_name: builtins.str,
        email: builtins.str,
        tags: typing.Mapping[builtins.str, builtins.str],
        iam_user_access_to_billing: typing.Optional["IamUserAccessToBilling"] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account_name: The friendly name of the member account.
        :param email: The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account. You must use a valid email address to complete account creation. You can't access the root user of the account or remove an account that was created with an invalid email address.
        :param tags: A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
        :param iam_user_access_to_billing: If set to ALLOW , the new account enables IAM users to access account billing information if they have the required permissions. If set to DENY , only the root user of the new account can access account billing information. Default: ALLOW
        :param role_name: The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. This role trusts the management account, allowing users in the management account to assume the role, as permitted by the management account administrator. The role has administrator permissions in the new member account. If you don't specify this parameter, the role name defaults to OrganizationAccountAccessRole.
        '''
        props = AccountProps(
            account_name=account_name,
            email=email,
            tags=tags,
            iam_user_access_to_billing=iam_user_access_to_billing,
            role_name=role_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        '''If the account was created successfully, the unique identifier (ID) of the new account.

        Exactly 12 digits.
        '''
        return typing.cast(builtins.str, jsii.get(self, "accountId"))


@jsii.data_type(
    jsii_type="@pepperize/cdk-organizations.AccountProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_name": "accountName",
        "email": "email",
        "tags": "tags",
        "iam_user_access_to_billing": "iamUserAccessToBilling",
        "role_name": "roleName",
    },
)
class AccountProps:
    def __init__(
        self,
        *,
        account_name: builtins.str,
        email: builtins.str,
        tags: typing.Mapping[builtins.str, builtins.str],
        iam_user_access_to_billing: typing.Optional["IamUserAccessToBilling"] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_name: The friendly name of the member account.
        :param email: The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account. You must use a valid email address to complete account creation. You can't access the root user of the account or remove an account that was created with an invalid email address.
        :param tags: A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
        :param iam_user_access_to_billing: If set to ALLOW , the new account enables IAM users to access account billing information if they have the required permissions. If set to DENY , only the root user of the new account can access account billing information. Default: ALLOW
        :param role_name: The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. This role trusts the management account, allowing users in the management account to assume the role, as permitted by the management account administrator. The role has administrator permissions in the new member account. If you don't specify this parameter, the role name defaults to OrganizationAccountAccessRole.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "account_name": account_name,
            "email": email,
            "tags": tags,
        }
        if iam_user_access_to_billing is not None:
            self._values["iam_user_access_to_billing"] = iam_user_access_to_billing
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def account_name(self) -> builtins.str:
        '''The friendly name of the member account.'''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''The email address of the owner to assign to the new member account.

        This email address must not already be associated with another AWS account. You must use a valid email address to complete account creation. You can't access the root user of the account or remove an account that was created with an invalid email address.
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''A list of tags that you want to attach to the newly created account.

        For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
        '''
        result = self._values.get("tags")
        assert result is not None, "Required property 'tags' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def iam_user_access_to_billing(self) -> typing.Optional["IamUserAccessToBilling"]:
        '''If set to ALLOW , the new account enables IAM users to access account billing information if they have the required permissions.

        If set to DENY , only the root user of the new account can access account billing information.

        :default: ALLOW
        '''
        result = self._values.get("iam_user_access_to_billing")
        return typing.cast(typing.Optional["IamUserAccessToBilling"], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''The name of an IAM role that AWS Organizations automatically preconfigures in the new member account.

        This role trusts the management account, allowing users in the management account to assume the role, as permitted by the management account administrator. The role has administrator permissions in the new member account.

        If you don't specify this parameter, the role name defaults to OrganizationAccountAccessRole.
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@pepperize/cdk-organizations.FeatureSet")
class FeatureSet(enum.Enum):
    '''Specifies the feature set supported by the new organization.

    Each feature set supports different levels of functionality.

    :see: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set
    '''

    CONSOLIDATED_BILLING = "CONSOLIDATED_BILLING"
    '''All member accounts have their bills consolidated to and paid by the management account.

    For more information, see [Consolidated billing]{@link https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-cb-only} in the AWS Organizations User Guide. The consolidated billing feature subset isn’t available for organizations in the AWS GovCloud (US) Region.
    '''
    ALL = "ALL"
    '''In addition to all the features supported by the consolidated billing feature set, the management account can also apply any policy type to any member account in the organization.

    For more information, see [All features]{@link https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-all} in the AWS Organizations User Guide.
    '''


@jsii.enum(jsii_type="@pepperize/cdk-organizations.IamUserAccessToBilling")
class IamUserAccessToBilling(enum.Enum):
    '''
    :see: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/control-access-billing.html#ControllingAccessWebsite-Activate
    '''

    ALLOW = "ALLOW"
    '''If set to ALLOW, the new account enables IAM users to access account billing information if they have the required permissions.'''
    DENY = "DENY"
    '''If set to DENY, only the root user of the new account can access account billing information.'''


class Organization(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@pepperize/cdk-organizations.Organization",
):
    '''Creates an organization to consolidate your AWS accounts so that you can administer them as a single unit.

    An organization has one management account along with zero or more member accounts. You can organize the accounts in a hierarchical, tree-like structure with a root at the top and organizational units nested under the root. Each account can be directly in the root, or placed in one of the OUs in the hierarchy. An organization has the functionality that is determined by the feature set that you enable.

    The account whose user is calling the CreateOrganization operation automatically becomes the management account of the new organization.

    For deletion of an organization you must previously remove all the member accounts, OUs, and policies from the organization!

    :see: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html#create-org
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        feature_set: typing.Optional[FeatureSet] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param feature_set: Enabling features in your organization. Default: ALL
        '''
        props = OrganizationProps(feature_set=feature_set)

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.str:
        '''The unique identifier (ID) of an organization.

        The regex pattern for an organization ID string requires "o-" followed by from 10 to 32 lowercase letters or digits.
        '''
        return typing.cast(builtins.str, jsii.get(self, "organizationId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rootId")
    def root_id(self) -> builtins.str:
        '''The unique identifier (ID) for the root.

        The regex pattern for a root ID string requires "r-" followed by from 4 to 32 lowercase letters or digits.
        '''
        return typing.cast(builtins.str, jsii.get(self, "rootId"))


@jsii.data_type(
    jsii_type="@pepperize/cdk-organizations.OrganizationProps",
    jsii_struct_bases=[],
    name_mapping={"feature_set": "featureSet"},
)
class OrganizationProps:
    def __init__(self, *, feature_set: typing.Optional[FeatureSet] = None) -> None:
        '''
        :param feature_set: Enabling features in your organization. Default: ALL
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if feature_set is not None:
            self._values["feature_set"] = feature_set

    @builtins.property
    def feature_set(self) -> typing.Optional[FeatureSet]:
        '''Enabling features in your organization.

        :default: ALL

        :see: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html
        '''
        result = self._values.get("feature_set")
        return typing.cast(typing.Optional[FeatureSet], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OrganizationalUnit(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@pepperize/cdk-organizations.OrganizationalUnit",
):
    '''A container for accounts within a root.

    An OU also can contain other OUs, enabling you to create a hierarchy that resembles an upside-down tree, with a root at the top and branches of OUs that reach down, ending in accounts that are the leaves of the tree. When you attach a policy to one of the nodes in the hierarchy, it flows down and affects all the branches (OUs) and leaves (accounts) beneath it. An OU can have exactly one parent, and currently each account can be a member of exactly one OU.

    You must first move all accounts out of the OU and any child OUs, and then you can delete the child OUs.
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        organizational_unit_name: builtins.str,
        parent_id: builtins.str,
        tags: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param organizational_unit_name: The friendly name to assign to the new OU.
        :param parent_id: The unique identifier (ID) of the parent root or OU that you want to create the new OU in.
        :param tags: A list of tags that you want to attach to the newly created organizational unit. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
        '''
        props = OrganizationalUnitProps(
            organizational_unit_name=organizational_unit_name,
            parent_id=parent_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@pepperize/cdk-organizations.OrganizationalUnitProps",
    jsii_struct_bases=[],
    name_mapping={
        "organizational_unit_name": "organizationalUnitName",
        "parent_id": "parentId",
        "tags": "tags",
    },
)
class OrganizationalUnitProps:
    def __init__(
        self,
        *,
        organizational_unit_name: builtins.str,
        parent_id: builtins.str,
        tags: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param organizational_unit_name: The friendly name to assign to the new OU.
        :param parent_id: The unique identifier (ID) of the parent root or OU that you want to create the new OU in.
        :param tags: A list of tags that you want to attach to the newly created organizational unit. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "organizational_unit_name": organizational_unit_name,
            "parent_id": parent_id,
            "tags": tags,
        }

    @builtins.property
    def organizational_unit_name(self) -> builtins.str:
        '''The friendly name to assign to the new OU.'''
        result = self._values.get("organizational_unit_name")
        assert result is not None, "Required property 'organizational_unit_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_id(self) -> builtins.str:
        '''The unique identifier (ID) of the parent root or OU that you want to create the new OU in.'''
        result = self._values.get("parent_id")
        assert result is not None, "Required property 'parent_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''A list of tags that you want to attach to the newly created organizational unit.

        For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
        '''
        result = self._values.get("tags")
        assert result is not None, "Required property 'tags' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationalUnitProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Policy(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@pepperize/cdk-organizations.Policy",
):
    '''Policies in AWS Organizations enable you to apply additional types of management to the AWS accounts in your organization.

    You can use policies when all features are enabled in your organization.

    :see: FeatureSet
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        content: builtins.str,
        policy_name: builtins.str,
        policy_type: "PolicyType",
        tags: typing.Mapping[builtins.str, builtins.str],
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param content: The policy text content to add to the new policy. The text that you supply must adhere to the rules of the policy type you specify in the Type parameter.
        :param policy_name: The friendly name to assign to the policy.
        :param policy_type: The type of policy to create. You can specify one of the following values:
        :param tags: A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
        :param description: An optional description to assign to the policy.
        '''
        props = PolicyProps(
            content=content,
            policy_name=policy_name,
            policy_type=policy_type,
            tags=tags,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@pepperize/cdk-organizations.PolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "policy_name": "policyName",
        "policy_type": "policyType",
        "tags": "tags",
        "description": "description",
    },
)
class PolicyProps:
    def __init__(
        self,
        *,
        content: builtins.str,
        policy_name: builtins.str,
        policy_type: "PolicyType",
        tags: typing.Mapping[builtins.str, builtins.str],
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: The policy text content to add to the new policy. The text that you supply must adhere to the rules of the policy type you specify in the Type parameter.
        :param policy_name: The friendly name to assign to the policy.
        :param policy_type: The type of policy to create. You can specify one of the following values:
        :param tags: A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
        :param description: An optional description to assign to the policy.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "policy_name": policy_name,
            "policy_type": policy_type,
            "tags": tags,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def content(self) -> builtins.str:
        '''The policy text content to add to the new policy.

        The text that you supply must adhere to the rules of the policy type you specify in the Type parameter.
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The friendly name to assign to the policy.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_type(self) -> "PolicyType":
        '''The type of policy to create.

        You can specify one of the following values:
        '''
        result = self._values.get("policy_type")
        assert result is not None, "Required property 'policy_type' is missing"
        return typing.cast("PolicyType", result)

    @builtins.property
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''A list of tags that you want to attach to the newly created policy.

        For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
        '''
        result = self._values.get("tags")
        assert result is not None, "Required property 'tags' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description to assign to the policy.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@pepperize/cdk-organizations.PolicyType")
class PolicyType(enum.Enum):
    '''Organizations offers policy types in the following two broad categories:       Authorization policies help you to centrally manage the security of the AWS accounts in your organization.      Management policies enable you to centrally configure and manage AWS services and their features. .

    :see: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html#orgs-policy-types
    '''

    SERVICE_CONTROL_POLICY = "SERVICE_CONTROL_POLICY"
    '''Service control policies (SCPs) offer central control over the maximum available permissions for all of the accounts in your organization.'''
    TAG_POLICY = "TAG_POLICY"
    '''Tag policies help you standardize the tags attached to the AWS resources in your organization's accounts.'''
    BACKUP_POLICY = "BACKUP_POLICY"
    '''Backup policies help you centrally manage and apply backup plans to the AWS resources across your organization's accounts.'''
    AISERVICES_OPT_OUT_POLICY = "AISERVICES_OPT_OUT_POLICY"
    '''Artificial Intelligence (AI) services opt-out policies enable you to control data collection for AWS AI services for all of your organization's accounts.'''


__all__ = [
    "Account",
    "AccountProps",
    "FeatureSet",
    "IamUserAccessToBilling",
    "Organization",
    "OrganizationProps",
    "OrganizationalUnit",
    "OrganizationalUnitProps",
    "Policy",
    "PolicyProps",
    "PolicyType",
]

publication.publish()
