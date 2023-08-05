from typing import Optional

from reqif.models.error_handling import ReqIFMissingTagException
from reqif.models.reqif_spec_object import SpecObjectAttribute
from reqif.models.reqif_spec_relation import (
    ReqIFSpecRelation,
)
from reqif.models.reqif_types import SpecObjectAttributeType
from reqif.parsers.spec_object_parser import ATTRIBUTE_STRING_TEMPLATE


class SpecRelationParser:
    @staticmethod
    def parse(xml_spec_relation) -> ReqIFSpecRelation:
        assert xml_spec_relation.tag == "SPEC-RELATION"

        children_tags = list(map(lambda el: el.tag, list(xml_spec_relation)))
        assert "TYPE" in children_tags
        if "SOURCE" not in children_tags:
            raise ReqIFMissingTagException(
                xml_node=xml_spec_relation, tag="SOURCE"
            ) from None
        if "TARGET" not in children_tags:
            raise ReqIFMissingTagException(
                xml_node=xml_spec_relation, tag="TARGET"
            ) from None

        attributes = xml_spec_relation.attrib
        assert "IDENTIFIER" in attributes, f"{attributes}"
        identifier = attributes["IDENTIFIER"]

        description: Optional[str] = (
            attributes["DESC"] if "DESC" in attributes else None
        )

        last_change: Optional[str] = (
            attributes["LAST-CHANGE"] if "LAST-CHANGE" in attributes else None
        )

        relation_type_ref = (
            xml_spec_relation.find("TYPE").find("SPEC-RELATION-TYPE-REF").text
        )

        spec_relation_source = (
            xml_spec_relation.find("SOURCE").find("SPEC-OBJECT-REF").text
        )

        spec_relation_target = (
            xml_spec_relation.find("TARGET").find("SPEC-OBJECT-REF").text
        )

        values_attribute: Optional[SpecObjectAttribute] = None
        xml_values = xml_spec_relation.find("VALUES")
        if xml_values is not None:
            xml_string_attribute = xml_values.find("ATTRIBUTE-VALUE-STRING")
            assert xml_string_attribute is not None
            attribute_value = xml_string_attribute.attrib["THE-VALUE"]
            attribute_name = xml_string_attribute[0][0].text
            values_attribute = SpecObjectAttribute(
                SpecObjectAttributeType.STRING,
                attribute_name,
                attribute_value,
                enum_values_then_definition_order=None,
            )

        spec_relation = ReqIFSpecRelation(
            children_tags=children_tags,
            xml_node=xml_spec_relation,
            description=description,
            identifier=identifier,
            last_change=last_change,
            relation_type_ref=relation_type_ref,
            source=spec_relation_source,
            target=spec_relation_target,
            values_attribute=values_attribute,
        )
        return spec_relation

    @staticmethod
    def unparse(spec_relation: ReqIFSpecRelation):
        output = "        <SPEC-RELATION"
        if spec_relation.description is not None:
            output += f' DESC="{spec_relation.description}"'
        output += f' IDENTIFIER="{spec_relation.identifier}"'
        if spec_relation.last_change is not None:
            output += f' LAST-CHANGE="{spec_relation.last_change}"'
        output += ">\n"

        for tag in spec_relation.children_tags:
            if tag == "TYPE":
                output += SpecRelationParser._unparse_spec_relation_type(
                    spec_relation
                )
            elif tag == "SOURCE":
                output += SpecRelationParser._unparse_spec_relation_source(
                    spec_relation
                )
            elif tag == "TARGET":
                output += SpecRelationParser._unparse_spec_relation_target(
                    spec_relation
                )
            elif tag == "VALUES":
                values_attribute = spec_relation.values_attribute
                if values_attribute is not None:
                    output += "          <VALUES>\n"
                    output += ATTRIBUTE_STRING_TEMPLATE.format(
                        name=values_attribute.name, value=values_attribute.value
                    )
                    output += "          </VALUES>\n"
                else:
                    raise NotImplementedError
            else:
                raise NotImplementedError(tag)

        output += "        </SPEC-RELATION>\n"
        return output

    @staticmethod
    def _unparse_spec_relation_type(spec_relation: ReqIFSpecRelation) -> str:
        output = ""
        output += "          <TYPE>\n"
        output += "            "
        output += (
            "<SPEC-RELATION-TYPE-REF>"
            f"{spec_relation.relation_type_ref}"
            "</SPEC-RELATION-TYPE-REF>\n"
        )
        output += "          </TYPE>\n"
        return output

    @staticmethod
    def _unparse_spec_relation_source(
        spec_relation: ReqIFSpecRelation,
    ) -> str:
        output = ""
        output += "          <SOURCE>\n"
        output += "            "
        output += f"<SPEC-OBJECT-REF>{spec_relation.source}</SPEC-OBJECT-REF>\n"
        output += "          </SOURCE>\n"
        return output

    @staticmethod
    def _unparse_spec_relation_target(
        spec_relation: ReqIFSpecRelation,
    ) -> str:
        output = ""
        output += "          <TARGET>\n"
        output += "            "
        output += f"<SPEC-OBJECT-REF>{spec_relation.target}</SPEC-OBJECT-REF>\n"
        output += "          </TARGET>\n"
        return output
