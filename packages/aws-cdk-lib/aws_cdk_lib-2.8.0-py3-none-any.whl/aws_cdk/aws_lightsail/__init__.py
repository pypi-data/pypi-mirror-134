'''
# AWS::Lightsail Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_lightsail as lightsail
```

> The construct library for this service is in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-lightsail-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Lightsail](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Lightsail.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnDatabase(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnDatabase",
):
    '''A CloudFormation ``AWS::Lightsail::Database``.

    The ``AWS::Lightsail::Database`` resource specifies an Amazon Lightsail database.

    :cloudformationResource: AWS::Lightsail::Database
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_database = lightsail.CfnDatabase(self, "MyCfnDatabase",
            master_database_name="masterDatabaseName",
            master_username="masterUsername",
            relational_database_blueprint_id="relationalDatabaseBlueprintId",
            relational_database_bundle_id="relationalDatabaseBundleId",
            relational_database_name="relationalDatabaseName",
        
            # the properties below are optional
            availability_zone="availabilityZone",
            backup_retention=False,
            ca_certificate_identifier="caCertificateIdentifier",
            master_user_password="masterUserPassword",
            preferred_backup_window="preferredBackupWindow",
            preferred_maintenance_window="preferredMaintenanceWindow",
            publicly_accessible=False,
            relational_database_parameters=[lightsail.CfnDatabase.RelationalDatabaseParameterProperty(
                allowed_values="allowedValues",
                apply_method="applyMethod",
                apply_type="applyType",
                data_type="dataType",
                description="description",
                is_modifiable=False,
                parameter_name="parameterName",
                parameter_value="parameterValue"
            )],
            rotate_master_user_password=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        master_database_name: builtins.str,
        master_username: builtins.str,
        relational_database_blueprint_id: builtins.str,
        relational_database_bundle_id: builtins.str,
        relational_database_name: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        backup_retention: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ca_certificate_identifier: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        relational_database_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDatabase.RelationalDatabaseParameterProperty", _IResolvable_da3f097b]]]] = None,
        rotate_master_user_password: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Lightsail::Database``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param master_database_name: The meaning of this parameter differs according to the database engine you use. *MySQL* The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, no database is created in the database resource. Constraints: - Must contain 1-64 letters or numbers. - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9). - Can't be a word reserved by the specified database engine. For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , and `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ . *PostgreSQL* The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, a database named ``postgres`` is created in the database resource. Constraints: - Must contain 1-63 letters or numbers. - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9). - Can't be a word reserved by the specified database engine. For more information about reserved words in PostgreSQL, see the SQL Key Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .
        :param master_username: The name for the primary user. *MySQL* Constraints: - Required for MySQL. - Must be 1-16 letters or numbers. Can contain underscores. - First character must be a letter. - Can't be a reserved word for the chosen database engine. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , or `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ . *PostgreSQL* Constraints: - Required for PostgreSQL. - Must be 1-63 letters or numbers. Can contain underscores. - First character must be a letter. - Can't be a reserved word for the chosen database engine. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .
        :param relational_database_blueprint_id: The blueprint ID for the database (for example, ``mysql_8_0`` ).
        :param relational_database_bundle_id: The bundle ID for the database (for example, ``medium_1_0`` ).
        :param relational_database_name: The name of the instance.
        :param availability_zone: The Availability Zone for the database.
        :param backup_retention: A Boolean value indicating whether automated backup retention is enabled for the database.
        :param ca_certificate_identifier: The certificate associated with the database.
        :param master_user_password: The password for the primary user of the database. The password can include any printable ASCII character except the following: /, ", or @. It cannot contain spaces. .. epigraph:: The ``MasterUserPassword`` and ``RotateMasterUserPassword`` parameters cannot be used together in the same template. *MySQL* Constraints: Must contain 8-41 characters. *PostgreSQL* Constraints: Must contain 8-128 characters.
        :param preferred_backup_window: The daily time range during which automated backups are created for the database (for example, ``16:00-16:30`` ).
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur for the database, formatted as follows: ``ddd:hh24:mi-ddd:hh24:mi`` . For example, ``Tue:17:00-Tue:17:30`` .
        :param publicly_accessible: A Boolean value indicating whether the database is accessible to anyone on the internet.
        :param relational_database_parameters: An array of parameters for the database.
        :param rotate_master_user_password: A Boolean value indicating whether to change the primary user password to a new, strong password generated by Lightsail . .. epigraph:: The ``RotateMasterUserPassword`` and ``MasterUserPassword`` parameters cannot be used together in the same template.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        '''
        props = CfnDatabaseProps(
            master_database_name=master_database_name,
            master_username=master_username,
            relational_database_blueprint_id=relational_database_blueprint_id,
            relational_database_bundle_id=relational_database_bundle_id,
            relational_database_name=relational_database_name,
            availability_zone=availability_zone,
            backup_retention=backup_retention,
            ca_certificate_identifier=ca_certificate_identifier,
            master_user_password=master_user_password,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            publicly_accessible=publicly_accessible,
            relational_database_parameters=relational_database_parameters,
            rotate_master_user_password=rotate_master_user_password,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDatabaseArn")
    def attr_database_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the database (for example, ``arn:aws:lightsail:us-east-2:123456789101:RelationalDatabase/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).

        :cloudformationAttribute: DatabaseArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatabaseArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterDatabaseName")
    def master_database_name(self) -> builtins.str:
        '''The meaning of this parameter differs according to the database engine you use.

        *MySQL*

        The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, no database is created in the database resource.

        Constraints:

        - Must contain 1-64 letters or numbers.
        - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9).
        - Can't be a word reserved by the specified database engine.

        For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , and `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ .

        *PostgreSQL*

        The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, a database named ``postgres`` is created in the database resource.

        Constraints:

        - Must contain 1-63 letters or numbers.
        - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9).
        - Can't be a word reserved by the specified database engine.

        For more information about reserved words in PostgreSQL, see the SQL Key Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterdatabasename
        '''
        return typing.cast(builtins.str, jsii.get(self, "masterDatabaseName"))

    @master_database_name.setter
    def master_database_name(self, value: builtins.str) -> None:
        jsii.set(self, "masterDatabaseName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUsername")
    def master_username(self) -> builtins.str:
        '''The name for the primary user.

        *MySQL*

        Constraints:

        - Required for MySQL.
        - Must be 1-16 letters or numbers. Can contain underscores.
        - First character must be a letter.
        - Can't be a reserved word for the chosen database engine.

        For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , or `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ .

        *PostgreSQL*

        Constraints:

        - Required for PostgreSQL.
        - Must be 1-63 letters or numbers. Can contain underscores.
        - First character must be a letter.
        - Can't be a reserved word for the chosen database engine.

        For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterusername
        '''
        return typing.cast(builtins.str, jsii.get(self, "masterUsername"))

    @master_username.setter
    def master_username(self, value: builtins.str) -> None:
        jsii.set(self, "masterUsername", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="relationalDatabaseBlueprintId")
    def relational_database_blueprint_id(self) -> builtins.str:
        '''The blueprint ID for the database (for example, ``mysql_8_0`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseblueprintid
        '''
        return typing.cast(builtins.str, jsii.get(self, "relationalDatabaseBlueprintId"))

    @relational_database_blueprint_id.setter
    def relational_database_blueprint_id(self, value: builtins.str) -> None:
        jsii.set(self, "relationalDatabaseBlueprintId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="relationalDatabaseBundleId")
    def relational_database_bundle_id(self) -> builtins.str:
        '''The bundle ID for the database (for example, ``medium_1_0`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasebundleid
        '''
        return typing.cast(builtins.str, jsii.get(self, "relationalDatabaseBundleId"))

    @relational_database_bundle_id.setter
    def relational_database_bundle_id(self, value: builtins.str) -> None:
        jsii.set(self, "relationalDatabaseBundleId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="relationalDatabaseName")
    def relational_database_name(self) -> builtins.str:
        '''The name of the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasename
        '''
        return typing.cast(builtins.str, jsii.get(self, "relationalDatabaseName"))

    @relational_database_name.setter
    def relational_database_name(self, value: builtins.str) -> None:
        jsii.set(self, "relationalDatabaseName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone for the database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-availabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "availabilityZone", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="backupRetention")
    def backup_retention(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether automated backup retention is enabled for the database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-backupretention
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "backupRetention"))

    @backup_retention.setter
    def backup_retention(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "backupRetention", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="caCertificateIdentifier")
    def ca_certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''The certificate associated with the database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-cacertificateidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertificateIdentifier"))

    @ca_certificate_identifier.setter
    def ca_certificate_identifier(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "caCertificateIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> typing.Optional[builtins.str]:
        '''The password for the primary user of the database.

        The password can include any printable ASCII character except the following: /, ", or @. It cannot contain spaces.
        .. epigraph::

           The ``MasterUserPassword`` and ``RotateMasterUserPassword`` parameters cannot be used together in the same template.

        *MySQL*

        Constraints: Must contain 8-41 characters.

        *PostgreSQL*

        Constraints: Must contain 8-128 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masteruserpassword
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUserPassword"))

    @master_user_password.setter
    def master_user_password(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "masterUserPassword", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preferredBackupWindow")
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range during which automated backups are created for the database (for example, ``16:00-16:30`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredbackupwindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredBackupWindow"))

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "preferredBackupWindow", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur for the database, formatted as follows: ``ddd:hh24:mi-ddd:hh24:mi`` .

        For example, ``Tue:17:00-Tue:17:30`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredmaintenancewindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the database is accessible to anyone on the internet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-publiclyaccessible
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="relationalDatabaseParameters")
    def relational_database_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDatabase.RelationalDatabaseParameterProperty", _IResolvable_da3f097b]]]]:
        '''An array of parameters for the database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseparameters
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDatabase.RelationalDatabaseParameterProperty", _IResolvable_da3f097b]]]], jsii.get(self, "relationalDatabaseParameters"))

    @relational_database_parameters.setter
    def relational_database_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDatabase.RelationalDatabaseParameterProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "relationalDatabaseParameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rotateMasterUserPassword")
    def rotate_master_user_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether to change the primary user password to a new, strong password generated by Lightsail .

        .. epigraph::

           The ``RotateMasterUserPassword`` and ``MasterUserPassword`` parameters cannot be used together in the same template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-rotatemasteruserpassword
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "rotateMasterUserPassword"))

    @rotate_master_user_password.setter
    def rotate_master_user_password(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "rotateMasterUserPassword", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDatabase.RelationalDatabaseParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_values": "allowedValues",
            "apply_method": "applyMethod",
            "apply_type": "applyType",
            "data_type": "dataType",
            "description": "description",
            "is_modifiable": "isModifiable",
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class RelationalDatabaseParameterProperty:
        def __init__(
            self,
            *,
            allowed_values: typing.Optional[builtins.str] = None,
            apply_method: typing.Optional[builtins.str] = None,
            apply_type: typing.Optional[builtins.str] = None,
            data_type: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            is_modifiable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            parameter_name: typing.Optional[builtins.str] = None,
            parameter_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``RelationalDatabaseParameter`` is a property of the `AWS::Lightsail::Database <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html>`_ resource. It describes parameters for the database.

            :param allowed_values: The valid range of values for the parameter.
            :param apply_method: Indicates when parameter updates are applied. Can be ``immediate`` or ``pending-reboot`` .
            :param apply_type: Specifies the engine-specific parameter type.
            :param data_type: The valid data type of the parameter.
            :param description: A description of the parameter.
            :param is_modifiable: A Boolean value indicating whether the parameter can be modified.
            :param parameter_name: The name of the parameter.
            :param parameter_value: The value for the parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                relational_database_parameter_property = lightsail.CfnDatabase.RelationalDatabaseParameterProperty(
                    allowed_values="allowedValues",
                    apply_method="applyMethod",
                    apply_type="applyType",
                    data_type="dataType",
                    description="description",
                    is_modifiable=False,
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if apply_method is not None:
                self._values["apply_method"] = apply_method
            if apply_type is not None:
                self._values["apply_type"] = apply_type
            if data_type is not None:
                self._values["data_type"] = data_type
            if description is not None:
                self._values["description"] = description
            if is_modifiable is not None:
                self._values["is_modifiable"] = is_modifiable
            if parameter_name is not None:
                self._values["parameter_name"] = parameter_name
            if parameter_value is not None:
                self._values["parameter_value"] = parameter_value

        @builtins.property
        def allowed_values(self) -> typing.Optional[builtins.str]:
            '''The valid range of values for the parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def apply_method(self) -> typing.Optional[builtins.str]:
            '''Indicates when parameter updates are applied.

            Can be ``immediate`` or ``pending-reboot`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applymethod
            '''
            result = self._values.get("apply_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def apply_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the engine-specific parameter type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applytype
            '''
            result = self._values.get("apply_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_type(self) -> typing.Optional[builtins.str]:
            '''The valid data type of the parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-datatype
            '''
            result = self._values.get("data_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def is_modifiable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value indicating whether the parameter can be modified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-ismodifiable
            '''
            result = self._values.get("is_modifiable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def parameter_name(self) -> typing.Optional[builtins.str]:
            '''The name of the parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametername
            '''
            result = self._values.get("parameter_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameter_value(self) -> typing.Optional[builtins.str]:
            '''The value for the parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelationalDatabaseParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnDatabaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "master_database_name": "masterDatabaseName",
        "master_username": "masterUsername",
        "relational_database_blueprint_id": "relationalDatabaseBlueprintId",
        "relational_database_bundle_id": "relationalDatabaseBundleId",
        "relational_database_name": "relationalDatabaseName",
        "availability_zone": "availabilityZone",
        "backup_retention": "backupRetention",
        "ca_certificate_identifier": "caCertificateIdentifier",
        "master_user_password": "masterUserPassword",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "publicly_accessible": "publiclyAccessible",
        "relational_database_parameters": "relationalDatabaseParameters",
        "rotate_master_user_password": "rotateMasterUserPassword",
        "tags": "tags",
    },
)
class CfnDatabaseProps:
    def __init__(
        self,
        *,
        master_database_name: builtins.str,
        master_username: builtins.str,
        relational_database_blueprint_id: builtins.str,
        relational_database_bundle_id: builtins.str,
        relational_database_name: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        backup_retention: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ca_certificate_identifier: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        relational_database_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnDatabase.RelationalDatabaseParameterProperty, _IResolvable_da3f097b]]]] = None,
        rotate_master_user_password: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDatabase``.

        :param master_database_name: The meaning of this parameter differs according to the database engine you use. *MySQL* The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, no database is created in the database resource. Constraints: - Must contain 1-64 letters or numbers. - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9). - Can't be a word reserved by the specified database engine. For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , and `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ . *PostgreSQL* The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, a database named ``postgres`` is created in the database resource. Constraints: - Must contain 1-63 letters or numbers. - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9). - Can't be a word reserved by the specified database engine. For more information about reserved words in PostgreSQL, see the SQL Key Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .
        :param master_username: The name for the primary user. *MySQL* Constraints: - Required for MySQL. - Must be 1-16 letters or numbers. Can contain underscores. - First character must be a letter. - Can't be a reserved word for the chosen database engine. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , or `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ . *PostgreSQL* Constraints: - Required for PostgreSQL. - Must be 1-63 letters or numbers. Can contain underscores. - First character must be a letter. - Can't be a reserved word for the chosen database engine. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .
        :param relational_database_blueprint_id: The blueprint ID for the database (for example, ``mysql_8_0`` ).
        :param relational_database_bundle_id: The bundle ID for the database (for example, ``medium_1_0`` ).
        :param relational_database_name: The name of the instance.
        :param availability_zone: The Availability Zone for the database.
        :param backup_retention: A Boolean value indicating whether automated backup retention is enabled for the database.
        :param ca_certificate_identifier: The certificate associated with the database.
        :param master_user_password: The password for the primary user of the database. The password can include any printable ASCII character except the following: /, ", or @. It cannot contain spaces. .. epigraph:: The ``MasterUserPassword`` and ``RotateMasterUserPassword`` parameters cannot be used together in the same template. *MySQL* Constraints: Must contain 8-41 characters. *PostgreSQL* Constraints: Must contain 8-128 characters.
        :param preferred_backup_window: The daily time range during which automated backups are created for the database (for example, ``16:00-16:30`` ).
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur for the database, formatted as follows: ``ddd:hh24:mi-ddd:hh24:mi`` . For example, ``Tue:17:00-Tue:17:30`` .
        :param publicly_accessible: A Boolean value indicating whether the database is accessible to anyone on the internet.
        :param relational_database_parameters: An array of parameters for the database.
        :param rotate_master_user_password: A Boolean value indicating whether to change the primary user password to a new, strong password generated by Lightsail . .. epigraph:: The ``RotateMasterUserPassword`` and ``MasterUserPassword`` parameters cannot be used together in the same template.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_database_props = lightsail.CfnDatabaseProps(
                master_database_name="masterDatabaseName",
                master_username="masterUsername",
                relational_database_blueprint_id="relationalDatabaseBlueprintId",
                relational_database_bundle_id="relationalDatabaseBundleId",
                relational_database_name="relationalDatabaseName",
            
                # the properties below are optional
                availability_zone="availabilityZone",
                backup_retention=False,
                ca_certificate_identifier="caCertificateIdentifier",
                master_user_password="masterUserPassword",
                preferred_backup_window="preferredBackupWindow",
                preferred_maintenance_window="preferredMaintenanceWindow",
                publicly_accessible=False,
                relational_database_parameters=[lightsail.CfnDatabase.RelationalDatabaseParameterProperty(
                    allowed_values="allowedValues",
                    apply_method="applyMethod",
                    apply_type="applyType",
                    data_type="dataType",
                    description="description",
                    is_modifiable=False,
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )],
                rotate_master_user_password=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "master_database_name": master_database_name,
            "master_username": master_username,
            "relational_database_blueprint_id": relational_database_blueprint_id,
            "relational_database_bundle_id": relational_database_bundle_id,
            "relational_database_name": relational_database_name,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if backup_retention is not None:
            self._values["backup_retention"] = backup_retention
        if ca_certificate_identifier is not None:
            self._values["ca_certificate_identifier"] = ca_certificate_identifier
        if master_user_password is not None:
            self._values["master_user_password"] = master_user_password
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if relational_database_parameters is not None:
            self._values["relational_database_parameters"] = relational_database_parameters
        if rotate_master_user_password is not None:
            self._values["rotate_master_user_password"] = rotate_master_user_password
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def master_database_name(self) -> builtins.str:
        '''The meaning of this parameter differs according to the database engine you use.

        *MySQL*

        The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, no database is created in the database resource.

        Constraints:

        - Must contain 1-64 letters or numbers.
        - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9).
        - Can't be a word reserved by the specified database engine.

        For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , and `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ .

        *PostgreSQL*

        The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, a database named ``postgres`` is created in the database resource.

        Constraints:

        - Must contain 1-63 letters or numbers.
        - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9).
        - Can't be a word reserved by the specified database engine.

        For more information about reserved words in PostgreSQL, see the SQL Key Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterdatabasename
        '''
        result = self._values.get("master_database_name")
        assert result is not None, "Required property 'master_database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_username(self) -> builtins.str:
        '''The name for the primary user.

        *MySQL*

        Constraints:

        - Required for MySQL.
        - Must be 1-16 letters or numbers. Can contain underscores.
        - First character must be a letter.
        - Can't be a reserved word for the chosen database engine.

        For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , or `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ .

        *PostgreSQL*

        Constraints:

        - Required for PostgreSQL.
        - Must be 1-63 letters or numbers. Can contain underscores.
        - First character must be a letter.
        - Can't be a reserved word for the chosen database engine.

        For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterusername
        '''
        result = self._values.get("master_username")
        assert result is not None, "Required property 'master_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relational_database_blueprint_id(self) -> builtins.str:
        '''The blueprint ID for the database (for example, ``mysql_8_0`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseblueprintid
        '''
        result = self._values.get("relational_database_blueprint_id")
        assert result is not None, "Required property 'relational_database_blueprint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relational_database_bundle_id(self) -> builtins.str:
        '''The bundle ID for the database (for example, ``medium_1_0`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasebundleid
        '''
        result = self._values.get("relational_database_bundle_id")
        assert result is not None, "Required property 'relational_database_bundle_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relational_database_name(self) -> builtins.str:
        '''The name of the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasename
        '''
        result = self._values.get("relational_database_name")
        assert result is not None, "Required property 'relational_database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone for the database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_retention(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether automated backup retention is enabled for the database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-backupretention
        '''
        result = self._values.get("backup_retention")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def ca_certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''The certificate associated with the database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-cacertificateidentifier
        '''
        result = self._values.get("ca_certificate_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_password(self) -> typing.Optional[builtins.str]:
        '''The password for the primary user of the database.

        The password can include any printable ASCII character except the following: /, ", or @. It cannot contain spaces.
        .. epigraph::

           The ``MasterUserPassword`` and ``RotateMasterUserPassword`` parameters cannot be used together in the same template.

        *MySQL*

        Constraints: Must contain 8-41 characters.

        *PostgreSQL*

        Constraints: Must contain 8-128 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masteruserpassword
        '''
        result = self._values.get("master_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range during which automated backups are created for the database (for example, ``16:00-16:30`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredbackupwindow
        '''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur for the database, formatted as follows: ``ddd:hh24:mi-ddd:hh24:mi`` .

        For example, ``Tue:17:00-Tue:17:30`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the database is accessible to anyone on the internet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def relational_database_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDatabase.RelationalDatabaseParameterProperty, _IResolvable_da3f097b]]]]:
        '''An array of parameters for the database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseparameters
        '''
        result = self._values.get("relational_database_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDatabase.RelationalDatabaseParameterProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def rotate_master_user_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether to change the primary user password to a new, strong password generated by Lightsail .

        .. epigraph::

           The ``RotateMasterUserPassword`` and ``MasterUserPassword`` parameters cannot be used together in the same template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-rotatemasteruserpassword
        '''
        result = self._values.get("rotate_master_user_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatabaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDisk(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnDisk",
):
    '''A CloudFormation ``AWS::Lightsail::Disk``.

    The ``AWS::Lightsail::Disk`` resource specifies a disk that can be attached to an Amazon Lightsail instance that is in the same AWS Region and Availability Zone.

    :cloudformationResource: AWS::Lightsail::Disk
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_disk = lightsail.CfnDisk(self, "MyCfnDisk",
            disk_name="diskName",
            size_in_gb=123,
        
            # the properties below are optional
            add_ons=[lightsail.CfnDisk.AddOnProperty(
                add_on_type="addOnType",
        
                # the properties below are optional
                auto_snapshot_add_on_request=lightsail.CfnDisk.AutoSnapshotAddOnProperty(
                    snapshot_time_of_day="snapshotTimeOfDay"
                ),
                status="status"
            )],
            availability_zone="availabilityZone",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        disk_name: builtins.str,
        size_in_gb: jsii.Number,
        add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDisk.AddOnProperty", _IResolvable_da3f097b]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Lightsail::Disk``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param disk_name: The name of the disk.
        :param size_in_gb: The size of the disk in GB.
        :param add_ons: An array of add-ons for the disk. .. epigraph:: If the disk has an add-on enabled when performing a delete disk request, the add-on is automatically disabled before the disk is deleted.
        :param availability_zone: The AWS Region and Availability Zone location for the disk (for example, ``us-east-1a`` ).
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        '''
        props = CfnDiskProps(
            disk_name=disk_name,
            size_in_gb=size_in_gb,
            add_ons=add_ons,
            availability_zone=availability_zone,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachedTo")
    def attr_attached_to(self) -> builtins.str:
        '''The instance to which the disk is attached.

        :cloudformationAttribute: AttachedTo
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachedTo"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAttachmentState")
    def attr_attachment_state(self) -> builtins.str:
        '''(Deprecated) The attachment state of the disk.

        .. epigraph::

           In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

        :cloudformationAttribute: AttachmentState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDiskArn")
    def attr_disk_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the disk.

        :cloudformationAttribute: DiskArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDiskArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIops")
    def attr_iops(self) -> jsii.Number:
        '''The input/output operations per second (IOPS) of the disk.

        :cloudformationAttribute: Iops
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrIops"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIsAttached")
    def attr_is_attached(self) -> _IResolvable_da3f097b:
        '''A Boolean value indicating whether the disk is attached to an instance.

        :cloudformationAttribute: IsAttached
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsAttached"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPath")
    def attr_path(self) -> builtins.str:
        '''The path of the disk.

        :cloudformationAttribute: Path
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPath"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceType")
    def attr_resource_type(self) -> builtins.str:
        '''The resource type of the disk (for example, ``Disk`` ).

        :cloudformationAttribute: ResourceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the disk (for example, ``in-use`` ).

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSupportCode")
    def attr_support_code(self) -> builtins.str:
        '''The support code of the disk.

        Include this code in your email to support when you have questions about a disk or another resource in Lightsail . This code helps our support team to look up your Lightsail information.

        :cloudformationAttribute: SupportCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSupportCode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="diskName")
    def disk_name(self) -> builtins.str:
        '''The name of the disk.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-diskname
        '''
        return typing.cast(builtins.str, jsii.get(self, "diskName"))

    @disk_name.setter
    def disk_name(self, value: builtins.str) -> None:
        jsii.set(self, "diskName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sizeInGb")
    def size_in_gb(self) -> jsii.Number:
        '''The size of the disk in GB.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-sizeingb
        '''
        return typing.cast(jsii.Number, jsii.get(self, "sizeInGb"))

    @size_in_gb.setter
    def size_in_gb(self, value: jsii.Number) -> None:
        jsii.set(self, "sizeInGb", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="addOns")
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDisk.AddOnProperty", _IResolvable_da3f097b]]]]:
        '''An array of add-ons for the disk.

        .. epigraph::

           If the disk has an add-on enabled when performing a delete disk request, the add-on is automatically disabled before the disk is deleted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-addons
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDisk.AddOnProperty", _IResolvable_da3f097b]]]], jsii.get(self, "addOns"))

    @add_ons.setter
    def add_ons(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDisk.AddOnProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "addOns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The AWS Region and Availability Zone location for the disk (for example, ``us-east-1a`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-availabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "availabilityZone", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDisk.AddOnProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_on_type": "addOnType",
            "auto_snapshot_add_on_request": "autoSnapshotAddOnRequest",
            "status": "status",
        },
    )
    class AddOnProperty:
        def __init__(
            self,
            *,
            add_on_type: builtins.str,
            auto_snapshot_add_on_request: typing.Optional[typing.Union["CfnDisk.AutoSnapshotAddOnProperty", _IResolvable_da3f097b]] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``AddOn`` is a property of the `AWS::Lightsail::Disk <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html>`_ resource. It describes the add-ons for a disk.

            :param add_on_type: The add-on type (for example, ``AutoSnapshot`` ). .. epigraph:: ``AutoSnapshot`` is the only add-on that can be enabled for a disk.
            :param auto_snapshot_add_on_request: The parameters for the automatic snapshot add-on, such as the daily time when an automatic snapshot will be created.
            :param status: The status of the add-on. Valid Values: ``Enabled`` | ``Disabled``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                add_on_property = lightsail.CfnDisk.AddOnProperty(
                    add_on_type="addOnType",
                
                    # the properties below are optional
                    auto_snapshot_add_on_request=lightsail.CfnDisk.AutoSnapshotAddOnProperty(
                        snapshot_time_of_day="snapshotTimeOfDay"
                    ),
                    status="status"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "add_on_type": add_on_type,
            }
            if auto_snapshot_add_on_request is not None:
                self._values["auto_snapshot_add_on_request"] = auto_snapshot_add_on_request
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def add_on_type(self) -> builtins.str:
            '''The add-on type (for example, ``AutoSnapshot`` ).

            .. epigraph::

               ``AutoSnapshot`` is the only add-on that can be enabled for a disk.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-addontype
            '''
            result = self._values.get("add_on_type")
            assert result is not None, "Required property 'add_on_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auto_snapshot_add_on_request(
            self,
        ) -> typing.Optional[typing.Union["CfnDisk.AutoSnapshotAddOnProperty", _IResolvable_da3f097b]]:
            '''The parameters for the automatic snapshot add-on, such as the daily time when an automatic snapshot will be created.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-autosnapshotaddonrequest
            '''
            result = self._values.get("auto_snapshot_add_on_request")
            return typing.cast(typing.Optional[typing.Union["CfnDisk.AutoSnapshotAddOnProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the add-on.

            Valid Values: ``Enabled`` | ``Disabled``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDisk.AutoSnapshotAddOnProperty",
        jsii_struct_bases=[],
        name_mapping={"snapshot_time_of_day": "snapshotTimeOfDay"},
    )
    class AutoSnapshotAddOnProperty:
        def __init__(
            self,
            *,
            snapshot_time_of_day: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``AutoSnapshotAddOn`` is a property of the `AddOn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html>`_ property. It describes the automatic snapshot add-on for a disk.

            :param snapshot_time_of_day: The daily time when an automatic snapshot will be created. Constraints: - Must be in ``HH:00`` format, and in an hourly increment. - Specified in Coordinated Universal Time (UTC). - The snapshot will be automatically created between the time specified and up to 45 minutes after.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-autosnapshotaddon.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                auto_snapshot_add_on_property = lightsail.CfnDisk.AutoSnapshotAddOnProperty(
                    snapshot_time_of_day="snapshotTimeOfDay"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if snapshot_time_of_day is not None:
                self._values["snapshot_time_of_day"] = snapshot_time_of_day

        @builtins.property
        def snapshot_time_of_day(self) -> typing.Optional[builtins.str]:
            '''The daily time when an automatic snapshot will be created.

            Constraints:

            - Must be in ``HH:00`` format, and in an hourly increment.
            - Specified in Coordinated Universal Time (UTC).
            - The snapshot will be automatically created between the time specified and up to 45 minutes after.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-autosnapshotaddon.html#cfn-lightsail-disk-autosnapshotaddon-snapshottimeofday
            '''
            result = self._values.get("snapshot_time_of_day")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoSnapshotAddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnDiskProps",
    jsii_struct_bases=[],
    name_mapping={
        "disk_name": "diskName",
        "size_in_gb": "sizeInGb",
        "add_ons": "addOns",
        "availability_zone": "availabilityZone",
        "tags": "tags",
    },
)
class CfnDiskProps:
    def __init__(
        self,
        *,
        disk_name: builtins.str,
        size_in_gb: jsii.Number,
        add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnDisk.AddOnProperty, _IResolvable_da3f097b]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDisk``.

        :param disk_name: The name of the disk.
        :param size_in_gb: The size of the disk in GB.
        :param add_ons: An array of add-ons for the disk. .. epigraph:: If the disk has an add-on enabled when performing a delete disk request, the add-on is automatically disabled before the disk is deleted.
        :param availability_zone: The AWS Region and Availability Zone location for the disk (for example, ``us-east-1a`` ).
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_disk_props = lightsail.CfnDiskProps(
                disk_name="diskName",
                size_in_gb=123,
            
                # the properties below are optional
                add_ons=[lightsail.CfnDisk.AddOnProperty(
                    add_on_type="addOnType",
            
                    # the properties below are optional
                    auto_snapshot_add_on_request=lightsail.CfnDisk.AutoSnapshotAddOnProperty(
                        snapshot_time_of_day="snapshotTimeOfDay"
                    ),
                    status="status"
                )],
                availability_zone="availabilityZone",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "disk_name": disk_name,
            "size_in_gb": size_in_gb,
        }
        if add_ons is not None:
            self._values["add_ons"] = add_ons
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def disk_name(self) -> builtins.str:
        '''The name of the disk.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-diskname
        '''
        result = self._values.get("disk_name")
        assert result is not None, "Required property 'disk_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size_in_gb(self) -> jsii.Number:
        '''The size of the disk in GB.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-sizeingb
        '''
        result = self._values.get("size_in_gb")
        assert result is not None, "Required property 'size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDisk.AddOnProperty, _IResolvable_da3f097b]]]]:
        '''An array of add-ons for the disk.

        .. epigraph::

           If the disk has an add-on enabled when performing a delete disk request, the add-on is automatically disabled before the disk is deleted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-addons
        '''
        result = self._values.get("add_ons")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDisk.AddOnProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The AWS Region and Availability Zone location for the disk (for example, ``us-east-1a`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDiskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnInstance(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance",
):
    '''A CloudFormation ``AWS::Lightsail::Instance``.

    The ``AWS::Lightsail::Instance`` resource specifies an Amazon Lightsail instance.

    :cloudformationResource: AWS::Lightsail::Instance
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_instance = lightsail.CfnInstance(self, "MyCfnInstance",
            blueprint_id="blueprintId",
            bundle_id="bundleId",
            instance_name="instanceName",
        
            # the properties below are optional
            add_ons=[lightsail.CfnInstance.AddOnProperty(
                add_on_type="addOnType",
        
                # the properties below are optional
                auto_snapshot_add_on_request=lightsail.CfnInstance.AutoSnapshotAddOnProperty(
                    snapshot_time_of_day="snapshotTimeOfDay"
                ),
                status="status"
            )],
            availability_zone="availabilityZone",
            hardware=lightsail.CfnInstance.HardwareProperty(
                cpu_count=123,
                disks=[lightsail.CfnInstance.DiskProperty(
                    disk_name="diskName",
                    path="path",
        
                    # the properties below are optional
                    attached_to="attachedTo",
                    attachment_state="attachmentState",
                    iops=123,
                    is_system_disk=False,
                    size_in_gb="sizeInGb"
                )],
                ram_size_in_gb=123
            ),
            key_pair_name="keyPairName",
            networking=lightsail.CfnInstance.NetworkingProperty(
                ports=[lightsail.CfnInstance.PortProperty(
                    access_direction="accessDirection",
                    access_from="accessFrom",
                    access_type="accessType",
                    cidr_list_aliases=["cidrListAliases"],
                    cidrs=["cidrs"],
                    common_name="commonName",
                    from_port=123,
                    ipv6_cidrs=["ipv6Cidrs"],
                    protocol="protocol",
                    to_port=123
                )],
        
                # the properties below are optional
                monthly_transfer=123
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_data="userData"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        blueprint_id: builtins.str,
        bundle_id: builtins.str,
        instance_name: builtins.str,
        add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnInstance.AddOnProperty", _IResolvable_da3f097b]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        hardware: typing.Optional[typing.Union["CfnInstance.HardwareProperty", _IResolvable_da3f097b]] = None,
        key_pair_name: typing.Optional[builtins.str] = None,
        networking: typing.Optional[typing.Union["CfnInstance.NetworkingProperty", _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Lightsail::Instance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param blueprint_id: The blueprint ID for the instance (for example, ``os_amlinux_2016_03`` ).
        :param bundle_id: The bundle ID for the instance (for example, ``micro_1_0`` ).
        :param instance_name: The name of the instance.
        :param add_ons: An array of add-ons for the instance. .. epigraph:: If the instance has an add-on enabled when performing a delete instance request, the add-on is automatically disabled before the instance is deleted.
        :param availability_zone: The Availability Zone for the instance.
        :param hardware: The hardware properties for the instance, such as the vCPU count, attached disks, and amount of RAM. .. epigraph:: The instance restarts when performing an attach disk or detach disk request. This resets the public IP address of your instance if a static IP isn't attached to it.
        :param key_pair_name: The name of the key pair to use for the instance. If no key pair name is specified, the Regional Lightsail default key pair is used.
        :param networking: The public ports and the monthly amount of data transfer allocated for the instance.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        :param user_data: The optional launch script for the instance. Specify a launch script to configure an instance with additional user data. For example, you might want to specify ``apt-get -y update`` as a launch script. .. epigraph:: Depending on the blueprint of your instance, the command to get software on your instance varies. Amazon Linux and CentOS use ``yum`` , Debian and Ubuntu use ``apt-get`` , and FreeBSD uses ``pkg`` .
        '''
        props = CfnInstanceProps(
            blueprint_id=blueprint_id,
            bundle_id=bundle_id,
            instance_name=instance_name,
            add_ons=add_ons,
            availability_zone=availability_zone,
            hardware=hardware,
            key_pair_name=key_pair_name,
            networking=networking,
            tags=tags,
            user_data=user_data,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHardwareCpuCount")
    def attr_hardware_cpu_count(self) -> jsii.Number:
        '''The number of vCPUs the instance has.

        :cloudformationAttribute: Hardware.CpuCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrHardwareCpuCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHardwareRamSizeInGb")
    def attr_hardware_ram_size_in_gb(self) -> jsii.Number:
        '''The amount of RAM in GB on the instance (for example, ``1.0`` ).

        :cloudformationAttribute: Hardware.RamSizeInGb
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrHardwareRamSizeInGb"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrInstanceArn")
    def attr_instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance (for example, ``arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).

        :cloudformationAttribute: InstanceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInstanceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIsStaticIp")
    def attr_is_static_ip(self) -> _IResolvable_da3f097b:
        '''A Boolean value indicating whether the instance has a static IP assigned to it.

        :cloudformationAttribute: IsStaticIp
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsStaticIp"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationAvailabilityZone")
    def attr_location_availability_zone(self) -> builtins.str:
        '''The AWS Region and Availability Zone where the instance is located.

        :cloudformationAttribute: Location.AvailabilityZone
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationAvailabilityZone"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationRegionName")
    def attr_location_region_name(self) -> builtins.str:
        '''The AWS Region of the instance.

        :cloudformationAttribute: Location.RegionName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationRegionName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrNetworkingMonthlyTransferGbPerMonthAllocated")
    def attr_networking_monthly_transfer_gb_per_month_allocated(self) -> builtins.str:
        '''The amount of allocated monthly data transfer (in GB) for an instance.

        :cloudformationAttribute: Networking.MonthlyTransfer.GbPerMonthAllocated
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNetworkingMonthlyTransferGbPerMonthAllocated"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPrivateIpAddress")
    def attr_private_ip_address(self) -> builtins.str:
        '''The private IP address of the instance.

        :cloudformationAttribute: PrivateIpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrivateIpAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublicIpAddress")
    def attr_public_ip_address(self) -> builtins.str:
        '''The public IP address of the instance.

        :cloudformationAttribute: PublicIpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublicIpAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceType")
    def attr_resource_type(self) -> builtins.str:
        '''The resource type of the instance (for example, ``Instance`` ).

        :cloudformationAttribute: ResourceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSshKeyName")
    def attr_ssh_key_name(self) -> builtins.str:
        '''The name of the SSH key pair used by the instance.

        :cloudformationAttribute: SshKeyName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSshKeyName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStateCode")
    def attr_state_code(self) -> jsii.Number:
        '''The status code of the instance.

        :cloudformationAttribute: State.Code
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrStateCode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStateName")
    def attr_state_name(self) -> builtins.str:
        '''The state of the instance (for example, ``running`` or ``pending`` ).

        :cloudformationAttribute: State.Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStateName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSupportCode")
    def attr_support_code(self) -> builtins.str:
        '''The support code of the instance.

        Include this code in your email to support when you have questions about an instance or another resource in Lightsail . This code helps our support team to look up your Lightsail information.

        :cloudformationAttribute: SupportCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSupportCode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUserName")
    def attr_user_name(self) -> builtins.str:
        '''The user name for connecting to the instance (for example, ``ec2-user`` ).

        :cloudformationAttribute: UserName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blueprintId")
    def blueprint_id(self) -> builtins.str:
        '''The blueprint ID for the instance (for example, ``os_amlinux_2016_03`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-blueprintid
        '''
        return typing.cast(builtins.str, jsii.get(self, "blueprintId"))

    @blueprint_id.setter
    def blueprint_id(self, value: builtins.str) -> None:
        jsii.set(self, "blueprintId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> builtins.str:
        '''The bundle ID for the instance (for example, ``micro_1_0`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-bundleid
        '''
        return typing.cast(builtins.str, jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: builtins.str) -> None:
        jsii.set(self, "bundleId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceName")
    def instance_name(self) -> builtins.str:
        '''The name of the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-instancename
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceName"))

    @instance_name.setter
    def instance_name(self, value: builtins.str) -> None:
        jsii.set(self, "instanceName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="addOns")
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnInstance.AddOnProperty", _IResolvable_da3f097b]]]]:
        '''An array of add-ons for the instance.

        .. epigraph::

           If the instance has an add-on enabled when performing a delete instance request, the add-on is automatically disabled before the instance is deleted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-addons
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnInstance.AddOnProperty", _IResolvable_da3f097b]]]], jsii.get(self, "addOns"))

    @add_ons.setter
    def add_ons(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnInstance.AddOnProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "addOns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone for the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-availabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "availabilityZone", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hardware")
    def hardware(
        self,
    ) -> typing.Optional[typing.Union["CfnInstance.HardwareProperty", _IResolvable_da3f097b]]:
        '''The hardware properties for the instance, such as the vCPU count, attached disks, and amount of RAM.

        .. epigraph::

           The instance restarts when performing an attach disk or detach disk request. This resets the public IP address of your instance if a static IP isn't attached to it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-hardware
        '''
        return typing.cast(typing.Optional[typing.Union["CfnInstance.HardwareProperty", _IResolvable_da3f097b]], jsii.get(self, "hardware"))

    @hardware.setter
    def hardware(
        self,
        value: typing.Optional[typing.Union["CfnInstance.HardwareProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "hardware", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keyPairName")
    def key_pair_name(self) -> typing.Optional[builtins.str]:
        '''The name of the key pair to use for the instance.

        If no key pair name is specified, the Regional Lightsail default key pair is used.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-keypairname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPairName"))

    @key_pair_name.setter
    def key_pair_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "keyPairName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networking")
    def networking(
        self,
    ) -> typing.Optional[typing.Union["CfnInstance.NetworkingProperty", _IResolvable_da3f097b]]:
        '''The public ports and the monthly amount of data transfer allocated for the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-networking
        '''
        return typing.cast(typing.Optional[typing.Union["CfnInstance.NetworkingProperty", _IResolvable_da3f097b]], jsii.get(self, "networking"))

    @networking.setter
    def networking(
        self,
        value: typing.Optional[typing.Union["CfnInstance.NetworkingProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "networking", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userData")
    def user_data(self) -> typing.Optional[builtins.str]:
        '''The optional launch script for the instance.

        Specify a launch script to configure an instance with additional user data. For example, you might want to specify ``apt-get -y update`` as a launch script.
        .. epigraph::

           Depending on the blueprint of your instance, the command to get software on your instance varies. Amazon Linux and CentOS use ``yum`` , Debian and Ubuntu use ``apt-get`` , and FreeBSD uses ``pkg`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-userdata
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "userData", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.AddOnProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_on_type": "addOnType",
            "auto_snapshot_add_on_request": "autoSnapshotAddOnRequest",
            "status": "status",
        },
    )
    class AddOnProperty:
        def __init__(
            self,
            *,
            add_on_type: builtins.str,
            auto_snapshot_add_on_request: typing.Optional[typing.Union["CfnInstance.AutoSnapshotAddOnProperty", _IResolvable_da3f097b]] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``AddOn`` is a property of the `AWS::Lightsail::Instance <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html>`_ resource. It describes the add-ons for an instance.

            :param add_on_type: The add-on type (for example, ``AutoSnapshot`` ). .. epigraph:: ``AutoSnapshot`` is the only add-on that can be enabled for an instance.
            :param auto_snapshot_add_on_request: The parameters for the automatic snapshot add-on, such as the daily time when an automatic snapshot will be created.
            :param status: The status of the add-on. Valid Values: ``Enabled`` | ``Disabled``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                add_on_property = lightsail.CfnInstance.AddOnProperty(
                    add_on_type="addOnType",
                
                    # the properties below are optional
                    auto_snapshot_add_on_request=lightsail.CfnInstance.AutoSnapshotAddOnProperty(
                        snapshot_time_of_day="snapshotTimeOfDay"
                    ),
                    status="status"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "add_on_type": add_on_type,
            }
            if auto_snapshot_add_on_request is not None:
                self._values["auto_snapshot_add_on_request"] = auto_snapshot_add_on_request
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def add_on_type(self) -> builtins.str:
            '''The add-on type (for example, ``AutoSnapshot`` ).

            .. epigraph::

               ``AutoSnapshot`` is the only add-on that can be enabled for an instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-addontype
            '''
            result = self._values.get("add_on_type")
            assert result is not None, "Required property 'add_on_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auto_snapshot_add_on_request(
            self,
        ) -> typing.Optional[typing.Union["CfnInstance.AutoSnapshotAddOnProperty", _IResolvable_da3f097b]]:
            '''The parameters for the automatic snapshot add-on, such as the daily time when an automatic snapshot will be created.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-autosnapshotaddonrequest
            '''
            result = self._values.get("auto_snapshot_add_on_request")
            return typing.cast(typing.Optional[typing.Union["CfnInstance.AutoSnapshotAddOnProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the add-on.

            Valid Values: ``Enabled`` | ``Disabled``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.AutoSnapshotAddOnProperty",
        jsii_struct_bases=[],
        name_mapping={"snapshot_time_of_day": "snapshotTimeOfDay"},
    )
    class AutoSnapshotAddOnProperty:
        def __init__(
            self,
            *,
            snapshot_time_of_day: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``AutoSnapshotAddOn`` is a property of the `AddOn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html>`_ property. It describes the automatic snapshot add-on for an instance.

            :param snapshot_time_of_day: The daily time when an automatic snapshot will be created. Constraints: - Must be in ``HH:00`` format, and in an hourly increment. - Specified in Coordinated Universal Time (UTC). - The snapshot will be automatically created between the time specified and up to 45 minutes after.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                auto_snapshot_add_on_property = lightsail.CfnInstance.AutoSnapshotAddOnProperty(
                    snapshot_time_of_day="snapshotTimeOfDay"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if snapshot_time_of_day is not None:
                self._values["snapshot_time_of_day"] = snapshot_time_of_day

        @builtins.property
        def snapshot_time_of_day(self) -> typing.Optional[builtins.str]:
            '''The daily time when an automatic snapshot will be created.

            Constraints:

            - Must be in ``HH:00`` format, and in an hourly increment.
            - Specified in Coordinated Universal Time (UTC).
            - The snapshot will be automatically created between the time specified and up to 45 minutes after.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html#cfn-lightsail-instance-autosnapshotaddon-snapshottimeofday
            '''
            result = self._values.get("snapshot_time_of_day")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoSnapshotAddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.DiskProperty",
        jsii_struct_bases=[],
        name_mapping={
            "disk_name": "diskName",
            "path": "path",
            "attached_to": "attachedTo",
            "attachment_state": "attachmentState",
            "iops": "iops",
            "is_system_disk": "isSystemDisk",
            "size_in_gb": "sizeInGb",
        },
    )
    class DiskProperty:
        def __init__(
            self,
            *,
            disk_name: builtins.str,
            path: builtins.str,
            attached_to: typing.Optional[builtins.str] = None,
            attachment_state: typing.Optional[builtins.str] = None,
            iops: typing.Optional[jsii.Number] = None,
            is_system_disk: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            size_in_gb: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``Disk`` is a property of the `Hardware <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html>`_ property. It describes a disk attached to an instance.

            :param disk_name: The unique name of the disk.
            :param path: The disk path.
            :param attached_to: The resources to which the disk is attached.
            :param attachment_state: (Deprecated) The attachment state of the disk. .. epigraph:: In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.
            :param iops: The input/output operations per second (IOPS) of the disk.
            :param is_system_disk: A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
            :param size_in_gb: The size of the disk in GB.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                disk_property = lightsail.CfnInstance.DiskProperty(
                    disk_name="diskName",
                    path="path",
                
                    # the properties below are optional
                    attached_to="attachedTo",
                    attachment_state="attachmentState",
                    iops=123,
                    is_system_disk=False,
                    size_in_gb="sizeInGb"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "disk_name": disk_name,
                "path": path,
            }
            if attached_to is not None:
                self._values["attached_to"] = attached_to
            if attachment_state is not None:
                self._values["attachment_state"] = attachment_state
            if iops is not None:
                self._values["iops"] = iops
            if is_system_disk is not None:
                self._values["is_system_disk"] = is_system_disk
            if size_in_gb is not None:
                self._values["size_in_gb"] = size_in_gb

        @builtins.property
        def disk_name(self) -> builtins.str:
            '''The unique name of the disk.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-diskname
            '''
            result = self._values.get("disk_name")
            assert result is not None, "Required property 'disk_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def path(self) -> builtins.str:
            '''The disk path.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attached_to(self) -> typing.Optional[builtins.str]:
            '''The resources to which the disk is attached.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachedto
            '''
            result = self._values.get("attached_to")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def attachment_state(self) -> typing.Optional[builtins.str]:
            '''(Deprecated) The attachment state of the disk.

            .. epigraph::

               In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachmentstate
            '''
            result = self._values.get("attachment_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''The input/output operations per second (IOPS) of the disk.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def is_system_disk(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-issystemdisk
            '''
            result = self._values.get("is_system_disk")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def size_in_gb(self) -> typing.Optional[builtins.str]:
            '''The size of the disk in GB.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-sizeingb
            '''
            result = self._values.get("size_in_gb")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DiskProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.HardwareProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu_count": "cpuCount",
            "disks": "disks",
            "ram_size_in_gb": "ramSizeInGb",
        },
    )
    class HardwareProperty:
        def __init__(
            self,
            *,
            cpu_count: typing.Optional[jsii.Number] = None,
            disks: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnInstance.DiskProperty", _IResolvable_da3f097b]]]] = None,
            ram_size_in_gb: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``Hardware`` is a property of the `AWS::Lightsail::Instance <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html>`_ resource. It describes the hardware properties for the instance, such as the vCPU count, attached disks, and amount of RAM.

            :param cpu_count: The number of vCPUs the instance has. .. epigraph:: The ``CpuCount`` property is read-only and should not be specified in a create instance or update instance request.
            :param disks: The disks attached to the instance. The instance restarts when performing an attach disk or detach disk request. This resets the public IP address of your instance if a static IP isn't attached to it.
            :param ram_size_in_gb: The amount of RAM in GB on the instance (for example, ``1.0`` ). .. epigraph:: The ``RamSizeInGb`` property is read-only and should not be specified in a create instance or update instance request.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                hardware_property = lightsail.CfnInstance.HardwareProperty(
                    cpu_count=123,
                    disks=[lightsail.CfnInstance.DiskProperty(
                        disk_name="diskName",
                        path="path",
                
                        # the properties below are optional
                        attached_to="attachedTo",
                        attachment_state="attachmentState",
                        iops=123,
                        is_system_disk=False,
                        size_in_gb="sizeInGb"
                    )],
                    ram_size_in_gb=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cpu_count is not None:
                self._values["cpu_count"] = cpu_count
            if disks is not None:
                self._values["disks"] = disks
            if ram_size_in_gb is not None:
                self._values["ram_size_in_gb"] = ram_size_in_gb

        @builtins.property
        def cpu_count(self) -> typing.Optional[jsii.Number]:
            '''The number of vCPUs the instance has.

            .. epigraph::

               The ``CpuCount`` property is read-only and should not be specified in a create instance or update instance request.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-cpucount
            '''
            result = self._values.get("cpu_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def disks(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnInstance.DiskProperty", _IResolvable_da3f097b]]]]:
            '''The disks attached to the instance.

            The instance restarts when performing an attach disk or detach disk request. This resets the public IP address of your instance if a static IP isn't attached to it.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-disks
            '''
            result = self._values.get("disks")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnInstance.DiskProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def ram_size_in_gb(self) -> typing.Optional[jsii.Number]:
            '''The amount of RAM in GB on the instance (for example, ``1.0`` ).

            .. epigraph::

               The ``RamSizeInGb`` property is read-only and should not be specified in a create instance or update instance request.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-ramsizeingb
            '''
            result = self._values.get("ram_size_in_gb")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HardwareProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zone": "availabilityZone",
            "region_name": "regionName",
        },
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            availability_zone: typing.Optional[builtins.str] = None,
            region_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``Location`` is a property of the `AWS::Lightsail::Instance <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html>`_ resource. It describes the location for an instance.

            :param availability_zone: The Availability Zone for the instance.
            :param region_name: The name of the AWS Region for the instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                location_property = lightsail.CfnInstance.LocationProperty(
                    availability_zone="availabilityZone",
                    region_name="regionName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if availability_zone is not None:
                self._values["availability_zone"] = availability_zone
            if region_name is not None:
                self._values["region_name"] = region_name

        @builtins.property
        def availability_zone(self) -> typing.Optional[builtins.str]:
            '''The Availability Zone for the instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-availabilityzone
            '''
            result = self._values.get("availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region_name(self) -> typing.Optional[builtins.str]:
            '''The name of the AWS Region for the instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-regionname
            '''
            result = self._values.get("region_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.MonthlyTransferProperty",
        jsii_struct_bases=[],
        name_mapping={"gb_per_month_allocated": "gbPerMonthAllocated"},
    )
    class MonthlyTransferProperty:
        def __init__(
            self,
            *,
            gb_per_month_allocated: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``MonthlyTransfer`` is a property of the `Networking <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html>`_ property. It describes the amount of allocated monthly data transfer (in GB) for an instance.

            :param gb_per_month_allocated: The amount of allocated monthly data transfer (in GB) for an instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                monthly_transfer_property = lightsail.CfnInstance.MonthlyTransferProperty(
                    gb_per_month_allocated="gbPerMonthAllocated"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if gb_per_month_allocated is not None:
                self._values["gb_per_month_allocated"] = gb_per_month_allocated

        @builtins.property
        def gb_per_month_allocated(self) -> typing.Optional[builtins.str]:
            '''The amount of allocated monthly data transfer (in GB) for an instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html#cfn-lightsail-instance-monthlytransfer-gbpermonthallocated
            '''
            result = self._values.get("gb_per_month_allocated")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonthlyTransferProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.NetworkingProperty",
        jsii_struct_bases=[],
        name_mapping={"ports": "ports", "monthly_transfer": "monthlyTransfer"},
    )
    class NetworkingProperty:
        def __init__(
            self,
            *,
            ports: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnInstance.PortProperty", _IResolvable_da3f097b]]],
            monthly_transfer: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``Networking`` is a property of the `AWS::Lightsail::Instance <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html>`_ resource. It describes the public ports and the monthly amount of data transfer allocated for the instance.

            :param ports: An array of ports to open on the instance.
            :param monthly_transfer: The monthly amount of data transfer, in GB, allocated for the instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                networking_property = lightsail.CfnInstance.NetworkingProperty(
                    ports=[lightsail.CfnInstance.PortProperty(
                        access_direction="accessDirection",
                        access_from="accessFrom",
                        access_type="accessType",
                        cidr_list_aliases=["cidrListAliases"],
                        cidrs=["cidrs"],
                        common_name="commonName",
                        from_port=123,
                        ipv6_cidrs=["ipv6Cidrs"],
                        protocol="protocol",
                        to_port=123
                    )],
                
                    # the properties below are optional
                    monthly_transfer=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "ports": ports,
            }
            if monthly_transfer is not None:
                self._values["monthly_transfer"] = monthly_transfer

        @builtins.property
        def ports(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnInstance.PortProperty", _IResolvable_da3f097b]]]:
            '''An array of ports to open on the instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html#cfn-lightsail-instance-networking-ports
            '''
            result = self._values.get("ports")
            assert result is not None, "Required property 'ports' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnInstance.PortProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def monthly_transfer(self) -> typing.Optional[jsii.Number]:
            '''The monthly amount of data transfer, in GB, allocated for the instance.'''
            result = self._values.get("monthly_transfer")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.PortProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_direction": "accessDirection",
            "access_from": "accessFrom",
            "access_type": "accessType",
            "cidr_list_aliases": "cidrListAliases",
            "cidrs": "cidrs",
            "common_name": "commonName",
            "from_port": "fromPort",
            "ipv6_cidrs": "ipv6Cidrs",
            "protocol": "protocol",
            "to_port": "toPort",
        },
    )
    class PortProperty:
        def __init__(
            self,
            *,
            access_direction: typing.Optional[builtins.str] = None,
            access_from: typing.Optional[builtins.str] = None,
            access_type: typing.Optional[builtins.str] = None,
            cidr_list_aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
            cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
            common_name: typing.Optional[builtins.str] = None,
            from_port: typing.Optional[jsii.Number] = None,
            ipv6_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
            protocol: typing.Optional[builtins.str] = None,
            to_port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``Port`` is a property of the `Networking <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html>`_ property. It describes information about ports for an instance.

            :param access_direction: The access direction ( ``inbound`` or ``outbound`` ). .. epigraph:: Lightsail currently supports only ``inbound`` access direction.
            :param access_from: The location from which access is allowed. For example, ``Anywhere (0.0.0.0/0)`` , or ``Custom`` if a specific IP address or range of IP addresses is allowed.
            :param access_type: The type of access ( ``Public`` or ``Private`` ).
            :param cidr_list_aliases: An alias that defines access for a preconfigured range of IP addresses. The only alias currently supported is ``lightsail-connect`` , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.
            :param cidrs: The IPv4 address, or range of IPv4 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol. .. epigraph:: The ``ipv6Cidrs`` parameter lists the IPv6 addresses that are allowed to connect to an instance. Examples: - To allow the IP address ``192.0.2.44`` , specify ``192.0.2.44`` or ``192.0.2.44/32`` . - To allow the IP addresses ``192.0.2.0`` to ``192.0.2.255`` , specify ``192.0.2.0/24`` .
            :param common_name: The common name of the port information.
            :param from_port: The first port in a range of open ports on an instance. Allowed ports: - TCP and UDP - ``0`` to ``65535`` - ICMP - The ICMP type for IPv4 addresses. For example, specify ``8`` as the ``fromPort`` (ICMP type), and ``-1`` as the ``toPort`` (ICMP code), to enable ICMP Ping. - ICMPv6 - The ICMP type for IPv6 addresses. For example, specify ``128`` as the ``fromPort`` (ICMPv6 type), and ``0`` as ``toPort`` (ICMPv6 code).
            :param ipv6_cidrs: The IPv6 address, or range of IPv6 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol. Only devices with an IPv6 address can connect to an instance through IPv6; otherwise, IPv4 should be used. .. epigraph:: The ``cidrs`` parameter lists the IPv4 addresses that are allowed to connect to an instance.
            :param protocol: The IP protocol name. The name can be one of the following: - ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead. - ``all`` - All transport layer protocol types. - ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead. - ``icmp`` - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached. When you specify ``icmp`` as the ``protocol`` , you must specify the ICMP type using the ``fromPort`` parameter, and ICMP code using the ``toPort`` parameter.
            :param to_port: The last port in a range of open ports on an instance. Allowed ports: - TCP and UDP - ``0`` to ``65535`` - ICMP - The ICMP code for IPv4 addresses. For example, specify ``8`` as the ``fromPort`` (ICMP type), and ``-1`` as the ``toPort`` (ICMP code), to enable ICMP Ping. - ICMPv6 - The ICMP code for IPv6 addresses. For example, specify ``128`` as the ``fromPort`` (ICMPv6 type), and ``0`` as ``toPort`` (ICMPv6 code).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                port_property = lightsail.CfnInstance.PortProperty(
                    access_direction="accessDirection",
                    access_from="accessFrom",
                    access_type="accessType",
                    cidr_list_aliases=["cidrListAliases"],
                    cidrs=["cidrs"],
                    common_name="commonName",
                    from_port=123,
                    ipv6_cidrs=["ipv6Cidrs"],
                    protocol="protocol",
                    to_port=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if access_direction is not None:
                self._values["access_direction"] = access_direction
            if access_from is not None:
                self._values["access_from"] = access_from
            if access_type is not None:
                self._values["access_type"] = access_type
            if cidr_list_aliases is not None:
                self._values["cidr_list_aliases"] = cidr_list_aliases
            if cidrs is not None:
                self._values["cidrs"] = cidrs
            if common_name is not None:
                self._values["common_name"] = common_name
            if from_port is not None:
                self._values["from_port"] = from_port
            if ipv6_cidrs is not None:
                self._values["ipv6_cidrs"] = ipv6_cidrs
            if protocol is not None:
                self._values["protocol"] = protocol
            if to_port is not None:
                self._values["to_port"] = to_port

        @builtins.property
        def access_direction(self) -> typing.Optional[builtins.str]:
            '''The access direction ( ``inbound`` or ``outbound`` ).

            .. epigraph::

               Lightsail currently supports only ``inbound`` access direction.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessdirection
            '''
            result = self._values.get("access_direction")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def access_from(self) -> typing.Optional[builtins.str]:
            '''The location from which access is allowed.

            For example, ``Anywhere (0.0.0.0/0)`` , or ``Custom`` if a specific IP address or range of IP addresses is allowed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessfrom
            '''
            result = self._values.get("access_from")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def access_type(self) -> typing.Optional[builtins.str]:
            '''The type of access ( ``Public`` or ``Private`` ).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accesstype
            '''
            result = self._values.get("access_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cidr_list_aliases(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An alias that defines access for a preconfigured range of IP addresses.

            The only alias currently supported is ``lightsail-connect`` , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrlistaliases
            '''
            result = self._values.get("cidr_list_aliases")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The IPv4 address, or range of IPv4 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol.

            .. epigraph::

               The ``ipv6Cidrs`` parameter lists the IPv6 addresses that are allowed to connect to an instance.

            Examples:

            - To allow the IP address ``192.0.2.44`` , specify ``192.0.2.44`` or ``192.0.2.44/32`` .
            - To allow the IP addresses ``192.0.2.0`` to ``192.0.2.255`` , specify ``192.0.2.0/24`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrs
            '''
            result = self._values.get("cidrs")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def common_name(self) -> typing.Optional[builtins.str]:
            '''The common name of the port information.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-commonname
            '''
            result = self._values.get("common_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def from_port(self) -> typing.Optional[jsii.Number]:
            '''The first port in a range of open ports on an instance.

            Allowed ports:

            - TCP and UDP - ``0`` to ``65535``
            - ICMP - The ICMP type for IPv4 addresses. For example, specify ``8`` as the ``fromPort`` (ICMP type), and ``-1`` as the ``toPort`` (ICMP code), to enable ICMP Ping.
            - ICMPv6 - The ICMP type for IPv6 addresses. For example, specify ``128`` as the ``fromPort`` (ICMPv6 type), and ``0`` as ``toPort`` (ICMPv6 code).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-fromport
            '''
            result = self._values.get("from_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ipv6_cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The IPv6 address, or range of IPv6 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol.

            Only devices with an IPv6 address can connect to an instance through IPv6; otherwise, IPv4 should be used.
            .. epigraph::

               The ``cidrs`` parameter lists the IPv4 addresses that are allowed to connect to an instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-ipv6cidrs
            '''
            result = self._values.get("ipv6_cidrs")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The IP protocol name.

            The name can be one of the following:

            - ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead.
            - ``all`` - All transport layer protocol types.
            - ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
            - ``icmp`` - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached. When you specify ``icmp`` as the ``protocol`` , you must specify the ICMP type using the ``fromPort`` parameter, and ICMP code using the ``toPort`` parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def to_port(self) -> typing.Optional[jsii.Number]:
            '''The last port in a range of open ports on an instance.

            Allowed ports:

            - TCP and UDP - ``0`` to ``65535``
            - ICMP - The ICMP code for IPv4 addresses. For example, specify ``8`` as the ``fromPort`` (ICMP type), and ``-1`` as the ``toPort`` (ICMP code), to enable ICMP Ping.
            - ICMPv6 - The ICMP code for IPv6 addresses. For example, specify ``128`` as the ``fromPort`` (ICMPv6 type), and ``0`` as ``toPort`` (ICMPv6 code).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-toport
            '''
            result = self._values.get("to_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.StateProperty",
        jsii_struct_bases=[],
        name_mapping={"code": "code", "name": "name"},
    )
    class StateProperty:
        def __init__(
            self,
            *,
            code: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``State`` is a property of the `AWS::Lightsail::Instance <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html>`_ resource. It describes the status code and the state (for example, ``running`` ) of an instance.

            :param code: The status code of the instance.
            :param name: The state of the instance (for example, ``running`` or ``pending`` ).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                state_property = lightsail.CfnInstance.StateProperty(
                    code=123,
                    name="name"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if code is not None:
                self._values["code"] = code
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def code(self) -> typing.Optional[jsii.Number]:
            '''The status code of the instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-code
            '''
            result = self._values.get("code")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The state of the instance (for example, ``running`` or ``pending`` ).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "blueprint_id": "blueprintId",
        "bundle_id": "bundleId",
        "instance_name": "instanceName",
        "add_ons": "addOns",
        "availability_zone": "availabilityZone",
        "hardware": "hardware",
        "key_pair_name": "keyPairName",
        "networking": "networking",
        "tags": "tags",
        "user_data": "userData",
    },
)
class CfnInstanceProps:
    def __init__(
        self,
        *,
        blueprint_id: builtins.str,
        bundle_id: builtins.str,
        instance_name: builtins.str,
        add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnInstance.AddOnProperty, _IResolvable_da3f097b]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        hardware: typing.Optional[typing.Union[CfnInstance.HardwareProperty, _IResolvable_da3f097b]] = None,
        key_pair_name: typing.Optional[builtins.str] = None,
        networking: typing.Optional[typing.Union[CfnInstance.NetworkingProperty, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstance``.

        :param blueprint_id: The blueprint ID for the instance (for example, ``os_amlinux_2016_03`` ).
        :param bundle_id: The bundle ID for the instance (for example, ``micro_1_0`` ).
        :param instance_name: The name of the instance.
        :param add_ons: An array of add-ons for the instance. .. epigraph:: If the instance has an add-on enabled when performing a delete instance request, the add-on is automatically disabled before the instance is deleted.
        :param availability_zone: The Availability Zone for the instance.
        :param hardware: The hardware properties for the instance, such as the vCPU count, attached disks, and amount of RAM. .. epigraph:: The instance restarts when performing an attach disk or detach disk request. This resets the public IP address of your instance if a static IP isn't attached to it.
        :param key_pair_name: The name of the key pair to use for the instance. If no key pair name is specified, the Regional Lightsail default key pair is used.
        :param networking: The public ports and the monthly amount of data transfer allocated for the instance.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        :param user_data: The optional launch script for the instance. Specify a launch script to configure an instance with additional user data. For example, you might want to specify ``apt-get -y update`` as a launch script. .. epigraph:: Depending on the blueprint of your instance, the command to get software on your instance varies. Amazon Linux and CentOS use ``yum`` , Debian and Ubuntu use ``apt-get`` , and FreeBSD uses ``pkg`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_instance_props = lightsail.CfnInstanceProps(
                blueprint_id="blueprintId",
                bundle_id="bundleId",
                instance_name="instanceName",
            
                # the properties below are optional
                add_ons=[lightsail.CfnInstance.AddOnProperty(
                    add_on_type="addOnType",
            
                    # the properties below are optional
                    auto_snapshot_add_on_request=lightsail.CfnInstance.AutoSnapshotAddOnProperty(
                        snapshot_time_of_day="snapshotTimeOfDay"
                    ),
                    status="status"
                )],
                availability_zone="availabilityZone",
                hardware=lightsail.CfnInstance.HardwareProperty(
                    cpu_count=123,
                    disks=[lightsail.CfnInstance.DiskProperty(
                        disk_name="diskName",
                        path="path",
            
                        # the properties below are optional
                        attached_to="attachedTo",
                        attachment_state="attachmentState",
                        iops=123,
                        is_system_disk=False,
                        size_in_gb="sizeInGb"
                    )],
                    ram_size_in_gb=123
                ),
                key_pair_name="keyPairName",
                networking=lightsail.CfnInstance.NetworkingProperty(
                    ports=[lightsail.CfnInstance.PortProperty(
                        access_direction="accessDirection",
                        access_from="accessFrom",
                        access_type="accessType",
                        cidr_list_aliases=["cidrListAliases"],
                        cidrs=["cidrs"],
                        common_name="commonName",
                        from_port=123,
                        ipv6_cidrs=["ipv6Cidrs"],
                        protocol="protocol",
                        to_port=123
                    )],
            
                    # the properties below are optional
                    monthly_transfer=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_data="userData"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "blueprint_id": blueprint_id,
            "bundle_id": bundle_id,
            "instance_name": instance_name,
        }
        if add_ons is not None:
            self._values["add_ons"] = add_ons
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if hardware is not None:
            self._values["hardware"] = hardware
        if key_pair_name is not None:
            self._values["key_pair_name"] = key_pair_name
        if networking is not None:
            self._values["networking"] = networking
        if tags is not None:
            self._values["tags"] = tags
        if user_data is not None:
            self._values["user_data"] = user_data

    @builtins.property
    def blueprint_id(self) -> builtins.str:
        '''The blueprint ID for the instance (for example, ``os_amlinux_2016_03`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-blueprintid
        '''
        result = self._values.get("blueprint_id")
        assert result is not None, "Required property 'blueprint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> builtins.str:
        '''The bundle ID for the instance (for example, ``micro_1_0`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-bundleid
        '''
        result = self._values.get("bundle_id")
        assert result is not None, "Required property 'bundle_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_name(self) -> builtins.str:
        '''The name of the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-instancename
        '''
        result = self._values.get("instance_name")
        assert result is not None, "Required property 'instance_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnInstance.AddOnProperty, _IResolvable_da3f097b]]]]:
        '''An array of add-ons for the instance.

        .. epigraph::

           If the instance has an add-on enabled when performing a delete instance request, the add-on is automatically disabled before the instance is deleted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-addons
        '''
        result = self._values.get("add_ons")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnInstance.AddOnProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone for the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hardware(
        self,
    ) -> typing.Optional[typing.Union[CfnInstance.HardwareProperty, _IResolvable_da3f097b]]:
        '''The hardware properties for the instance, such as the vCPU count, attached disks, and amount of RAM.

        .. epigraph::

           The instance restarts when performing an attach disk or detach disk request. This resets the public IP address of your instance if a static IP isn't attached to it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-hardware
        '''
        result = self._values.get("hardware")
        return typing.cast(typing.Optional[typing.Union[CfnInstance.HardwareProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def key_pair_name(self) -> typing.Optional[builtins.str]:
        '''The name of the key pair to use for the instance.

        If no key pair name is specified, the Regional Lightsail default key pair is used.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-keypairname
        '''
        result = self._values.get("key_pair_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def networking(
        self,
    ) -> typing.Optional[typing.Union[CfnInstance.NetworkingProperty, _IResolvable_da3f097b]]:
        '''The public ports and the monthly amount of data transfer allocated for the instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-networking
        '''
        result = self._values.get("networking")
        return typing.cast(typing.Optional[typing.Union[CfnInstance.NetworkingProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''The optional launch script for the instance.

        Specify a launch script to configure an instance with additional user data. For example, you might want to specify ``apt-get -y update`` as a launch script.
        .. epigraph::

           Depending on the blueprint of your instance, the command to get software on your instance varies. Amazon Linux and CentOS use ``yum`` , Debian and Ubuntu use ``apt-get`` , and FreeBSD uses ``pkg`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-userdata
        '''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStaticIp(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnStaticIp",
):
    '''A CloudFormation ``AWS::Lightsail::StaticIp``.

    The ``AWS::Lightsail::StaticIp`` resource specifies a static IP that can be attached to an Amazon Lightsail instance that is in the same AWS Region and Availability Zone.

    :cloudformationResource: AWS::Lightsail::StaticIp
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_static_ip = lightsail.CfnStaticIp(self, "MyCfnStaticIp",
            static_ip_name="staticIpName",
        
            # the properties below are optional
            attached_to="attachedTo"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        static_ip_name: builtins.str,
        attached_to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Lightsail::StaticIp``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param static_ip_name: The name of the static IP.
        :param attached_to: The instance that the static IP is attached to.
        '''
        props = CfnStaticIpProps(
            static_ip_name=static_ip_name, attached_to=attached_to
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIpAddress")
    def attr_ip_address(self) -> builtins.str:
        '''The IP address of the static IP.

        :cloudformationAttribute: IpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIsAttached")
    def attr_is_attached(self) -> _IResolvable_da3f097b:
        '''A Boolean value indicating whether the static IP is attached to an instance.

        :cloudformationAttribute: IsAttached
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsAttached"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStaticIpArn")
    def attr_static_ip_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the static IP (for example, ``arn:aws:lightsail:us-east-2:123456789101:StaticIp/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).

        :cloudformationAttribute: StaticIpArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStaticIpArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="staticIpName")
    def static_ip_name(self) -> builtins.str:
        '''The name of the static IP.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-staticipname
        '''
        return typing.cast(builtins.str, jsii.get(self, "staticIpName"))

    @static_ip_name.setter
    def static_ip_name(self, value: builtins.str) -> None:
        jsii.set(self, "staticIpName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attachedTo")
    def attached_to(self) -> typing.Optional[builtins.str]:
        '''The instance that the static IP is attached to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-attachedto
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attachedTo"))

    @attached_to.setter
    def attached_to(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "attachedTo", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnStaticIpProps",
    jsii_struct_bases=[],
    name_mapping={"static_ip_name": "staticIpName", "attached_to": "attachedTo"},
)
class CfnStaticIpProps:
    def __init__(
        self,
        *,
        static_ip_name: builtins.str,
        attached_to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnStaticIp``.

        :param static_ip_name: The name of the static IP.
        :param attached_to: The instance that the static IP is attached to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_static_ip_props = lightsail.CfnStaticIpProps(
                static_ip_name="staticIpName",
            
                # the properties below are optional
                attached_to="attachedTo"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "static_ip_name": static_ip_name,
        }
        if attached_to is not None:
            self._values["attached_to"] = attached_to

    @builtins.property
    def static_ip_name(self) -> builtins.str:
        '''The name of the static IP.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-staticipname
        '''
        result = self._values.get("static_ip_name")
        assert result is not None, "Required property 'static_ip_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attached_to(self) -> typing.Optional[builtins.str]:
        '''The instance that the static IP is attached to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-attachedto
        '''
        result = self._values.get("attached_to")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStaticIpProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDatabase",
    "CfnDatabaseProps",
    "CfnDisk",
    "CfnDiskProps",
    "CfnInstance",
    "CfnInstanceProps",
    "CfnStaticIp",
    "CfnStaticIpProps",
]

publication.publish()
